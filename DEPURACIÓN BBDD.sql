CREATE TABLE Respuestas AS
SELECT *
FROM Answer;

DELETE FROM Respuestas
WHERE questionid IN (9, 11, 13, 15, 21, 22, 25, 26, 29, 32, 50, 51, 52, 57, 58, 59, 60, 61, 62, 63, 64, 66, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 80, 82, 84, 86, 87, 88, 90, 91, 95, 96, 98, 99, 100, 101, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113);

DELETE FROM Respuestas WHERE AnswerText = -1;

DELETE FROM Respuestas WHERE AnswerText NOT BETWEEN 18 AND 67 AND QuestionID = 1;

DELETE FROM Respuestas WHERE UserID = 365;
DELETE FROM Respuestas WHERE UserID = 1825;
DELETE FROM Respuestas WHERE UserID = 735;
DELETE FROM Respuestas WHERE UserID = 1917;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Female' THEN 'Femenino'
    WHEN answertext IN ('Masculine', 'Male', 'masculino') THEN 'Masculino'
    ELSE 'Otro'
END
WHERE questionid = 2;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = '1' THEN 'Si'
    WHEN answertext = '0' THEN 'No'
END
WHERE questionid = 5;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
				WHEN answertext = "I don't know" THEN 'No sé'
    ELSE 'No'
END
WHERE questionid = 6;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = '1' THEN 'Si'
    WHEN answertext = '0' THEN 'No'
END
WHERE questionid = 7;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
    WHEN answertext = 'No' THEN 'No'
    WHEN answertext = "Don't know" THEN 'No lo sé'
				WHEN answertext = "I don't know" THEN 'No lo sé'
				WHEN answertext = 'Not eligible for coverage / NA' THEN 'No elegible/Sin cobertura'
END
WHERE questionid = 10;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
    WHEN answertext = 'No' THEN 'No'
    WHEN answertext = 'Maybe' THEN 'Tal vez'
END
WHERE questionid = 12;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
    WHEN answertext = 'No' THEN 'No'
    WHEN answertext = 'I am not sure' THEN 'No estoy seguro(a)'
END
WHERE questionid = 14;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
    WHEN answertext = 'No' THEN 'No'
    WHEN answertext = "I don't know" THEN 'No lo sé'
END
WHERE questionid = 16;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Very easy' THEN 'Muy fácil'
    WHEN answertext = 'Somewhat easy' THEN 'Fácil'
    WHEN answertext = 'Neither easy nor difficult' THEN 'Más o menos'
				WHEN answertext = 'Very difficult' THEN 'Muy difícil'
				WHEN answertext = "I don't know" THEN 'No sé'
				WHEN answertext = 'Somewhat difficult' OR 'Difficult' THEN 'Difícil'
				ELSE 'Difícil'
END
WHERE questionid = 17;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
    WHEN answertext = 'No' THEN 'No'
    WHEN answertext = 'Maybe' THEN 'Tal vez'
END
WHERE questionid = 18;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
    WHEN answertext = 'No' THEN 'No'
    WHEN answertext = 'Maybe' THEN 'Tal vez'
END
WHERE questionid = 19;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = '1' THEN 'Si'
    WHEN answertext = '0' THEN 'No'
END
WHERE questionid = 20;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes, they all did' THEN 'Si, todos lo hicieron'
    WHEN answertext = 'No, none did' THEN 'No, ninguno lo hizo'
				WHEN answertext = "I don't know" THEN 'No sé'
				WHEN answertext = 'Some did' THEN 'Algunos lo hicieron'
END
WHERE questionid = 23;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'N/A (not currently aware)' THEN 'No conocía ninguna'
    WHEN answertext = 'I was aware of some' THEN 'Conocía algunas'
    WHEN answertext = 'Yes, I was aware of all of them' THEN 'Si, las conocía'
				WHEN answertext = 'No, I only became aware later' THEN 'No, las conocí después'
				WHEN answertext = 'N/A (was not aware)' THEN 'Conocía muy pocas'
				WHEN answertext = 'N/A (none offered)' THEN 'No me ofrecieron ninguna'
