import streamlit as st
import pandas as pd
import sqlite3 
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
st.set_page_config(
    page_title = 'Dashboard MayDay',
    page_icon = '✅',
    layout = 'wide'
)

##### Nos conectamos con la base de datos

conn = sqlite3.connect('accidentes.db') 
#print(conn) #Imprimimos para observar si todo va bien

##### Creamos el cursor para ejecutar sentencias en SQLite

cursor = conn.cursor()
cursor

##### Cargamos los DataFrames
df = pd.read_sql_query('select * from sucesos limit 5',con=conn)
wb = pd.read_sql_query('select * from worldbank limit 5',con=conn)
wb = wb.set_index('index')




st.title('Dashboard MayDay - SoyHenry!!')

#### Graficamos dos plots
st.markdown('Fallecidos y sobrevientes por año') # see *
image = Image.open('Charts/cantidad de fallecidos.png')
st.image(image)

st.markdown('Rperesentación de accidentes por despegue y aterrizaje, distribuido por ciudades') # see *
chart1, chart2, = st.columns(2)
with chart1:
    image = Image.open('Charts/accidene despegue.png')
    st.image(image, caption='Ciudades mas peligrosas para el despegue')
with chart2:
    image = Image.open('Charts/accidene aterrizaje.png')
    st.image(image, caption='Ciudades mas peligrosas para el aterrizaje')

chart3,chart4 = st.columns(2)
with chart3:
    image = Image.open('Charts/fallecidos por año.png')
    st.image(image, caption='Cantidad de fallecidos desde 1970 al 2009')
with chart4:
    image = Image.open('Charts/world bank.png')
    st.image(image, caption='crecimiento de personas que utilizan el avión como medio de transporte')

st.write('Descubrimos que existe una correlación negativa entre los 2 registros, lo que significa que a medida que la cantidad de pasajeros sigue aumentando, esperamos ver una disminución en la cantidad de muertes. Llegamos a la conclusión que es mas seguro viajar en avión hoy en día.') # see *



