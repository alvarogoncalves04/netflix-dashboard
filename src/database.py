# database.py
# Este archivo maneja la conexión con SQLite

import sqlite3
import pandas as pd
from src.config import DB_PATH

def save_to_database(df):
    """
    Guarda un DataFrame en SQLite
    Args: df = DataFrame a guardar
    """
    print("🗄️ Guardando datos en SQLite...")
    
    # Conectar a la base de datos (se crea si no existe)
    conn = sqlite3.connect(DB_PATH)
    
    # Guardar el DataFrame como tabla 'netflix'
    df.to_sql('netflix', conn, if_exists='replace', index=False)
    
    # Cerrar conexión
    conn.close()
    
    print(f"✅ Datos guardados en: {DB_PATH}")

def test_connection():
    """
    Prueba que la base de datos funciona
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Ver cuántas tablas hay
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()
    
    print(f"📊 Tablas en la base de datos: {tablas}")
    
    # Ver cuántos registros tiene la tabla netflix
    cursor.execute("SELECT COUNT(*) FROM netflix;")
    total = cursor.fetchone()[0]
    print(f"📊 Registros en 'netflix': {total}")
    
    conn.close()