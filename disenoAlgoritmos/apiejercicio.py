import requests

def obtener_datos_completos():
    """Obtiene los datos completos de los países de la API y los retorna."""
    url = "https://restcountries.com/v3.1/region/europe"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos de la API: {e}")
        return None

def busqueda_binaria_url(lista_datos_completos, pais_a_buscar):
    """
    Busca un país usando búsqueda binaria y retorna la URL de su mapa de Google.
    
    Args:
        lista_datos_completos (list): La lista de diccionarios con todos los datos de los países.
        pais_a_buscar (str): El nombre del país que se desea buscar.
    
    Returns:
        str: La URL de Google Maps del país, o None si no se encuentra.
    """
    # 1. Crear la lista de nombres de países usando un bucle for.
    nombres_paises = []
    for pais in lista_datos_completos:
        nombres_paises.append(pais['name']['common'])
        
    # 2. Ordenar la lista para la búsqueda binaria.
    nombres_paises.sort()
    
    # 3. Implementar la búsqueda binaria en la lista de nombres.
    izquierda = 0
    derecha = len(nombres_paises) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = nombres_paises[medio]
        
        if valor_medio == pais_a_buscar:
            # 4. Si se encuentra el nombre, buscar su diccionario completo en la lista original.
            for pais in lista_datos_completos:
                if pais['name']['common'] == pais_a_buscar:
                    # 5. Retornar la URL.
                    return pais['maps']['googleMaps']
        elif valor_medio < pais_a_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    # Si el bucle termina, el país no fue encontrado.
    return None

# --- Ejecución del código ---
lista_paises_europa = obtener_datos_completos()

if lista_paises_europa:
    pais_a_buscar = "Spain"
    url_mapa = busqueda_binaria_url(lista_paises_europa, pais_a_buscar)

    if url_mapa:
        print(f"La URL de Google Maps para '{pais_a_buscar}' es:\n{url_mapa}")
    else:
        print(f"El país '{pais_a_buscar}' no se encontró o no tiene una URL de mapa.")