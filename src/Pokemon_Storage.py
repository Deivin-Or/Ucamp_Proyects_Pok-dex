import json
import os

# Función para guardar los datos del Pokémon en un archivo JSON
def save_pokemon_to_json(pokemon_name, pokemon_data):
    # Crear la carpeta 'pokedex' si no existe
    pokedex_folder = 'Pokemon_Container_Box'
    if not os.path.exists(pokedex_folder):
        os.makedirs(pokedex_folder)  # Crear la carpeta si no existe
    
    # Ruta del archivo .json con el nombre del Pokémon
    file_path = os.path.join(pokedex_folder, f"{pokemon_name}.json")
    
    # Guardar los datos del Pokémon en formato JSON
    with open(file_path, 'w') as json_file:
        json.dump(pokemon_data, json_file, indent=4)  # Guardar con indentación para mejor lectura
