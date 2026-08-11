# config.py
# Este archivo guarda las ubicaciones de nuestros archivos

import os

# ¿Dónde está la carpeta principal?
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ¿Dónde están los datos?
DATA_DIR = os.path.join(BASE_DIR, 'data')

# ¿Dónde guardaremos los resultados?
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')

# Nombre de los archivos
RAW_DATA = os.path.join(DATA_DIR, 'netflix_titles.csv')
CLEAN_DATA = os.path.join(DATA_DIR, 'netflix_limpio.csv')
DB_PATH = os.path.join(OUTPUT_DIR, 'netflix.db')

# Crear carpetas si no existen
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
# src/config.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')

RAW_DATA = os.path.join(DATA_DIR, 'netflix_titles.csv')
CLEAN_DATA = os.path.join(DATA_DIR, 'netflix_limpio.csv')
DB_PATH = os.path.join(OUTPUT_DIR, 'netflix.db')

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)