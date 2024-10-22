# Archivo principal que inicia el proyecto de la Pokédex

from API_Interaction import get_pokemon_data  # Importa la función para obtener los datos del Pokémon
from grafic_interfaz import PokedexApp  # Importa la clase de la interfaz gráfica
from Pokemon_Storage import save_pokemon_to_json  # Importa la función para guardar los datos del Pokémon en un archivo JSON

def main():
    # Ejecutar la aplicación gráfica de la Pokédex
    PokedexApp().run()

if __name__ == "__main__":
    main()  # Iniciar el programa principal