END
WHERE questionid = 24;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes, always' THEN 'Si, siempre'
    WHEN answertext = 'Sometimes' THEN 'A veces'
	WHEN answertext = 'No' THEN 'No'
    WHEN answertext = "I don't know" THEN 'No lo sé'
END
WHERE questionid = 27;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Some of my previous employers' THEN 'Con algunos de mis jefes anteriores'
    WHEN answertext = 'No, at none of my previous employers' THEN 'No, con ninguno de mis jefes anteriores'
				WHEN answertext = 'Yes, at all of my previous employers' THEN 'Si, con todos mis jefes anteriores'
				WHEN answertext = "I don't know" THEN 'No sé'
    WHEN answertext = 'Yes, all of my previous supervisors' THEN 'Si, con todos mis supervisores anteriores'
    WHEN answertext = 'No, none of my previous supervisors' THEN 'No, con ninguno de mis supervisores anteriores'
				WHEN answertext = 'Some of my previous supervisors' THEN 'Con algunos de mis jefes anteriores'
END
WHERE questionid = 28;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Somewhat open' THEN 'Dispuesto(a)'
    WHEN answertext = 'Neutral' THEN 'Neutral'
	WHEN answertext = 'Not applicable to me (I do not have a mental illness)' THEN 'No es mi caso (no tengo una enfermedad mental)'
	WHEN answertext = 'Very open' THEN 'Muy dispuesto'
    WHEN answertext = 'Not open at all' THEN 'No estoy dispuesto(a)'
    WHEN answertext = 'Somewhat not open' THEN 'No dispuesto(a)'
END
WHERE questionid = 30;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
    WHEN answertext = 'Maybe' THEN 'Tal vez'
	WHEN answertext = 'No' THEN 'No'
END
WHERE questionid = 31;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
    WHEN answertext = 'Maybe' THEN 'Tal vez'
				WHEN answertext = 'No' THEN 'No'
    WHEN answertext = 'Possibly' THEN 'Seguramente si'
				WHEN answertext = "Don't Know" THEN 'No lo sé'	
END
WHERE questionid = 33;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
    WHEN answertext = 'No' THEN 'No'
END
WHERE questionid = 34;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Not applicable to me' THEN 'No tengo una enfermedad mental'
    WHEN answertext = 'Sometimes' THEN 'A veces'
				WHEN answertext = 'Rarely' THEN 'Raramente'
    WHEN answertext = 'Never' THEN 'Nunca'
				WHEN answertext = 'Often' THEN 'A menudo'	
END
WHERE questionid = 48;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Not applicable to me' THEN 'No tengo una enfermedad mental'
    WHEN answertext = 'Sometimes' THEN 'A veces'
				WHEN answertext = 'Rarely' THEN 'Raramente'
    WHEN answertext = 'Never' THEN 'Nunca'
	WHEN answertext = 'Often' THEN 'A menudo'	
END
WHERE questionid = 49;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Sometimes, if it comes up' THEN 'Depende, si me lo preguntan'
    WHEN answertext = 'No, because it would impact me negatively' THEN 'No, influiriá negativamente'
				WHEN answertext = 'Not applicable to me' THEN 'No tengo una enfermedad mental'
    WHEN answertext = 'Yes, always' THEN 'Si, siempre'
				WHEN answertext = "No, because it doesn't matter" THEN 'No, no me importa'	
END
WHERE questionid = 53;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Unsure' THEN 'No estoy seguro(a)'
				WHEN answertext = 'Not applicable to me' THEN 'No tengo una enfermedad mental'
    WHEN answertext = 'Yes' THEN 'Si'
				WHEN answertext = 'No' THEN 'No'	
END
WHERE questionid = 54;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Maybe/Not sure' THEN 'Tal vez/No estoy seguro(a)'
				WHEN answertext = 'Yes, I experienced' THEN 'Si, me ha pasado'
    WHEN answertext = 'Yes, I observed' THEN 'Si, lo he visto'
				WHEN answertext = 'No' THEN 'No'
				WHEN answertext = "I've always been self-employed" THEN 'Siempre he sido mi propio jefe(a)'	
