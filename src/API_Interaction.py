import requests

# Función para obtener los datos del Pokémon desde la PokeAPI
def get_pokemon_data(pokemon_name):
    """
    Envía una solicitud GET a la PokeAPI para obtener los datos de un Pokémon específico.

    Parámetros:
    - pokemon_name (str): Nombre del Pokémon a buscar.

    Retorno:
    - JSON con los datos del Pokémon si la solicitud es exitosa.
    - None si el Pokémon no se encuentra o si ocurre un error en la solicitud.
    """
    # URL para obtener los datos del Pokémon usando su nombre en minúsculas
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    try:
        # Realizar la solicitud GET a la PokeAPI
        response = requests.get(url)
        
        # Verificar el código de respuesta
        if response.status_code == 200:
            return response.json()  # Retornar los datos en formato JSON
        
        elif response.status_code == 404:
            # Si el Pokémon no se encuentra, retornar None y mostrar un mensaje
            print("Pokémon no encontrado.")
            return None
        
        else:
            # Manejar otros códigos de error
            print(f"Error en la solicitud: Código de estado {response.status_code}")
            return None
    
    except requests.exceptions.ConnectionError:
        # Manejar error de conexión
        print("Error: No se pudo conectar a la API de Pokémon. Verifique su conexión a internet.")
        return None
    
    except requests.exceptions.RequestException as error:
        # Manejar otros errores relacionados con la solicitud
        print(f"Error en la solicitud a la API: {error}")
        return None
