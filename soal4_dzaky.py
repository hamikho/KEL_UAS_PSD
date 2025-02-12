import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import home

def run():
    st.title("Soal 4")
    st.write("Ini adalah konten untuk Soal 4.")
    st.write("Menampilklan banyak penyewa perminggu menggukan histogram?- 10123181 - Muhamad Dzaky Abdullah")
    
    st.title("Analisis Penyewaan Sepeda")

    # Mengambil dataset yang sudah dibersihkan dari home.py
    day = home.DATA_DAY  # Menggunakan dataset 'day' yang sudah dibersihkan dari home.py
    
    # Plot histogram jumlah penyewa per minggu
    day["dteday"] = pd.to_datetime(day["dteday"])
    day["week_number"] = day["dteday"].dt.isocalendar().week
    
    # Menghitung total penyewa per minggu
    weekly_rentals = day.groupby("week_number")["cnt"].sum()

    # Menyesuaikan label dan judul
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(weekly_rentals.index, weekly_rentals.values, color="lightcoral", edgecolor="black")
    ax.set_xlabel("Minggu ke-")
    ax.set_ylabel("Jumlah Penyewa Sepeda")
    ax.set_title("Distribusi Penyewaan Sepeda per Minggu dalam Setahun")

    # Menampilkan plot
    st.pyplot(fig)
    
# Jika dijalankan langsung (bukan dari import)
if __name__ == "__main__":
    run()
