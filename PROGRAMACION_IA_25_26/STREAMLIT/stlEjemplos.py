# EJEMPLOS DE STREAMLIT
# Obtenidos de: https://docs.streamlit.io/get-started



import streamlit as st
import pandas as pd
import numpy as np

st.write("Primer intento de creación de una tabla:")
st.write(pd.DataFrame({
    'Primera columna': [1, 2, 3, 4],
    'Segunda columna': [10, 20, 30, 40]
}))

st.write("Primer intento para mostrar un dataframe:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("Primer intento de gráfico:")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("Primer intento de mapa:")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

## WIDGETS ##
st.write("Widgets interactivos:")

import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'al cuadrado es ', x * x)

st.text_input("Dime tu nombre", key="name")

# Se puede acceder al valor en cualquier momento con:
st.session_state.name

# Usando checkbox para mostrar/ocultar un dataframe

if st.checkbox('Mostrar dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
# Usando un selectbox para elegir una opción
df = pd.DataFrame({
    'primera columna': [1, 2, 3, 4],
    'segunda columna': [10, 20, 30, 40]
    })

option = st.selectbox(
    '¿Que número te gusta?',
     df['primera columna'])

'Has seleccionado: ', option