from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.image import Image as CoreImage
from io import BytesIO
import requests
from kivymd.uix.card import MDCard
from API_Interaction import get_pokemon_data  # Importar la función para obtener datos del Pokémon
from Pokemon_Storage import save_pokemon_to_json  # Importar la función para guardar los datos en JSON

# Definición del diseño KV para la interfaz gráfica usando KivyMD
KV = '''
BoxLayout:
    orientation: 'horizontal'  # Layout principal horizontal
    padding: 20
    spacing: 20

    MDBoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.5
        padding: 10

        MDTextField:
            id: pokemon_input
            hint_text: "Introduce el nombre del Pokémon"  # Entrada de texto para el nombre del Pokémon
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Buscar Pokémon"  # Botón para iniciar la búsqueda
            pos_hint: {"center_x": 0.5}
            on_release: app.search_pokemon()  # Llamada a la función de búsqueda

    CustomCard:
        id: pokemon_card
        orientation: 'vertical'
        size_hint: None, None
        size: 500, 800  # Tamaño de la tarjeta donde se mostrará la información del Pokémon
        md_bg_color: 0.1, 0.1, 0.1, 1  # Color de fondo
        padding: 20
        spacing: 20
        radius: [20,]

        MDBoxLayout:
            orientation: 'vertical'
            padding: 10
            spacing: 10
            size_hint_y: None
            height: 400

            Image:
                id: image_pokemon  # Widget para mostrar la imagen del Pokémon
                size_hint: None, None
                size: 300, 300  # Tamaño de la imagen
                allow_stretch: True
                pos_hint: {"center_x": 0.5}

            MDLabel:
                id: name_label  # Mostrar el nombre del Pokémon
                text: "Nombre: "
                halign: "center"
                font_style: "H4"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDLabel:
                id: type_label  # Mostrar los tipos del Pokémon
                text: "Tipo: "
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0.6, 0.6, 0.6, 1

        MDBoxLayout:
            orientation: 'horizontal'
            padding: 10
            spacing: 10
            size_hint_y: None
            height: 200

            MDLabel:
                id: stats_label  # Mostrar las estadísticas (Ataque, Defensa, Velocidad)
                text: "Estadísticas: \\nAtaque: \\nDefensa: \\nVelocidad: "
                halign: "left"
                font_style: "H6"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDLabel:
                id: extra_info_label  # Mostrar información adicional (Altura, Peso, Habilidades)
                text: "Altura: \\nPeso: \\nHabilidades: "
                halign: "left"
                font_style: "H6"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
'''

class CustomCard(MDCard):
    pass

class PokedexApp(MDApp):
    # Función principal que construye la aplicación
    def build(self):
        return Builder.load_string(KV)

    # Función para buscar los datos del Pokémon usando el nombre ingresado
    def search_pokemon(self):
        pokemon_name = self.root.ids.pokemon_input.text.lower()  # Obtener el nombre del Pokémon ingresado
        pokemon_data = get_pokemon_data(pokemon_name)  # Llamada a la API para obtener los datos del Pokémon

        if pokemon_data:
            self.update_pokemon_card(pokemon_data)  # Actualizar la tarjeta con los datos obtenidos
            save_pokemon_to_json(pokemon_name, pokemon_data)  # Guardar los datos en un archivo JSON
        else:
            self.root.ids.name_label.text = "Pokémon no encontrado"  # Mostrar mensaje si el Pokémon no es encontrado

    # Función para actualizar la tarjeta con la información del Pokémon
    def update_pokemon_card(self, pokemon_data):
        # Cargar la imagen del Pokémon desde la URL proporcionada por la API
        image_url = pokemon_data['sprites']['front_default']
        response_img = requests.get(image_url)
        pokemon_image = CoreImage(BytesIO(response_img.content), ext='png')
        self.root.ids.image_pokemon.texture = pokemon_image.texture

        # Actualizar el texto con el nombre y tipo del Pokémon
        self.root.ids.name_label.text = f"Nombre: {pokemon_data['name'].capitalize()}"
        self.root.ids.type_label.text = f"Tipo: {', '.join([type['type']['name'] for type in pokemon_data['types']])}"

        # Actualizar las estadísticas con números en lugar de barras
        attack = pokemon_data['stats'][1]['base_stat']
        defense = pokemon_data['stats'][2]['base_stat']
        speed = pokemon_data['stats'][5]['base_stat']
        stats_text = f"Estadísticas:\nAtaque: {attack}\nDefensa: {defense}\nVelocidad: {speed}"
        self.root.ids.stats_label.text = stats_text

        # Obtener información adicional: altura, peso y habilidades del Pokémon
        height = pokemon_data['height'] / 10  # Convertir de decímetros a metros
        weight = pokemon_data['weight'] / 10  # Convertir de hectogramos a kilogramos
        abilities = ', '.join([ability['ability']['name'] for ability in pokemon_data['abilities']])
        extra_info_text = f"Altura: {height} m\nPeso: {weight} kg\nHabilidades: {abilities}"
        self.root.ids.extra_info_label.text = extra_info_text

if __name__ == "__main__":
    PokedexApp().run()
