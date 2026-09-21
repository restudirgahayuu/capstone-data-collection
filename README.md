# Capstone Project - Data Collection E-Commerce

## 1. Deskripsi Proyek

Proyek ini merupakan tugas Capstone pada tahap Data Collection dengan domain permasalahan E-Commerce/Penjualan. Proyek ini bertujuan untuk mengumpulkan dan menyiapkan data penjualan serta data cuaca yang dapat digunakan sebagai sumber data untuk analisis lebih lanjut.

## 2. Sumber Data

### Data 1 - E-Commerce Sales & Profit Analysis

* Sumber: Kaggle
* Format: CSV
* File: `ecommerce_sales_data.csv`
* Jumlah data: 3.500 baris dan 7 kolom
* Periode: 2022-2024
* Variabel: Order Date, Product Name, Category, Region, Quantity, Sales, Profit

### Data 2 - Open-Meteo Weather API

* Sumber: Open-Meteo
* Format: REST API (JSON)
* Lokasi: Makassar, Sulawesi Selatan
* Variabel: tanggal, suhu maksimum, suhu minimum, dan curah hujan
* Satuan: °C dan mm

## 3. Struktur Repository

```text
capstone-data-collection/
├── data/
│   └── raw/
│       ├── ecommerce_sales_data.csv
│       └── weather_data.csv
├── data_collection.py
├── requirements.txt
└── README.md
```

## 4. Data Collection

Proses pengumpulan data dilakukan menggunakan Python. File `data_collection.py` digunakan untuk membaca data e-commerce dari file CSV dan mengambil data cuaca dari Open-Meteo Weather API.

## 5. Requirements

Library Python yang digunakan:

* pandas
* requests

Install library dengan perintah:

```bash
pip install -r requirements.txt
```

## 6. Menjalankan Program

Jalankan file `data_collection.py` dari folder utama repository dengan perintah:

```bash
python data_collection.py
```

Program akan membaca data e-commerce dan mengambil data cuaca dari Open-Meteo, kemudian menyimpan data cuaca ke dalam folder `data/raw/`.
