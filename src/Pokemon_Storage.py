import json
import os

# Función para guardar los datos del Pokémon en un archivo JSON
def save_pokemon_to_json(pokemon_name, pokemon_data):
    # Verificar si la carpeta 'pokedex' existe, si no, se crea
    pokedex_folder = 'Pokemon_Container_Box'
    if not os.path.exists(pokedex_folder):
        os.makedirs(pokedex_folder)  # Crear la carpeta si no existe

    # Guardar los datos del Pokémon en un archivo JSON dentro de la carpeta 'pokedex'
    file_path = os.path.join(pokedex_folder, f"{pokemon_name}.json")
    
    # Abrir el archivo JSON para escribir los datos del Pokémon
    with open(file_path, 'w') as json_file:
        json.dump(pokemon_data, json_file, indent=4)  # Guardar los datos con formato JSON legible
