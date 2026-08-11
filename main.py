# main.py
import sys
import os
import sqlite3
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.config import RAW_DATA, CLEAN_DATA, DB_PATH, OUTPUT_DIR
from src.data_loader import load_raw_data, save_clean_data
from src.data_cleaner import clean_data, mostrar_info
from src.database import save_to_database, test_connection
from src.queries import QUERIES
from src.graficos import crear_todos_los_graficos, guardar_dashboard

def main():
    print("="*60)
    print("🎬 PROYECTO NETFLIX - ANÁLISIS DE DATOS")
    print("="*60)
    
    # PASO 1: Cargar datos
    print("\n📂 PASO 1: Cargar datos")
    print("-"*40)
    df = load_raw_data()
    
    # PASO 2: Limpiar datos
    print("\n🧹 PASO 2: Limpiar datos")
    print("-"*40)
    df_clean = clean_data(df)
    
    # PASO 3: Mostrar información
    mostrar_info(df_clean)
    
    # PASO 4: Guardar CSV limpio
    print("\n💾 PASO 4: Guardar datos limpios")
    print("-"*40)
    save_clean_data(df_clean)
    
    # PASO 5: Guardar en SQLite
    print("\n🗄️ PASO 5: Guardar en SQLite")
    print("-"*40)
    save_to_database(df_clean)
    
    # PASO 6: Probar conexión
    print("\n🔍 PASO 6: Probar conexión SQL")
    print("-"*40)
    test_connection()
    
    # PASO 7: Ejecutar consultas SQL
    print("\n🔍 PASO 7: Ejecutar consultas SQL")
    print("-"*40)
    
    conn = sqlite3.connect(DB_PATH)
    
    # Ejecutar todas las consultas
    resultados = {}
    for nombre, query in QUERIES.items():
        print(f"📊 Ejecutando: {nombre}")
        resultados[nombre] = pd.read_sql_query(query, conn)
    
    conn.close()
    
    # PASO 8: Crear gráficos
    print("\n📊 PASO 8: Crear gráficos")
    print("-"*40)
    figuras = crear_todos_los_graficos(resultados)
    
    # PASO 9: Guardar dashboard
    print("\n💾 PASO 9: Guardar dashboard")
    print("-"*40)
    guardar_dashboard(figuras)
    
    print("\n✅ ¡PROYECTO COMPLETADO!")
    print("Archivos generados:")
    print(f"  - {CLEAN_DATA}")
    print(f"  - {DB_PATH}")
    print(f"  - {os.path.join(OUTPUT_DIR, 'dashboard.png')}")

if __name__ == "__main__":
    main()