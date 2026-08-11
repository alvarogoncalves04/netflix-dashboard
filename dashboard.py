# dashboard.py
import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from src.config import DB_PATH

# Configurar página
st.set_page_config(
    page_title="Dashboard Netflix",
    page_icon="🎬",
    layout="wide"
)

# Título
st.title("🎬 Dashboard de Netflix")
st.markdown("---")

# Conectar a SQL
@st.cache_data
def cargar_datos():
    conn = sqlite3.connect(DB_PATH)
    
    query1 = "SELECT type, COUNT(*) as total FROM netflix GROUP BY type"
    query2 = "SELECT release_year, COUNT(*) as total FROM netflix GROUP BY release_year ORDER BY total DESC LIMIT 10"
    query3 = "SELECT country, COUNT(*) as total FROM netflix WHERE country != 'No especificado' GROUP BY country ORDER BY total DESC LIMIT 5"
    query4 = "SELECT rating, COUNT(*) as total FROM netflix GROUP BY rating ORDER BY total DESC LIMIT 5"
    query5 = "SELECT release_year, COUNT(*) as total FROM netflix WHERE release_year >= 2013 GROUP BY release_year ORDER BY release_year DESC"
    
    df1 = pd.read_sql_query(query1, conn)
    df2 = pd.read_sql_query(query2, conn)
    df3 = pd.read_sql_query(query3, conn)
    df4 = pd.read_sql_query(query4, conn)
    df5 = pd.read_sql_query(query5, conn)
    
    conn.close()
    
    return df1, df2, df3, df4, df5

# Cargar datos
df1, df2, df3, df4, df5 = cargar_datos()

# FILA 1: Métricas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Títulos", len(df1))
with col2:
    peliculas = df1[df1['type'] == 'Movie']['total'].values[0]
    st.metric("Películas", peliculas)
with col3:
    series = df1[df1['type'] == 'TV Show']['total'].values[0]
    st.metric("Series", series)
with col4:
    total_paises = len(df3)
    st.metric("Países Productores", total_paises)

st.markdown("---")

# FILA 2: Gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Películas vs Series")
    fig, ax = plt.subplots()
    ax.bar(df1['type'], df1['total'], color=['#3498db', '#e74c3c'])
    ax.set_ylabel("Cantidad")
    st.pyplot(fig)
    plt.close()

with col2:
    st.subheader("🏆 Top 5 Ratings")
    fig, ax = plt.subplots()
    ax.bar(df4['rating'], df4['total'], color='#9b59b6')
    ax.set_ylabel("Cantidad")
    st.pyplot(fig)
    plt.close()

# FILA 3: Gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌍 Top 5 Países")
    fig, ax = plt.subplots()
    ax.barh(df3['country'], df3['total'], color='#f39c12')
    ax.set_xlabel("Cantidad")
    st.pyplot(fig)
    plt.close()

with col2:
    st.subheader("📈 Top 10 Años con Más Contenido")
    df2_sorted = df2.sort_values('release_year')
    fig, ax = plt.subplots()
    ax.bar(df2_sorted['release_year'], df2_sorted['total'], color='#2ecc71')
    ax.set_xlabel("Año")
    ax.set_ylabel("Cantidad")
    plt.xticks(rotation=45)
    st.pyplot(fig)
    plt.close()

# FILA 4: Evolución
st.subheader("📈 Evolución de Contenido (2013-2023)")
df5_sorted = df5.sort_values('release_year')
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(df5_sorted['release_year'], df5_sorted['total'], marker='o', color='#e67e22', linewidth=2)
ax.set_xlabel("Año")
ax.set_ylabel("Cantidad")
st.pyplot(fig)
plt.close()

st.markdown("---")
st.caption("Dashboard creado con Streamlit | Datos de Netflix")