import streamlit as st
import pandas as pd
import plotly.express as px

st.title('🎈 Streamlit test')

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
    gender = st.selectbox('Gender', ('female', 'male'))


st.subheader('Data Visualization')
fig = px.scatter(
    df,
    x='bill_length_mm',
    y = 'bill_depth_mm',
    color='island',
    title='Bill length vs. Bill Depth by Island'
)
st.plotly_chart(fig)

fig2=px.histogram(
    df,
    x='body_mass_g',
    nbins=30,
    title='Distribution of Body Mass'
)

st.plotly_chart(fig2)

data = {
    'island': island,
    'bill_length_mm': bill_length_mm,
    'bill_depth_mm': bill_depth_mm,
    'flipper_length_mm': flipper_length_mm,
    'body_mass_g': body_mass_g,
    'sex': gender
}

input_df = pd.DataFrame(data, index=[0])
input_penguins = pd.concat([input_df, X_row], axis=0)

with st.expander('Input features'):
    st.write('**Input plugins**')
    st.datafframe(input_df)
    st.write('**Combined penguins data**')
    st.dataframe(input_penguins)

encode = ['island', 'sex']
df.penguins = pd.get_dummies(input_penguins, prefix=encode)

X = df_penguins[1:]
input_row = df_penguins[:1]

target_mapper = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
def target_encode(val):
    return target_mapper[val]

y = y_raw.apply(target_encode)

with st.expander('Data preparation'):
    st.write('**Encoded X (input penguin)**')
    st.dataframe(input_row)
    st.write('**Encoded y **')
    st.write(y)
    
