import pygame
import sys
from funciones import *


class Top5Screen:
    def __init__(self):
        pygame.init()

        self.width, self.height = 984, 640
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("TOP 5")

        self.background_image = pygame.image.load(r"cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\menu_de_inicio.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.font = pygame.font.Font(None, 36)

    def mostrar_texto(self, texto, x, y):
        texto_renderizado = self.font.render(texto, True, "white")
        self.screen.blit(texto_renderizado, (x, y))

    def mostrar_top5(self):
        nombres = []
        puntos = []
        font_path = r"cuatrimestre_1\carpeta_juego\fuentes\5\DS-DIGI.TTF"

        datos = leer_datos_jugadores(r"cuatrimestre_1\carpeta_juego\dati os_jugadores.json")
        for i, jugador in enumerate(datos):
            nombre = jugador.get('nombre', 'Nombre no proporcionado')
            punto = jugador.get('puntos', 0)

            nombres.append(nombre)
            puntos.append(punto)

        nombre1, nombre2, nombre3, nombre4, nombre5 = nombres[:5]
        puntos1, puntos2, puntos3, puntos4, puntos5 = puntos[:5]
        run = True
        while run:
            self.screen.blit(self.background_image, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    key_name = pygame.key.name(event.key)
                    if key_name == "escape":
                        run = False
                        return 4

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 1 representa el clic izquierdo del mouse
                        mouse_x, mouse_y = event.pos      
                        if (self.width - 100) <= mouse_x <= (self.width) and 0 <= mouse_y <= 45:
                            print("ir al menu")
                            run = False
                            return 4
                            
            dibujar_cuadrado_con_texto(self.screen,((self.width)-100),0,100,45,3,(117, 233, 236),"Menu",font_path,35,"purple")

            pygame.draw.rect(self.screen, "black", (self.width // 6 - 70, self.height // 4, 2 * self.width // 3 + 140, self.height // 2), 2)

            for i in range(1, 7):
                pygame.draw.line(self.screen, "black", (self.width // 6 - 70, self.height // 4 + i * (self.height // 12)), (5 * self.width // 6 + 70, self.height // 4 + i * (self.height // 12)), 2)

            pygame.draw.line(self.screen, "black", (self.width // 2, self.height // 4), (self.width // 2, self.height // 4 + self.height // 2), 2)

            self.mostrar_texto("TOP 5", self.width // 2 - 30  , self.height // 4 -30)

            self.mostrar_texto("Nombre", self.width // 4 , self.height // 4 + 20)
            self.mostrar_texto("Puntos", self.width // 2 + 135, self.height // 4 + 20)

            self.mostrar_texto(nombre1, self.width // 4 , self.height // 4 + 70)
            self.mostrar_texto(str(puntos1), self.width // 2 + 135, self.height // 4 + 70)

            self.mostrar_texto(nombre2, self.width // 4 , self.height // 4 + 120)
            self.mostrar_texto(str(puntos2), self.width // 2 + 135, self.height // 4 + 120)

            self.mostrar_texto(nombre3, self.width // 4 , self.height // 4 + 170)
            self.mostrar_texto(str(puntos3), self.width // 2 + 135, self.height // 4 + 170)

            self.mostrar_texto(nombre4, self.width // 4 , self.height // 4 + 220)
            self.mostrar_texto(str(puntos4), self.width // 2 + 135, self.height // 4 + 220)

            self.mostrar_texto(nombre5, self.width // 4 , self.height // 4 + 270)
            self.mostrar_texto(str(puntos5), self.width // 2 + 135, self.height // 4 + 270)


            pygame.display.flip()
            pygame.time.Clock().tick(60)
            pygame.display.update()

# top5_screen = Top5Screen()
# top5_screen.mostrar_top5()
