import requests

def obtener_paises():
    url = "https://restcountries.com/v3.1/region/europe"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        # Extraemos solo el nombre común y la url de google maps
        paises = []
        for p in respuesta.json():
            paises.append({
                "nombre": p['name']['common'].lower(),
                "googleMaps": p['maps']['googleMaps']
            })
        # IMPORTANTE: Ordenar para la búsqueda binaria
        return sorted(paises, key=lambda x: x['nombre'])
    except Exception as e:
        print(f"Error al conectar con la API: {e}")
        return []

def busqueda_lineal(lista, objetivo):
    for pais in lista:
        if pais['nombre'] == objetivo:
            return pais
    return None

def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio]['nombre'] == objetivo:
            return lista[medio]
        elif lista[medio]['nombre'] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return None

def menu():
    print("--- Buscador de Países Europeos ---")
    datos = obtener_paises()
    
    if not datos:
        return

    nombre_buscar = input("Introduce el nombre del país (en inglés, ej: Sweden): ").strip().lower()
    print("\nSelecciona el tipo de búsqueda:")
    print("1. Lineal")
    print("2. Binaria")
    opcion = input("Opción: ")

    resultado = None
    if opcion == "1":
        resultado = busqueda_lineal(datos, nombre_buscar)
    elif opcion == "2":
        resultado = busqueda_binaria(datos, nombre_buscar)
    else:
        print("Opción no válida.")
        return

    if resultado:
        print(f"\nNombre: {resultado['nombre'].capitalize()}")
        print(f"URL: {resultado['googleMaps']}")
    else:
        print("\nPaís no encontrado.")

if __name__ == "__main__":
    menu()