END
WHERE questionid = 56;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'No change' THEN 'No cambió'
    WHEN answertext = "I'm not sure" THEN 'No estoy seguro(a)'
				WHEN answertext = 'Not applicable to me' THEN 'No tengo una enfermedad mental'
    WHEN answertext = 'Negatively' THEN 'Cambió negativamente'
				WHEN answertext = 'Positively' THEN 'Cambió positivamente'	
END
WHERE questionid = 67;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = '1' THEN 'Si'
    WHEN answertext = '0' THEN 'No'
END
WHERE questionid = 78;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = '1' THEN 'Si'
    WHEN answertext = '0' THEN 'No'
END
WHERE questionid = 79;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Maybe/Not sure' THEN 'Tal vez/No estoy seguro(a)'
				WHEN answertext = 'Yes, I experienced' THEN 'Si, me ha pasado'
    WHEN answertext = 'Yes, I observed' THEN 'Si, lo he visto'
				WHEN answertext = 'No' THEN 'No'
				WHEN answertext = "I've always been self-employed" THEN 'Siempre he sido mi propio jefe(a)'	
END
WHERE questionid = 83;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = '1' THEN 'Nada'
				WHEN answertext = '2' THEN 'Poco'
    WHEN answertext = '3' THEN 'Más o menos'
				WHEN answertext = '4' THEN 'Lo suficiente'
				WHEN answertext = '5' THEN 'Mucho'	
END
WHERE questionid = 85;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'White' THEN 'Blanco(a)'
				WHEN answertext = 'More than one of the above' THEN 'Multiracial'
    WHEN answertext = 'Asian' THEN 'Asiático(a)'
				WHEN answertext = 'Black or African American' THEN 'Negro(a) o Afroamericano(a)'
				WHEN answertext = 'American Indian or Alaska Native' THEN 'Nativo Americano(a) o Nativo(a) de Aleska'
    WHEN answertext = 'I prefer not to answer' THEN 'Prefiero no responder'
				WHEN answertext = 'Hispanic' THEN 'Hispano(a)'
				WHEN answertext = 'White Hispanic' THEN 'Blanco hispano(a)'
    WHEN answertext = 'European American' THEN 'Americano (Descendiente Europeo)'
				WHEN answertext = 'Caucasian' THEN 'Caucásico'	
END
WHERE questionid = 89;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Sometimes' THEN 'A veces'
    WHEN answertext = 'Never' THEN 'Nunca'
    WHEN answertext = 'Often' THEN 'Usualmente'
				WHEN answertext = 'Rarely' THEN 'Raramente'	
END
WHERE questionid = 92;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
				WHEN answertext = 'No' THEN 'No'
END
WHERE questionid = 93;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
    WHEN answertext = 'Not sure' THEN 'No estoy seguro(a)'
				WHEN answertext = 'No' THEN 'No'
END
WHERE questionid = 94;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Very easy' THEN 'Muy fácil'
    WHEN answertext = 'Somewhat easy' THEN 'Fácil'
    WHEN answertext = 'Neither easy nor difficult' THEN 'Más o menos'
				WHEN answertext = 'Very difficult' THEN 'Muy difícil'
				WHEN answertext = "Don't know" THEN 'No sé'
				WHEN answertext = 'Somewhat difficult' OR 'Difficult' THEN 'Difícil'
END
WHERE questionid = 97;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes' THEN 'Si'
				WHEN answertext = 'No' THEN 'No'
END
WHERE questionid = 102;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Yes, they do' THEN 'Si lo hacen'
				WHEN answertext = "No, I don't think they would" THEN 'No, pienso que no lo harían'
    WHEN answertext = 'Yes, I think they would' THEN 'Si, pienso que lo harían'
				WHEN answertext = 'Maybe' THEN 'Tal vez'
    WHEN answertext = 'No, they do not' THEN 'No, no lo hacen'
END
WHERE questionid = 114;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Sometimes' THEN 'A veces'
				WHEN answertext = 'Never' THEN 'Nunca'	
				WHEN answertext = 'Always' THEN 'Siempre'		
