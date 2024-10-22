# Archivo principal que inicia el proyecto de la Pokédex

# Archivo principal que ejecuta la Pokédex usando Tkinter

from API_Interaction import get_pokemon_data  # Importar función para obtener datos de la PokeAPI
from grafic_interfaz import show_pokemon_in_interface  # Importar función para mostrar la interfaz
from Pokemon_Storage import save_pokemon_to_json  # Importar función para guardar datos en JSON

def main():
    pokemon_name = input("Introduce el nombre del Pokémon: ")  # Solicitar nombre del Pokémon al usuario
    
    # Obtener los datos del Pokémon
    pokemon_data = get_pokemon_data(pokemon_name)
    
    if pokemon_data:
        # Mostrar la información en la interfaz gráfica usando Tkinter
        show_pokemon_in_interface(pokemon_data)
        
        # Guardar la información del Pokémon en un archivo .json
        save_pokemon_to_json(pokemon_name, pokemon_data)
        print(f"Información de {pokemon_name} guardada en 'pokedex/{pokemon_name}.json'.")
    else:
        print(f"El Pokémon '{pokemon_name}' no existe.")

if __name__ == "__main__":
    main()  # Ejecutar la función principal
