import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import home  # Pastikan modul ini sudah berisi DATA_DAY

def run():
    st.title("Analisis Lanjutan Peminjaman Sepeda")
    st.write("Menampilkan berbagai analisis peminjaman sepeda berdasarkan musim, cuaca, dan faktor lainnya - 10123180 - Sendi Fauzan")

    # Load dataset
    day = home.DATA_DAY

    # 1. Total Peminjaman Sepeda per Musim (Bar Chart)
    st.subheader("1. Total Peminjaman Sepeda per Musim")
    musim_data = day.groupby('season')['cnt'].sum()
    musim_label = {1: 'Musim Dingin', 2: 'Musim Panas', 3: 'Musim Semi', 4: 'Musim Gugur'}
    musim_data.index = musim_data.index.map(musim_label)

    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=musim_data.index, y=musim_data.values, palette="viridis", ax=ax1)
    ax1.set_title("Total Peminjaman Sepeda per Musim")
    ax1.set_xlabel("Musim")
    ax1.set_ylabel("Total Peminjaman")
    st.pyplot(fig1)

    # 2. Rata-rata Peminjaman per Hari di Setiap Musim
    st.subheader("2. Rata-rata Peminjaman Sepeda per Hari di Setiap Musim")
    avg_musim_data = day.groupby('season')['cnt'].mean()
    avg_musim_data.index = avg_musim_data.index.map(musim_label)

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=avg_musim_data.index, y=avg_musim_data.values, palette="magma", ax=ax2)
    ax2.set_title("Rata-rata Peminjaman Sepeda per Hari di Setiap Musim")
    ax2.set_xlabel("Musim")
    ax2.set_ylabel("Rata-rata Peminjaman per Hari")
    st.pyplot(fig2)

    # 3. Pengaruh Cuaca terhadap Peminjaman Sepeda
    st.subheader("3. Pengaruh Cuaca terhadap Peminjaman Sepeda")
    cuaca_data = day.groupby('weathersit')['cnt'].sum()
    cuaca_label = {1: 'Cerah', 2: 'Berkabut', 3: 'Hujan Ringan', 4: 'Hujan Lebat'}
    cuaca_data.index = cuaca_data.index.map(cuaca_label)

    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=cuaca_data.index, y=cuaca_data.values, palette="coolwarm", ax=ax3)
    ax3.set_title("Pengaruh Cuaca terhadap Peminjaman Sepeda")
    ax3.set_xlabel("Kondisi Cuaca")
    ax3.set_ylabel("Total Peminjaman")
    st.pyplot(fig3)

    # 4. Peminjaman Sepeda Berdasarkan Hari Kerja vs Hari Libur
    st.subheader("4. Peminjaman Sepeda Berdasarkan Hari Kerja vs Hari Libur")
    hari_data = day.groupby('workingday')['cnt'].sum()
    hari_label = {0: 'Hari Libur', 1: 'Hari Kerja'}
    hari_data.index = hari_data.index.map(hari_label)

    fig4, ax4 = plt.subplots(figsize=(8, 6))
    ax4.pie(hari_data, labels=hari_data.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen'])
    ax4.set_title("Peminjaman Sepeda Berdasarkan Hari Kerja vs Hari Libur")
    st.pyplot(fig4)


# Jika dijalankan langsung (bukan dari import)
if __name__ == "__main__":
    run()