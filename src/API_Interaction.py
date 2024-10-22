# src/api.py
import requests

# Función para obtener los datos del Pokémon desde la PokeAPI
def get_pokemon_data(pokemon_name):
    # URL de la API con el nombre del Pokémon ingresado
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    # Realizar una solicitud GET a la API para obtener los datos del Pokémon
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        return response.json()  # Devolver los datos del Pokémon en formato JSON
    else:
        return None  # Retornar None si no se encuentra el Pokémon