END
WHERE questionid = 118;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = '0' THEN 'Nada importante'
				WHEN answertext = '1' THEN 'Muy poco importante'	
				WHEN answertext = '2' THEN 'Poco importante'
			 WHEN answertext = '3' THEN 'Moderadamente importante'
				WHEN answertext = '4' THEN 'Moderadamente importante'
				WHEN answertext = '5' THEN 'Medianamente importante'
				WHEN answertext = '6' THEN 'Medianamente importante'
				WHEN answertext = '7' THEN 'Algo importante'	
				WHEN answertext = '8' THEN 'Importante'
				WHEN answertext = '9' THEN 'Muy importante'
				WHEN answertext = '10' THEN 'Sumamente importante'	
END
WHERE questionid = 65;

UPDATE Respuestas
SET answertext = CASE
				WHEN answertext = 'More than 1000' THEN 'Más de 1000'
				WHEN answertext = '6-25' THEN '6-25'
				WHEN answertext = '26-100' THEN '26-100'
				WHEN answertext = '100-500' THEN '100-500'
				WHEN answertext = '1-5' THEN '1-5'
				WHEN answertext = '500-1000' THEN '500-1000'
END
WHERE questionid = 8;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = '0' THEN 'Muy mal'
				WHEN answertext = '1' THEN 'Mal'	
				WHEN answertext = '2' THEN 'Sin comentarios'
			 WHEN answertext = '3' THEN 'Indiferente'
				WHEN answertext = '4' THEN 'No creo que le(s) importe'
				WHEN answertext = '5' THEN 'Normal'
				WHEN answertext = '6' THEN 'Bien'
				WHEN answertext = '7' THEN 'Muy bien'	
				WHEN answertext = '8' THEN 'Me entiende(n)'
				WHEN answertext = '9' THEN 'Me apoya(n)'
				WHEN answertext = '10' THEN 'Me apoya(n) mucho'	
END
WHERE questionid = 81;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Anxiety Disorder (Generalized, Social, Phobia, etc)' THEN 'Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)'
				WHEN answertext = 'Mood Disorder (Depression, Bipolar Disorder, etc)' THEN 'Trastorno del Estado del Ánimo (Depresión, Trastorno Bipolar, etc.)'	
				WHEN answertext = 'Stress Response Syndromes' THEN 'Síndrome de Respuesta de Estrés'
			 WHEN answertext = 'Substance Use Disorder' THEN 'Trastorno de Consumo de Sustancias'
				WHEN answertext = 'Obsessive-Compulsive Disorder' THEN 'Trastorno Obsesivo-Compulsivo'
				WHEN answertext = 'Eating Disorder (Anorexia, Bulimia, etc)' THEN 'Trastorno de la Conducta Alimentaria (Anorexia, Bulimia, etc.)'
				WHEN answertext = 'Personality Disorder (Borderline, Antisocial, Paranoid, etc)' THEN 'Trastorno de la Personalidad (Peronalidad Límite, Antisocial, Paranoía, etc.)'
				WHEN answertext = 'Attention Deficit Hyperactivity Disorder' THEN 'Trastorno por Déficit de Atención e Hiperactividad'	
				WHEN answertext = 'Addictive Disorder' THEN 'Trastorno Adictivo'
				WHEN answertext = 'Post-traumatic Stress Disorder' THEN 'Trastorno de Estrés Post-Traumático'
				WHEN answertext = 'Pervasive Developmental Disorder (Not Otherwise Specified)' THEN 'Trastorno Generalizados del Desarrollo (TGD) (No específicado)'
    WHEN answertext = 'Seasonal Affective Disorder' THEN 'Trastorno Afectivo Estacional'
				WHEN answertext = 'Burn out' THEN 'Síndrome del Trabajador Quemado (Burn Out)'	
				WHEN answertext = 'PDD-NOS' THEN 'Trastorno Generalizados del Desarrollo (TGD)'
			 WHEN answertext = 'Dissociative Disorder' THEN 'Trastorno Disociativo'
				WHEN answertext = 'Depression' THEN 'Depresión'
				WHEN answertext = "Autism (Asperger's)" THEN 'Asperger'
				WHEN answertext = 'Traumatic Brain Injury' THEN 'Lesión Cerebral Traumática'
				WHEN answertext = 'Gender Dysphoria' THEN 'Disforía de Género'	
				WHEN answertext = 'Asperges' THEN 'Asperger'
				WHEN answertext = 'PTSD (undiagnosed)' THEN 'Trastorno de Estrés Post-Traumático (Sin diagnosticar)'
				WHEN answertext = 'Psychotic Disorder (Schizophrenia, Schizoaffective, etc)' THEN 'Trastorno Psicótico (Esquizofrenia, Esquizoafectivo, etc.)'
    WHEN answertext = 'Autism' THEN 'Autismo'
				WHEN answertext = 'Sexual addiction' THEN 'Adicción Sexual'	
				WHEN answertext = 'Combination of physical impairment (strongly near-sighted) with a possibly mental one (MCD / "ADHD", though its actually a stimulus filtering 		impairment)' THEN 'Combinación de una limitación física (Miopía) con una mental (DDH)'
			 WHEN answertext = 'Sleeping Disorder' THEN 'Trastorno del Sueño'
				WHEN answertext = "I haven't been formally diagnosed, so I felt uncomfortable answering, but Social Anxiety and Depression." THEN 'No he sido formalmente diagnosticado y me siento incómodo contestando, pero Ansiedad Social y Depresión'	
				WHEN answertext = 'Autism Spectrum Disorder' THEN 'Autismo'
				WHEN answertext = 'Transgender' THEN 'Transgénero'
				WHEN answertext = 'Intimate Disorder' THEN 'Trastorno Íntimo'
    WHEN answertext = 'ADD (w/o Hyperactivity)' THEN 'Trastorno por Déficit de Atención e Hiperactividad'
				WHEN answertext = 'Schizotypal Personality Disorder' THEN 'Trastorno Esquizotípico de la Personalidad'
				WHEN answertext = 'Autism spectrum disorder' THEN 'Autismo'	
