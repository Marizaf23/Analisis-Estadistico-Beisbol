import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect(r'C:/Users/rsanchez/Downloads/mental_health.sqlite')

cur = conn.cursor()

# Ejecutar la consulta SQL
cur.execute("""
SELECT
    S.SurveyID AS Año_Encuesta,
    COUNT(DISTINCT A.UserID) AS Encuestados,
    GROUP_CONCAT(DISTINCT A2.AnswerText) AS Generos,
    ROUND(AVG(CAST(A.AnswerText AS INTEGER)), 2) AS Edad_Promedio,
    MIN(CAST(A.AnswerText AS INTEGER)) AS Edad_Minima,
    MAX(CAST(A.AnswerText AS INTEGER)) AS Edad_Maxima
FROM Answer A
JOIN Survey S ON A.SurveyID = S.SurveyID
JOIN Answer A2 ON S.SurveyID = A2.SurveyID AND A2.QuestionID = 2
WHERE A.QuestionID = 1
GROUP BY S.SurveyID, A2.AnswerText;
""")

# Obtener los resultados de la consulta
rows = cur.fetchall()

# Imprimir los resultados
for row in rows:
    print(f"Año de encuesta: {row[0]}, Encuestados: {row[1]}, Géneros: {row[2].split(',')}, Edad promedio: {row[3]}, Edad mínima: {row[4]}, Edad máxima: {row[5]}")