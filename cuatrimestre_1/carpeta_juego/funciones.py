import pygame 
import re 
import json
import os
pygame.init()

def ajustes_de_volumen():
    for i in leer_json(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\volumen.json"):
        musica_volumen = float(i["volumen"])
        return musica_volumen
    
def girar_imagenes(lista_original,flip_x,flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen,flip_x,flip_y))
    return lista_girada

def rotar_imagen(lista_original,angulo):
    lista_rotada = []
    for i in lista_original:
        lista_rotada.append(pygame.transform.rotate(i, angulo))
    return lista_rotada

def rescalar_imagenes(diccionario_animaciones,tamaño:tuple):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            superficie = diccionario_animaciones[clave][i]
            superficie = diccionario_animaciones[clave][i] = pygame.transform.scale(superficie,tamaño)

def animacion_nave():  
        diccionario_de_animaciones = {}
        diccionario_de_animaciones["derecha"] = personaje_derecha
        diccionario_de_animaciones["quieto"] = personaje_quieto
        diccionario_de_animaciones["izquierda"] = personaje_izquierda
        diccionario_de_animaciones["abajo"] = personaje_abajo
        diccionario_de_animaciones["arriba"] = personaje_quieto
        
        return diccionario_de_animaciones

def animacion_corazon():
    diccionario_de_animaciones = {}
    diccionario_de_animaciones["normal"] = corazones
    return diccionario_de_animaciones


def sonido_inicial(musica_inicial,volumen):
    pygame.mixer.music.load(musica_inicial)
    pygame.mixer.music.set_volume(volumen)
    return pygame.mixer.music.play(-1)



corazones = [pygame.image.load(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\objetos\vida.png")]

#personaje
personaje_quieto  = [pygame.image.load(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\nave\nave.png")]
personaje_desplazamiento = [pygame.image.load(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\nave\nave.png"),
                        pygame.image.load(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\nave\nave.png") ]
personaje_derecha = rotar_imagen(personaje_desplazamiento,-90)
personaje_izquierda = rotar_imagen(personaje_desplazamiento,90)
personaje_abajo = girar_imagenes(personaje_desplazamiento,True,True)



def validacion_de_menu(respuesta:str):
    """
    valida lo que se puede ingresar en el menu
    devuelve:
    * -1 si es invalida
    * devuelve el str si es valido 
    """
    validacion = r'[0-9A-Za-z]{1,10}+$'
    #^(?=(?:[a-zA-Z]*[0-9]*){11}$)[a-zA-Z0-9]{11}$
    if re.match(validacion,respuesta):
        mensaje = respuesta
    else :
        mensaje = -1 
    return mensaje



def actualizar_datos_jugadores(nombre, puntos):
    """
    guarda los puntos y el nombre en un archivo json

    """
    # Ruta del archivo JSON
    ruta_archivo = r'Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\dati os_jugadores.json'

    # Verificar si el archivo ya existe
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_existente: # Si el archivo existe, cargar los datos existentes
            datos_existente = json.load(archivo_existente)

        datos_existente["jugadores"].append({"nombre": nombre, "puntos": puntos})# Agregar el nuevo jugador al archivo existente

        datos_existente["jugadores"] = sorted(datos_existente["jugadores"], key=lambda x: x["puntos"], reverse=True)# Ordenar la lista de jugadores por puntos de mayor a menor

        datos_existente["jugadores"] = datos_existente["jugadores"][:5]# Limitar la lista a los 5 mejores jugadores

        with open(ruta_archivo, 'w') as archivo_json:# Escribir todos los datos de nuevo al archivo JSON
            json.dump(datos_existente, archivo_json, indent=2)
    else:
        with open(ruta_archivo, 'w') as archivo_json: # Si el archivo no existe, simplemente escribir los datos
            json.dump({"jugadores": [{"nombre": nombre, "puntos": puntos}]}, archivo_json, indent=2)

    print(f"Se ha actualizado el archivo JSON en {ruta_archivo}")


def leer_datos_jugadores(ruta_archivo):
    """
    Lee los datos de jugadores desde un archivo JSON.
    Parameters:
    - ruta_archivo (str): La ruta del archivo JSON.
    Returns:
    - list: Una lista de diccionarios que representan los datos de los jugadores.
    """
    # Verificar si el archivo existe
    if not os.path.exists(ruta_archivo):
        print(f"El archivo {ruta_archivo} no existe.")
        return []

    # Leer los datos del archivo JSON
    with open(ruta_archivo, 'r') as archivo_json:
        datos_jugadores = json.load(archivo_json)

    # Obtener la lista de jugadores del diccionario
    jugadores = datos_jugadores.get("jugadores", [])

    return jugadores







def dibujar_cuadrado_con_texto(fondo, x, y, ancho_cuadrado, largo, ancho_del_cuadrado, color_del_cuadrado, texto, tipografia, tamaño_tipografia, color):
    # Obtener la posición del mouse
    pos_mouse = pygame.mouse.get_pos()

    # Crear un rectángulo que representa el cuadrado
    rectangulo_cuadrado = pygame.Rect(x, y, ancho_cuadrado, largo)

    # Verificar si el mouse está sobre el cuadrado
    if rectangulo_cuadrado.collidepoint(pos_mouse):
        color_del_cuadrado = (200, 200, 200)  # Cambiar el color cuando el mouse está sobre el cuadrado

    # Dibujar el cuadrado
    pygame.draw.rect(fondo, color_del_cuadrado, (x, y, ancho_cuadrado, largo), ancho_del_cuadrado)

    # Crear el texto
    fuente = pygame.font.Font(tipografia, tamaño_tipografia)
    texto_surface = fuente.render(texto, True, color)

    # Centrar el texto dentro del cuadrado
    text_rect = texto_surface.get_rect(center=(x + ancho_cuadrado // 2, y + largo // 2))

    # Dibujar el texto
    fondo.blit(texto_surface, text_rect)


    
def dibujar_cuadrado_con_texto(fondo, x, y, ancho_cuadrado, largo, ancho_del_cuadrado, color_del_cuadrado, texto, tipografia, tamaño_tipografia, color):
    """
    fondo: fondo de pantalla | x,y 

    if (self.width - 100) <= mouse_x <= (self.width) and 0 <= mouse_y <= 45:
    dibujar_cuadrado_con_texto(self.screen,((self.width)-100),0,100,45,3,(117, 233, 236),"Exit",font_path,35,"purple")


    """
    pygame.draw.rect(fondo, color_del_cuadrado, (x, y, ancho_cuadrado, largo), ancho_del_cuadrado)
    fuente = pygame.font.Font(tipografia, tamaño_tipografia)
    texto_surface = fuente.render(texto, True, color)
    # Centrar el texto dentro del cuadrado
    text_rect = texto_surface.get_rect(center=(x + ancho_cuadrado // 2, y + largo // 2))
    fondo.blit(texto_surface, text_rect)


def dibujar_triangulo_vacio(fondo, x, y, ancho, alto, color, grosor_linea, direccion="derecha"):
    if direccion == "derecha":
        pygame.draw.polygon(fondo, color, [(x, y), (x + ancho, y + alto // 2), (x, y + alto)], grosor_linea)
    elif direccion == "izquierda":
        pygame.draw.polygon(fondo, color, [(x + ancho, y), (x, y + alto // 2), (x + ancho, y + alto)], grosor_linea)
    elif direccion == "arriba":
        pygame.draw.polygon(fondo, color, [(x, y + alto), (x + ancho // 2, y), (x + ancho, y + alto)], grosor_linea)




def escribir_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo)



def leer_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos_leidos = json.load(archivo)
    return datos_leidos