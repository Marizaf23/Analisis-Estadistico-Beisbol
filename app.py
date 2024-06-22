# %%
import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as px
import streamlit as st


# Título de la aplicación
st.title("Problemáticas y Estigmas de las Enfermedades Mentales en la Industria Tecnológica Estadounidense 2016-2019")

# Crea un menú de pestañas
tab1, tab2 = st.tabs(["Página 1", "Página 2"])

# Contenido de la página 1
with tab1:
    st.header("Datos")
    st.write("Información de la Data Suministrada.")

# Carga los DataFrames desde los archivos.csv
df_2016 = pd.read_csv('Investigacion1.csv')
df_2017 = pd.read_csv('Investigacion2.csv')
df_2018 = pd.read_csv('Investigacion3.csv')
df_2019 = pd.read_csv('Investigacion4.csv')

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

st.write("""
## Introducción

El conjunto de datos **Iris** es uno de los conjuntos de datos más conocidos en la comunidad de ciencia de datos. Este conjunto de datos fue introducido por el biólogo y estadístico británico Ronald A. Fisher en su artículo de 1936 "The use of multiple measurements in taxonomic problems". El conjunto de datos contiene 150 observaciones de iris con cuatro características: longitud del sépalo, anchura del sépalo, longitud del pétalo y anchura del pétalo. Además, cada observación pertenece a una de las tres especies de iris: Iris setosa, Iris versicolor o Iris virginica.

En esta aplicación, exploraremos el conjunto de datos Iris mediante gráficos y estadísticas descriptivas. A continuación, se muestra una tabla con las primeras filas del conjunto de datos.
""")