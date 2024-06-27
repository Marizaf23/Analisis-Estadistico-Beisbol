import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as px
import streamlit as st
import requests
from io import StringIO
import plotly.express as px

# Título de la aplicación
st.title("Problemáticas y Estigmas de las Enfermedades Mentales en la Industria Tecnológica Estadounidense 2016-2019")


st.header("Visualización de los Datos")
st.write("Información de la Data Suministrada.")

@st.cache
def load_csv_from_github(url):
        response = requests.get(url)
        if response.status_code == 200:
            return pd.read_csv(StringIO(response.text))
        else:
            st.error("Failed to load data from GitHub.")
            return None

# Identificar los URLs de los CSV del repositorio
urls = {
    '2016': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/95f59adcc416732d98f3b9aa494eb78cadd12c0d/CSV/Investigacion1.csv',
    '2017': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/95f59adcc416732d98f3b9aa494eb78cadd12c0d/CSV/Investigacion2.csv',
    '2018': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/95f59adcc416732d98f3b9aa494eb78cadd12c0d/CSV/Investigacion3.csv',
    '2019': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/95f59adcc416732d98f3b9aa494eb78cadd12c0d/CSV/Investigacion4.csv'
}

# Cargar los CSV desde GitHub
df_2016 = load_csv_from_github(urls['2016'])
df_2017 = load_csv_from_github(urls['2017'])
df_2018 = load_csv_from_github(urls['2018'])
df_2019 = load_csv_from_github(urls['2019'])

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


st.header("Variables Cuantitativas")
st.subheader("Estadísticas Descriptivas de Edad por Año")

Edad_2016 = df_2016.dropna(subset=['Edad'])['Edad'].describe().to_frame().T.round(2)

Edad_2017 = df_2017['Edad'].describe().to_frame().T.round(2)

Edad_2018 = df_2018['Edad'].describe().to_frame().T.round(2)

Edad_2019 = df_2019.dropna(subset=['Edad'])['Edad'].describe().to_frame().T.round(2)

# Unir los DataFrames en uno
Edad_inv = pd.concat([Edad_2016, Edad_2017, Edad_2018, Edad_2019], ignore_index=True)

# Renombrar las filas con los años correspondientes
Edad_inv.index = ['2016', '2017', '2018', '2019']

# Renombrar las columnas
Edad_inv.columns = ['Muestra', 'Media', 'SD', 'Min', 'Q1', 'Md', 'Q3', 'Max']

Edad_inv = Edad_inv[['Muestra', 'Media', 'Md', 'SD', 'Min', 'Máx', 'Q1', 'Q3']]

st.dataframe(Edad_inv)

Edad_inv_graph = Edad_inv.drop(['Muestra', 'SD'], axis=1)

# Renombrar las columnas
Edad_inv_graph.columns = ['mean', '50%', 'min', 'max', '25%', '75%']

fig_edad = px.box(Edad_inv_graph, x=Edad_inv_graph.index, y=Edad_inv_graph.columns, 
                 title='Distribución de Edades por Año', 
                 color_discrete_sequence=['#0033cc'])

fig_edad.update_layout(
    xaxis_title="Año",
    yaxis_title="Edades"
)

st.plotly(fig_edad, use_container_width=True)