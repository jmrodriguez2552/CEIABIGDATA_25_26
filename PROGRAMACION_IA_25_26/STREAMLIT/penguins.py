import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
 
st.title("Palmer's Penguins") 
st.markdown('¡Utiliza esta aplicación Streamlit para crear tu propio diagrama de dispersión sobre pingüinos!') 
 
selected_x_var = st.selectbox('¿Qué valor quieres que tenga la variable x?', 
  ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']) 
selected_y_var = st.selectbox('Y para la variable y?', 
  ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g']) 
 
penguin_file = st.file_uploader('Selecciona tu fichero CSV de pingüinos de tu disco local',) 
if penguin_file is not None: 
	penguins_df = pd.read_csv(penguin_file) 
else: 
	st.stop()

sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
fig, ax = plt.subplots() 
ax = sns.scatterplot(data = penguins_df, x = selected_x_var, 
  y = selected_y_var, hue = 'species', markers = markers,
  style = 'species') 
plt.xlabel(selected_x_var) 
plt.ylabel(selected_y_var) 
plt.title("Diagrama de dispersión de los pingüinos de Palmer") 
st.pyplot(fig) 