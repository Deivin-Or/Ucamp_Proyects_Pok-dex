import requests

# Función para obtener los datos del Pokémon desde la PokeAPI
def get_pokemon_data(pokemon_name):
    # URL para obtener los datos del Pokémon usando su nombre
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    # Realizar la solicitud GET a la PokeAPI
    response = requests.get(url)
    
    # Si la solicitud es exitosa (código 200), devolver los datos como JSON
    if response.status_code == 200:
        return response.json()  # Retornar los datos en formato JSON
    else:
        return None  # Si no se encuentra el Pokémon, devolver None
