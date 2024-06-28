import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import requests
from io import StringIO
from PIL import Image
import plotly.graph_objects as go

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
st.write("""
<style>
p {
  text-align: justify;
}
</style>
<p>La enfermedad mental puede ocasionar problemas en la vida cotidiana, por ejemplo, en la escuela, el trabajo o en las relaciones interpersonales. En la mayor parte de los casos, los síntomas pueden tratarse con una combinación de medicamentos y terapia de conversación (psicoterapia).</p>
<p>Las personas manifiestan problemas de salud mental de vez en cuando. Pero un problema de salud mental se convierte en una enfermedad mental cuando los signos y los síntomas se hacen permanentes, causan estrés y afectan la capacidad de funcionar normalmente.</p>
<p>Las enfermedades mentales son trastornos que van de leves a graves, que afectan el pensamiento, el estado de ánimo y/o el comportamiento de una persona. Según el Instituto Nacional de Salud Mental, casi uno de cada cinco adultos vive con una enfermedad mental.</p>
<p>Muchos factores contribuyen a tener problemas de salud mental, entre ellos:</p>
<ul>
  <li>Atributos hereditarios. La enfermedad mental es más frecuente en las personas cuyos parientes consanguíneos también la padecen. Ciertos genes pueden aumentar el riesgo de contraer una enfermedad mental y la situación de vida en particular puede desencadenarla.</li>
  <li>Exposición ambiental anterior al nacimiento. La exposición a factores de estrés ambientales, enfermedades inflamatorias, toxinas, drogas o alcohol en el útero puede asociarse, en algunos casos, con la enfermedad mental.</li>
  <li>Química del cerebro. Los neurotransmisores son sustancias químicas que se encuentran naturalmente en el cerebro y que transmiten señales a otras partes del cerebro y del cuerpo. Cuando las redes neuronales que contienen estas sustancias químicas se ven alteradas, la función de los receptores nerviosos y de los sistemas nerviosos cambia, lo que genera depresión y otros trastornos emocionales.</li>
</ul>
<p>Según los Centros para el Control de Enfermedades, los trastornos de salud mental afectan a más del 18 por ciento de los adultos solo en los Estados Unidos.</p>
<p>Y la Organización Mundial de la Salud informa que la depresión es la principal causa de discapacidad en todo el mundo. Aunque se informa que las enfermedades de salud mental no tratadas les cuestan a las empresas estadounidenses alrededor de $500 mil millones en pérdida de productividad, sin embargo, cuando las empresas priorizan la salud mental de sus trabajadores, pueden tener éxito y prosperar en el lugar de trabajo. Los empleadores deben considerar proporcionar recursos sólidos y sistemas de apoyo para los empleados, incluidos los técnicos de mantenimiento. (U.S Centers for Disease Control and Prevention [CDC], 2019).</p>
<p>La relación entre la salud mental y la productividad es innegable. Cuando los colaboradores están mentalmente saludables, tienden a ser más productivos. El estrés, la ansiedad y otros problemas de salud mental pueden afectar negativamente la concentración, la toma de decisiones y la calidad del trabajo.</p>
<p>Además, los problemas de salud mental no tratados pueden llevar a una mayor rotación de personal y ausentismo, lo que interrumpe la continuidad del trabajo y aumenta los costos para la empresa. Por otro lado ésto conlleva a crear estigmas dentro de éste entorno, los estigmas son una asociación de estereotipos negativos a una etiqueta y que discrimina a las personas, para las personas con enfermedades mentales el ser discriminados puede llevarlos a punto inimaginables, es por ello la importancia de estar informados y que ellos den a conocer su enfermedad sin sentir temor.</p>
<p>Para seguir siendo competitivas y ofrecer beneficios integrales, las empresas de mantenimiento deben priorizar la salud mental de sus empleados. Cuando los empleados tienen satisfechas sus necesidades básicas, que incluyen la salud mental, pueden generar más valor para sus organizaciones</p>
""", unsafe_allow_html=True)

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

st.header("Pregunta 2")
st.subheader("¿Cuáles son los 5 estados con mayor registro de enfermedades mentales diagnosticadas y cuál es la enfermedad mental predominante en cada uno?")
st.subheader("Mapa General de EEUU con la Enfermedades Mentales Más Comunes")

import plotly.express as px
import pandas as pd

