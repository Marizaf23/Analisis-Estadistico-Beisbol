import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as px
import streamlit as st
import requests
from io import StringIO

def set_bg_hack_url():
    ''' 
    A function to unpack an image from url and set as bg. 
    Returns 
    ------- 
    The background. 
    ''' 
          
    st.markdown( 
          f""" 
          <style> 
         .stApp {{ 
              background: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fusing-artificial-intelligence-help-mental-health-shelley-goodman-mba-kpudc&psig=AOvVaw1mQVphZiA_S7XdkzNLhYj2&ust=1719350349209000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCID6sq6V9YYDFQAAAAAdAAAAABAp"); 
              background-size: cover 
          }} 
          </style> 
          """, 
          unsafe_allow_html=True 
      ) 

set_bg_hack_url()

# Título de la aplicación
st.title("Problemáticas y Estigmas de las Enfermedades Mentales en la Industria Tecnológica Estadounidense 2016-2019")

st.header("Introducción")
st.write("Información de la Data Suministrada.")
