import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import itertools

np.random.seed(42)
random.seed(42)

# --- CONFIGURATION ---
START_DATE = datetime(2023, 1, 1)
DAYS = 180
CHANNELS = ['TikTok Ads', 'Instagram Ads', 'Shopee Ads', 'Google Ads']
CAMP_TYPES = ['Awareness', 'Conversion', 'Retargeting']
REGIONS = ['Jabodetabek', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Sumatera', 'Kalimantan', 'Sulawesi', 'Bali & Nusa Tenggara', 'Indonesia Timur']
DEVICES = ['Mobile', 'Desktop']
AGE_GROUPS = ['18-24', '25-34', '35-44']
CATEGORIES = ['Skincare', 'Makeup', 'Bodycare']
PRICE_TIERS = ['Low', 'Mid', 'High']

dates = [START_DATE + timedelta(days=i) for i in range(DAYS)]

# --- CAMPAIGN SETUP ---
# 8 campaigns per channel
AWARENESS_THEMES = ["Glow Up Series Launch", "Skincare Secrets Revealed", "Beauty Expo Mega Brand", "Viral Makeup Challenge", "Summer Aesthetics Collection", "K-Beauty Festival", "Anti-Aging Masterclass", "Local Pride Beauty Fest", "Flawless Skin Journey", "Radiant Beauty Reveal"]
CONVERSION_THEMES = ["Payday Super Sale", "Flash Sale Midnight Hour", "Promo Tanggal Kembar", "Buy 1 Get 1 Full Size", "Diskon 50% All Items", "Gratis Ongkir Super", "Bundling Cantik Hemat", "Clearance Sale Lebaran", "Gajian Beauty Deals", "Birthday Flash Sale"]
RETARGETING_THEMES = ["Checkout Now (Last Chance)", "Your Cart is Waiting!", "We Miss You - 20% Off", "Exclusive VIP Cashback", "Secret Stash Return Promo"]

campaigns = []
for ch in CHANNELS:
    for i in range(8):
        c_type = np.random.choice(CAMP_TYPES, p=[0.4, 0.4, 0.2])
        if c_type == 'Awareness':
            c_name = f"{np.random.choice(AWARENESS_THEMES)} | {ch.split()[0]}"
        elif c_type == 'Conversion':
            c_name = f"{np.random.choice(CONVERSION_THEMES)} | {ch.split()[0]}"
        else:
            c_name = f"{np.random.choice(RETARGETING_THEMES)} | {ch.split()[0]}"
            
        campaigns.append({
            'channel': ch,
            'campaign_name': c_name,
            'campaign_type': c_type
        })
camp_df = pd.DataFrame(campaigns)

# --- BASE DATA GENERATION (CROSS PRODUCT) ---
print("Generating full combinations...")
full_grid = list(itertools.product(dates, campaigns, REGIONS, DEVICES, AGE_GROUPS))

# To hit 30,000 - 40,000 rows, sample ~35,000 combinations
print("Sampling rows...")
selected_indices = np.random.choice(len(full_grid), 35000, replace=False)
selected_grid = [full_grid[i] for i in selected_indices]

df = pd.DataFrame({
    'date': [x[0] for x in selected_grid],
    'channel': [x[1]['channel'] for x in selected_grid],
    'campaign_name': [x[1]['campaign_name'] for x in selected_grid],
    'campaign_type': [x[1]['campaign_type'] for x in selected_grid],
    'region': [x[2] for x in selected_grid],
    'device': [x[3] for x in selected_grid],
    'audience_age_group': [x[4] for x in selected_grid],
})

df['product_category'] = np.random.choice(CATEGORIES, size=len(df))
df['product_price_tier'] = np.random.choice(PRICE_TIERS, size=len(df))

print("Applying rules and formulas...")
# --- IMPRESSIONS ---
base_imp = 15000
ch_imp_mult = {'TikTok Ads': 3.0, 'Instagram Ads': 1.0, 'Shopee Ads': 0.3, 'Google Ads': 0.8}
typ_imp_mult = {'Awareness': 3.0, 'Conversion': 1.0, 'Retargeting': 0.2}

df['days_since_start'] = (pd.to_datetime(df['date']) - START_DATE).dt.days
df['fatigue_mult'] = np.maximum(0.3, 1.0 - (df['days_since_start'] / DAYS) * 0.5)

df['is_weekend'] = pd.to_datetime(df['date']).dt.dayofweek >= 5
df['weekend_mult_imp'] = np.where(df['is_weekend'], 1.2, 1.0)

df['impressions'] = (
    base_imp 
    * df['channel'].map(ch_imp_mult) 
    * df['campaign_type'].map(typ_imp_mult) 
    * df['fatigue_mult'] 
    * df['weekend_mult_imp'] 
    * np.random.uniform(0.5, 1.5, size=len(df))
).astype(int)

# --- CTR & CLICKS ---
# Rules: 0.5% - 5%, Mobile higher, TikTok high, 18-24 high, 35-44 low
ch_ctr_mod = {'TikTok Ads': 1.5, 'Instagram Ads': 1.0, 'Shopee Ads': 1.0, 'Google Ads': 1.2}
age_ctr_mod = {'18-24': 1.3, '25-34': 1.0, '35-44': 0.7}
device_ctr_mod = {'Mobile': 1.2, 'Desktop': 0.8}

ctr_mult = (
    df['channel'].map(ch_ctr_mod) 
    * df['audience_age_group'].map(age_ctr_mod) 
    * df['device'].map(device_ctr_mod) 
    * np.where(df['is_weekend'], 1.3, 1.0)
)
df['ctr'] = 0.02 * ctr_mult * np.random.uniform(0.7, 1.3, size=len(df))
df['ctr'] = np.clip(df['ctr'], 0.005, 0.05)

df['clicks'] = (df['impressions'] * df['ctr']).astype(int)

# --- ADD TO CART ---
# Rules: 3% - 15%
df['atc_rate'] = np.random.uniform(0.03, 0.15, size=len(df))
df['add_to_cart'] = (df['clicks'] * df['atc_rate']).astype(int)

# --- CONVERSIONS ---
# Rules: 1% - 10%, TikTok Low, Shopee High, Google High, Desktop High, 25-34 best
ch_cvr_mod = {'TikTok Ads': 0.5, 'Instagram Ads': 1.0, 'Shopee Ads': 1.8, 'Google Ads': 1.5}
typ_cvr_mod = {'Awareness': 0.3, 'Conversion': 1.0, 'Retargeting': 2.5}
age_cvr_mod = {'18-24': 0.6, '25-34': 1.5, '35-44': 1.2}
device_cvr_mod = {'Mobile': 0.8, 'Desktop': 1.3}

cvr_mult = (
    df['channel'].map(ch_cvr_mod) 
    * df['campaign_type'].map(typ_cvr_mod) 
    * df['audience_age_group'].map(age_cvr_mod) 
    * df['device'].map(device_cvr_mod) 
    * np.where(df['is_weekend'], 1.2, 1.0)
)
df['cvr'] = 0.04 * cvr_mult * np.random.uniform(0.7, 1.3, size=len(df))
df['cvr'] = np.clip(df['cvr'], 0.01, 0.10)

df['conversions'] = (df['clicks'] * df['cvr']).astype(int)

# Funnel strictness (pre-noise)
df['clicks'] = np.minimum(df['clicks'], df['impressions'])
df['add_to_cart'] = np.minimum(df['add_to_cart'], df['clicks'])
df['conversions'] = np.minimum(df['conversions'], df['add_to_cart'])

# --- PROMOS ---
promo_dates = pd.to_datetime(['2023-02-02', '2023-03-03', '2023-04-04', '2023-05-05', '2023-06-06']).date
promo_mask = df['date'].dt.date.isin(promo_dates)
df.loc[promo_mask, 'impressions'] = (df.loc[promo_mask, 'impressions'] * 1.8).astype(int)
df.loc[promo_mask, 'clicks'] = (df.loc[promo_mask, 'clicks'] * 2.0).astype(int)
df.loc[promo_mask, 'add_to_cart'] = (df.loc[promo_mask, 'add_to_cart'] * 2.5).astype(int)
df.loc[promo_mask, 'conversions'] = (df.loc[promo_mask, 'conversions'] * 3.0).astype(int)

# Ensure funnel strictness again after promo multi
df['clicks'] = np.minimum(df['clicks'], df['impressions'])
df['add_to_cart'] = np.minimum(df['add_to_cart'], df['clicks'])
df['conversions'] = np.minimum(df['conversions'], df['add_to_cart'])

# --- FINANCIALS ---
# Cost: Google Ads High Cost
ch_cost_mod = {'TikTok Ads': 0.4, 'Instagram Ads': 1.0, 'Shopee Ads': 0.6, 'Google Ads': 2.0}
df['cpc_base'] = df['channel'].map(ch_cost_mod) * np.random.uniform(1500, 3500, size=len(df))
df['cost'] = df['clicks'] * df['cpc_base']

# Revenue: 50,000 - 300,000
price_map_center = {'Low': 75000, 'Mid': 150000, 'High': 250000}
df['avg_price'] = df['product_price_tier'].map(price_map_center) * np.random.uniform(0.8, 1.2, size=len(df))
# Clip revenue per conversion to 50k-300k as requested
df['avg_price'] = np.clip(df['avg_price'], 50000, 300000)
df['revenue'] = df['conversions'] * df['avg_price']

print("Adding noise...")
# --- REQUIRED NOISE ---
n = len(df)

# 1. 3-5% missing values pada clicks, add_to_cart, conversions
missing_pct1 = np.random.uniform(0.03, 0.05)
missing_pct2 = np.random.uniform(0.03, 0.05)
missing_pct3 = np.random.uniform(0.03, 0.05)

idx_clicks = np.random.choice(n, int(n * missing_pct1), replace=False)
idx_atc = np.random.choice(n, int(n * missing_pct2), replace=False)
idx_conv = np.random.choice(n, int(n * missing_pct3), replace=False)

# Convert to float to allow NaNs
df['clicks'] = df['clicks'].astype('float64')
df['add_to_cart'] = df['add_to_cart'].astype('float64')
df['conversions'] = df['conversions'].astype('float64')

# 3. 1% data tidak konsisten (conversions > add_to_cart) -> BEFORE we apply NaN so we can operate on it
inconsist_idx = np.random.choice(n, int(n * 0.01), replace=False)
df.loc[inconsist_idx, 'conversions'] = df.loc[inconsist_idx, 'add_to_cart'] + np.random.randint(1, 15, size=len(inconsist_idx))

# Apply the NaNs now
df.loc[idx_clicks, 'clicks'] = np.nan
df.loc[idx_atc, 'add_to_cart'] = np.nan
df.loc[idx_conv, 'conversions'] = np.nan

# 2. 2-3% outlier (cost tinggi tapi conversion rendah)
outlier_pct = np.random.uniform(0.02, 0.03)
outlier_idx = np.random.choice(n, int(n * outlier_pct), replace=False)
df.loc[outlier_idx, 'cost'] *= np.random.uniform(8.0, 15.0, size=len(outlier_idx))
# ensure low conversions for outliers safely
df.loc[outlier_idx, 'conversions'] = np.floor(df.loc[outlier_idx, 'conversions'] * 0.1)

# Format floats for money
df['cost'] = df['cost'].round(2)
df['revenue'] = df['revenue'].round(2)

# 4. 1-2% duplicate data
dup_pct = np.random.uniform(0.01, 0.02)
dup_idx = np.random.choice(n, int(n * dup_pct), replace=False)
duplicates = df.iloc[dup_idx].copy()
df = pd.concat([df, duplicates], ignore_index=True)

# Shuffle the dataframe fully to make it realistic
df = df.sample(frac=1.0, random_state=42).reset_index(drop=True)

# Select and order columns
final_cols = [
    'date', 'channel', 'campaign_name', 'campaign_type', 'region', 'device',
    'audience_age_group', 'product_category', 'product_price_tier',
    'impressions', 'clicks', 'add_to_cart', 'conversions', 'cost', 'revenue'
]
df = df[final_cols]

# Optional format date string
df['date'] = df['date'].dt.strftime('%Y-%m-%d')

# For integers, when there are NaNs, pandas converts to float.
# To keep Int64 formatting while supporting NaNs, we can use 'Int64' nullable type.
df['impressions'] = df['impressions'].astype('Int64')
df['clicks'] = df['clicks'].astype('Int64')
df['add_to_cart'] = df['add_to_cart'].astype('Int64')
df['conversions'] = df['conversions'].astype('Int64')

# Save to CSV
output_filename = "synthetic_beauty_marketing_data.csv"
print(f"Saving to {output_filename}...")
df.to_csv(output_filename, index=False)

print(f"Data generation complete. Final shape: {df.shape}")
