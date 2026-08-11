# data_loader.py
# Este archivo carga y guarda los datos

import pandas as pd
from src.config import RAW_DATA, CLEAN_DATA

def load_raw_data():
    """
    Carga el archivo CSV original de Netflix
    Returns: Un DataFrame (tabla) con todos los datos
    """
    print("📂 Cargando datos desde:", RAW_DATA)
    df = pd.read_csv(RAW_DATA)
    print(f"✅ Datos cargados: {len(df)} filas y {len(df.columns)} columnas")
    return df

def save_clean_data(df):
    """
    Guarda los datos ya limpios en un nuevo CSV
    Args: df = DataFrame limpio
    """
    df.to_csv(CLEAN_DATA, index=False)
    print(f"✅ Datos limpios guardados en: {CLEAN_DATA}")