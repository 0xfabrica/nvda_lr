# app/app.py
import streamlit as st
from documentacion import mostrar_documentacion
import requests

st.set_page_config(
    page_title="Aplicación de Predicción de NVDA",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

# Menú de navegación
opcion = st.selectbox("Selecciona una sección", ["Inicio", "Predicción", "Documentación"])

if opcion == "Inicio":
    st.title("Bienvenido a la Aplicación de Predicción de NVDA")
    st.write("Utiliza el menú desplegable para navegar entre las diferentes secciones de la aplicación.")
elif opcion == "Predicción":
    st.title("Predicción del Precio de Cierre de NVDA")
    # Aquí puedes incluir el código o importar la función correspondiente a la sección de predicción
    # from prediccion import mostrar_prediccion
    # mostrar_prediccion()
elif opcion == "Documentación":
    mostrar_documentacion()




# URL de la API
API_URL = # La dirección de tu api desplegada

# Título de la aplicación
st.title("Predicción del Precio de Cierre de NVDA")

# Descripción
st.write("""
Esta aplicación predice el **Precio de Cierre** de las acciones de NVIDIA Corporation (NVDA) basado en los siguientes parámetros:
- **Open**: Precio de apertura
- **High**: Precio máximo durante la sesión
- **Low**: Precio mínimo durante la sesión
- **Volume**: Volumen de acciones negociadas
""")

# Formularios de entrada
open_price = st.number_input("Precio de Apertura (Open):", min_value=0.0, format="%.2f")
high_price = st.number_input("Precio Máximo (High):", min_value=0.0, format="%.2f")
low_price = st.number_input("Precio Mínimo (Low):", min_value=0.0, format="%.2f")
close_price = st.number_input("Precio de Cierre (Close):", min_value=0.0, format="%.2f")
volume = st.number_input("Volumenn del día (sin puntos):", min_value=0, format="%d")

# Botón de predicción
if st.button("Predecir"):
    # Crear el payload para la solicitud POST
    payload = {
        "Open": open_price,
        "High": high_price,
        "Low": low_price,
        "Close": close_price,
        "Volume": volume
    }
    # Realizar la solicitud POST a la API
    response = requests.post(API_URL, json=payload)
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        resultado = response.json()
        st.success(f"El precio de cierre predicho para el día siguiente es: ${resultado['prediccion']:.2f}")
    else:
        st.error("Error en la predicción. Por favor, intenta nuevamente.")
