import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import home

def run():
    st.title("Soal 1")
    st.write("Menampilkan banyak jumlah penyewaan sepeda di masing masing musim menggunakan histogram  - 10123180 - Sendi Fauzan")
   
    # Load dataset (Pastikan file CSV tersedia)
    day = home.DATA_DAY

    # Chart peminjaman sepeda berdasarkan musim
    musim_data = day.groupby('season')['cnt'].sum()

    # Membuat label untuk musim
    musim_label = {1: 'Musim Dingin', 2: 'Musim Panas', 3: 'Musim Semi', 4: 'Musim Gugur'}
    musim_data.index = musim_data.index.map(musim_label)

    # Membuat pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(musim_data, labels=musim_data.index, autopct='%1.1f%%', startangle=90, 
        colors=['skyblue', 'lightgreen', 'orange', 'gold'])
    ax.set_title("Peminjaman Sepeda Berdasarkan Musim")

    # Tampilkan di Streamlit
    st.pyplot(fig)


# Jika dijalankan langsung (bukan dari import)
if __name__ == "__main__":
    run()