END
WHERE questionid = 115;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Back-end Developer' THEN 'Programador(a) Back-End'
				WHEN answertext = 'Front-end Developer' THEN 'Programador(a) Front-End'	
				WHEN answertext = 'Supervisor/Team Lead' THEN 'Supervisor(a)/Líder de Equipo'	
				WHEN answertext = 'Executive Leadership' THEN 'Director(a) Ejecutivo'	
    WHEN answertext = 'Dev Evangelist/Advocate' THEN 'Promotor(a) de Desarrollo'	
				WHEN answertext = 'DevOps/SysAdmin' THEN 'DevOps/Administrador(a) de Sistemas'
				WHEN answertext = 'Support' THEN 'Soporte o Ayuda'	
				WHEN answertext = 'Designer' THEN 'Diseñador(a)'	
				WHEN answertext = 'One-person shop' THEN 'Emprendedor(a)'	
				WHEN answertext = 'Other' THEN 'Otros'	
				WHEN answertext = 'Sales' THEN 'Vendedor(a)'	
			 WHEN answertext = 'HR' THEN 'Recursos Humanos'
END
WHERE questionid = 117;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'New York' THEN 'Nueva York'
    WHEN answertext = 'North Carolina' THEN 'Carolina del Norte'
    WHEN answertext = 'South Carolina' THEN 'Carolina del Sur'
				WHEN answertext = 'New Jersey' THEN 'Nueva Jersey'
    WHEN answertext = 'Pennsylvania' THEN 'Pensilvania'
    WHEN answertext = 'New Mexico' THEN 'Nuevo México'
				WHEN answertext = 'DC' THEN 'Washington DC'
    WHEN answertext = 'District of Columbia' THEN 'Distrito de Columbia'
    WHEN answertext = 'West Virginia' THEN 'Virginia del Oeste'
				WHEN answertext = 'New Hampshire' THEN 'Nuevo Hampshire'
    WHEN answertext = 'South Dakota' THEN 'Dakota del Sur'
    WHEN answertext = 'North Dakota' THEN 'Dakota del Norte'
