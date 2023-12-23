import pygame
import sys
from funciones import *
from class_personaje import *
from class_disparo import *
import time
from vidas import *
from pausa import *
#ajustes generales
pygame.init() 
width, height = 984, 640
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
background_color = (0, 0, 0)

def mostrar_texto(texto, x, y, duracion, fondo,ancho,largo):
    # Cargar la imagen de fondo
    fondo_pantalla = pygame.image.load(fondo)
    fondo_pantalla = pygame.transform.scale(fondo_pantalla, (ancho, largo))

    # Obtener el tiempo inicial
    tiempo_inicial = pygame.time.get_ticks()

    # Bucle principal
    while pygame.time.get_ticks() - tiempo_inicial < duracion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Dibujar la imagen de fondo en cada iteración
        screen.blit(fondo_pantalla, (0, 0))
        
        # Dibujar el texto
        texto_surface = font.render(texto, True, text_color)
        rect = texto_surface.get_rect(center=(x, y))
        screen.blit(texto_surface, rect)

        pygame.display.flip()
        clock.tick(60)


class Nivel:
    def __init__(self, ancho_screen, largo_screen, fps,tiempo,fondo,nivel):
        pygame.init()
        self.nivel = nivel
        self.interfas = -2
        # Tamaño de la ventana
        self.ancho_screen = ancho_screen #widh
        self.largo_screen = largo_screen # heig
        self.screen = pygame.display.set_mode((self.ancho_screen, self.largo_screen))

        # Carga la imagen del fondo
        fondo1 = pygame.image.load(fondo).convert()
        self.fondo1 = pygame.transform.scale(fondo1, (self.ancho_screen, self.largo_screen))


        # Fuentes/font_title
        fuente_titulo =  r"C:\Users\matia\OneDrive\Escritorio\UTN\Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\fuentes\5\DS-DIGI.TTF"
        self.fuente = pygame.font.Font(fuente_titulo, 30)  #fuente de texto contador y puntos

        # Coordenadas iniciales del cuadradito
        self.mis_disparos = pygame.sprite.Group()

        self.x_pos = (self.ancho_screen / 2) - 30
        self.y_pos = largo_screen-100
        
        diccionario_de_animaciones = animacion_nave() # genera la nave
        self.nave = Personaje(diccionario_de_animaciones, self.x_pos, self.y_pos, (90, 80), 10, "quieto",self.mis_disparos)
        
        #configuracion del reloj
        self.tiempo = tiempo
        self.reloj = pygame.time.Clock()
        self.fps = fps
        self.tiempo_ejecusion_del_juego = tiempo
        self.start_time = time.time() # se inicializa el timer
        self.puntos = 0 # se inicializa los puntos

        # self.vidas = Vidas()        
        self.vida = pygame.sprite.Group()
        self.vida.add(Vidas(60,60))

        self.vida2 = pygame.sprite.Group()
        self.vida2.add(Vidas(30,60))

        self.vida3 = pygame.sprite.Group()
        self.vida3.add(Vidas(0,60))


    
        imagen_pausa_path = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\boton.jpg"
        imagen_pausa = pygame.image.load(imagen_pausa_path)
        
        # Escalar la imagen a las dimensiones deseadas (100x100)
        self.imagen_pausa = pygame.transform.scale(imagen_pausa, (50, 50))
        
        # Obtener el rectángulo de la imagen
        self.rect_imagen_pausa = imagen_pausa.get_rect()

        # Definir la posición de la imagen en la esquina derecha
        self.pos_x_pausa = self.ancho_screen - 50
        self.pos_y_pausa = 0
        self.pausado = False  
        self.teclas = None
        self.volumen = ajustes_de_volumen()
    def verificar_pausa(self, mouse_x, mouse_y):
        # Verificar colisión con la imagen de pausa
        if self.pos_x_pausa <= mouse_x <= self.pos_x_pausa + self.rect_imagen_pausa.width and \
            self.pos_y_pausa <= mouse_y <= self.pos_y_pausa + self.rect_imagen_pausa.height:
            print("pausado")      

    def ejecutar(self):
        self.reloj.tick(self.fps)
        self.screen.blit(self.fondo1, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                print(key_name)
                self.teclas = key_name
                if key_name == 'p': 
                    
                    top5_screen = Pausa(self.nivel)
                    self.tiempo += top5_screen.iniciar()
                    self.interfas = top5_screen.ajustes()
                    self.volumen = ajustes_de_volumen()

                    # ajustes_de_volumen()



            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.verificar_pausa(mouse_x, mouse_y)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 1 representa el clic izquierdo del mouse
                        mouse_x, mouse_y = event.pos      
                        if (self.ancho_screen - 100) <= mouse_x <= (self.ancho_screen) and 0 <= mouse_y <= 45:
                            print("ir al menu")
                            top5_screen = Pausa(self.nivel)
                            self.tiempo += top5_screen.iniciar()
                            self.interfas = top5_screen.ajustes()
                            self.volumen = ajustes_de_volumen()

    

    def timer(self):
        """
        se lee el tiempo de ejecucion del juego y se blitea un contador del mismo
        """
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        # print(elapsed_time)
        tiempo_restante = self.tiempo - elapsed_time
        self.tiempo_ejecusion_del_juego = tiempo_restante
        #texto del timer
        text = self.fuente.render(f"Tiempo: {int(self.tiempo_ejecusion_del_juego)}", True, ("purple"))
        self.screen.blit(text, (0, 30)) #posicion en donde se dibuja en la pantalla
    
    def controlador_tiempo(self):
        """
        sirve para monitorear el tiempo y devuelve el mismo 
        esto se hace para evitar errores al llamar varibles menos especificas
        retorna el tiempo monitorizado
        """
        tiempo =  self.tiempo_ejecusion_del_juego 
        return tiempo

    def ejecusion_final(self):
        """
        se encarga de la ejecucion tanto del tiempo como de la ejeucion de las 3
        vidas del personaje
        """
        self.timer()
        self.volumen = ajustes_de_volumen()
        texto = f"puntos : {self.puntos}" 
        # este es el texto del contador de puntos
        titulo_del_inicio = self.fuente.render((texto ), True, ("purple"))  # Color del texto (purple)
        self.screen.blit(titulo_del_inicio ,(0, 0)) # posicion en donde se dibuja en la pantalla
        # self.screen.blit(self.imagen_pausa, (self.pos_x_pausa, self.pos_y_pausa))

        # Vidas.update()

        #se actualiza las vidas en la pantalla
        self.vida.update(self.nave.vidas)
        self.vida.draw(self.screen)
        # self.screen.blit(self.imagen, (self.pos_x_pausa, self.pos_y_pausa))

        self.vida2.update()
        self.vida2.draw(self.screen)

        self.vida3.update()
        self.vida3.draw(self.screen)
        
        # aca se elimina las vidas segun las colisiones que ocurran
        if self.nave.vidas <= 2:
            if  self.nave.vidas == 2:
                self.vida.empty()
            elif self.nave.vidas == 1:
                self.vida2.empty()
            elif self.nave.vidas == 0:
                self.vida3.empty()
                
        dibujar_cuadrado_con_texto(self.screen,((self.ancho_screen)-100),0,100,45,3,(117, 233, 236),"Menu",None,35,"purple")
