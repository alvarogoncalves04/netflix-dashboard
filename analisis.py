import pandas as pd
import sqlite3

# ============================================
# 1. CARGAR DATOS
# ============================================
print("Cargando datos...")
df = pd.read_csv('netflix_titles.csv')
print(f"✅ Datos cargados: {len(df)} filas")

# ============================================
# 2. LIMPIEZA DE DATOS
# ============================================
print("\n=== LIMPIEZA DE DATOS ===")

# 2.1 Ver nulos iniciales
print("\nValores nulos iniciales:")
print(df.isnull().sum())

# 2.2 Eliminar rating vacío
df = df.dropna(subset=['rating'])
print(f"\n✅ Eliminados {4} registros sin rating")

# 2.3 Rellenar valores vacíos
df['director'] = df['director'].fillna('Desconocido')
df['country'] = df['country'].fillna('No especificado')

# 2.4 Corregir ratings malos
ratings_malos = ['74 min', '84 min', '66 min', 'UR']
df['rating'] = df['rating'].replace({
    '74 min': 'NR',
    '84 min': 'NR',
    '66 min': 'NR',
    'UR': 'NR'
})

# 2.5 Verificar limpieza
print("\nValores nulos después de limpiar:")
print(df[['director', 'country', 'rating']].isnull().sum())

print(f"\n✅ Limpieza completada: {len(df)} filas")

# ============================================
# 3. GUARDAR CSV LIMPIO
# ============================================
df.to_csv('netflix_limpio.csv', index=False)
print("\n✅ Archivo guardado: netflix_limpio.csv")