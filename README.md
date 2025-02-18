# Proyecto de Predicción de Precio de Cierre de NVDA

Este proyecto es una aplicación de Machine Learning que utiliza un modelo de regresión lineal para predecir el precio de cierre de las acciones de NVIDIA Corporation (NVDA) basándose en datos históricos. La solución se compone de dos partes principales:

- **API de Predicción (FastAPI):** Un servicio backend que expone un endpoint para recibir datos de entrada y devolver la predicción.
- **Frontend (Streamlit):** Una interfaz web interactiva que consume la API y permite al usuario ingresar datos y visualizar el resultado.

La aplicación ha alcanzado una precisión de **0.9999** en el modelo, lo que demuestra una excelente capacidad predictiva.

---

## Tabla de Contenidos

- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación y Configuración](#instalación-y-configuración)
- [Uso](#uso)
- [Despliegue](#despliegue)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Características

- **Modelo de Machine Learning:** Utiliza regresión lineal para predecir el precio de cierre de NVDA.
- **API con FastAPI:** Servicio REST que recibe datos y devuelve la predicción.
- **Frontend con Streamlit:** Interfaz de usuario amigable para interactuar con la API.
- **Alta Precisión:** El modelo entrenado alcanza una precisión de 0.9999.

---

## Estructura del Proyecto

```
tu_proyecto/
├── api/
│   ├── main.py                # Punto de entrada de la API con FastAPI
│   └── __pycache__/
├── app/
│   ├── main.py                # Archivo principal de la aplicación Streamlit
│   ├── documentacion.py       # Sección de documentación del proyecto
│   └── __pycache__/
├── modelo/
│   └── modelo_entrenado.pkl   # Modelo de Machine Learning entrenado y serializado
└── venv/                      # Entorno virtual de Python
```

---

## Tecnologías Utilizadas

- **Python 3.x**
- **FastAPI:** Framework para construir APIs de alto rendimiento.
- **Streamlit:** Framework para crear aplicaciones web interactivas.
- **scikit-learn:** Librería para Machine Learning (entrenamiento del modelo de regresión lineal).
- **Pandas:** Manejo y procesamiento de datos.
- **Pickle:** Serialización y carga del modelo entrenado.

---

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

> **Nota:** Asegúrate de tener un archivo `requirements.txt` que incluya las dependencias como `fastapi`, `uvicorn`, `streamlit`, `pandas`, `scikit-learn`, etc.

---

## Uso

### API (FastAPI)

1. Navega al directorio `api`:
    ```bash
    cd api
    ```
2. Ejecuta la API:
    ```bash
    uvicorn main:app --reload
    ```
3. La API estará disponible en `http://localhost:8000`. El endpoint para la predicción es `POST /predict`.

### Frontend (Streamlit)

1. Navega al directorio `app`:
    ```bash
    cd app
    ```
2. Ejecuta la aplicación de Streamlit:
    ```bash
    streamlit run main.py
    ```
3. Utiliza el menú lateral para navegar entre la sección de predicción y la documentación del proyecto.

---

## Despliegue

- **API:** Se recomienda desplegar la API en un servicio de hosting (por ejemplo, Heroku, AWS, Azure, etc.) para que tenga una URL pública accesible.
- **Frontend:** Puedes desplegar la aplicación de Streamlit en [share.streamlit.io](https://share.streamlit.io/). Recuerda actualizar la variable `API_URL` en el código de Streamlit para que apunte a la URL pública de tu API.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto o agregar nuevas funcionalidades, por favor abre un _pull request_ o una _issue_ en el repositorio.

---

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

*Este proyecto fue desarrollado por un Data Science Junior, demostrando la aplicación práctica de técnicas de Machine Learning y el desarrollo de APIs y frontends modernos.*
```

Este README.md ofrece una visión completa del proyecto, abarcando desde la descripción general hasta instrucciones de instalación, uso, despliegue y contribuciones. Puedes ajustarlo según tus necesidades y agregar información adicional si lo consideras necesario.
