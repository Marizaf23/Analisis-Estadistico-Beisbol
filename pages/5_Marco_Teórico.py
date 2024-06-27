import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as px
import streamlit as st
import requests
from io import StringIO

# Título de la aplicación
st.title("Problemáticas y Estigmas de las Enfermedades Mentales en la Industria Tecnológica Estadounidense 2016-2019")

st.header("Marco Teórico")
st.write("""
<style>
p {
  text-align: justify;
}
</style>
<p>La enfermedad mental puede ocasionar problemas en la vida cotidiana, por ejemplo, en la escuela, el trabajo o en las relaciones interpersonales. En la mayor parte de los casos, los síntomas pueden tratarse con una combinación de medicamentos y terapia de conversación (psicoterapia).</p>
<p>Las personas manifiestan problemas de salud mental de vez en cuando. Pero un problema de salud mental se convierte en una enfermedad mental cuando los signos y los síntomas se hacen permanentes, causan estrés y afectan la capacidad de funcionar normalmente.</p>
<p>Las enfermedades mentales son trastornos que van de leves a graves, que afectan el pensamiento, el estado de ánimo y/o el comportamiento de una persona. Según el Instituto Nacional de Salud Mental, casi uno de cada cinco adultos vive con una enfermedad mental.</p>
<p>Muchos factores contribuyen a tener problemas de salud mental, entre ellos:</p>
<ul>
  <li>Atributos hereditarios. La enfermedad mental es más frecuente en las personas cuyos parientes consanguíneos también la padecen. Ciertos genes pueden aumentar el riesgo de contraer una enfermedad mental y la situación de vida en particular puede desencadenarla.</li>
  <li>Exposición ambiental anterior al nacimiento. La exposición a factores de estrés ambientales, enfermedades inflamatorias, toxinas, drogas o alcohol en el útero puede asociarse, en algunos casos, con la enfermedad mental.</li>
  <li>Química del cerebro. Los neurotransmisores son sustancias químicas que se encuentran naturalmente en el cerebro y que transmiten señales a otras partes del cerebro y del cuerpo. Cuando las redes neuronales que contienen estas sustancias químicas se ven alteradas, la función de los receptores nerviosos y de los sistemas nerviosos cambia, lo que genera depresión y otros trastornos emocionales.</li>
</ul>
<p>Según los Centros para el Control de Enfermedades, los trastornos de salud mental afectan a más del 18 por ciento de los adultos solo en los Estados Unidos.</p>
<p>Y la Organización Mundial de la Salud informa que la depresión es la principal causa de discapacidad en todo el mundo. Aunque se informa que las enfermedades de salud mental no tratadas les cuestan a las empresas estadounidenses alrededor de $500 mil millones en pérdida de productividad, sin embargo, cuando las empresas priorizan la salud mental de sus trabajadores, pueden tener éxito y prosperar en el lugar de trabajo. Los empleadores deben considerar proporcionar recursos sólidos y sistemas de apoyo para los empleados, incluidos los técnicos de mantenimiento. (U.S Centers for Disease Control and Prevention [CDC], 2019).</p>
<p>La relación entre la salud mental y la productividad es innegable. Cuando los colaboradores están mentalmente saludables, tienden a ser más productivos. El estrés, la ansiedad y otros problemas de salud mental pueden afectar negativamente la concentración, la toma de decisiones y la calidad del trabajo.</p>
<p>Además, los problemas de salud mental no tratados pueden llevar a una mayor rotación de personal y ausentismo, lo que interrumpe la continuidad del trabajo y aumenta los costos para la empresa. Por otro lado ésto conlleva a crear estigmas dentro de éste entorno, los estigmas son una asociación de estereotipos negativos a una etiqueta y que discrimina a las personas, para las personas con enfermedades mentales el ser discriminados puede llevarlos a punto inimaginables, es por ello la importancia de estar informados y que ellos den a conocer su enfermedad sin sentir temor.</p>
<p>Para seguir siendo competitivas y ofrecer beneficios integrales, las empresas de mantenimiento deben priorizar la salud mental de sus empleados. Cuando los empleados tienen satisfechas sus necesidades básicas, que incluyen la salud mental, pueden generar más valor para sus organizaciones</p>
""", unsafe_allow_html=True)

