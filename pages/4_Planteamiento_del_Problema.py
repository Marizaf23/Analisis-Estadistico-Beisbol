import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as px
import streamlit as st
import requests
from io import StringIO


st.header("Planteamiento Del Problema")
st.subheader("Contexto del Problema")
st.write('<p style="text-align: justify;">La Organización Mundial de la Salud (OMS) define salud como “Un estado completo del bienestar físico, mental, social y no solamente la ausencia de afecciones o enfermedades” (Organización Mundial de la Salud [OMS], 2024). También declara de forma general que "no existe la salud sin la salud mental" y señala que "la salud mental es primordial para el desenvolvimiento humano, social y económico de las naciones y esencial para otras áreas de políticas públicas como son la asistencia social, los derechos humanos, la educación y el empleo" (OMS, 2024). </p>', unsafe_allow_html=True)

st.write('<p style="text-align: justify;">Una Enfermedad Mental o el Trastorno de Salud Mental es una alteración de tipo emocional, cognitivo y/o comportamiento, en que quedan afectados procesos psicológicos básicos como son la emoción, motivación, cognición, conciencia, conducta, percepción, sensación, aprendizaje, lenguaje, entre otros. Lo que dificulta a la persona su adaptación al entorno cultural y social en el que vive, creando de alguna forma un malestar subjetivo.</p>', unsafe_allow_html=True) 

st.write('<p style="text-align: justify;">Cada persona experimenta la salud mental de formas diferentes. Existen muchos determinantes individuales, sociales y estructurales que influyen en ella, tales como factores psicológicos y biológicos individuales, habilidades emocionales, el abuso de sustancias y la genética, que pueden hacer que las personas sean más vulnerables a las afecciones de salud mental. Estas enfermedades pueden manifestarse en cualquier etapa de la vida y durante la infancia son particularmente perjudiciales. Algunos pueden ser crónicos (de larga duración), otros pueden aparecer y desaparecer en un corto período de tiempo.</p>', unsafe_allow_html=True) 

st.write('<p style="text-align: justify;">Según afirma la OIT (Organización Internacional del Trabajo) en Estados Unidos: La depresión clínica se ha convertido en una de las enfermedades más comunes, que llega a afectar cada año a una décima parte de los adultos en edad laboral. Los trastornos de ansiedad, trastornos bipolares y la depresión son algunos de los más comunes. De hecho, uno de cada cinco adultos estadounidenses experimenta una enfermedad mental cada año.</p>', unsafe_allow_html=True) 

st.write('<p style="text-align: justify;">Cerca del 60% de la población mundial trabaja. Para las personas con problemas de salud mental, el trabajo decente puede contribuir a la recuperación, inclusión e integración del individuo a la sociedad (Organización Internacional del Trabajo [OIT], s.f.).</p>', unsafe_allow_html=True)

st.write('<p style="text-align: justify;">Los entornos de trabajo seguros y sanos no solo son un derecho fundamental, sino que también tienen más probabilidades de minimizar la tensión y los conflictos en ese ámbito, mejorando la lealtad del personal y  así obtener un mayor rendimiento en la productividad laboral.</p>', unsafe_allow_html=True) 

st.write('<p style="text-align: justify;">Por el contrario, un ambiente laboral que tenga faltas de estructuras efectivas y apoyo en el trabajo, especialmente para quienes viven con trastornos mentales puede afectar la capacidad de las personas, decayendo el rendimiento de las actividades. Un empleado que enfrenta problemas de salud mental puede experimentar dificultades para comunicarse efectivamente, colaborar en equipo o resolver conflictos de manera constructiva. Esto puede generar problemas que a su vez afectan la dinámica y armonía del equipo de trabajo.</p>', unsafe_allow_html=True) 

