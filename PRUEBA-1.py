import pandas as pd
import numpy  as np
import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect(r'C:\Users\maria\Documents\UCV MARY\EECA\SEMESTRE 2024-1\SEMESTRE II\COMPUTACIÓN II\TRABAJO FINAL\SALUD MENTAL EN LA INDUSTRIA TECNOLÓGICA.sqlite')

cur = conn.cursor()

cur.execute("SELECT * FROM Survey")
rows = cur.fetchall()

for row in rows:
    print(row)