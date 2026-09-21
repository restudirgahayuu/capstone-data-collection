import pandas as pd
import requests
from pathlib import Path


# Folder penyimpanan data
RAW_DATA_DIR = Path("data/raw")
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


# =========================
# 1. Membaca data E-Commerce
# =========================
ecommerce_file = RAW_DATA_DIR / "ecommerce_sales_data.csv"

if ecommerce_file.exists():
    ecommerce_data = pd.read_csv(ecommerce_file)
    print("Data e-commerce berhasil dibaca.")
    print(f"Jumlah baris: {len(ecommerce_data)}")
else:
    print("File ecommerce_sales_data.csv tidak ditemukan.")


# =========================
# 2. Mengambil data cuaca
# =========================
url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=-5.1477"
    "&longitude=119.4327"
    "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
    "&timezone=auto"
)

response = requests.get(url, timeout=30)
response.raise_for_status()

weather_json = response.json()

weather_data = pd.DataFrame({
    "date": weather_json["daily"]["time"],
    "temperature_max": weather_json["daily"]["temperature_2m_max"],
    "temperature_min": weather_json["daily"]["temperature_2m_min"],
    "precipitation_sum": weather_json["daily"]["precipitation_sum"]
})


# =========================
# 3. Menyimpan data cuaca
# =========================
weather_file = RAW_DATA_DIR / "weather_data.csv"
weather_data.to_csv(weather_file, index=False)

print("Data cuaca berhasil diambil dari Open-Meteo.")
print(f"Data cuaca disimpan ke: {weather_file}")
print(f"Jumlah data cuaca: {len(weather_data)}")
