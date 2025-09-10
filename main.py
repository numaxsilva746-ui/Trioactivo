from flask import Flask, jsonify
import pandas as pd
import random
import os

app = Flask(__name__)

# --- FUNCIONES DE PREDICCIÓN ---
def prediccion_trio():
    archivo = "data/trio.csv"
    if not os.path.exists(archivo):
        return ["No hay historial de Trío"]
    df = pd.read_csv(archivo)
    numeros = df["Numero"].astype(str).tolist()
    frecuentes = pd.Series(numeros).value_counts().head(10).index.tolist()
    return random.sample(frecuentes, min(4, len(frecuentes)))

def prediccion_loto():
    # Loto Activo: 0–36 y 00
    universo = [str(i).zfill(2) for i in range(1, 37)] + ["00"]
    return random.sample(universo, 5)

def prediccion_guacharo():
    # Guácharo Activo: 0–75 y 00
    universo = [str(i).zfill(2) for i in range(1, 76)] + ["00"]
    return random.sample(universo, 5)

# --- ENDPOINTS ---
@app.route("/")
def home():
    return "✅ Motor de Loterías Activo: Trio, Loto y Guacharo"

@app.route("/predict/trio")
def predict_trio():
    return jsonify({"loteria": "Trio Activo", "prediccion": prediccion_trio()})

@app.route("/predict/loto")
def predict_loto():
    return jsonify({"loteria": "Loto Activo", "prediccion": prediccion_loto()})

@app.route("/predict/guacharo")
def predict_guacharo():
    return jsonify({"loteria": "Guacharo Activo", "prediccion": prediccion_guacharo()})

# --- EJECUCIÓN LOCAL ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
