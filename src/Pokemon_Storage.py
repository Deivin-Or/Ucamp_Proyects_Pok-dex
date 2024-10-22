import json
import os

# Función para guardar los datos del Pokémon en un archivo JSON
def save_pokemon_to_json(pokemon_name, pokemon_data):
    """
    Guarda los datos del Pokémon en un archivo JSON dentro de una carpeta llamada 'Pokemon_Container_Box'.
    
    Parámetros:
    - pokemon_name (str): Nombre del Pokémon.
    - pokemon_data (dict): Datos del Pokémon obtenidos de la PokeAPI.
    """
    # Definir la carpeta donde se guardarán los archivos
    pokedex_folder = 'Pokemon_Container_Box'
    
    # Si la carpeta 'Pokemon_Container_Box' no existe, crearla
    if not os.path.exists(pokedex_folder):
        os.makedirs(pokedex_folder)  # Crear la carpeta
    
    # Definir la ruta del archivo donde se guardarán los datos
    file_path = os.path.join(pokedex_folder, f"{pokemon_name}.json")
    
    # Abrir el archivo JSON en modo escritura y guardar los datos
    with open(file_path, 'w') as json_file:
        json.dump(pokemon_data, json_file, indent=4)  # Guardar los datos con indentación para mejor lectura
