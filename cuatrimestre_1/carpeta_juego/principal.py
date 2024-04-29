
import pygame
from funciones import *
from nivel_1 import *
from nivel_2 import Nivel2
from nivel_3 import Nivel3
from top_5 import *
from perdiste import *
from ganaste import *


pygame.init()
ancho_screen = 984
largo_screen = 640
screen = pygame.display.set_mode((ancho_screen, largo_screen))
pygame.display.set_caption("Mi Juego")

direccion_de_la_imagen = r"cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\iniciomod.png"
# Carga la imagen del fondo
fondo = pygame.image.load(direccion_de_la_imagen)
# Escala la imagen para que coincida con las dimensiones de la ventana
fondo = pygame.transform.scale(fondo, (ancho_screen, largo_screen))
clock = pygame.time.Clock()

# Fuentes/font_title
fuente_titulo = r"cuatrimestre_1\carpeta_juego\fuentes\4\airstrikehalf.ttf"
fuente = pygame.font.Font(fuente_titulo, 60)  #titulo
texto = " space INVADERS"#invaders


font_path = r"cuatrimestre_1\carpeta_juego\fuentes\5\DS-DIGI.TTF"
# fuente_nombre = pygame.font.Font(font_path,35) #texto ingreasado
nombre_del_jugador = ""
color= "green"

puntos = 0
nivel_actual = 6
running = True
for i in leer_json(r"cuatrimestre_1\carpeta_juego\volumen.json"):
    musica_volumen = float(i["volumen"])
    print(musica_volumen)
musica_de_fondo(pantalla_de_inicio_musica,musica_volumen)
while running:

    
    screen.blit(fondo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)

            if key_name == "space" or key_name  == "backspace" or validacion_de_menu(key_name)!= -1:
                print(f"Tecla presionada: {key_name}")
                if key_name == "backspace":
                    nombre_del_jugador = nombre_del_jugador[:-1]

                elif key_name == "space":
                    nombre_del_jugador += " "

                elif len(nombre_del_jugador)>8:
                    nombre_del_jugador += ""
                else:
                    nombre_del_jugador += key_name 
    
        # Verifica si se hizo clic en el mouse
        elif event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1:  # 1 representa el clic izquierdo del mouse
                mouse_x, mouse_y = event.pos
                if ((ancho_screen // 2) - 60) <= mouse_x <= ((ancho_screen // 2) + 45) and 300 <= mouse_y <= 345:
                    top5_screen = Top5Screen()
                    nivel_actual = top5_screen.mostrar_top5()

                if ((ancho_screen // 2) - 60) <= mouse_x <= ((ancho_screen // 2) + 45) and 350 <= mouse_y <= 395:
                    nombre_archivo = r"cuatrimestre_1\carpeta_juego\volumen.json"
                    datos = {}
                    datos["volumen"] = 0.7
                    archivos = []
                    archivos.append(datos)
                    escribir_json(nombre_archivo, archivos)
                    pygame.quit()
                    sys.exit()

                if ((ancho_screen // 2) - 24) <= mouse_x <= ((ancho_screen // 2) + 16) and 250 <= mouse_y <= 275 and len(nombre_del_jugador)>0 :
                    print("Clic dentro del cuadrado más pequeño")
                    nivel_actual = 0
                    parar_musica(1)
                if ((ancho_screen // 2) - 60) <= mouse_x <= ((ancho_screen // 2) + 45) and 400 <= mouse_y <= 445:
                    if color == "green":
                        color = "red"
                        nombre_archivo = r"cuatrimestre_1\carpeta_juego\volumen.json"
                        datos = {}
                        datos["volumen"] = 0
                        archivos = []
                        archivos.append(datos)
                        escribir_json(nombre_archivo, archivos)
                        parar_musica(3)

                    elif color == "red":
                        color = "green"
                        nombre_archivo = r"cuatrimestre_1\carpeta_juego\volumen.json"
                        datos = {}
                        datos["volumen"] = 0.7
                        archivos = []
                        archivos.append(datos)
                        escribir_json(nombre_archivo, archivos)
                        for i in leer_json(r"cuatrimestre_1\carpeta_juego\volumen.json"):
                            musica_volumen = float(i["volumen"])
                        musica_de_fondo(pantalla_de_inicio_musica,musica_volumen)
                    



    titulo_del_inicio = fuente.render(texto, True, ("purple"))  # Color del texto (purple)
    screen.blit(titulo_del_inicio, (((ancho_screen//2)-ancho_screen//3.51), (largo_screen//5.4167))) 

    #cuadrado de nombre
    dibujar_cuadrado_con_texto(screen,((ancho_screen//2)-100),200,200,45,4,(117, 233, 236),nombre_del_jugador,font_path,35,"purple")
    dibujar_cuadrado_con_texto(screen,((ancho_screen//2)-60),300,100,45,3,(117, 233, 236),"top 5",font_path,35,"purple")
    dibujar_cuadrado_con_texto(screen,((ancho_screen//2)-60),350,100,45,3,(117, 233, 236),"Exit",font_path,35,"purple")
    dibujar_cuadrado_con_texto(screen,((ancho_screen//2)-60),400,100,45,3,color,"musica",font_path,35,"purple")


    #cuadrado mas chicquito de play
    dibujar_cuadrado_con_texto(screen,((ancho_screen//2)-24),250,40,25,2,(243, 250, 110),"",None,20,(211, 107, 242))
    dibujar_triangulo_vacio(screen, ((ancho_screen // 2) -11), 255, 16, 15, (211, 107, 242), 2)

    # niveles 
    if nivel_actual == 0:
        if nivel_actual == 0:
            nivel_1 = Nivel1()
            nivel_actual = nivel_1.ejecutar_nivel()
            print(nivel_actual)
            puntos +=  nivel_1.puntos()

        if nivel_actual == 1:
            nivel_2 = Nivel2()
            nivel_actual = nivel_2.ejecutar_nivel()
            puntos += nivel_2.puntos()

        if nivel_actual == 2:
            nivel_3 = Nivel3()
            nivel_actual = nivel_3.ejecutar_nivel()
            puntos += nivel_3.puntos() 

        if nivel_actual == -1:
            #PERDISTE
            nombre_archivo = r"cuatrimestre_1\carpeta_juego\mini.json"
            datos = {}
            datos["nombre"] = nombre_del_jugador
            datos["puntos"] = puntos
            archivos = []
            archivos.append(datos)
            actualizar_datos_jugadores(nombre_del_jugador, puntos)
            escribir_json(nombre_archivo, archivos)
            juego_finalizado = perdiste()
            nivel_actual = juego_finalizado.iniciar()
            puntos = 0

        if nivel_actual == 3:
            #GANASTE
            nombre_archivo = r"cuatrimestre_1\carpeta_juego\mini.json"
            datos = {}
            datos["nombre"] = nombre_del_jugador
            datos["puntos"] = puntos 
            archivos = []
            archivos.append(datos)
            actualizar_datos_jugadores(nombre_del_jugador, puntos)
            escribir_json(nombre_archivo, archivos)
            juego_finalizado = Ganaste()
            nivel_actual = juego_finalizado.iniciar()
            puntos = 0

        if nivel_actual == 4:
            nombre_del_jugador = ""
            nivel_actual = 6
            # parar_musica(2)
            musica_de_fondo(pantalla_de_inicio_musica,ajustes_de_volumen())

            #volver al inicio

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