data = pd.DataFrame({
'State': ['Alabama', 'Arizona', "California","Carolina del Norte", "Carolina del Sur", "Connecticut", "Delaware", "Florida","Georgia", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Missouri","Nebraska","Nueva Jersey","Nueva York","Nuevo Hampshire","Ohio","Oklahoma","Oregon","Pensilvania","Rhode Island","Tennessee","Texas","Utah","Vermont","Virginia","Virginia del Oeste","Washington","Wisconsin"],
'Frequency': [2,1,34,8,1,3,1,5,3,2,18,8,2,2,2,2,3,4,12,12,2,2,3,13,1,6,2,11,16,1,6,13,3,1,4,1,10,5]
    })

# Group the data by state and sum the frequencies
data = data.groupby('State')['Frequency'].sum().reset_index()

# Create a column with state abbreviations
data['State Abbrev'] = data['State'].map({
    "Alabama":"AL",
    "Arizona": "AZ",
    "California": "CA",
    "Carolina del Norte": "NC",
    "Carolina del Sur":"SC",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",        
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Missouri": "MO",
    "Nebraska": "NE",
    "Nueva Jersey": "NJ",
    "Nueva York": "NY",
    "Nuevo Hampshire": "NH",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pensilvania": "PA",
    "Rhode Island": "RI",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Virginia del Oeste": "WV",
    "Washington": "WA",
    "Wisconsin": "WI"
    })

# Add a new column with mental health condition information
data['Mental Health Condition'] = data['State'].map({
   "Alabama":"Trastorno del Estado del Ánimo (Depresion, Trastorno Bipolar, etc.)",
    "Arizona": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "California": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Carolina del Norte": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Carolina del Sur":"Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Connecticut": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Delaware": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Florida": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Georgia": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Idaho": "Trastorno del Estado del Ánimo (Depresion, Trastorno Bipolar, etc.)",
    "Illinois": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Indiana": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Kansas": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Kentucky": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Louisiana": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Maine": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Maryland": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Massachusetts": "Trastorno del Estado del Ánimo (Depresion, Trastorno Bipolar, etc.)",
    "Michigan": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Minnesota": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Missouri": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Nebraska": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Nueva Jersey": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Nueva York": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Nuevo Hampshire": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Ohio": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Oklahoma": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Oregon": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Pensilvania": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Rhode Island": "Trastorno Obsesivo-Compulsivo",
    "Tennessee": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Texas": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Utah": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Vermont": "Trastorno de Consumo de Sustancias",
    "Virginia": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Virginia del Oeste": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Washington": "Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)",
    "Wisconsin": "Trastorno del Estado del Ánimo (Depresion, Trastorno Bipolar, etc.)"
    })

# Create a choropleth map
figp2 = px.choropleth(
        data,
        locations="State Abbrev",  
        locationmode="USA-states",
        color="Frequency",
        scope="usa",
        color_continuous_scale=[
            (0, "lightgray"), 
            (0.2, "lightblue"),  
            (0.4, "skyblue"),  
            (0.6, "blue"), 
            (0.8, "darkblue"),  
            (1, "navy") 
        ],
        hover_name="State",
        hover_data=["Frequency", "Mental Health Condition"],  
        color_continuous_midpoint=data['Frequency'].mean(),  
        title="Frecuencia de Condiciones de Salud Mental por Estado en EE. UU.", 
        )

figp2.update_layout(coloraxis_colorbar=dict(title="Frecuencia de Casos"))

st.write("Se observa en la siguiente gráfica el mapa de EEUU separado en estados y la enfermedad mental diagnosticada más comun.")

st.plotly_chart(figp2, use_container_width=True)

st.header("Pregunta 3")
st.subheader('Según la cantidad de empleados en las empresas tecnológicas ¿Cuál tiene la mayor cantidad de empleados con enfermedades mentales? ¿Estas ofrecen algún beneficio o algún tipo de convenio?')

# Crea un selectbox con las opciones
option = st.selectbox('Año:', ['2016', '2017', '2018', '2019'], key='year_selectbox')

if option == '2016':
    df1 = pd.DataFrame([["1-5", "3", "2"], ["6-25", "19", "9"], ["26-100", "50", "25"], ["100-500", "80", "21"], ["500-1000", "85", "8"], ["Más de 1000","85", "44"]],
                   columns = ["Tamaño de la Empresa", "Cantidad de Personas dentro de la Empresa con una Enfermedad mental diagnosticada", "Cantidad de Empleados con una Enfermedad Mental que saben de los Beneficios que ofrece la empresa para ellos"])

    x = ['1-5', '6-25', '26-100', '100-500', "500-1000","Más de 1000" ]

    figp3_1 = go.Figure(data=[
        go.Bar(
            name='Cantidad de Personas con una Enfermedad Mental que conocen los Beneficios que Ofrece la Empresa',
            x=x,
            y=[2, 9, 25, 21, 8, 44],
            marker_color='#b366ff'  # changed color
            ),
        go.Bar(
            name='Cantidad de Personas dentro de la Empresa con una Enfermedad Mental Diagnosticada',
            x=x,
            y=[3, 19, 50, 80, 85, 82],
            marker_color='#cc99ff'  # changed color
            )
        ])

    figp3_1.update_layout(barmode='group', 
                title= "Cantidad de empleados con una Enfermedad Mental y si Conocen de los Beneficios que Ofrece su Empresa (2016)")

    st.plotly_chart(figp3_1, use_container_width=True)

elif option == '2017':
    df2 = pd.DataFrame ([["1-5", "7", "0"], ["6-25", "25", "4"], ["26-100", "46", "3"], ["100-500", "107", "37"], ["500-1000", "36", "11"], ["Más de 1000","88", "46"]],
                   columns = ["Tamaño de la Empresa", "Cantidad de Personas dentro de la Empresa con una Enfermedad mental diagnosticada", "Cantidad de Empleados con una Enfermedad Mental que saben de los Beneficios que ofrece la empresa para ellos"])

    random_x = np.random.randint(1, 101, 100)
    random_y = np.random.randint(1, 101, 100)

    x = ['1-5', '6-25', '26-100', '100-500', "500-1000","Más de 1000" ]

    figp3_2 = go.Figure(data=[
        go.Bar(
            name='Cantidad de Personas con una Enfermedad Mental que conocen los Beneficios que Ofrece la Empresa',
            x=x,
            y=[0, 4, 3, 37, 11, 46],
            marker_color='#b366ff'  # changed color
            ),
        go.Bar(
            name='Cantidad de Personas dentro de la Empresa con una Enfermedad Mental Diagnosticada',
            x=x,
            y=[7, 25, 46, 107, 36, 88],
            marker_color='#cc99ff'  # changed color
            )
        ])

    figp3_2.update_layout(barmode='group', title="Cantidad de empleados con Enfermedad Mental y si Conocen de los Beneficios que Ofrece su Empresa (2017)")

    st.plotly_chart(figp3_2, use_container_width=True)

elif option == '2018':
    df3 = pd.DataFrame ([["1-5", "3", "1"], ["6-25", "24", "3"], ["26-100", "30", "8"], ["100-500", "44", "20"], ["500-1000", "31", "10"], ["Más de 1000","71", "35"]],
                   columns = ["Tamaño de la Empresa", "Cantidad de Personas dentro de la Empresa con una Enfermedad mental diagnosticada", "Cantidad de Empleados con una Enfermedad Mental que saben de los Beneficios que ofrece la empresa para ellos"])

    random_x = np.random.randint(1, 101, 100)
    random_y = np.random.randint(1, 101, 100)

    x = ['1-5', '6-25', '26-100', '100-500', "500-1000","Más de 1000" ]

    figp3_3 = go.Figure(data=[
        go.Bar(
            name='Cantidad de Personas con una Enfermedad Mental que conocen los Beneficios que Ofrece la Empresa',
            x=x,
            y=[1, 3, 8, 20, 10, 35],
            marker_color='#b366ff'  # changed color
            ),
        go.Bar(
            name='Cantidad de Personas dentro de la Empresa con una Enfermedad Mental Diagnosticada',
            x=x,
            y=[3, 24, 30, 44, 31, 71],
            marker_color='#cc99ff'  # changed color
            )
        ])

    figp3_3.update_layout(barmode='group', title="Cantidad de empleados con Enfermedad Mental y si Conocen de los Beneficios que Ofrece su Empresa (2018)")

    st.plotly_chart(figp3_3, use_container_width=True)

elif option == '2019':
    df4 = pd.DataFrame ([["1-5", "3", "0"], ["6-25", "15", "3"], ["26-100", "21", "3"], ["100-500", "33", "11"], ["500-1000", "11", "3"], ["Más de 1000","48", "32"]],
                   columns = ["Tamaño de la Empresa", "Cantidad de Personas dentro de la Empresa con una Enfermedad mental diagnosticada", "Cantidad de Empleados con una Enfermedad Mental que saben de los Beneficios que ofrece la empresa para ellos"])

    random_x = np.random.randint(1, 101, 100)
    random_y = np.random.randint(1, 101, 100)

    x = ['1-5', '6-25', '26-100', '100-500', "500-1000","Más de 1000" ]

    figp3_4 = go.Figure(data=[
        go.Bar(
            name='Cantidad de Personas con una Enfermedad Mental que conocen los Beneficios que Ofrece la Empresa',
            x=x,
            y=[0,3, 3, 11, 3, 32],
            marker_color='#b366ff'
            ),
        go.Bar(
            name='Cantidad de Personas dentro de la Empresa con una Enfermedad Mental Diagnosticada',
            x=x,
            y=[3, 15, 21, 33, 11, 48],
            marker_color='#cc99ff'  # changed color
            )
        ])

    figp3_4.update_layout(barmode='group', title="Cantidad de empleados con Enfermedad Mental y si Conocen de los Beneficios que Ofrece su Empresa (2019)")

    st.plotly_chart(figp3_4, use_container_width=True)
