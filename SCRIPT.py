import pandas as pd
import numpy  as np
import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect(r'C:\Users\maria\Documents\UCV MARY\EECA\SEMESTRE 2024-1\SEMESTRE II\COMPUTACIÓN II\TRABAJO FINAL\SALUD MENTAL EN LA INDUSTRIA TECNOLÓGICA 1.sqlite')

cur = conn.cursor()

consulta_ntablas = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"

# Mostrar las entidades
print("Entidades en la base de datos:")
entidades = pd.read_sql_query(sql = consulta_ntablas, con = conn)
entidades

consulta = "SELECT * FROM Respuestas;"
df_Respuestas = pd.read_sql_query(sql = consulta, con = conn)

conn.close()