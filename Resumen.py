import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as px
import streamlit as st
import requests
from io import StringIO
from PIL import Image

st.set_page_config(layout="wide")

# Título de la aplicación
st.title("Problemáticas y Estigmas de las Enfermedades Mentales en la Industria Tecnológica Estadounidense 2016-2019")

# Contenido de la página 1
st.header("Introducción")
st.write('<p style="text-align: justify;">La salud mental es un aspecto crítico del desarrollo humano, social, económico, y es esencial para la salud en general.  Para los empleados de la TI (Industria Tecnológica) es un tema de preocupación creciente debido a las características únicas de este sector, el cual pueden contribuir de manera positiva o negativa al bienestar psicológico de sus empleados. Identificarse como una persona que padece de una Enfermedad Mental se ha convertido en un problema, una de las principales razones es el estigma y la discriminación que rodea las Enfermedades Mentales. La gente teme ser juzgada o tratada de manera diferente por sus compañeros de trabajo, familiares y amigos si se identifican con ello.</p>', unsafe_allow_html=True)

# Contenido de la página 2
st.header("Visualización de los Datos")

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

st.write('<p style="text-align: justify;">La base de datos depurada y estructurada para esta investigación abarca los años 2016-2019. La fuente es Kaggle y su vez las encuestas anónimas realizadas por la organización OSMI para estudiar el conocimiento y aceptación de enfermedades mentales en la industria tecnológica. Se analizaron variables como diagnóstico, creencias, antecedentes heredofamiliares, trabajo remoto, recursos de apoyo, percepción externa, género y edad. El enfoque en este período previo a la pandemia permite observar cambios antes de la creciente conciencia sobre salud mental. A pesar de los desafíos en la normalización y limpieza de datos, se utilizaron herramientas como SQLite, Python y PowerBi para llevar a cabo la investigación.</p>', unsafe_allow_html=True)

st.header("Variables Cuantitativas")

st.subheader("Estadísticas Descriptivas de Edad por Año")

try:
    df_2016['Edad'] = pd.to_numeric(df_2016['Edad'], errors='coerce')
except Exception as e:
    st.write(f"Error: {e}")

Edad_2016 = df_2016['Edad'].describe().to_frame().T.round(2)

Edad_2017 = df_2017['Edad'].describe().to_frame().T.round(2)

Edad_2018 = df_2018['Edad'].describe().to_frame().T.round(2)

try:
    df_2019['Edad'] = pd.to_numeric(df_2019['Edad'], errors='coerce')
except Exception as e:
    st.write(f"Error: {e}")

Edad_2019 = df_2019['Edad'].describe().to_frame().T.round(2)

# Unir los DataFrames en uno
Edad_inv = pd.concat([Edad_2016, Edad_2017, Edad_2018, Edad_2019], ignore_index=True)

# Renombrar las filas con los años correspondientes
Edad_inv.index = ['2016', '2017', '2018', '2019']

# Renombrar las columnas
Edad_inv.columns = ['Muestra', 'Media', 'SD', 'Min', 'Q1', 'Md', 'Q3', 'Máx']

Edad_inv = Edad_inv[['Muestra', 'Media', 'Md', 'SD', 'Min', 'Máx', 'Q1', 'Q3']]

st.dataframe(Edad_inv, width=1800, height=178)

# Contenido de la página 3
st.header("Planteamiento Del Problema")
st.subheader("Objetivos")
st.write('<ul><li>Determinar las características e incidencias de las enfermedades mentales en la industria tecnológica estadounidense tomando en cuenta el diagnóstico, antecedentes heredofamiliares, edad, género y puesto de trabajo de los afectados.</li><li>Identificar el nivel de productividad de los empleados de la industria tecnológica estadounidense con enfermedades mentales y qué beneficios reciben para su tratamiento.</li><li>Indagar la percepción externa de los trabajadores sobre las enfermedades mentales en la industria tecnológica estadounidense.</li></ul>', unsafe_allow_html=True)

# Contenido de la página 4
st.header("Marco Teórico")
st.write("marco.")

# Contenido de la página 5
st.header("Pregunta 1")
st.subheader("¿Cuántas personas en la industria tecnológica tienen una enfermedad mental diagnosticada y, dentro de este grupo, existe algún historial familiar dentro de este ámbito?")

