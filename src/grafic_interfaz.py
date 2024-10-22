import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Función para mostrar la información del Pokémon en una interfaz gráfica usando Tkinter
def show_pokemon_in_interface(pokemon_data):
    # Crear la ventana principal de Tkinter
    window = tk.Tk()
    window.title(f"{pokemon_data['name'].capitalize()} - Pokédex")
    
    # Cargar la imagen del Pokémon desde la URL
    image_url = pokemon_data['sprites']['front_default']
    response = requests.get(image_url)
    pokemon_image = Image.open(BytesIO(response.content))
    
    # Cambiar el uso de Image.ANTIALIAS por Image.LANCZOS
    pokemon_image = pokemon_image.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(pokemon_image)

    # Mostrar la imagen del Pokémon
    img_label = tk.Label(window, image=img)
    img_label.image = img  # Necesario para que la imagen no se elimine
    img_label.pack()

    # Mostrar las estadísticas del Pokémon
    name = pokemon_data['name'].capitalize()
    weight = pokemon_data['weight']
    height = pokemon_data['height']
    types = [tipo['type']['name'] for tipo in pokemon_data['types']]
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]

    info_text = f"Nombre: {name}\nPeso: {weight} hg\nAltura: {height} dm\nTipos: {', '.join(types)}\nHabilidades: {', '.join(abilities)}"
    info_label = tk.Label(window, text=info_text)
    info_label.pack()

    # Botón para cerrar la ventana
    close_button = tk.Button(window, text="Cerrar", command=window.destroy)
    close_button.pack()

    # Ejecutar el loop principal de la ventana
    window.mainloop()
