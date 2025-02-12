import streamlit as st
import pandas as pd
import soal1_sendi
import soal2_nopan
import soal3_ziddan
import soal4_dzaky
import soal5_azmi
import soal6_viezal

# Navbar
st.sidebar.title("Navigasi")
option = st.sidebar.radio(
    "Pilih Halaman:", 
    ("Home", "Soal 1", "Soal 2", "Soal 3", "Soal 4", "Soal 5", "Soal 6"), 
    key="sidebar_menu"
)


# Load dataset
day = pd.read_csv('day.csv')
hour = pd.read_csv('hour.csv')

# Data Cleaning
day = day.dropna().dropna(axis=1).drop_duplicates()
hour = hour.dropna().dropna(axis=1).drop_duplicates()

# Konversi kolom tanggal
day['dteday'] = pd.to_datetime(day['dteday'])
day['month'] = day['dteday'].dt.month

# Simpan hasil cleaning agar bisa digunakan di Soal 1
day.to_csv('day_cleaned.csv', index=False)
hour.to_csv('hour_cleaned.csv', index=False)

# Menyediakan dataset agar bisa diimpor ke soal lain
DATA_DAY = day
DATA_HOUR = hour

# Tampilkan halaman sesuai pilihan
if option == "Home":
    
    st.title("KELOMPOK 3 PSD PROJEK TUGAS BESAR")
    st.title("Analisis day.csv dan hour.csv")
    st.write("Nama Anggota:")
    st.write("[SENDI FAUZAN                - 10123180]")
    st.write("[MUHAMMAD ZIDDAN ARYAN       - 10123185]")
    st.write("[NOPAN RIZKI RAMDANI         - 10123199]")
    st.write("[MUHAMAD DZAKY ABDULLAH      - 10123181]")
    st.write("[MUHAMMAD AZMI FADHLUROHMMAN - 10123192]")
    st.write("[VIEZAL NABIL DZAIKRA        - 10123192]")



elif option == "Soal 1":
    soal1_sendi.run()

elif option == "Soal 2":
    soal2_nopan.run()

elif option == "Soal 3":
    soal3_ziddan.run()

elif option == "Soal 4":
    soal4_dzaky.run()

elif option == "Soal 5":
    soal5_azmi.run()

elif option == "Soal 6":
    soal6_viezal.run()