# Crea un selectbox con las opciones
option = st.selectbox('Año de Encuesta:', ['2016', '2017', '2018', '2019'], key='year_selectbox')

if option == '2016':

    #Crear la tabla bivariante con pandas
    Pregunta2016_1 = pd.crosstab(df_2016['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], 
                        df_2016['Antecedentes Heredofamiliares'], 
                        margins=True, 
                        margins_name='Total')

    # Renombrar el índice
    Pregunta2016_1.index.name = "Antecedentes Heredofamiliares"
    
    # Agregar una fila debajo de los títulos de las columnas 
    Pregunta2016_1.loc['Enfermedad Mental'] = ['', '', '', '']

    Pregunta2016_1 = Pregunta2016_1.reindex(['Enfermedad Mental'] + [i for i in Pregunta2016_1.index if i != 'Enfermedad Mental'])
    
    Pregunta2016_1.rename(columns={'index': 'Enfermedad Mental'})

    st.dataframe(Pregunta2016_1, width=1500, height=177)

elif option == '2017':
    
    #Crear la tabla bivariante con pandas
    Pregunta2017_1 = pd.crosstab(df_2017['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], 
                        df_2017['Antecedentes Heredofamiliares'], 
                        margins=True, 
                        margins_name='Total')

    # Renombrar el índice
    Pregunta2017_1.index.name = "Antecedentes Heredofamiliares"
    
    # Agregar una fila debajo de los títulos de las columnas 
    Pregunta2017_1.loc['Enfermedad Mental'] = ['', '', '', '']

    Pregunta2017_1 = Pregunta2017_1.reindex(['Enfermedad Mental'] + [i for i in Pregunta2017_1.index if i != 'Enfermedad Mental'])
    
    Pregunta2017_1.rename(columns={'index': 'Enfermedad Mental'})

    Pregunta2017_1 = Pregunta2017_1.reindex(['Enfermedad Mental'] + [i for i in Pregunta2017_1.index if i not in ['Enfermedad Mental', 'No respondió', 'Total']] + ['No respondió'] + ['Total'])
    
    st.dataframe(Pregunta2017_1, width=800, height=212)

elif option == '2018':
    
    #Crear la tabla bivariante con pandas
    Pregunta2018_1 = pd.crosstab(df_2018['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], 
                        df_2018['Antecedentes Heredofamiliares'], 
                        margins=True, 
                        margins_name='Total')

    # Renombrar el índice
    Pregunta2018_1.index.name = "Antecedentes Heredofamiliares"
    
    # Agregar una fila debajo de los títulos de las columnas 
    Pregunta2018_1.loc['Enfermedad Mental'] = ['', '', '', '']

    Pregunta2018_1 = Pregunta2018_1.reindex(['Enfermedad Mental'] + [i for i in Pregunta2018_1.index if i != 'Enfermedad Mental'])
    
    Pregunta2018_1.rename(columns={'index': 'Enfermedad Mental'})

    Pregunta2018_1 = Pregunta2018_1.reindex(['Enfermedad Mental'] + [i for i in Pregunta2018_1.index if i not in ['Enfermedad Mental', 'No respondió', 'Total']] + ['No respondió'] + ['Total'])
    
    st.dataframe(Pregunta2018_1, width=800, height=212)

elif option == '2019':

    #Crear la tabla bivariante con pandas
    Pregunta2019_1 = pd.crosstab(df_2019['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], 
                        df_2019['Antecedentes Heredofamiliares'], 
                        margins=True, 
                        margins_name='Total')

    # Renombrar el índice
    Pregunta2019_1.index.name = "Antecedentes Heredofamiliares"
    
    # Agregar una fila debajo de los títulos de las columnas 
    Pregunta2019_1.loc['Enfermedad Mental'] = ['', '', '', '']

    Pregunta2019_1 = Pregunta2019_1.reindex(['Enfermedad Mental'] + [i for i in Pregunta2019_1.index if i != 'Enfermedad Mental'])
    
    Pregunta2019_1.rename(columns={'index': 'Enfermedad Mental'})

    Pregunta2019_1 = Pregunta2019_1.reindex(['Enfermedad Mental'] + [i for i in Pregunta2019_1.index if i not in ['Enfermedad Mental', 'No respondió', 'Total']] + ['No respondió'] + ['Total'])

    st.dataframe(Pregunta2019_1, width=800, height=212)