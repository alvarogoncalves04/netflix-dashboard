# queries.py
import pandas as pd
# Diccionario con todas las consultas
QUERIES = {
    'movies_vs_series': """
        SELECT type, COUNT(*) as total
        FROM netflix
        GROUP BY type
    """,
    'top_years': """
        SELECT release_year, COUNT(*) as total
        FROM netflix
        GROUP BY release_year
        ORDER BY total DESC
        LIMIT 10
    """,
    'top_countries': """
        SELECT country, COUNT(*) as total
        FROM netflix
        WHERE country != 'No especificado'
        GROUP BY country
        ORDER BY total DESC
        LIMIT 5
    """,
    'top_ratings': """
        SELECT rating, COUNT(*) as total
        FROM netflix
        GROUP BY rating
        ORDER BY total DESC
        LIMIT 5
    """,
    'content_by_year': """
        SELECT release_year, COUNT(*) as total
        FROM netflix
        WHERE release_year >= 2013
        GROUP BY release_year
        ORDER BY release_year DESC
    """
}

def ejecutar_consulta(conn, query, nombre):
    print(f"\n📊 {nombre}")
    print("-"*40)
    resultado = pd.read_sql_query(query, conn)
    print(resultado)
    return resultado

def todas_las_consultas(conn):
    print("\n" + "="*50)
    print("🔍 CONSULTAS SQL")
    print("="*50)
    
    query1 = """
        SELECT type, COUNT(*) as total
        FROM netflix
        GROUP BY type
    """
    ejecutar_consulta(conn, query1, "1. PELÍCULAS VS SERIES")
    
    query2 = """
        SELECT release_year, COUNT(*) as total
        FROM netflix
        GROUP BY release_year
        ORDER BY total DESC
        LIMIT 10
    """
    ejecutar_consulta(conn, query2, "2. TOP 10 AÑOS CON MÁS CONTENIDO")
    
    query3 = """
        SELECT country, COUNT(*) as total
        FROM netflix
        WHERE country != 'No especificado'
        GROUP BY country
        ORDER BY total DESC
        LIMIT 5
    """
    ejecutar_consulta(conn, query3, "3. TOP 5 PAÍSES PRODUCTORES")
    
    query4 = """
        SELECT rating, COUNT(*) as total
        FROM netflix
        GROUP BY rating
        ORDER BY total DESC
        LIMIT 5
    """
    ejecutar_consulta(conn, query4, "4. TOP 5 RATINGS MÁS COMUNES")
    
    query5 = """
        SELECT release_year, COUNT(*) as total
        FROM netflix
        WHERE release_year >= 2013
        GROUP BY release_year
        ORDER BY release_year DESC
    """
    ejecutar_consulta(conn, query5, "5. CONTENIDO POR AÑO (2013-2023)")