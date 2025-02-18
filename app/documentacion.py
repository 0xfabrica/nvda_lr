# app/documentacion.py
import streamlit as st

def mostrar_documentacion():
    st.title("Documentación del Proyecto")

    st.header("Introducción")
    st.write("""
    ¡Hola! Soy un Data Science Junior apasionado por el análisis de datos y el desarrollo de modelos predictivos.
    Este proyecto es una aplicación de Machine Learning que utiliza un modelo de regresión lineal para predecir el
    precio de cierre de las acciones de NVIDIA Corporation (NVDA) basado en datos históricos.
    """)

    st.header("Descripción del Proyecto")
    st.write("""
    La regresión lineal es una técnica estadística que modela la relación entre una variable dependiente y una o más
    variables independientes. En este caso, el objetivo es predecir el **precio de cierre** de las acciones de NVDA
    utilizando las siguientes variables:
    - **Open**: Precio de apertura
    - **High**: Precio máximo durante la sesión
    - **Low**: Precio mínimo durante la sesión
    - **Volume**: Volumen de acciones negociadas

    El modelo ha sido entrenado con datos históricos y ha alcanzado una precisión de 0.9999, lo que indica una excelente
    capacidad predictiva.
    """)

    st.header("Uso de la Aplicación")
    st.write("""
    Para utilizar la aplicación, navega a la sección de predicción en el menú principal. Ingresa los valores correspondientes
    a las variables mencionadas anteriormente y haz clic en el botón de predicción. La aplicación enviará estos datos a la API,
    que procesará la información y devolverá el precio de cierre estimado.

    Esta herramienta es útil para analistas financieros y traders que buscan estimar el comportamiento del precio de las acciones
    de NVIDIA en función de datos intradía.
    """)
