# graficos.py
# Este archivo crea gráficos con los datos de Netflix

import matplotlib.pyplot as plt
import pandas as pd

def configurar_estilo():
    """Configura el estilo de los gráficos"""
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 10

def grafico_barras(df, x, y, titulo, xlabel, ylabel, color='skyblue'):
    """
    Crea un gráfico de barras
    Args:
        df: DataFrame con los datos
        x: nombre de la columna para eje X
        y: nombre de la columna para eje Y
        titulo: título del gráfico
        xlabel: etiqueta eje X
        ylabel: etiqueta eje Y
        color: color de las barras
    """
    fig, ax = plt.subplots()
    
    # Crear barras
    ax.bar(df[x], df[y], color=color)
    
    # Personalizar
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    # Rotar etiquetas si son muchas
    if len(df) > 5:
        plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    return fig

def grafico_linea(df, x, y, titulo, xlabel, ylabel, color='green'):
    """
    Crea un gráfico de línea
    Args: mismos parámetros que grafico_barras
    """
    fig, ax = plt.subplots()
    
    # Crear línea
    ax.plot(df[x], df[y], marker='o', color=color, linewidth=2)
    
    # Personalizar
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig

def crear_todos_los_graficos(resultados):
    """
    Crea todos los gráficos del dashboard
    Args: resultados = diccionario con DataFrames de las consultas
    """
    configurar_estilo()
    
    print("\n" + "="*50)
    print("📊 CREANDO GRÁFICOS")
    print("="*50)
    
    # 1. Películas vs Series (barras)
    print("1. Creando: Películas vs Series...")
    fig1 = grafico_barras(
        resultados['movies_vs_series'],
        'type', 'total',
        'Películas vs Series en Netflix',
        'Tipo', 'Cantidad',
        color=['#3498db', '#e74c3c']
    )
    
    # 2. Top 10 años (barras horizontales)
    print("2. Creando: Top 10 años...")
    df_years = resultados['top_years'].sort_values('release_year')
    fig2 = grafico_barras(
        df_years,
        'release_year', 'total',
        'Top 10 Años con Más Contenido',
        'Año', 'Cantidad',
        color='#2ecc71'
    )
    
    # 3. Top 5 países (barras)
    print("3. Creando: Top 5 países...")
    fig3 = grafico_barras(
        resultados['top_countries'],
        'country', 'total',
        'Top 5 Países Productores de Contenido',
        'País', 'Cantidad',
        color='#f39c12'
    )
    
    # 4. Top 5 ratings (barras)
    print("4. Creando: Top 5 ratings...")
    fig4 = grafico_barras(
        resultados['top_ratings'],
        'rating', 'total',
        'Top 5 Ratings Más Comunes',
        'Rating', 'Cantidad',
        color='#9b59b6'
    )
    
    # 5. Evolución por año (línea)
    print("5. Creando: Evolución por año...")
    df_year_evo = resultados['content_by_year'].sort_values('release_year')
    fig5 = grafico_linea(
        df_year_evo,
        'release_year', 'total',
        'Evolución de Contenido en Netflix (2013-2023)',
        'Año', 'Cantidad',
        color='#e67e22'
    )
    
    print("\n✅ Gráficos creados")
    
    return [fig1, fig2, fig3, fig4, fig5]

def guardar_dashboard(figures, nombre_archivo='dashboard.png'):
    """
    Guarda todos los gráficos en un solo archivo
    Args:
        figures: lista de figuras
        nombre_archivo: nombre del archivo a guardar
    """
    from src.config import OUTPUT_DIR
    import os
    
    ruta_completa = os.path.join(OUTPUT_DIR, nombre_archivo)
    
    print(f"\n💾 Guardando dashboard en: {ruta_completa}")
    
    # Crear una figura grande con subplots
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    axes = axes.flatten()
    
    # Copiar cada gráfico a un subplot
    for i, ax in enumerate(axes):
        if i < len(figures):
            # Copiar el contenido de cada figura
            for child in figures[i].get_children():
                if hasattr(child, 'get_children'):
                    for subchild in child.get_children():
                        ax.add_artist(subchild)
        else:
            ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(ruta_completa, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    print(f"✅ Dashboard guardado: {ruta_completa}")
    