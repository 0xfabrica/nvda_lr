from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

MODEL_PATH = (r"C:\Users\HP\Desktop\api_nvda_ml\modelo\nvda_model.pkl")

with open(r'C:\Users\HP\Desktop\api_nvda_ml\modelo\nvda_model.pkl', 'rb') as file:
    modelo = pickle.load(file)


app = FastAPI()

# Definir el esquema de datos de entrada
class DatosEntrada(BaseModel):
    Open: float
    High: float
    Low: float
    Close: float
    Volume: int
    


@app.post("/predict")
def predict(datos: DatosEntrada):
    # Convertir los datos de entrada a un DataFrame (manteniendo el mismo preprocesamiento que en entrenamiento)
    data = pd.DataFrame([datos.dict()])
    # Realizar la predicción con el modelo de regresión lineal
    prediccion = modelo.predict(data)
    return {"prediccion": prediccion[0]}


# Para ejecutar localmente: 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)