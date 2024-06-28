import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as px
import streamlit as st
import requests
from io import StringIO
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

st.header("Conclusión")
st.write("""
<style>
p {
  text-align: justify;
}
</style>
<ul>
    <li>La enfermedad mental es un problema común en el sector tecnológico estadounidense, que provoca que las personas sufran síntomas como fatiga, falta de concentración y productividad reducida, lo que puede afectar negativamente su desempeño laboral y su bienestar general
    <li>Las empresas deben velar por la salud mental de sus trabajadores, dado que si tienen empleados sanos la empresa tendrá mejor rendimiento.
    <li>El top 3 de puestos de trabajo  en la Industria Tecnológica con mayores registros de enfermedades mentales son: Los Programadores Back y Font end y los supervisores y líderes de equipo.
    <li>La enfermedad mental más común dentro de la Industria Tecnológica es el Trastorno de ansiedad.
    <li>Las empresas generalmente no promueven el sistema de apoyo que ofrecen a sus trabajadores, esto podría ocasionar recortes del presupuesto destinados a programas de salud mental, ocasionando que personas que sí reciban el apoyo puedan perderlo eventualmente
    <li>El número de personas con enfermedades mentales se mantiene estable a través de los años, esto es un problema ya que de alguna manera no se genera ningún cambio significativo, lo que quiere decir que la situación no mejora.
</ul>
<p>En última instancia, todos somos responsables de crear una cultura laboral que valore la salud mental y promueva el bienestar. Juntos, podemos marcar la diferencia y construir un futuro tecnológico más humano y sostenible.</p>
""", unsafe_allow_html=True)

st.subheader("Recomendaciones")
st.write("""
<style>
p {
  text-align: justify;
}
</style>
<ul>
    <li>Promover la Comunicación Abierta: Establecer un espacio seguro para que los empleados compartan sus preocupaciones y desafíos es fundamental. La comunicación abierta reduce el estrés y fomenta un sentido de comunidad.</p>
    <li>Fomentar el Equilibrio entre el Trabajo y la Vida Personal: Establecer límites claros entre el tiempo de trabajo y el tiempo personal ayuda a los empleados a desconectar y recargar energías, lo que es vital para su bienestar.</p>
    <li>Ofrecer Recursos de Apoyo: Proporcionar acceso a recursos como asesoramiento, programas de bienestar, y capacitación en manejo del estrés puede marcar una gran diferencia en la vida de los empleados.</p>
    <li>Incentivar el Desarrollo Profesional y Personal: Apoyar el crecimiento y desarrollo integral de los empleados, tanto en el ámbito profesional como personal, puede aumentar su satisfacción laboral y bienestar.</p>
    <li>Promover la Autocuidado: Incentivar prácticas de autocuidado, como el ejercicio, la meditación y el tiempo de descanso, puede contribuir a una mejor salud mental y un mayor rendimiento laboral.</p>
<ul>
""", unsafe_allow_html=True)
