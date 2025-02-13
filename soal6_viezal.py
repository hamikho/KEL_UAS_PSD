import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.title("Soal 6")
    st.write("Bagaimana pengaruh suhu terhadap peminjaman pada musim panas? - 10123213 - Viezal Nabil Dzaikra")

    #membaca dataset dari file day.csv
    day = pd.read_csv('day.csv')

    #Pastikan kolom 'dteday' adalah datetime
    day['dteday'] = pd.to_datetime(day['dteday'])

    #Menambahkan kolom bulan dan musim
    day['month'] = day['dteday'].dt.month

    #Memfilter data untuk musim Panas (Maret, April, Mei)
    summer_data = day[day['month'].isin([3, 4, 5])]

    #Membuat scatter plot untuk melihat hubungan suhu dengan peminjaman sepeda
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(summer_data['temp'], summer_data['cnt'], color='orange', alpha=0.5)
    ax.set_title('Hubungan Suhu dengan Peminjaman Sepeda pada Musim Panas')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Jumlah Peminjaman Sepeda')
    ax.grid(True)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

    # Jika dijalankan langsung (bukan dari import)
if __name__ == "__main__":
    run()