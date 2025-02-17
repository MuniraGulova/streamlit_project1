import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.write('Welcome 🌸🌸🌸🌸 !')


df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

with st.expander('Data'):
    st.write('X')
    X_row = df.drop("species", exis=1)
    st.dataframe(X_row)

    st.write("y")
    y_row=df.species
    st.dataframe(X_row)
