# Data Dictionary: Synthetic Beauty Marketing Data

> [!WARNING]
> **DISCLAIMER**: Dataset ini adalah **data sintetis (buatan)** yang di-generate menggunakan skrip Python secara terkomputerisasi. Data ini **TIDAK** didasarkan pada data pelanggan, kampanye, atau transaksi aktual dari perusahaan atau individu mana pun, melainkan murni untuk tujuan simulasi, pembelajaran, *dashboarding*, dan pengujian model pada skenario *marketing analytics*.

## Ringkasan Dataset
Dataset ini merepresentasikan kinerja *digital marketing* dari sebuah brand *beauty retail* fiktif selama 6 bulan (180 hari). Tersedia metrik di berbagai tingkatan dalam funnel marketing (mulai dari tayangan iklan hingga konversi akhir) untuk beberapa saluran pemasaran digital dan tingkat segmentasi audiens. Data juga telah sengaja "dikotori" dengan *noise* (contoh: *missing values*, duplikasi data, anomali pada *funnel*) demi menyimulasikan tantangan analisis pada *data wrangling* di dunia nyata.

- **Total Data**: ~35.000 baris
- **Total Kolom**: 15 kolom
- **Periode Waktu**: 1 Januari 2023 - 29 Juni 2023 (180 Hari)
- **Mata Uang**: Rupiah (IDR)

---

## Keterangan Kolom (Data Schema)

| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `date` | Date/String | Tanggal observasi metrik (Format: YYYY-MM-DD). Terdapat tren kenaikan metrik pada akhir pekan dan tanggal *double discount* (02-02, 03-03, dst). |
| `channel` | Kategorikal | Platform *digital marketing* tempat berjalannya kampanye. Terdiri dari: `TikTok Ads`, `Instagram Ads`, `Shopee Ads`, dan `Google Ads`. |
| `campaign_name` | String | Nama unik dari setiap percobaan kampanye, merepresentasikan genre / pendekatan iklannya. |
| `campaign_type` | Kategorikal | Tujuan atau fungsi utama kampanye iklan. Terbagi menjadi 3 jenis: `Awareness` (Tujuan impresi luas), `Conversion` (Tujuan transaksi), dan `Retargeting` (Membidik kembali pelanggan lama). |
| `region` | Kategorikal | Target area pemirsa iklan di Indonesia. Terdiri atas: `Jabodetabek`, `Jawa Barat`, `Jawa Tengah`, `Jawa Timur`, `Sumatera`, `Kalimantan`, `Sulawesi`, `Bali & Nusa Tenggara`, `Indonesia Timur`. |
| `device` | Kategorikal | Tipe perangkat klien yang melihat dan mengeklik tayangan. Kombinasi: `Mobile` dan `Desktop`. |
| `audience_age_group` | Kategorikal | Rentang usia target kampanye. Terdapat tiga klasifikasi: `18-24`, `25-34`, dan `35-44`. |
| `product_category` | Kategorikal | Jenis lini barang dagangan *beauty retail* yang di iklankan. Terdiri dari `Skincare`, `Makeup`, dan `Bodycare`. |
| `product_price_tier` | Kategorikal | Klasifikasi strata harga item yang dijajakan pada kampanye: `Low`, `Mid`, dan `High`. |
| **`impressions`** | Integer | Frekuensi pemunculan iklan di medium digital penggunanya. |
| **`clicks`** | Integer | Total pelanggan yang mengeklik iklan setelah melihat tayangan (*impressions*). Kemungkinan ada *missing values* (Data disengaja kosong < NaN >). |
| **`add_to_cart`** | Integer | Total barang yang telah dimasukkan ke dalam keranjang pengguna (setingkat lebih dekat dengan transaksi) pasca-klik iklan. Kemungkinan juga terdapat *missing values*. |
| **`conversions`** | Integer | Jumlah terjadinya pembelian tuntas dari rentetan peristiwa yang ditarget oleh kampanye iklan. Berpotensi mengandung kekosongan nilai (NaN), bahkan sengaja dibuat cacat *funnel* (jumlah konversi lebih banyak daripada jumlah penambahan keranjang). |
| **`cost`** | Float | Evaluasi total biaya (Rupiah - IDR) yang dibelanjakan *advertiser* pada kampanye di hari tersebut. Angka didesain serealistis CPC pasaran (Rp1.500 - Rp3.500). Terdapat disfungsi data *outlier* di sebagian nilai acak demi pengujian. |
| **`revenue`** | Float | Estimasi pendapatan teralisasi (Rupiah - IDR) pada seluruh proses konversi. Nominal asumtif di *bracket* harga ritel rata-rata Beauty di Indonesia Rp 50.000 hingga Rp 300.000,- / Conversions. |

## Contoh Skenario Penggunaan
Dataset sintetis ini sangat cocok untuk:
1. **Analisis Konversi (Funnel Drops)**: Memeriksa laju *drop-off* antara Clicks &rarr; Add to Cart &rarr; Conversions.
2. **Perhitungan Atribusi & ROI (Return on Investment)**: Menganalisis *channel* dan tipe perangkat manakah yang mendatangkan nilai `revenue` terbanyak bila dikomparasi secara proporsional dengan `cost`.
3. **Data Cleansing Case Studies**: Menangani isu kualitas data marketing di dunia industri berupa NaN values, cacat logika numerik dalam porsi kecil, dan observasi identik/redundan (Duplicate rows).