END
WHERE questionid = 4 AND answertext IN ('New York', 'North Carolina', 'Pennsylvania', 'New Mexico', 'West Virginia', 'New Hampshire', 'New Jersey', 'South Carolina', 'South Dakota', 'North Dakota', 'District of Columbia');

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'United States' THEN 'Estados Unidos'
				WHEN answertext = 'Canada' THEN 'Canadá'	
				WHEN answertext = 'United Kingdom' THEN 'Reino Unido'
			 WHEN answertext = 'Bulgaria' THEN 'Bulgaria'
				WHEN answertext = 'France' THEN 'Francia'
				WHEN answertext = 'Portugal' THEN 'Portugal'
				WHEN answertext = 'Netherlands' THEN 'Holanda'
				WHEN answertext = 'Switzerland' THEN 'Suiza'	
				WHEN answertext = 'Poland' THEN 'Polonia'
				WHEN answertext = 'Australia' THEN 'Australia'
				WHEN answertext = 'Germany' THEN 'Alemania'
    WHEN answertext = 'Russia' THEN 'Rusia'
				WHEN answertext = 'Mexico' THEN 'México'	
				WHEN answertext = 'Brazil' THEN 'Brasil'
			 WHEN answertext = 'Slovenia' THEN 'Eslovenia'
				WHEN answertext = 'Costa Rica' THEN 'Costa Rica'
				WHEN answertext = 'Austria' THEN 'Austria'
				WHEN answertext = 'Ireland' THEN 'Irlanda'
				WHEN answertext = 'India' THEN 'India'	
				WHEN answertext = 'South Africa' THEN 'Sudáfrica'
				WHEN answertext = 'Italy' THEN 'Italia'
				WHEN answertext = 'Sweden' THEN 'Suecia'
    WHEN answertext = 'Colombia' THEN 'Colombia'
				WHEN answertext = 'Latvia' THEN 'Letonia'	
				WHEN answertext = 'Romania' THEN 'Rumanía'
			 WHEN answertext = 'Belgium' THEN 'Bélgica'
				WHEN answertext = 'New Zealand' THEN 'Nueva Zelanda'	
				WHEN answertext = 'Zimbabwe' THEN 'Zimbabue'
				WHEN answertext = 'Spain' THEN 'España'
				WHEN answertext = 'Finland' THEN 'Finlandia'
    WHEN answertext = 'Uruguay' THEN 'Uruguay'
				WHEN answertext = 'Israel' THEN 'Israel'
				WHEN answertext = 'Bosnia and Herzegovina' THEN 'Bosnia y Herzegovina'
				WHEN answertext = 'Hungary' THEN 'Hungría'
				WHEN answertext = 'Singapore' THEN 'Singapur'
    WHEN answertext = 'Japan' THEN 'Japón'
				WHEN answertext = 'Nigeria' THEN 'Nigeria'	
				WHEN answertext = 'Croatia' THEN 'Croacia'
			 WHEN answertext = 'Norway' THEN 'Noruega'
				WHEN answertext = 'Thailand' THEN 'Tailandia'
				WHEN answertext = 'Denmark' THEN 'Dinamarca'
				WHEN answertext = 'Bahamas, The' THEN 'Bahamas'
				WHEN answertext = 'Greece' THEN 'Grecia'	
				WHEN answertext = 'Moldova' THEN 'Moldavia'
				WHEN answertext = 'Georgia' THEN 'Georgia'
				WHEN answertext = 'China' THEN 'China'
    WHEN answertext = 'Czech Republic' THEN 'República Checa'
				WHEN answertext = 'Philippines' THEN 'Filipinas'	
				WHEN answertext = 'United States of America' THEN 'Estados Unidos'
			 WHEN answertext = 'Lithuania' THEN 'Lituania'
				WHEN answertext = 'Venezuela' THEN 'Venezuela'	
				WHEN answertext = 'Argentina' THEN 'Argentina'
				WHEN answertext = 'Vietnam' THEN 'Vietnam'
				WHEN answertext = 'Slovakia' THEN 'Eslovaquia'
    WHEN answertext = 'Bangladesh' THEN 'Bangladesh'
				WHEN answertext = 'Algeria' THEN 'Argelia'
				WHEN answertext = 'Pakistan' THEN 'Pakistán'
				WHEN answertext = 'Afghanistan' THEN 'Afghanistán'	
				WHEN answertext = 'Other' THEN 'Otros'
			 WHEN answertext = 'Brunei' THEN 'Brunéi'
				WHEN answertext = 'Iran' THEN 'Irán'
				WHEN answertext = 'Ecuador' THEN 'Ecuador'
				WHEN answertext = 'Chile' THEN 'Chile'
				WHEN answertext = 'Guatemala' THEN 'Guatemala'	
				WHEN answertext = 'Taiwan' THEN 'Taiwán'
				WHEN answertext = 'Serbia' THEN 'Serbia'
				WHEN answertext = 'Estonia' THEN 'Estonia'
    WHEN answertext = 'Iceland' THEN 'Islandia'
				WHEN answertext = 'Indonesia' THEN 'Indonesia'	
				WHEN answertext = 'Jordan' THEN 'Jordania'
			 WHEN answertext = 'Ukraine' THEN 'Ucrania'
				WHEN answertext = 'Belarus' THEN 'Bielorrusia'
				WHEN answertext = 'Turkey' THEN 'Turquía'
				WHEN answertext = 'Mauritius' THEN 'Mauricio'	
				WHEN answertext = 'Saudi Arabia' THEN 'Arabia Saudita'
				WHEN answertext = 'Kenya' THEN 'Kenia'
				WHEN answertext = 'Ethiopia' THEN 'Etiopía'
    WHEN answertext = 'Macedonia' THEN 'Macedonia del Norte'
				WHEN answertext = 'Hong Kong' THEN 'Hong Kong'	
				WHEN answertext = 'Ghana' THEN 'Ghana'
