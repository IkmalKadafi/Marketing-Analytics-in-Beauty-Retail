# Marketing-Analytics-in-Beauty-Retail
Marketing Analytics in Beauty Retail: Optimizing Campaign Performance and ROI Across Digital Channels

## 📊 Rangkuman Laporan (Executive Summary)
Berdasarkan analisis performa kampanye marketing digital selama periode 1 Januari 2023 - 29 Juni 2023, laporan memberikan wawasan mendalam mengenai pengoptimalan biaya dan return on investment (ROI). Metrik utama yang dianalisis mencakup *Return on Ad Spend* (ROAS), *Conversion Rate*, dan efektivitas berbagai segmentasi (Platform, Usia, Perangkat, dan Regional).

**Poin Utama Analisis:**
- **Evaluasi KPI Keseluruhan:** Mengukur metrik kunci secara komprehensif, mencakup total biaya (Cost), total pendapatan (Revenue), tingkat konversi (Conversion Rate), dan ROAS secara agregat.
- **Kinerja per Channel:** Analisis performa platform iklan seperti TikTok Ads, Instagram Ads, Shopee Ads, dan Google Ads untuk mengidentifikasi channel dengan akuisisi dan pendapatan tertinggi.
- **Segmentasi Pelanggan:** Menganalisis *audience* berdasarkan Perangkat (Mobile vs. Desktop), Kelompok Usia (18-24, 25-34, 35-44), dan Regional di Indonesia untuk melihat segmen mana yang memberikan ROAS terbesar.
- **Analisis Funnel (Funnel Drops):** Melacak efektivitas perjalanan pengguna dari *Impressions* -> *Clicks* -> *Add to Cart* -> *Conversions*, untuk mengidentifikasi titik *drop-off* tertinggi.
- **Analisis Tren Waktu:** Memonitor tren harian, pergerakan trafik pada akhir pekan, serta hari khusus (*double discount*).

Laporan ini dirancang untuk memberikan informasi yang terstruktur dalam optimalisasi alokasi budget kampanye digital di masa mendatang agar memperoleh margin keuntungan maksimal.

---

## 🗂️ Rangkuman Data Dictionary
Proyek ini menggunakan dataset sintetis (buatan) yang menyimulasikan kinerja kampanye pemasaran spesifik di bidang retail kecantikan (*beauty retail*). Data ini mencakup berbagai kondisi realistis seperti *missing values* dan *outliers* untuk menguji kemampuan pembersihan dan analisis data.

- **Total Data:** ~35.000 baris observasi.
- **Periode Waktu:** 180 Hari pengamatan (Januari - Juni 2023).

**Struktur Utama Dataset:**
1. **Atribut Kampanye:** `date`, `channel` (TikTok, IG, Google, Shopee), `campaign_name`, `campaign_type` (Awareness, Conversion, Retargeting).
2. **Segmentasi Audiens:** `region` (Jabodetabek, Jawa Barat, dll), `device` (Mobile, Desktop), `audience_age_group` (18-24, 25-34, 35-44).
3. **Produk:** `product_category` (Skincare, Makeup, Bodycare), `product_price_tier` (Low, Mid, High).
4. **Metrik Funnel & Finansial:**
   - **`impressions`**: Total tayangan iklan.
   - **`clicks`**: Total klik pada iklan.
   - **`add_to_cart`**: Total penambahan ke keranjang belanja.
   - **`conversions`**: Total transaksi yang berhasil terjadi.
   - **`cost`** (IDR): Biaya penayangan iklan.
   - **`revenue`** (IDR): Estimasi pendapatan yang dihasilkan dari konversi.

> **Catatan:** Dataset ini dirancang untuk simulasi analitik lanjutan termasuk *Data Cleansing* dan *ROI Optimization*. Selengkapnya mengenai deskripsi setiap kolom dapat dilihat pada file `DATA_DICTIONARY.md`.
