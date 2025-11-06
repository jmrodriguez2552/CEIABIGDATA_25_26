import streamlit as st
import numpy as np
import time

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)
for i in range(1, 101):
    new_rows = last_rows + np.random.randn(5, 1).cumsum(axis=0)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)
progress_bar.empty()
# Los widgets de streamlit se actualizan automáticamente cuando el script se vuelve a ejecutar.
# Por lo tanto, no es necesario un bucle infinito para actualizar la gráfica.
st.button("Actualizar gráfica")