st.subheader("Problemas de Salud Mental")
st.write("""
<style>
p {
  text-align: justify;
}
</style>
<ul>
  <li>Anorexia: Es un trastorno alimentario que resulta en una pérdida de peso poco saludable. Las personas con anorexia pueden tener una imagen corporal distorsionada y restringen sus calorías y/o se purgan para alcanzar objetivos de peso poco realistas.</p>
  <li>Autismo: Son un grupo de afecciones diversas. Se caracterizan por algún grado de dificultad en la interacción social y la comunicación. Otras características que presentan son patrones atípicos de actividad y comportamiento; por ejemplo, dificultad para pasar de una actividad a otra, gran atención a los detalles y reacciones poco habituales a las sensaciones.</p>
<ul>
<p>En el año 2013, el autismo pasó a llamarse trastorno del espectro autista (TEA), justamente debido a la comprobación de que existen varios tipos de autismo. En general, el trastorno se define por la presencia de déficit persistentes en la interacción social y en la comunicación.</p>
<p>Aunque en el autismo o trastorno del espectro autista (TEA) se considera un trastorno mental según los dos sistemas de clasificación más importantes de los trastornos mentales, el DSM-V y el CIE-11. Sin embargo, en algunos países anglosajones, como Reino Unido, Canadá y Australia, se está optando cada vez más por entenderlo como una condición.</p>
<ul>  
  <li>Bulimia: Es un trastorno de la conducta alimentaria en el que el enfermo tiene una sensación de hambre anormal y muy acusada. Se caracteriza por momentos en los que el afectado come compulsivamente, seguidos de otros de culpabilidad y malestar que en ocasiones le inducen a provocar el vómito, tomar laxantes y/o abusar del ejercicio físico para contrarrestar el exceso de ingesta.</p>
  <li>Burn out: Síndrome de burnout o "síndrome del trabajador quemado": hace referencia a la cronificación del estrés laboral. Este se manifiesta a través de un estado de agotamiento físico y mental que se prolonga en el tiempo y llega a alterar la personalidad y autoestima del trabajador. Es un proceso en el que progresivamente el trabajador sufre una pérdida del interés por sus tareas y va desarrollando una reacción psicológica negativa hacia su ocupación laboral.</p>
  <li>Depresión: Es un trastorno mental caracterizado fundamentalmente por un bajo estado de ánimo y sentimientos de tristeza, asociados a alteraciones del comportamiento, del grado de actividad y del pensamiento.</p>
  <li>Disforia de Género: Es una sensación de angustia o incomodidad que puede experimentar una persona cuando su identidad de género no coincide con su sexo biológico o con las características físicas relacionadas con el sexo. Esta sensación puede ser tan intensa que puede llevar a depresión, ansiedad y tener un impacto negativo en la vida cotidiana.</p>
  <li>Drogadicción (trastorno de consumo de sustancias): Es una enfermedad que afecta el cerebro y el comportamiento de una persona, y da lugar a una incapacidad para controlar el consumo de medicamentos o drogas ilícitas. El alcohol, la marihuana y la nicotina también se consideran sustancias adictivas. Cuando eres adicto, es posible que sigas consumiendo la sustancia adictiva a pesar del daño que provoca.</p>
  <li>Esquizofrenia: Es un trastorno mental grave por el cual las personas interpretan la realidad de manera anormal. La esquizofrenia puede provocar una combinación de alucinaciones, delirios y trastornos graves en el pensamiento y el comportamiento, que afecta el funcionamiento diario y puede ser incapacitante.</p>
  <li>Lesión cerebral traumática: Suele ocurrir como resultado de un golpe o impacto violento en la cabeza o el cuerpo. Un objeto que penetra el cráneo, como una bala o un pedazo roto de cráneo, también puede provocar una lesión cerebral traumática.</p>
  <li>Sexo adicción:  Tiene su base en una activación psicofisiológica que deriva en una dependencia a todo lo relacionado con el sexo, incrementando su frecuencia hasta derivar en consecuencias negativas para el desarrollo normal del día a día puesto que el sexo se vuelve el centro de todo en sus vidas dejando a un lado todo lo demás, Por ello, la adicción al sexo se puede comparar con otras adicciones como el adicto a las drogas, al juego o al alcohol, donde nunca se ven saciados y tienden a la pérdida de control.
  <li>Síndrome de Asperger: Es un trastorno del neurodesarrollo; el cerebro de la persona con Síndrome de Asperger funciona de manera diferente a la habitual, especialmente en la comunicación e interacción social y en la adaptación flexible a las demandas diarias.
<ul>
""", unsafe_allow_html=True)

