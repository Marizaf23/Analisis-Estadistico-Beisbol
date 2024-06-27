import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
from pywaffle import Waffle
import plotly.graph_objects as go
import streamlit as st
import requests
from io import StringIO
import plotly.express as px


@st.cache
def load_csv_from_github(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from GitHub.")
        return None

# URLs of CSV files in GitHub repository
urls = {
    '2016': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/95f59adcc416732d98f3b9aa494eb78cadd12c0d/CSV/Investigacion1.csv',
    '2017': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/95f59adcc416732d98f3b9aa494eb78cadd12c0d/CSV/Investigacion2.csv',
    '2018': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/95f59adcc416732d98f3b9aa494eb78cadd12c0d/CSV/Investigacion3.csv',
    '2019': 'https://raw.githubusercontent.com/Marizaf23/Analisis-Estadistico-Salud-Mental-Tecnologia/95f59adcc416732d98f3b9aa494eb78cadd12c0d/CSV/Investigacion4.csv'
}

# Load CSV files from GitHub
df_2016 = load_csv_from_github(urls['2016'])
df_2017 = load_csv_from_github(urls['2017'])
df_2018 = load_csv_from_github(urls['2018'])
df_2019 = load_csv_from_github(urls['2019'])


# Contenido de la página 5
st.header("Pregunta 2")
st.subheader('"¿Cuáles son los 5 estados con mayor registro de enfermedades mentales diagnosticadas y cuál es la enfermedad mental predominante en cada uno?"')

# Crea un selectbox con las opciones
option = st.selectbox('EEUU:', ['General','Estados'])

if option == 'General':
    #Mapa con la enfermedad mas frecuente registrada

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

    st.plotly_chart(figp2, use_container_width=True)
    
    st.write("Se observa en la siguiente gráfica el mapa de EEUU separado en estados y la enfermedad mental diagnosticada más comun.")