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


st.header("Pregunta 5")
st.subheader('¿Cuál es la disposición de los empleados de la industria tegnológica a a hora de hablar sobre su Enfermedad Mental?')

st.header("Disposición Para Hablar")
st.subheader("Disposición a la hora de hablar sobre tu salud mental con supervisor")

st.subheader("2016")
filtro_si_diagnosticado = df_2016['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'] == 'Si'
pregunta_5_2016 = pd.crosstab(df_2016[filtro_si_diagnosticado]['Disposición de Hablar de Salud Mental con un Supervisor'], 
                                df_2016[filtro_si_diagnosticado]['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], margins=True)
pregunta_5_2016 = pregunta_5_2016.rename(columns={'Si': 'Diagnosticado con Enfermedad Mental'})
pregunta_5_2016 = pregunta_5_2016.drop('All', axis=0).drop('All', axis=1)  # Elimina las filas y columnas "All"
st.dataframe(pregunta_5_2016)

st.subheader("2017")
filtro_si_diagnosticado = df_2017['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'] == 'Si'
pregunta_5_2017 = pd.crosstab(df_2017[filtro_si_diagnosticado]['Disposición de Hablar de Salud Mental con un Supervisor'], 
                                df_2017[filtro_si_diagnosticado]['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], margins=True)
pregunta_5_2017 = pregunta_5_2017.rename(columns={'Si': 'Diagnosticado con Enfermedad Mental'})
pregunta_5_2017 = pregunta_5_2017.drop('All', axis=0).drop('All', axis=1)  # Elimina las filas y columnas "All"
st.dataframe(pregunta_5_2017)

st.subheader("2018")
filtro_si_diagnosticado = df_2018['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'] == 'Si'
pregunta_5_2018 = pd.crosstab(df_2018[filtro_si_diagnosticado]['Disposición de Hablar de Salud Mental con un Supervisor'], 
                                df_2018[filtro_si_diagnosticado]['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], margins=True)
pregunta_5_2018 = pregunta_5_2018.rename(columns={'Si': 'Diagnosticado con Enfermedad Mental'})
pregunta_5_2018 = pregunta_5_2018.drop('All', axis=0).drop('All', axis=1)  # Elimina las filas y columnas "All"
st.dataframe(pregunta_5_2018)

st.subheader("2019")
filtro_si_diagnosticado = df_2019['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'] == 'Si'
pregunta_5_2019 = pd.crosstab(df_2019[filtro_si_diagnosticado]['Disposición de Hablar de Salud Mental con un Supervisor'], 
                                df_2019[filtro_si_diagnosticado]['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], margins=True)
pregunta_5_2019 = pregunta_5_2019.rename(columns={'Si': 'Diagnosticado con Enfermedad Mental'})
pregunta_5_2019 = pregunta_5_2019.drop('All', axis=0).drop('All', axis=1)  # Elimina las filas y columnas "All"
st.dataframe(pregunta_5_2019)

import plotly.graph_objects as go
import pandas as pd

Pregunta_5_2016 = pd.DataFrame({'Diagnosticado con Enfermedad Mental': [19, 157, 228, 25, 44]}, index=['Si, con todos mis jefes', 'No, con ninguno de mis jefes', 'Con algunos de mis jefes', 'No sé', 'No respondió'])
Pregunta_5_2017 = pd.DataFrame({'Diagnosticado con Enfermedad Mental': [12, 86, 115, 8, 23]}, index=['Si, con todos mis jefes', 'No, con ninguno de mis jefes', 'Con algunos de mis jefes', 'No sé', 'No respondió'])
Pregunta_5_2018 = pd.DataFrame({'Diagnosticado con Enfermedad Mental': [8, 48, 73, 9, 21]}, index=['Si, con todos mis jefes', 'No, con ninguno de mis jefes', 'Con algunos de mis jefes', 'No sé', 'No respondió'])
Pregunta_5_2019 = pd.DataFrame({'Diagnosticado con Enfermedad Mental': [5, 35, 50, 4, 12]}, index=['Si, con todos mis jefes', 'No, con ninguno de mis jefes', 'Con algunos de mis jefes', 'No sé', 'No respondió'])

# Combinar los df
dataframes = [
    Pregunta_5_2016.reset_index(),
    Pregunta_5_2017.reset_index(),
    Pregunta_5_2018.reset_index(),
    Pregunta_5_2019.reset_index(),
]

# Crear la lista de nombres
frames = []
for i, df in enumerate(dataframes):
    frame = go.Frame(
        data=[go.Bar(x=df['index'], y=df['Diagnosticado con Enfermedad Mental'], 
                     name=f'Año {2016 + i}', 
                     marker=dict(color=f'rgba(0, 0, {255 - i*64}, 0.8)'),  # degradado de azul
                     orientation='v')],
        name=f'frame{i}',
        layout=go.Layout(title=f'Año {2016 + i}')
    )
    frames.append(frame)

# Crear la figura inicial
figp5_1 = go.Figure(
    data=[go.Bar(x=dataframes[0]['index'], y=dataframes[0]['Diagnosticado con Enfermedad Mental'], 
                 name='Año 2016', 
                 marker=dict(color='rgba(0, 0, 255, 0.8)'),  # degradado de azul
                 orientation='v')],
    layout=go.Layout(
        title='Disposición de Hablar de Salud Mental con un Supervisor',
        xaxis=dict(title='Respuestas'),
        yaxis=dict(title='Cantidad'),
        updatemenus=[
            dict(
                type="buttons",
                direction="down",
                buttons=list([
                    dict(label="Play", method="animate", args=[None, {"frame": {"duration": 7000, "fromcurrent": True}, "transition": {"duration": 500}}]),
                    dict(label="Pause", method="animate", args=[[None], {"frame": {"duration": 0, "fromcurrent": True}, "transition": {"duration": 0}}]),
                    dict(label="Restart", method="animate", args=[None, {"frame": {"duration": 0, "fromcurrent": False}, "transition": {"duration": 0}}])
                ]),
            )
        ]
    )
)
figp5_1.frames = frames
st.plotly_chart(figp5_1, use_container_width=True)

st.subheader("Análisis")
st.write("El gráfico indica la disposición para discutir temas de salud mental con un supervisor. En los últimos años, La mayoría de las personas no hablan de su salud mental con sus jefes, esto se debe a los estigmas explicados anteriormente. Los empleados tienden a sentir miedo al hablar sobre su condición, aunque hay número significativo que estaría dispuesto a hablar sobre ello pero con algunos en específico.")

st.subheader("Disposisión a la hora de hablar sobre tu salud mental con amigos y familiares")

st.subheader("2016")

filtro_si_diagnosticado = df_2016['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'] == 'Si'
pregunta1_5_2016 = pd.crosstab(df_2016[filtro_si_diagnosticado]['Disposición para Hablar Sobre Enfermedad Mental con Familia/Amigos'], 
                                df_2016[filtro_si_diagnosticado]['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], margins=True)
pregunta1_5_2016 = pregunta1_5_2016.rename(columns={'Si': 'Diagnosticado con Enfermedad Mental'})
pregunta1_5_2016 = pregunta1_5_2016.drop('All', axis=0).drop('All', axis=1)  # Eliminar fila y columna "All"

# Seleccionar las filas que contienen "no dispuesto (a)" y "no estoy dispuesto (a)"
no_dispuestos = pregunta1_5_2016.loc[['No estoy dispuesto(a)', 'No dispuesto(a)']]

# Sumar las filas seleccionadas
no_dispuestos_sum = no_dispuestos.sum()

# Reemplazar las filas originales con la nueva fila sumada
pregunta1_5_2016.loc['No Dispuesto'] = no_dispuestos_sum
pregunta1_5_2016 = pregunta1_5_2016.drop(['No estoy dispuesto(a)', 'No dispuesto(a)'], axis=0)

st.dataframe(pregunta1_5_2016)

st.subheader("2017")
filtro_si_diagnosticado = df_2017['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'] == 'Si'
pregunta2_5_2017 = pd.crosstab(df_2017[filtro_si_diagnosticado]['Disposición para Hablar Sobre Enfermedad Mental con Familia/Amigos'], 
                                df_2017[filtro_si_diagnosticado]['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], margins=True)
pregunta2_5_2017 = pregunta2_5_2017.rename(columns={'Si': 'Diagnosticado con Enfermedad Mental'})
pregunta2_5_2017 = pregunta2_5_2017.drop('All', axis=0).drop('All', axis=1)

# Seleccionar las filas que contienen "no dispuesto (a)" y "no estoy dispuesto (a)"
no_dispuestos = pregunta2_5_2017.loc[['No estoy dispuesto(a)', 'No dispuesto(a)']]

# Sumar las filas seleccionadas
no_dispuestos_sum = no_dispuestos.sum()

# Reemplazar las filas originales con la nueva fila sumada
pregunta2_5_2017.loc['No Dispuesto'] = no_dispuestos_sum
pregunta2_5_2017 = pregunta2_5_2017.drop(['No estoy dispuesto(a)', 'No dispuesto(a)'], axis=0)

st.dataframe(pregunta2_5_2017)

st.subheader("2018")
filtro_si_diagnosticado = df_2018['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'] == 'Si'
pregunta3_5_2018 = pd.crosstab(df_2018[filtro_si_diagnosticado]['Disposición para Hablar Sobre Enfermedad Mental con Familia/Amigos'], 
                                df_2018[filtro_si_diagnosticado]['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], margins=True)
pregunta3_5_2018 = pregunta3_5_2018.rename(columns={'Si': 'Diagnosticado con Enfermedad Mental'})
pregunta3_5_2018 = pregunta3_5_2018.drop('All', axis=0).drop('All', axis=1)  # Eliminar fila y columna "All"

# Seleccionar las filas que contienen "no dispuesto (a)" y "no estoy dispuesto (a)"
no_dispuestos = pregunta3_5_2018.loc[['No estoy dispuesto(a)', 'No dispuesto(a)']]

# Sumar las filas seleccionadas
no_dispuestos_sum = no_dispuestos.sum()

# Reemplazar las filas originales con la nueva fila sumada
pregunta3_5_2018.loc['No Dispuesto'] = no_dispuestos_sum
pregunta3_5_2018 = pregunta3_5_2018.drop(['No estoy dispuesto(a)', 'No dispuesto(a)'], axis=0)

st.dataframe(pregunta3_5_2018)

st.subheader("2019")
filtro_si_diagnosticado = df_2019['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'] == 'Si'
pregunta4_5_2019 = pd.crosstab(df_2019[filtro_si_diagnosticado]['Disposición para Hablar Sobre Enfermedad Mental con Familia/Amigos'], 
                                df_2019[filtro_si_diagnosticado]['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], margins=True)
pregunta4_5_2019 = pregunta4_5_2019.rename(columns={'Si': 'Diagnosticado con Enfermedad Mental'})
pregunta4_5_2019 = pregunta4_5_2019.drop('All', axis=0).drop('All', axis=1)  # Eliminar fila y columna "All"

# Seleccionar las filas que contienen "no dispuesto (a)" y "no estoy dispuesto (a)"
no_dispuestos = pregunta4_5_2019.loc[['No estoy dispuesto(a)', 'No dispuesto(a)']]

# Sumar las filas seleccionadas
no_dispuestos_sum = no_dispuestos.sum()

# Reemplazar las filas originales con la nueva fila sumada
pregunta4_5_2019.loc['No Dispuesto'] = no_dispuestos_sum
pregunta4_5_2019 = pregunta4_5_2019.drop(['No estoy dispuesto(a)', 'No dispuesto(a)'], axis=0)

st.dataframe(pregunta4_5_2019)

import plotly.graph_objects as go
import pandas as pd

Pregunta1_5_2016 = pd.DataFrame({'Diagnosticado con Enfermedad Mental': [238, 86, 37, 104]}, index=['Dispuesto(a)', 'No dispuesto', 'Neutral', 'Muy dispuesto(a)'])
Pregunta2_5_2017 = pd.DataFrame({'Diagnosticado con Enfermedad Mental': [18, 33, 18, 175]}, index=['Dispuesto(a)', 'No dispuesto', 'Neutral', 'Muy dispuesto(a)'])
Pregunta3_5_2018 = pd.DataFrame({'Diagnosticado con Enfermedad Mental': [5, 22, 13, 119]}, index=['Dispuesto(a)','No dispuesto', 'Neutral', 'Muy dispuesto(a)'])
Pregunta4_5_2019 = pd.DataFrame({'Diagnosticado con Enfermedad Mental': [9, 12, 11, 74]}, index=['Dispuesto(a)','No dispuesto', 'Neutral', 'Muy dispuesto(a)'])

# Combinar los df
dataframes = [
    Pregunta1_5_2016.reset_index(),
    Pregunta2_5_2017.reset_index(),
    Pregunta3_5_2018.reset_index(),
    Pregunta4_5_2019.reset_index(),
]


for i, df in enumerate(dataframes):
    frame = go.Frame(
        data=[go.Bar(x=df['index'], y=df['Diagnosticado con Enfermedad Mental'], 
                     name=f'Año {2016 + i}', 
                     marker=dict(color=f'rgba(128, 0, {255 - i*64}, 0.8)'),  # degradado de morado
                     orientation='v')],
        name=f'frame{i}',
        layout=go.Layout(title=f'Año {2016 + i}')
    )
    frames.append(frame)

#...

figp5_2 = go.Figure(
    data=[go.Bar(x=dataframes[0]['index'], y=dataframes[0]['Diagnosticado con Enfermedad Mental'], 
                 name='Año 2016', 
                 marker=dict(color='rgba(128, 0, 255, 0.8)'),  # degradado de morado
                 orientation='v')],
    layout=go.Layout(
        title='Disposición para Hablar Sobre Enfermedad Mental con Familia/Amigos',
        xaxis=dict(title='Respuestas'),
        yaxis=dict(title='Cantidad'),
        updatemenus=[
            dict(
                type="buttons",
                direction="down",
                buttons=list([
                    dict(label="Play", method="animate", args=[None, {"frame": {"duration": 7000, "fromcurrent": True}, "transition": {"duration": 500}}]),
                    dict(label="Pause", method="animate", args=[[None], {"frame": {"duration": 0, "fromcurrent": True}, "transition": {"duration": 0}}]),
                    dict(label="Restart", method="animate", args=[None, {"frame": {"duration": 0, "fromcurrent": False}, "transition": {"duration": 0}}])
                ]),
            )
        ]
    )
)

figp5_2.frames = frames
st.plotly_chart(figp5_2, use_container_width=True)

st.write("En esta gráfica se muestra la disposición para hablar sobre enfermedades mentales con familliares y amigos. Ciertamente las personas tienden a sentirse cada vez más comodas para hablar sobre su salud mental con allegados a través de los años.")


