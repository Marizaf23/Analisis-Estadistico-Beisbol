import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as px
import streamlit as st
import requests
from io import StringIO

# Título de la aplicación
st.title("Problemáticas y Estigmas de las Enfermedades Mentales en la Industria Tecnológica Estadounidense 2016-2019")

# Crea un menú de pestañas
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs(["Introducción", "Datos", "Planteamiento del Problema", "Marco Teórico", "Pregunta #1", "Pregunta #2", "Pregunta #3", "Pregunta #4", "Pregunta #5", "Pregunta #6", "Conclusión", "Bibliografía"])

# Contenido de la página 1
with tab1:
    st.header("Introducción")
    st.write("Información de la Data Suministrada.")

# Contenido de la página 2
with tab2:
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
        '2016': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/f9543f9242e7869a95a82e55fb2d1289971a9c40/CSV/Investigacion1.csv',
        '2017': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/f9543f9242e7869a95a82e55fb2d1289971a9c40/CSV/Investigacion2.csv',
        '2018': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/f9543f9242e7869a95a82e55fb2d1289971a9c40/CSV/Investigacion3.csv',
        '2019': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/f9543f9242e7869a95a82e55fb2d1289971a9c40/CSV/Investigacion4.csv'
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

# Contenido de la página 3
with tab3:
    st.header("Planteamiento Del Problema")
    st.write("planteamiento.")

# Contenido de la página 4
with tab4:
    st.header("Marco Teórico")
    st.write("marco.")

# Contenido de la página 5
with tab5:
    st.header("Pregunta #1: ¿Cuántas personas en la industria tecnológica tienen una enfermedad mental diagnosticada y, dentro de este grupo, existe algún historial familiar dentro de este ámbito?")
    st.write("#1")

    # Crea un selectbox con las opciones
    option = st.selectbox('Año de Encuesta:', ['Todos','2016', '2017', '2018', '2019'])

if option == '2016':
    st.write("¿Cuántas personas en la industria tecnológica tienen una enfermedad mental diagnosticada y, dentro de este grupo, existe algún historial familiar dentro de este ámbito?")

    Pregunta1 = pd.crosstab(df_2016['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], 
                        df_2016['Historial Familiar'], 
                        margins=True, 
                        margins_name='Total')

    Pregunta1 = Pregunta1.rename_axis(index='Enfermedad Mental', columns='Historial Familiar')
    st.write("Tabla de Contingencia")
    st.table(Pregunta1.T.reset_index().rename(columns={'index': 'Historial Familiar'}))