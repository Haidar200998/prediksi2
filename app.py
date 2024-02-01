import streamlit as st
import pandas as pd
import pickle

# Memuat model yang disimpan
model = pickle.load(open('trained_model.pkl', 'rb'))

# Membuat antarmuka pengguna di Streamlit
st.title("Prediksi Harga Emas")

# Membuat form input untuk fitur-fitur
with st.form("prediction_form"):
    st.write("Silakan masukkan informasi berikut:")
    ihsg = st.number_input("Nilai IHSG", min_value=0.0, max_value=10000.0, value=5000.0)
    usd_rate = st.number_input("Nilai Kurs USD", min_value=0.0, max_value=20000.0, value=14000.0)
    inflation = st.number_input("Tingkat Inflasi", min_value=0.0, max_value=100.0, value=3.0)
    submit_button = st.form_submit_button("Prediksi")

# Proses input dan buat prediksi menggunakan model
if submit_button:
    input_data = pd.DataFrame([[ihsg, usd_rate, inflation]], columns=['IHSG', 'Kurs Jual', 'Data Inflasi'])
    prediction = model.predict(input_data)

    # Tampilkan hasil prediksi
    st.subheader("Hasil Prediksi Harga Emas:")
    st.write("Prediksi Harga Emas:", prediction[0])