st.write('<p style="text-align: justify;">La salud mental en la industria tecnológica es un tema de preocupación creciente debido a las características únicas de este sector, el cual pueden contribuir de manera positiva o negativa al bienestar psicológico de sus empleados. Cabe destacar que cuando hablamos de tecnología en la industria, lo hacemos en la aplicación de la ciencia y la ingeniería en el desarrollo y producción de bienes y servicios. Una de las limitaciones en esta industria en  cuanto a salud mental es la poca información que se tiene sobre la participación que existe dentro de la industria tecnológica con sus trabajadores que padecen enfermedades mentales, ésta falta de  información pueden afectar negativamente a los trabajadores que presentan este tipo de problemas, haciendo a la industria perder dinero. La Organización Mundial de la Salud ha determinado que “cada año se pierden 12.000 millones de días de trabajo debido a la depresión y la ansiedad con un costo de US $1 billón por año en pérdidas de productividad” (Organización Mundial de la Salud [OMS], 2024). El estigma puede ser tan perjudicial que obliga a los empleados a evitar identificarse con intenciones de no ser juzgados por compañeros de trabajo e incluso en algunos casos impedir el despido. Abordar los problemas de salud mental como la ansiedad, la depresión e incluso el estrés laboral centrándonos en alentar a las empresas a tomar medidas para reducir los riesgos y crear un ambiente de trabajo saludable. Es por ello, que dada la encuesta realizada en la industria tecnológica entre los años 2014 y 2019 con excepción del 2015; se seleccionaron los años 2016-2019 con encuestados residentes en Estados Unidos por la completa elaboración de las preguntas y el número de encuestados que residen en el país antes mencionado; a pesar de que no todas las personas respondieron el cuestionario correctamente.</p>', unsafe_allow_html=True)

st.write('<p style="text-align: justify;">Teniendo en cuenta este contexto surge el planteamiento “Problemáticas y Estigmas de las Enfermedades Mentales en la Industria Tecnológica Estadounidense en los Años 2016-2019” desprendiéndose las siguientes interrogantes:</p>', unsafe_allow_html=True)

st.subheader("Preguntas de Investigación")
st.write("")

objectives = [
    "¿Cuántas personas en la industria tecnológica estadounidense tienen una enfermedad mental diagnosticada y dentro de este grupo, existe algún historial familiar?",
    "¿Cuáles son los 5 estados con mayor registro de enfermedades mentales diagnosticadas y cual es la enfermedad mental predominante en cada uno?",
    "Según la cantidad de empleados en las empresas tecnológicas ¿Cuál tiene la mayor cantidad de empleados con enfermedades mentales? ¿Estas ofrecen algún beneficio o algún tipo de convenio?",
    "¿Cuál es la enfermedad mental más común dentro de cada puesto de trabajo en la industria tecnológica estadounidense? ¿De este grupo cuántos son su propio jefe o trabajan remotamente?",
    "¿Qué disposición tienen los empleados de la industria tecnológica a la hora de hablar sobre su enfermedad mental?",
    "¿El nivel de productividad de los trabajadores estadounidenses con enfermedades mentales diagnosticadas varía según su rango de edad?"
]

st.write("<ul>", unsafe_allow_html=True)
for objective in objectives:
    st.write(f"<li>{objective}</li>", unsafe_allow_html=True)
st.write("</ul>", unsafe_allow_html=True)

st.write('<p style="text-align: justify;">Dentro de este marco de interrogantes, se desprenden los siguientes objetivos:</p>', unsafe_allow_html=True)

st.subheader("Objetivo General") 
st.write('<ul><li>Analizar las problemáticas y los estigmas de las enfermedades mentales dentro de la industria tecnológica estadounidense entre los años 2016 y 2019.</li></ul>', unsafe_allow_html=True)

st.subheader("Objetivos Específicos")
st.write("")

objectives = [
    "Determinar las características e incidencias de las enfermedades mentales en la industria tecnológica estadounidense tomando en cuenta el diagnóstico, historial familiar, edad, género y puesto de trabajo de los afectados.",
    "Identificar el nivel de productividad de los empleados de la industria tecnológica estadounidense con enfermedades mentales y qué beneficios reciben para su tratamiento.",
    "Indagar la percepción externa de los trabajadores sobre las enfermedades mentales en la industria tecnológica estadounidense."
]

st.write("<ul>", unsafe_allow_html=True)
for objective in objectives:
    st.write(f"<li>{objective}</li>", unsafe_allow_html=True)
st.write("</ul>", unsafe_allow_html=True)