st.write("""
<style>
p {
  text-align: justify;
}
</style>
<p>Comparte las características nucleares del autismo. La persona con Síndrome de Asperger tiene dificultades en la comunicación social y en la flexibilidad de pensamiento y comportamiento. Sin embargo, tiene un lenguaje fluido y una capacidad intelectual media e incluso superior a la media de la población.</p>
<ul>  
  <li>Síndrome de Respuesta al Estrés: Es la respuesta del cuerpo ante los estímulos estresores. Esta respuesta incluye cambios fisiológicos, como el cortisol, y psicológicos, como la ansiedad y la inquietud.</p>
  <li>Transgénero: La Organización Mundial de la Salud (OMS) ya no considera la transexualidad un trastorno mental, sino una "incongruencia de género" que se incluye en el capítulo de "condiciones relativas a la salud sexual" de su manual de enfermedades, así que ser transgénero no es una enfermedad mental en sí misma. Sin embargo, las personas transgénero pueden experimentar muchas afecciones mentales debido a factores como la presión social, la discriminación y la inaceptabilidad. Por ejemplo, las personas transgénero pueden tener niveles elevados de depresión, angustia, abuso de sustancias y un mayor riesgo de suicidio.</p>
  <li>Trastorno Adictivo: Es un comportamiento o consumo de sustancias que se caracteriza por un patrón compulsivo a pesar de las consecuencias negativas que pueda tener en la vida de la persona. Los trastornos adictivos pueden variar de leve a grave y pueden afectar el cerebro y el comportamiento de una persona.</p>
  <li>Trastorno bipolar: Es trastorno del estado del ánimo, es una enfermedad crónica y recurrente que se manifiesta principalmente por episodios alternantes de sintomatología depresiva (episodios depresivos) y periodos de exaltación del humor e incremento de la vitalidad (episodios maníacos o hipomaníacos).</p>
  <li>Trastorno Esquizoafectivo: Es un trastorno de salud mental que combina síntomas de esquizofrenia, como alucinaciones o delirios, y síntomas de trastornos del estado de ánimo, como depresión o manía. También puede causar pérdida de contacto con la realidad.</p>
  <li>Trastorno Esquizotípico de la Personalidad: Se suele caracterizar a las personas con trastorno esquizotípico de la personalidad como extrañas o excéntricas y por lo general tienen pocas o ninguna relación cercana. Generalmente no entienden cómo se forman las relaciones o el impacto de su conducta en los demás.</p>
  <li>Trastorno de Ansiedad Generalizada: Es una condición en la que las personas experimentan preocupación o ansiedad excesiva y continua, que es difícil de controlar y afecta su vida diaria.</p>
  <li>Trastorno de Ansiedad Social: Se puede conceptualizar en dos subtipos: el trastorno de ansiedad social generalizado y el trastorno de ansiedad social no generalizado. El generalizado se refiere a las personas que presentan temor a la mayoría de las situaciones de exposición social. El no generalizado se manifiesta con el temor a una o a unas pocas situaciones identificables.</p>
  <li>Trastorno de Déficit de Atención Hiperactividad (ADHD por sus siglas en inglés):  Es un trastorno psicológico común que se caracteriza por problemas de atención, impulsividad y/o hiperactividad. Los adultos que tienen problemas serios con la inatención, pero no tienen ningún o pocos síntomas de hiperactividad, se dice que tienen predominantemente un subtipo inatento de AD/HD.</p>
  <li>Trastornos de la Conducta Alimentaria (TCA): Entre este trastorno se encuentra la anorexia y la bulimia nerviosas, son trastornos psicológicos que comportan anomalías graves en el comportamiento de la ingesta nutricional.</p>
  <li>Trastorno del Sueño: Es una afección médica que altera los patrones normales de sueño. Puede afectar la calidad, el momento y la cantidad de sueño, y puede causar problemas en el funcionamiento durante el día.
<ul>
""", unsafe_allow_html=True)

st.write("""
<style>
p {
  text-align: justify;
}
</style>
<ul>  
  <li>Trastorno de Estrés Pos-Traumático: Es una enfermedad de salud mental desencadenada por una situación aterradora, ya sea que la hayas experimentado o presenciado. Los síntomas pueden incluir reviviscencias, pesadillas y angustia grave, así como pensamientos incontrolables sobre la situación.
  <li>Trastorno de Personalidad: Es una enfermedad de salud mental en la que las personas tienen un patrón de por vida de verse a sí mismas y reaccionar ante los demás de formas que causan problemas. Las personas con trastornos de la personalidad suelen tener dificultades para comprender las emociones y tolerar el sufrimiento emocional, y actúan de forma impulsiva.
  <li>Trastornos Generalizados del Desarrollo o TGD: Se refiere a un grupo de trastornos caracterizados por retrasos en el desarrollo de las aptitudes de socialización y comunicación.
  <li>Trastorno Íntimo: Es un problema que ocurre durante alguna fase del ciclo de respuesta sexual y que impide a la persona o pareja disfrutar de la actividad sexual.
  <li>Trastorno Límite de la Personalidad (TLP) o Borderline: Es una enfermedad mental que afecta gravemente la capacidad de una persona para controlar sus emociones. Este trastorno se caracteriza por inestabilidad del estado de ánimo, la conducta y las relaciones sociales.
  <li>Trastorno Obsesivo-Compulsivo:Es una afección mental que consiste en presentar pensamientos (obsesiones) y rituales (compulsiones) una y otra vez. Las obsesiones pueden ser pensamientos, impulsos, imágenes mentales o preocupaciones excesivas que causan ansiedad o angustia. Estos interfieren con su vida, pero no puede controlarlos ni detenerlos.
  <li>Trastorno por Déficit de Atención con Hiperactividad: Es un trastorno mental crónico que se caracteriza por una combinación de problemas persistentes, como dificultad para prestar atención, hiperactividad y conducta impulsiva. Este trastorno puede comenzar en la niñez y continuar hasta la adolescencia e incluso la edad adulta.
  <li>Trastorno Psicótico: Son desórdenes mentales graves caracterizados por una alteración global de la personalidad que provoca que las personas que los sufren tengan ideas y percepciones anormales, distorsionadas de la realidad.
<ul>
""", unsafe_allow_html=True)

