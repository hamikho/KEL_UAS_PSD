import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import home

def run():
    st.title("Soal 4")
    st.write("Ini adalah konten untuk Soal 4.")
    st.write("Menampilklan banyak penyewa perminggu menggukan histogram?- 10123181 - Muhamad Dzaky Abdullah")
    
    st.title("Analisis Penyewaan Sepeda")

    # Mengambil dataset yang sudah dibersihkan dari home.py
    day = home.DATA_DAY
    
    # Plot histogram jumlah penyewa per minggu
    day["dteday"] = pd.to_datetime(day["dteday"])
    day["week_number"] = day["dteday"].dt.isocalendar().week
    day["year"] = day["dteday"].dt.year
    day["month"] = day["dteday"].dt.month
    day["weekday"] = day["dteday"].dt.day_name()

    # Filter tahun untuk memilih tahun
    selected_year = st.selectbox("Pilih Tahun", day["year"].unique())
    filtered_data = day[day["year"] == selected_year]

    # Analisis dan visualisasi
    # Analisis Distribusi Penyewaan Sepeda per Minggu
    st.header("1. Distribusi Penyewaan Sepeda per Minggu Dalam Setahun")
    weekly_rentals = filtered_data.groupby("week_number")["cnt"].sum() # Menghitung total penyewa per minggu
    # Plot histogram jumlah penyewa per minggu
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(weekly_rentals.index, weekly_rentals.values, color="lightcoral", edgecolor="black")
    # Menyesuaikan label dan judul
    ax.set_xlabel("Minggu ke-")
    ax.set_ylabel("Jumlah Penyewa Sepeda")
    ax.set_title("Distribusi Penyewaan Sepeda per Minggu")
    st.pyplot(fig)# Menampilkan plot
    st.write("Dilihat dari histogram di atas pada 2011 penyewaan terbanyak ada di minggu ke-26 dan penyewaan terendah ada di minggu ke-4. Sedangkan pada 2012 penyewaan terbanyak ada di minggu ke-37 dan penyewaan terendah ada di minggu ke-52")

    # Analisis Tren Penyewaan Sepeda per Bulan
    st.header("2. Tren Penyewaan Sepeda per Bulan")
    monthly_rentals = filtered_data.groupby("month")["cnt"].sum()# Menghitung total penyewa per bulan
    # Plot grafik jumlah penyawa per bulan
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(monthly_rentals.index, monthly_rentals.values, marker="o", color="blue", linestyle="-")
    # Menyesuaikan label dan judul
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penyewa Sepeda")
    ax.set_title("Tren Penyewaan Sepeda per Bulan")
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    st.pyplot(fig)# Menampilkan plot
    st.write("Dari grafik di atas bisa dilihat pada 2011 grafik dari bulan januari hingga bulan juni cendurung menaik dan pada pertengahan bulan juni hingga bulan desember grafik mulai menurun. Sedangkan pada grafik penyewaan 2012 bulan januari hingga september grafik penyewaan cenderung naik dan pada pertengahan bulan september grafik mulai menurun hingga desember. ")

    # Analisis Distribusi Penyewaan Sepeda per Hari dalam Seminggu
    st.header("3. Distribusi Penyewaan Sepeda per Hari dalam Seminggu")
    weekday_rentals = filtered_data.groupby("weekday")["cnt"].sum().reindex(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])# Menghitung total penyewa per hari
    # Plot histogram jumlah penyawa per hari
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(weekday_rentals.index, weekday_rentals.values, color="green", edgecolor="black")
    # Menyesuaikan label dan judul
    ax.set_xlabel("Hari dalam Seminggu")
    ax.set_ylabel("Jumlah Penyewa Sepeda")
    ax.set_title("Distribusi Penyewaan Sepeda per Hari dalam Seminggu")
    st.pyplot(fig)# Menampilkan plot
    st.write("Dilihat dari histogram di atas terlihat penyewaan terbanyak pada tahun 2011 ada di hari senin, selasa, dan jumat sedangkan penyewaan terendah ada di hari rabu. Sedangkan pada 2012 penyewaan terbanyak ada di hari kamis dan penyewaan terendah ada di hari minggu.")

if __name__ == "__main__":
    run()
