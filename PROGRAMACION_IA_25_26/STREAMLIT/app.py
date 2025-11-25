import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# -----------------------------------------------------------
# Función de predicción
# -----------------------------------------------------------
def load_predictor():
    """Carga el preprocesador y la RNA desde sus archivos correspondientes"""

    # Cargar preprocesamiento
    with open("preprocess.pkl", "rb") as f:
        preprocess = pickle.load(f)

    # Cargar la red neuronal entrenada
    model = load_model("rna_wine_model_v3.keras", compile=False)
    model.compile(optimizer='adam', loss='mse')

    return preprocess, model


def predict_rating(preprocess, model, input_data):
    """
    Realiza la predicción usando el preprocesador y la RNA cargada.
    
    input_data debe ser un diccionario con los valores del vino.
    """

    # Convertir el input a DataFrame
    df = pd.DataFrame([input_data])

    # 🔧 Normalizar tipos
    # Convertir a los tipos EXACTOS que espera el modelo
    df["winery"] = df["winery"].astype(str)
    df["wine"] = df["wine"].astype(str)
    df["year"] = df["year"].astype(str)            # <-- MUY IMPORTANTE
    df["num_reviews"] = df["num_reviews"].astype(int)

    df["country"] = df["country"].astype(str)
    df["region"] = df["region"].astype(str)

    df["price"] = df["price"].astype(float)
    df["type"] = df["type"].astype(str)

    df["body"] = df["body"].astype(float)
    df["acidity"] = df["acidity"].astype(float)
    
    # Aplicar preprocesamiento sklearn
    X_processed = preprocess.transform(df)

    # Predecir con el modelo Keras
    prediction = model.predict(X_processed)

    # Devolver resultado en formato escalar
    return float(prediction[0][0])


# -----------------------------------------------------------
# Interfaz Streamlit
# -----------------------------------------------------------
def main():
    st.title("🍷 Predictor de Rating de Vinos")
    st.write("Introduce los datos del vino y el modelo estimará su puntuación.")

    # Entradas del usuario
    bodega = st.text_input("Bodega")
    vino = st.text_input("Vino")
    anyo = st.number_input("Año", min_value=1900, max_value=2025, value=2020)
    num_resenas = st.number_input("Número de reseñas", min_value=0, value=10)
    do = st.text_input("D.O.")
    pais = st.text_input("País")
    region = st.text_input("Región")
    precio = st.number_input("Precio (€)", min_value=0.0, step=0.1)
    cuerpo = st.slider("Cuerpo (1–5)", 1, 5, 3)
    acidez = st.slider("Acidez (1–5)", 1, 5, 3)

    # Botón de predicción
    if st.button("Predecir rating"):
        try:
            preprocess, model = load_predictor()

            # Diccionario de datos de entrada
            input_data = {
                "winery": bodega,
                "wine": vino,
                "year": anyo,
                "num_reviews": num_resenas,
                "country": pais,
                "region": region,
                "price": precio,
                "type": do,
                "body": cuerpo,
                "acidity": acidez
            }

            resultado = predict_rating(preprocess, model, input_data)

            st.success(f"⭐ Rating estimado: **{resultado:.2f}**")

        except FileNotFoundError as e:
            st.error(f"❌ Falta un archivo necesario: {e.filename}")
        except Exception as e:
            st.error(f"⚠️ Error al realizar la predicción: {e}")


if __name__ == "__main__":
    main()