st.subheader("Enfermedades Mentales en la TI")
st.write("""
<style>
p {
  text-align: justify;
}
</style>
<p>Se habla mucho de la escasez de talento en la industria tecnológica, la cual está sometida a una enorme presión gracias a las exigencias de la transformación digital actual. Es cierto que hay un déficit mundial de ingenieros de software y otros especialistas, cuyas habilidades son necesarias para ayudar a las empresas a salir adelante en tiempos difíciles.</p>
<p>El agotamiento está muy extendido en el sector TI, con un gran número de trabajadores tecnológicos que luchan contra problemas de salud mental como el estrés, la ansiedad y la depresión.</p>
<p>Los síntomas del estrés incluyen dolores de cabeza, ataques de ansiedad, insomnio, indigestión y cansancio continuo, éstos trabajadores se podrían clasificar como “constantemente estresados”. Igualmente, la ansiedad y la depresión que experimentan se manifiestan en forma de fatiga, tristeza, pesimismo, pérdida de interés, sentimientos de inutilidad y desesperanza.</p>
<p>Algunos grupos específicos del sector tecnológico son más propensos a padecer estrés, y los más expuestos son los que ya tienen un problema de salud de larga duración.  Los enfermos recientes de depresión y ansiedad, las mujeres, los jóvenes de 18 a 34 años, los bisexuales y los que se autodescriben como tales, así como los padres que regresan, son también grupos que declaran niveles de estrés significativamente más altos.</p>
<p>Un grupo que está especialmente bien representado en el sector tecnológico es el del personal neurodivergente. Neurodivergente es el término que se utiliza generalmente para las personas cuyo funcionamiento mental o neurológico difiere de lo que se considera típico, como los que tienen TDAH, autismo, dislexia, dispraxia, síndrome de Tourette y discalculia.</p>
<p>Neurotípico es el término utilizado para las personas no neurodivergente, es decir, las que no se identifican como poseedoras de ninguna de las condiciones mencionadas.</p>
<p>En este entorno, es imperativo que hagamos un esfuerzo consciente para priorizar la salud mental. Los empleadores tienen un papel esencial en esto al crear ambientes de trabajo que fomenten la apertura, la flexibilidad y el bienestar de los empleados.</p>
<ul>  
  <li>Promover la Comunicación Abierta: Establecer un espacio seguro para que los empleados compartan sus preocupaciones y desafíos es fundamental. La comunicación abierta reduce el estrés y fomenta un sentido de comunidad.</p>
  <li>Fomentar el Equilibrio entre el Trabajo y la Vida Personal: Establecer límites claros entre el tiempo de trabajo y el tiempo personal ayuda a los empleados a desconectar y recargar energías, lo que es vital para su bienestar.</p>
  <li>Ofrecer Recursos de Apoyo: Proporcionar acceso a recursos como asesoramiento, programas de bienestar, y capacitación en manejo del estrés puede marcar una gran diferencia en la vida de los empleados.</p>
  <li>Incentivar el Desarrollo Profesional y Personal: Apoyar el crecimiento y desarrollo integral de los empleados, tanto en el ámbito profesional como personal, puede aumentar su satisfacción laboral y bienestar.</p>
  <li>Promover la Autocuidado: Incentivar prácticas de autocuidado, como el ejercicio, la meditación y el tiempo de descanso, puede contribuir a una mejor salud mental y un mayor rendimiento laboral.</p>
<ul>
<p>En última instancia, todos somos responsables de crear una cultura laboral que valore la salud mental y promueva el bienestar. Juntos, podemos marcar la diferencia y construir un futuro tecnológico más humano y sostenible.</p>
""", unsafe_allow_html=True)
