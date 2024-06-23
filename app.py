import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as px
import streamlit as st
import os


# Título de la aplicación
st.title("Problemáticas y Estigmas de las Enfermedades Mentales en la Industria Tecnológica Estadounidense 2016-2019")

# Crea un menú de pestañas
tab1, tab2 = st.tabs(["Introducción", "Datos"])

# Contenido de la página 1
with tab1:
    st.header("Introducción")
    st.write("Información de la Data Suministrada.")

# Contenido de la página 2
with tab2:
    st.header("Visualización de los Datos")
    st.write("Información de la Data Suministrada.")

@st.cache
def load_csv(file_path):
    return pd.read_csv(file_path)

# Leer archivos CSV
df_2016 = load_csv('CSV/Investigacion1.csv')
df_2017 = load_csv('CSV/Investigacion2.csv')
df_2018 = load_csv('CSV/Investigacion3.csv')
df_2019 = load_csv('CSV/Investigacion4.csv')

# Crea un selectbox con las opciones
option = st.selectbox('Año de Encuesta:', ['2016', '2017', '2018', '2019'])

# Muestra el DataFrame correspondiente según la opción seleccionada
if option == '2016':
    st.dataframe(df_2016)
elif option == '2017':
    st.dataframe(df_2017)
elif option == '2018':
    st.dataframe(df_2018)
elif option == '2019':
    st.dataframe(df_2019)

