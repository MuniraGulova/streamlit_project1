import streamlit as st
import pandas as pd

st.title('🎈 Tojikiston ba pesh')

st.write('Welcome 🌸🌸🌸🌸 !')


df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

with st.expander('Data'):
    st.write('X')
    X_row = df.drop("species", axis=1)
    st.dataframe(X_row)

    st.write("y")
    y_row=df.species
    st.dataframe(X_row)


with st.sidebar:
    st.header("Введите признаки: ")
    island=st.selectbox('island', ('forgersen', 'Dream', 'Biscoe'))
    bill_length_mm = st.slider('Bill length (mm)', 32.1, 999.6, 44.5)
    bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.3)
    flipper_length_mm = st.slider('Flipper length (mm)', 32.1, 59.6, 44.5)
    body_mass_g = st.slider('Body mass (g)', 32.1, 59.6, 44.5)
    gender = st.selectbox('Gender', ('feamle', 'male'))
