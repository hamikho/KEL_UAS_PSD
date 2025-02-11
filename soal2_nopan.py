import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import home

def run():
    st.title("Soal 2")
    st.write("Ini adalah konten untuk Soal 2.")
    st.write("Silakan edit konten ini sesuai kebutuhan.")
    # Mengambil dataset yang sudah dibersihkan dari home.py
    day = home.DATA_DAY  # Menggunakan dataset 'day' yang sudah dibersihkan dari home.py

    # Menyaring data untuk musim dingin (Desember, Januari, Februari)
    winter_data = day[day['month'].isin([12, 1, 2])]

    # Menyaring data untuk hari kerja di musim dingin
    workingday_winter = winter_data[winter_data['workingday'] == 1]

    # Menampilkan judul dan deskripsi aplikasi
    st.title("Hubungan Suhu dengan Peminjaman Sepeda pada Hari Kerja di Musim Dingin")
    st.write("""
        Hubungan antara suhu dan jumlah peminjaman sepeda pada hari kerja di musim dingin
        (Desember, Januari, dan Februari). Data yang digunakan sudah dibersihkan dan disaring untuk musim dingin.
    """)

    # Menampilkan scatter plot
    st.subheader("Scatter Plot: Hubungan Suhu dengan Peminjaman Sepeda")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(workingday_winter['temp'], workingday_winter['cnt'], color='blue', alpha=0.5)
    ax.set_title('Hubungan Suhu dengan Peminjaman Sepeda pada Hari Kerja di Musim Dingin')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Jumlah Peminjaman Sepeda')
    ax.grid(True)
    st.pyplot(fig)

    # Menghitung korelasi antara suhu dan peminjaman sepeda
    correlation = workingday_winter[['temp', 'cnt']].corr()

    # Menampilkan hasil korelasi
    st.subheader("Korelasi antara Suhu dan Peminjaman Sepeda")
    st.write(correlation)

# Jika dijalankan langsung (bukan dari import)
if __name__ == "__main__":
    run()
