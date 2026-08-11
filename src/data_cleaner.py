# data_cleaner.py
# Este archivo limpia los datos de Netflix

import pandas as pd

def clean_data(df):
    """
    Limpia el dataset de Netflix:
    1. Elimina películas sin rating
    2. Rellena directores vacíos con "Desconocido"
    3. Rellena países vacíos con "No especificado"
    4. Corrige ratings mal escritos
    
    Args: df = DataFrame original
    Returns: df = DataFrame limpio
    """
    
    print("🧹 Iniciando limpieza...")
    print(f"Antes: {len(df)} filas")
    
    # 1. ELIMINAR RATING VACÍO
    # ¿Por qué? El rating es importante para el análisis
    # Solo hay 4, podemos eliminarlos
    df = df.dropna(subset=['rating'])
    print(f"✅ Eliminados registros sin rating")
    
    # 2. RELLENAR DIRECTOR VACÍO
    # ¿Por qué? Son 2634, no queremos perder tantos datos
    # Ponemos "Desconocido" para que no estén vacíos
    df['director'] = df['director'].fillna('Desconocido')
    print(f"✅ Rellenados directores vacíos con 'Desconocido'")
    
    # 3. RELLENAR PAÍS VACÍO
    # ¿Por qué? Son 831, no queremos perderlos
    df['country'] = df['country'].fillna('No especificado')
    print(f"✅ Rellenados países vacíos con 'No especificado'")
    
    # 4. CORREGIR RATINGS MALOS
    # ¿Qué pasó? Algunos ratings son duraciones (ej: '74 min')
    # Los cambiamos a 'NR' (No Rated)
    ratings_malos = {
        '74 min': 'NR',
        '84 min': 'NR',
        '66 min': 'NR',
        'UR': 'NR'
    }
    df['rating'] = df['rating'].replace(ratings_malos)
    print(f"✅ Corregidos ratings malos")
    
    print(f"Después: {len(df)} filas")
    print("✅ Limpieza completada")
    
    return df

def mostrar_info(df):
    """
    Muestra información de los datos limpios
    Args: df = DataFrame limpio
    """
    print("\n" + "="*50)
    print("INFORMACIÓN DE DATOS LIMPIOS")
    print("="*50)
    print(f"Total de películas/series: {len(df)}")
    print(f"Columnas: {df.columns.tolist()}")
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    print("="*50)