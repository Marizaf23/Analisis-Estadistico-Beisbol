import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as px
import streamlit as st
import requests
from io import StringIO
import plotly_express as px
import base64

LOGO_IMAGE1 = "logos/UCV.png"
LOGO_IMAGE2 = "logos/EECA.png"

st.markdown(
    f"""
    <div style="background-color:#80bfff;padding:10px;display:flex;justify-content:space-between;align-items:center;margin-top:-30px;">
        <img src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE1, "rb").read()).decode()}" style="height:40px;margin:30px;">
        <img src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE2, "rb").read()).decode()}" style="height:40px;margin:30px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title("Problemáticas y Estigmas de las Enfermedades Mentales en la Industria Tecnológica Estadounidense 2016-2019")

st.header("Introducción")
st.write('<p style="text-align: justify;">Las alteraciones de la salud mental (trastornos psiquiátricos o psicológicos) o Enfermedades Mentales implican alteraciones en el pensamiento, en las emociones y/o en la conducta. Las alteraciones leves de estos aspectos vitales son frecuentes, pero cuando provocan una angustia intensa a la persona afectada e interfieren en su vida diaria, se consideran enfermedades mentales o trastornos de la salud mental. Los efectos de la enfermedad mental pueden ser temporales o de larga duración. La salud mental en el trabajo debe concebirse desde un enfoque integral, en el cual la persona reconozca su bienestar en las diferentes áreas de su vida. Esto implica el terreno personal, familiar, laboral y económico. Buscar ayuda profesional ayudará a manejar mejor las situaciones de incertidumbre que puedan presentarse, así como evitar la aparición del estrés y otras enfermedades psicosociales. No solamente la empresa debe encargarse de mantener este equilibrio, sino también los empleados son responsables del autocuidado de su salud mental. Es por esto que las empresas deben estar dispuestas siempre al diálogo e intercambio entre los miembros de la empresa, lo que garantizará una mejor calidad de vida, rendimiento laboral y satisfacción personal. Por tanto, una adecuada salud mental se refleja de manera positiva en nuestro cuerpo, y por consecuencia, en el rendimiento laboral. Esto permite manejar mejor las situaciones de conflicto y disfrutar de buenas relaciones interpersonales. Con ello, se despliega todo nuestro potencial y se eleva la productividad en el trabajo.</p>', unsafe_allow_html=True)

