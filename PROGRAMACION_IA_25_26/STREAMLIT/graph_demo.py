import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Demostración de gráfica: Lanzamiento de moneda")
st.subheader("Ejemplo del teorema del límite central con STREAMLIT")
st.write(
    """
    En este ejemplo, simulamos el lanzamiento de una moneda utilizando una distribución binomial.
    Luego, calculamos la media de múltiples muestras y mostramos la distribución de estas medias.
    Según el teorema del límite central, la distribución de las medias tenderá a ser normal a medida que aumente el número de muestras.
    """
)

perc_heads = st.number_input(label = "Posibilidad de cara (%)", min_value=0.0, max_value=1.0, value=.5)
graph_title = st.text_input(label="Título del gráfico", value="Lanzamiento de moneda")
binom_dist = np.random.binomial(n=1, p=perc_heads, size=1000)
list_of_means = []
for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())
fig, ax = plt.subplots()
plt.hist(list_of_means, range=(0, 1), bins=20, density=True)
plt.title(graph_title)
st.pyplot(fig)