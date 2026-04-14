# KPI Overall
SELECT 
  SUM(revenue) AS total_revenue,
  SUM(cost) AS total_cost,
  -- Profitability
  SUM(revenue) / NULLIF(SUM(cost), 0) AS overall_roas,
  -- Conversion
  SUM(conversions) / NULLIF(SUM(clicks), 0) AS overall_conversion_rate

FROM clean_funnel_campaign_data;

# KPI per Channel
SELECT 
  channel,
  SUM(impressions) AS impressions,
  SUM(clicks) AS clicks,
  SUM(conversions) AS conversions,
  SUM(cost) AS cost,
  SUM(revenue) AS revenue,

  SUM(clicks) / NULLIF(SUM(impressions), 0) AS ctr,
  SUM(conversions) / NULLIF(SUM(clicks), 0) AS conversion_rate,
  SUM(revenue) / NULLIF(SUM(cost), 0) AS roas

FROM clean_funnel_campaign_data
GROUP BY channel
ORDER BY roas DESC;

# KPI per Campaign
SELECT 
  campaign_name,
  SUM(cost) AS total_cost,
  SUM(revenue) AS total_revenue,
  SUM(revenue) / NULLIF(SUM(cost), 0) AS roas,
  (SUM(revenue) - SUM(cost)) AS profit

FROM clean_funnel_campaign_data
GROUP BY campaign_name
ORDER BY roas DESC;

# Segment Analysis
#By Device
SELECT 
  device,
  SUM(impressions) AS impressions,
  SUM(clicks) AS clicks,
  SUM(conversions) AS conversions,
  SUM(cost) AS cost,
  SUM(revenue) AS revenue,
  SUM(clicks) / NULLIF(SUM(impressions), 0) AS ctr,
  SUM(conversions) / NULLIF(SUM(clicks), 0) AS conversion_rate,
  SUM(revenue) / NULLIF(SUM(cost), 0) AS roas
FROM clean_funnel_campaign_data
GROUP BY device
ORDER BY roas DESC;

# By Age Group
SELECT 
  audience_age_group,
  SUM(clicks) AS clicks,
  SUM(conversions) AS conversions,
  SUM(revenue) AS revenue,
  SUM(cost) AS cost,
  SUM(conversions) / NULLIF(SUM(clicks), 0) AS conversion_rate,
  SUM(revenue) / NULLIF(SUM(cost), 0) AS roas
FROM clean_funnel_campaign_data
GROUP BY audience_age_group
ORDER BY roas DESC;

# By Region
SELECT 
  region,
  SUM(clicks) AS clicks,
  SUM(conversions) AS conversions,
  SUM(cost) AS cost,
  SUM(revenue) AS revenue,
  SUM(conversions) / NULLIF(SUM(clicks), 0) AS conversion_rate,
  SUM(revenue) / NULLIF(SUM(cost), 0) AS roas
FROM clean_funnel_campaign_data
GROUP BY region
ORDER BY roas DESC;

# By Funnel
SELECT 
  device,
  SUM(clicks) / NULLIF(SUM(impressions), 0) AS ctr,
  SUM(add_to_cart) / NULLIF(SUM(clicks), 0) AS atc_rate,
  SUM(conversions) / NULLIF(SUM(add_to_cart), 0) AS atc_to_conversion
FROM clean_funnel_campaign_data
GROUP BY device;

SELECT
    channel,
    SUM(impressions) AS impressions,
    SUM(clicks) AS clicks,
    SUM(add_to_cart) AS add_to_cart,
    SUM(conversions) AS conversions
FROM clean_funnel_campaign_data
GROUP BY
    channel;

# Campaign Performance (TOP & WORST)
SELECT 
  campaign_name,
  channel,
  SUM(cost) AS cost,
  SUM(revenue) AS revenue,
  SUM(revenue) / NULLIF(SUM(cost), 0) AS roas
FROM clean_funnel_campaign_data
GROUP BY campaign_name, channel
ORDER BY roas DESC;

#  Trend Analysis
SELECT 
  date,
  SUM(revenue) AS revenue,
  SUM(cost) AS cost,
  SUM(revenue) / NULLIF(SUM(cost), 0) AS roas
FROM campaign_data
GROUP BY date
ORDER BY date;