# Ucamp_Proyects_Pok-dex
Respositorio de proyectos de la Ucamp corriespondiente al Módulo 4 de "Bootcamp fundamentos básicos de Puthon".

Proyecto principal del repositorio: Pokédex hecha en lenguaje python, con interfaz.

OJO: El siguiente proyecto necesita el uso de librerias externas a python, este proyecto tuvo una version de prube usando Tkinter, pero está version ya hace uso de Kivy, Pillow y de otras libreias pra su funcionamineto. Todas estás librerias y especificaciones estarán en un archivo requerimients.txt para que puedea instalarlo en su entorno de desarollo (usando *pin install -r requerimientes.txt*). Por razones por compatibilidad y de seguridada para el funcionamiento del archivo se recominedo usarlo en su entrono de desarrollo y solo utilizar las versiones ya indicadas en el archivo requerimientes.txt. (Nota desarrollodor: Ya que tuve problemas de compatibilidad con Kivy cuando empezé la interfaz a la hora de genearar la interfaz).

Descripción del proyecto: Proyecto destinado para la practica de conociminetos adquiridos durante el módulo. Se basa en el muy conocido anime de Pokémon, el cual consiste en un juego en el cual se pueden capturar pokémones, estos pokémones tienen un nombre, un tipo y una imagen. El proyecto es simular el aquel dispositivo, ya que este programa permite guardar pokémones en un archivo JSON, y mostrarlos en una interfaz gráfica, mostrando desde sus caracteristicas, ahbilidades, tipo, nombre e imagen para una mejor cokmpresión del pokémon. 

Hace uso del API de pokémon para obtener los datos de los pokémones, además incleye la carpeta Pokemon_Container_Box en el cual están guardadas solicitudes de pruebas, asi que puede utilizarlas o puede generar otras en la misma carpeta. Al ejecutar el programa eregerá una ventana en la cual debera escribir el nombre en la barra de busqueda en el lado izquierdo inferior (Se recomiendo escribir de manera correcta los nombres o se le mostrará un mensaje de error de "Pokémon no encontrado"). Además que muestra notificaciones si la API no está respondiendo correctamente.

Developers: Bien ahora vamos con algo más especifico. Este Proyecto está divido en:
Código principal: En el cual se encuentra el código principal del proyecto:
 - API_Interaction.py
 - grafic_interfaz.py
 - Pokedex_Proyect.py (Archivo main)
 - Pokemon_Storage.py

Carpetas de .josn y requeriminetos
 - Pokemon_Container_Box (Carpeta con archivos json)
 - requerimients.txt (Archivo con las librerias necesarias para el funcionamiento del proyecto)

La carpeta Pokemon_Container_Box contiene archivos json que contienen solicitudes de pokémones, los cuales se pueden utilizar para probar el funcionamiento del programa, pero puede eliminar está carpeta si cree que no necesita los .json de prueba ya que a la hora de generar solicitudes nuevas está carpeta se creará automaticamente mediante el módulo Pokemon_Storage.py (Aquei tambien puede modificar el nombre de dicha carpeta para que se adapte a su gusto, peuede cambiar el nombre en la linea 14 de dicho módulo).

Se separaron los .json fuera del src, a que si endadao caso que solo quiera los datos generados por el programa no tendrá que acceder a la carpeta con el código principal, de esa forma seria una forma más accesible para el usuario y de seguridad contra ccidentes a la hora de navegar por las carpetas.

Nota: Nota este programa por motivos de rendimineto y compatibilidad genera automaticamente una carpeta (_pycache_) con el caché para acelaerar ejecuciones posteriores. (Dicahas carpetas estarán en .pyc (Formato bytecoe)). En dado caso que este archivo este en el repositorio puede eliminarlo (Recomendado) ya que asi puede gerar sus propias carpetas de caché.

 - Como podrá notar grafic_interfaz contiene la interfaz gráfica del programa, en la cual se encuentra el código para la interfaz gráfica, el cual está basado en Kivy, una libreria para la creación de interfaces gráficas en python. (Nota: Si no tiene instalada Kivy puede instalarla usando pip install kivy).

 - API_Interaction.py: Este módulo contiene la función para la obtención de datos de pokémones, esta función hace uso de la API de pokémon para obtener los datos de los pokémones, y los devuelve en un diccionario. (Nota: Si no tiene instalada la API de pokémon puede instalarla usando pip install requests).

 - Pokedex_Proyect.py: Este módulo contiene la función main, la cual es la función principal del programa, esta función crea la interfaz gráfica y la muestra en la pantalla, y permite al usuario interactuar con ella. (Nota: Si no tiene instalada la API de pokémon puede instalarla usando pip install requests).

 Pokemon_Storage.py: Este módulo contiene la función para la obtención de datos de pokémones, esta función hace uso de la API de pokémon para obtener los datos de los pokémones, y los devuelve en un diccionario. (Nota: Si no tiene instalada la API de pokémon puede instalarla usando pip install requests).

Nota Propia: Los comentarios traté de hacerlos más al grano tanto para tener una vista mas limpia y poder se más directo (Además que me di cuenta que mis comentarios en proyectos anterirores llegaban hacer algo largos).

Contenido Repositorio: Carpeta src con todos los módulos ---> 9.19 KB....... En disco ---> 20.0 KB

Contenido Carpeta Completa: Librerias, Modulos de Código, .json de prueba ---> 246 MB....... En disco ---> 259 MB

(Si lose es muy pesado para un programa de ese tipo pero cuando sepa depurar el código se reducirá el tamaño del repositorio)

----------------------------------------------------------------------------------------------------------------------------------------------

Comentarios: Hasta ahora es el programa más demandante ya que tuve que usar todos los recursos y conociminetos que obtuve hasta ahora, además de que me di cuenta que no era tan fácil como pensaba, pero al final logré hacerlo (Lo cual me deja no hay que subestimar el código). Este programa tiene cosas que mejorar aún ya que no es el más eficiente, pero es un buen punto de partida para seguir aprendiendo.

Este asi un camino dificil ya que hay cosas que aun no estoy seguro de que las comprendo al 100%, pero se que puedo seguir practicando para mejorar mi conocimiento y habilidades en programación. Cuando tenia la primera versión no convencia mucho la interfaz y ver como mi primer código lo logre transformar en algo un poco más agradable para mi, me guisto mucho.

Muchas gracias por guiarme en el camino, ahora so me corresponde seguir avanzando y seguir aprendiendo. :)

----------------------------------------------------------------------------------------------------------------------------------------------

Nota: Si tiene alguna duda o pregunta puede contactarme en mi correo electrónico: baldeivin82@gmail.com