import requests
import cv2
import urllib
import numpy as np


url = "https://pokeapi.co/api/v2/pokemon?limit=10"

response = requests.get(url)

for index, pokemon in enumerate(response.json()["results"]):
    pokemon_name = pokemon["name"]
    response2 = requests.get(pokemon["url"])    
    pokemonDetail = response2.json()["sprites"]["other"]["official-artwork"]["front_default"]
    req = urllib.request.urlopen(pokemonDetail)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1) # 'Load it as it is'
    cv2.imshow(f'Pokemon - {pokemon_name}',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(pokemonDetail)
    print(f"#{index + 1} {pokemon_name}")

