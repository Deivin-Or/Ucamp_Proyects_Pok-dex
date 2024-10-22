# Archivo principal que inicia el proyecto de la Pokédex

from API_Interaction import get_pokemon_data  # Importar la función para obtener datos del Pokémon
from grafic_interfaz import PokedexApp  # Importar la clase de la interfaz gráfica
from Pokemon_Storage import save_pokemon_to_json  # Importar la función para guardar los datos del Pokémon en un archivo JSON

# Función principal que ejecuta la Pokédex
def main():
    """
    Función principal que ejecuta la interfaz gráfica de la Pokédex.
    Se encarga de gestionar el flujo de la aplicación.
    """
    # Ejecutar la aplicación gráfica de la Pokédex
    PokedexApp().run()

# Iniciar el programa principal
if __name__ == "__main__":
    main()  # Ejecutar la función principal
