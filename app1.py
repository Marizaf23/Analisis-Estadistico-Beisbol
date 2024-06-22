# Título de la aplicación
st.title("Problemáticas y Estigmas de las Enfermedades Mentales en la Industria Tecnológica Estadounidense en el Año 2016")

st.dataframe(df_Investigacion)

# Título de la aplicación
st.title("Análisis del Conjunto de Datos Iris")

st.write("""
## Introducción

""")

# %%

# PREGUNTA #1
#¿Cuántas personas en la industria tecnológica tienen una enfermedad mental diagnosticada y, dentro de este grupo, existe algún historial familiar dentro de este ámbito?

Pregunta1 = pd.crosstab(df_Investigacion['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], 
                        df_Investigacion['Historial Familiar'], 
                        margins=True, 
                        margins_name='Total')

Pregunta1.index.name = 'Historial Familiar'
Pregunta1.columns.name = '¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'

# Renderizar la tabla en formato HTML
html_table = Pregunta1.to_html()

print(html_table)


# %%
Pregunta1 = pd.crosstab(df_Investigacion['¿Alguna Vez Has Sido Diagnosticado con una Enfermedad Mental?'], 
                        df_Investigacion['Historial Familiar'], 
                        margins=True, 
                        margins_name='Total')

Pregunta1.columns.name = 'Historial Familiar'
Pregunta1.index.name = '¿Tienes Alguna Enfermedad Mental?'


# %%

import streamlit as st

# Call set_page_config() as the first Streamlit command
st.set_page_config(
    page_title="My App",
    page_icon=":shark:",
    layout="wide"
)

# Rest of your Streamlit app code goes here
st.write("Hello, World!")

# Título de la aplicación
st.title("Problemáticas y Estigmas de las Enfermedades Mentales en la Industria Tecnológica Estadounidense en el Año 2016")


# Crea un menú de pestañas
tab1, tab2 = st.tabs(["Página 1", "Página 2"])

# Contenido de la página 1
with tab1:
    st.header("Página 1")
    st.write("Este es el contenido de la página 1.")
    
# Contenido de la página 2
with tab2:
    st.header("Página 2")
    st.write("Este es el contenido de la página 2.")
    

st.dataframe(df_Investigacion)

st.write("""
## Introducción

""")

st.write("Tabla")
st.write(Pregunta1)

#%