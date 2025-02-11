import streamlit as st
import soal1_sendi
import soal2_nopan
import soal3_ziddan
import soal4_dzaky
import soal5_azmi
import soal6_viezal

# Navbar
st.sidebar.title("Navigasi")
option = st.sidebar.radio("Pilih Halaman:", 
                          ("Home", "Soal 1", "Soal 2", "Soal 3", "Soal 4", "Soal 5", "Soal 6"))

# Tampilkan halaman sesuai pilihan
if option == "Home":
    st.title("Proyek Streamlit")
    st.write("Nama Anggota:")
    st.write("[SENDI FAUZAN_10123180]  |  [MUHAMMAD ZIDDAN ARYAN_10123185]")
    st.write("[NOPAN RIZKI RAMDANI_10123199]  |  [MUHAMAD DZAKY ABDULLAH_10123181]")
    st.write("[MUHAMMAD AZMI FADHLUROHMMAN_10123192]  |  [VIEZAL NABIL DZAIKRA_10123192]")

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