END
WHERE questionid = 3;

UPDATE Respuestas
SET answertext = CASE
    WHEN answertext = 'Substance Use Disorder' THEN 'Trastorno de Consumo de Sustancias'
				WHEN answertext = 'Addictive Disorder' THEN 'Trastorno Adictivo'	
				WHEN answertext = 'Anxiety Disorder (Generalized, Social, Phobia, etc)' THEN 'Trastorno de Ansiedad (Genralizado, Social, Fobia, etc.)'
			 WHEN answertext = 'Mood Disorder (Depression, Bipolar Disorder, etc)' THEN 'Trastorno del Estado del Ánimo (Depresión, Trastorno Bipolar, etc.)'
				WHEN answertext = 'Attention Deficit Hyperactivity Disorder' THEN 'Trastorno por Déficit de Atención e Hiperactividad'
				WHEN answertext = 'Psychotic Disorder (Schizophrenia, Schizoaffective, etc)' THEN 'Trastorno Psicótico (Esquizofrenia, Esquizoafectivo, etc.)'
				WHEN answertext = 'Personality Disorder (Borderline, Antisocial, Paranoid, etc)' THEN 'Trastorno de la Personalidad (Peronalidad Límite, Antisocial, Paranoía, etc.)'
				WHEN answertext = 'Obsessive-Compulsive Disorder' THEN 'Trastorno Obsesivo-Compulsivo'	
				WHEN answertext = 'Eating Disorder (Anorexia, Bulimia, etc)' THEN 'Trastorno de la Conducta Alimentaria (Anorexia, Bulimia, etc.)'
				WHEN answertext = 'Stress Response Syndromes' THEN 'Síndrome de Respuesta de Estrés'
				WHEN answertext = 'Suicidal Ideation' THEN 'Ideación suicida'
    WHEN answertext = "We're all hurt, right?!" THEN 'No tengo una enfermedad mental'
				WHEN answertext = 'Burnout' THEN 'Síndrome del Trabajador Quemado (Burn Out)'	
				WHEN answertext = 'Gender Identity Disorder' THEN 'Disforía de Género'
			 WHEN answertext = 'Post-traumatic Stress Disorder' THEN 'Trastorno de Estrés Post-Traumático'
				WHEN answertext = 'Tinnitus' THEN 'No tengo una enfermedad mental'
				WHEN answertext = 'Dissociative Disorder' THEN 'Trastorno Disociativo'
				WHEN answertext = 'Depersonalisation' THEN 'Trastorno de Despersonalización-Desrealización'
				WHEN answertext = 'post-partum / anxiety' THEN 'Depresión Post-Parto/Ansiedad'	
				WHEN answertext = 'Asperger Syndrome' THEN 'Asperger'
				WHEN answertext = "Asperger's" THEN 'Asperger'
				WHEN answertext = 'depersonalization disorder' THEN 'Trastorno de Despersonalización-Desrealización'
    WHEN answertext = 'Autism' THEN 'Autismo'
END
WHERE questionid = 116;
