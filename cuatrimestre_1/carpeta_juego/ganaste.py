import pygame
import sys
from funciones import *
from ajustes_generales import mostrar_texto
from musica import *
class Ganaste:
    def __init__(self):
        pygame.init()

        self.width, self.height = 984, 640
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("TOP 5")

        self.background_image = pygame.image.load(r"cuatrimestre_1\carpeta_juego\imagenes\otras_img\sistema_solar_desde_la_naturaleza_by_elimiu_deqs9k1-414w-2x.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.font = pygame.font.Font(None, 36)

    def mostrar_texto(self, texto, x, y):
        texto_renderizado = self.font.render(texto, True, "white")
        self.screen.blit(texto_renderizado, (x, y))

    def iniciar(self):
        
        for i in leer_json("cuatrimestre_1\carpeta_juego\mini.json"):
            nombre_actual = i["nombre"]
            puntos_jugador = i["puntos"]
        tamaño = len(nombre_actual)
        tamaño2 = len(str(puntos_jugador))

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
        musica_de_fondo(pantalla_de_inicio_musica,0.5)
        mostrar_texto("Felicitaciones ", self.width // 2 -30, self.height // 2, 3000,r"cuatrimestre_1\carpeta_juego\imagenes\otras_img\sistema_solar_desde_la_naturaleza_by_elimiu_deqs9k1-414w-2x.jpg",self.width,self.height)
        mostrar_texto("ganaste ", self.width // 2 -30, self.height // 2, 3000,r"cuatrimestre_1\carpeta_juego\imagenes\otras_img\sistema_solar_desde_la_naturaleza_by_elimiu_deqs9k1-414w-2x.jpg",self.width,self.height)
        
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
                            parar_musica(3)
                            run = False
                            return 4
                        if (0) <= mouse_x <= (250) and 0 <= mouse_y <= 45:
                            parar_musica(3)
                            print("volver a jugar")
                            run = False
                            return 0


                            
            dibujar_cuadrado_con_texto(self.screen,((self.width)-100),0,100,45,3,(117, 233, 236),"Menu",font_path,35,"purple")
            dibujar_cuadrado_con_texto(self.screen,(0),0,250,45,3,(56, 245, 0),"volver a jugar",font_path,35,"purple")


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

            self.mostrar_texto("tu puntuacion de esta partida",((self.width//2)-150),20)
            self.mostrar_texto("Nombre  | puntos",((self.width//2)-100),50)
            self.mostrar_texto(f" | ",(self.width//2)-1,75)
            self.mostrar_texto(f"{puntos_jugador}",(((self.width//2)+tamaño2)+10),75)
            self.mostrar_texto(f"{nombre_actual}",(((self.width//2)-tamaño)-100),75)






            pygame.display.flip()
            pygame.time.Clock().tick(60)
            pygame.display.update()

# top5_screen = Ganaste()
# top5_screen.iniciar()
