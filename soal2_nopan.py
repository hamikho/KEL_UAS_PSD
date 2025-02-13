import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import home
import numpy as np

def run():
    st.title("Soal 2: Analisis Hubungan Suhu dengan Peminjaman Sepeda")
    st.write("Analisis oleh Nopan Rizki Ramdani - 10123199")
    
    # Mengambil dataset yang sudah dibersihkan dari home.py
    day = home.DATA_DAY  # Menggunakan dataset 'day' yang sudah dibersihkan dari home.py
    
    # Menyaring data untuk musim dingin (Desember, Januari, Februari)
    winter_data = day[day['month'].isin([12, 1, 2])]

    # Menyaring data untuk hari kerja di musim dingin
    workingday_winter = winter_data[winter_data['workingday'] == 1]
    
    st.subheader("Deskripsi Data")
    st.write(workingday_winter[['temp', 'cnt']].describe())
    
    # Scatter plot
    st.subheader("Scatter Plot: Hubungan Suhu dengan Peminjaman Sepeda")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(workingday_winter['temp'], workingday_winter['cnt'], color='blue', alpha=0.5)
    ax.set_title('Hubungan Suhu dengan Peminjaman Sepeda pada Hari Kerja di Musim Dingin')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Jumlah Peminjaman Sepeda')
    ax.grid(True)
    st.pyplot(fig)
    
    # Korelasi antara suhu dan peminjaman sepeda
    correlation = workingday_winter[['temp', 'cnt']].corr().iloc[0, 1]
    st.subheader("Korelasi antara Suhu dan Peminjaman Sepeda")
    st.write(f"Nilai korelasi: {correlation:.2f}")
    
    # Histogram untuk distribusi suhu dan jumlah peminjaman
    st.subheader("Distribusi Suhu dan Peminjaman Sepeda")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.histplot(workingday_winter['temp'], bins=20, kde=True, ax=axes[0], color='orange')
    axes[0].set_title("Distribusi Suhu di Musim Dingin")
    axes[0].set_xlabel("Suhu (°C)")
    
    sns.histplot(workingday_winter['cnt'], bins=20, kde=True, ax=axes[1], color='green')
    axes[1].set_title("Distribusi Peminjaman Sepeda")
    axes[1].set_xlabel("Jumlah Peminjaman Sepeda")
    
    st.pyplot(fig)
    
    # Regresi Linear tanpa sklearn
    st.subheader("Regresi Linear Sederhana: Prediksi Peminjaman Sepeda berdasarkan Suhu")
    X = workingday_winter['temp'].values
    y = workingday_winter['cnt'].values
    
    # Perhitungan manual regresi linear
    mean_x, mean_y = np.mean(X), np.mean(y)
    b1 = sum((X - mean_x) * (y - mean_y)) / sum((X - mean_x) ** 2)
    b0 = mean_y - b1 * mean_x
    
    # Prediksi nilai
    x_range = np.linspace(X.min(), X.max(), 100)
    y_pred = b0 + b1 * x_range
    
    # Plot hasil regresi
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(X, y, color='blue', alpha=0.5, label="Data Asli")
    ax.plot(x_range, y_pred, color='red', linewidth=2, label="Regresi Linear")
    ax.set_title('Regresi Linear: Hubungan Suhu dengan Peminjaman Sepeda')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Jumlah Peminjaman Sepeda')
    ax.legend()
    st.pyplot(fig)
    
    # Menampilkan persamaan regresi
    st.write(f"Persamaan regresi: cnt = {b1:.2f} * temp + {b0:.2f}")
    
    # Menampilkan interpretasi
    st.subheader("Interpretasi Analisis")
    if correlation > 0:
        st.write("Terdapat korelasi positif antara suhu dan jumlah peminjaman sepeda, artinya semakin hangat suhu, semakin banyak peminjaman sepeda.")
    else:
        st.write("Terdapat korelasi negatif atau lemah antara suhu dan jumlah peminjaman sepeda, artinya suhu mungkin bukan faktor utama yang mempengaruhi peminjaman.")
    
    st.write("Regresi linear menunjukkan bahwa setiap kenaikan 1°C dalam suhu berhubungan dengan peningkatan sekitar {:.2f} peminjaman sepeda.".format(b1))

# Jika dijalankan langsung (bukan dari import)
if __name__ == "__main__":
    run()
