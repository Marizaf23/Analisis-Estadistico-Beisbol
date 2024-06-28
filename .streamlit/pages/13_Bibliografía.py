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

st.header("Bibliografía")
st.markdown("""
*Adecco Institute. (s.f.). *Salud mental en un lugar de trabajo digitalizado*. https://www.adeccoinstitute.es/salud-y-prevencion/salud-mental-en-un-lugar-de-trabajo-digitalizado/](https://www.adeccoinstitute.es/salud-y-prevencion/salud-mental-en-un-lugar-de-trabajo-digitalizado/.

*Comisión para la Igualdad de Oportunidades en el Empleo (EEOC). (s.f.). *La Ley de Estadounidenses con Discapacidades: Una introducción para pequeñas empresas*. https://www.eeoc.gov/es/laws/guidance/la-ley-de-estadounidenses-con-discapacidades-una-introduccion-para-pequenas-empresas.

*Departamento de Salud y Servicios Humanos de EE. UU. (s.f.). *Prioridades del Cirujano General: Salud mental juvenil*. https://www.hhs.gov/es/surgeongeneral/priorities/youth-mental-health/index.html.

*Gobierno de Estados Unidos. (s.f.). *Instituto Nacional de la Salud Mental*. https://www.usa.gov/es/agencias/instituto-nacional-de-la-salud-mental.

*International Labour Organization (OIT). (2024). *Un informe de la OIT estudia la salud mental en el trabajo en Alemania, Estados Unidos, Finlandia, Polonia y Reino Unido*. https://www.ilo.org/es/resource/news/un-informe-de-la-oit-estudia-la-salud-mental-en-el-trabajoen-alemania.

*Inthavong, A. (2020). *Mental Health in the Tech Industry*. https://www.kaggle.com/datasets/anth7310/mental-health-in-the-tech-industry.

*ITI. (s.f.). *Bienestar y salud mental: ¿Puede la tecnología ayudarnos a mejorarlas?*. https://www.iti.es/blog/bienestar-y-salud-mental-puede-la-tecnologia-ayudarnos-a-mejorarlas/.

*Los Angeles Times en Español. (2022). *Abordar la crisis de salud mental requiere lo único que todos tenemos: empatía*. https://www.latimes.com/espanol/vida-y-estilo/articulo/2022-12-23/abordar-la-crisis-de-salud-mental-requiere-lo-unico-que-todos-tenemos-empatia.

*MedlinePlus. (s.f.). *Trastornos mentales*. https://medlineplus.gov/spanish/mentaldisorders.html.

*MenteVita. (s.f.). *El impacto de la tecnología en el estrés y la ansiedad laboral*. https://mentevita.com/el-impacto-de-la-tecnologia-en-el-estres-y-la-ansiedad-laboral/](https://mentevita.com/el-impacto-de-la-tecnologia-en-el-estres-y-la-ansiedad-laboral/.

*OBS Business School. (s.f.). *Importancia de la salud mental en las empresas*. https://www.obsbusiness.school/blog/importancia-de-la-salud-mental-en-las-empresas.

*Open Sourcing Mental Illness. (s.f.). OSMIhttps://osmihelp.org/.

*Organización Mundial de la Salud (OMS). (s.f.). *Preguntas más frecuentes*. https://www.who.int/es/about/frequently-asked-questions#:~:text=%C2%BFC%C3%B3mo%20define%20la%20OMS%20la,ausencia%20de%20afecciones%20o%20enfermedades%C2%BB.

*Organización Mundial de la Salud (OMS). (s.f.). *Por qué la salud mental debe ser una prioridad al adoptar medidas relacionadas con el cambio climático*. https://www.who.int/es/news/item/03-06-2022-why-mental-health-is-a-priority-for-action-on-climate-change#:~:text=La%20OMS%20define%20la%20salud.
""")