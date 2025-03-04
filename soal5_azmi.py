import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import home

def run():
    st.title("Soal 5")
    st.write("Ini adalah konten untuk Soal 5.")
    st.write("Silakan edit konten ini sesuai kebutuhan.")

    # Load data
    day = home.DATA_DAY  # Menggunakan dataset 'day' yang sudah dibersihkan dari home.py

    # Kelompokkan data berdasarkan kondisi cuaca (weathersit) dan jumlahkan peminjaman sepeda (cnt)
    weather_data = (day.groupby('weathersit')['cnt'].sum() / day['cnt'].sum()) * 100

    # Membuat label yang sesuai untuk kondisi cuaca
    weather_labels = {
        1: 'Cerah',
        2: 'Berawan',
        3: 'Hujan',
        4: 'Hujan Badai'
    }

    # Ganti index dengan label kondisi cuaca yang lebih deskriptif
    weather_data.index = weather_data.index.map(weather_labels)

    # Soal
    st.title("1. Kondisi cuaca mana yang paling banyak peminjaman sepeda?")
    st.write("""
        Kondisi cuaca yang paling banyak peminjaman sepeda adalah saat cuaca cerah karena lebih aman untuk bersepeda tanpa ada halangan hujan, badai, atau banjir.
        Untuk lebih jelasnya bisa dilihat dari grafik berikut!!
    """)

    st.title("2. Kondisi cuaca mana yang paling sedikit peminjaman sepeda?")
    st.write("""
        Kondisi cuaca yang paling sedikit peminjaman sepeda adalah saat hujan badai karena sangat berbahaya untuk bersepeda, dapat terjadi kecelakaan yang fatal.
        Untuk lebih jelasnya bisa dilihat dari grafik berikut!!
    """)

    # Streamlit UI
    st.header("Data Peminjaman Sepeda Berdasarkan Kondisi Cuaca")

    # Membuat bar chart
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(weather_data.index, weather_data, color=['skyblue', 'lightgreen', 'orange', 'red'])

    # Menampilkan nilai persentase di atas batang
    for i, v in enumerate(weather_data):
        ax.text(i, v + 1, f"{v:.1f}%", ha='center', fontsize=10)

    ax.set_xlabel("Kondisi Cuaca", fontsize=12)
    ax.set_ylabel("Persentase Peminjaman Sepeda (%)", fontsize=12)
    ax.set_title("Peminjaman Sepeda Berdasarkan Kondisi Cuaca", fontsize=14)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Tampilkan chart di Streamlit
    st.pyplot(fig)

# Jika dijalankan langsung (bukan dari import)
if __name__ == "__main__":
    run()
