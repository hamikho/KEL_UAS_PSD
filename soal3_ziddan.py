import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import home  # Asumsikan home.py adalah file yang berisi dataset yang sudah dibersihkan

def run():
    st.title("Soal 3: Analisis Peminjaman Sepeda pada Hari Libur di Musim Panas")
    st.write("Ini adalah konten untuk Soal 3(Muhammad Ziddan Aryan - 10123185).")
    st.write("Silakan edit konten ini sesuai kebutuhan.")
    
    # Mengambil dataset yang sudah dibersihkan dari home.py
    day = home.DATA_DAY  # Menggunakan dataset 'day' yang sudah dibersihkan dari home.py

    # Menyaring data untuk musim panas (Juni, Juli, Agustus)
    summer_data = day[day['month'].isin([6, 7, 8])]

    # Menyaring data untuk hari libur di musim panas
    holiday_summer = summer_data[summer_data['holiday'] == 1]

    # Menampilkan judul dan deskripsi aplikasi
    st.title("Hubungan Suhu dengan Peminjaman Sepeda pada Hari Libur di Musim Panas")
    st.write("""
        Analisis ini mengeksplorasi hubungan antara suhu dan jumlah peminjaman sepeda pada hari libur di musim panas
        (Juni, Juli, dan Agustus). Data yang digunakan sudah dibersihkan dan disaring untuk musim panas.
    """)

    # Menampilkan statistik dasar
    st.subheader("Statistik Dasar")
    st.write(f"Rata-rata Peminjaman Sepeda: {holiday_summer['cnt'].mean():.2f}")
    st.write(f"Median Peminjaman Sepeda: {holiday_summer['cnt'].median():.2f}")
    st.write(f"Rata-rata Suhu: {holiday_summer['temp'].mean():.2f} °C")

    # Menampilkan scatter plot
    st.subheader("Scatter Plot: Hubungan Suhu dengan Peminjaman Sepeda")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=holiday_summer, color='orange', alpha=0.6, ax=ax1)
    ax1.set_title('Hubungan Suhu dengan Peminjaman Sepeda pada Hari Libur di Musim Panas')
    ax1.set_xlabel('Suhu (°C)')
    ax1.set_ylabel('Jumlah Peminjaman Sepeda')
    ax1.grid(True)
    st.pyplot(fig1)

    # Menampilkan histogram distribusi peminjaman sepeda
    st.subheader("Histogram: Distribusi Peminjaman Sepeda")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.histplot(holiday_summer['cnt'], bins=20, color='green', kde=True, ax=ax2)
    ax2.set_title('Distribusi Jumlah Peminjaman Sepeda pada Hari Libur di Musim Panas')
    ax2.set_xlabel('Jumlah Peminjaman Sepeda')
    ax2.set_ylabel('Frekuensi')
    st.pyplot(fig2)

    # Menampilkan box plot distribusi suhu
    st.subheader("Box Plot: Distribusi Suhu")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=holiday_summer['temp'], color='purple', ax=ax3)
    ax3.set_title('Distribusi Suhu pada Hari Libur di Musim Panas')
    ax3.set_xlabel('Suhu (°C)')
    st.pyplot(fig3)

    # Menghitung korelasi antara suhu dan peminjaman sepeda
    correlation = holiday_summer[['temp', 'cnt']].corr()

    # Menampilkan hasil korelasi
    st.subheader("Korelasi antara Suhu dan Peminjaman Sepeda")
    st.write(correlation)

    # Perbandingan dengan hari kerja di musim panas
    st.subheader("Perbandingan Peminjaman Sepeda: Hari Libur vs Hari Kerja")
    workingday_summer = summer_data[summer_data['workingday'] == 1]
    comparison_data = {
        'Hari Libur': holiday_summer['cnt'].mean(),
        'Hari Kerja': workingday_summer['cnt'].mean()
    }
    st.write(comparison_data)

    # Menampilkan bar plot untuk perbandingan
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=list(comparison_data.keys()), y=list(comparison_data.values()), palette='coolwarm', ax=ax4)
    ax4.set_title('Perbandingan Rata-rata Peminjaman Sepeda: Hari Libur vs Hari Kerja di Musim Panas')
    ax4.set_ylabel('Rata-rata Peminjaman Sepeda')
    st.pyplot(fig4)

# Jika dijalankan langsung (bukan dari import)
if __name__ == "__main__":
    run()