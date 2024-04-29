import pygame
import sys
from funciones import *


class Pausa:
    def __init__(self,nivel):
        pygame.init()

        self.width, self.height = 984, 640
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("TOP 5")

        self.background_image = pygame.image.load(r"cuatrimestre_1\carpeta_juego\imagenes\otras_img\pausa.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        self.configuracion = -2
        self.nivel = nivel

        self.font = pygame.font.Font(None, 36)

    def mostrar_texto(self, texto, x, y):
        texto_renderizado = self.font.render(texto, True, "white")
        self.screen.blit(texto_renderizado, (x, y))

    def iniciar(self):
        start_time = pygame.time.get_ticks()
        run = True
        if ajustes_de_volumen() == 0:
            color = "red"
        if ajustes_de_volumen() == 0.7:
            color = "green"
        while run:
            self.screen.blit(self.background_image, (0, 0))
            current_time = pygame.time.get_ticks() - start_time
            elapsed_time = current_time // 1000  # Convertir de milisegundos a segundos
            # print(elapsed_time)
            if ajustes_de_volumen() == 0:
                pygame.mixer.music.set_volume(0)

            if ajustes_de_volumen() == 0.7:
                pygame.mixer.music.set_volume(0.7)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 1 representa el clic izquierdo del mouse
                        mouse_x, mouse_y = event.pos      
                        
                        
                        if ((self.width//2)-300) <= mouse_x <= ((self.width//2)-300) + 140 and ((self.height//2)-70) <= mouse_y <= ((self.height//2)-70) + 45:
                            print("despausar") 
                            run = False
                            return elapsed_time  

                        if ((self.width//2)-130) <= mouse_x <= ((self.width//2)-130) + 100 and ((self.height//2)-70) <= mouse_y <= ((self.height//2)-70) + 45:
                            print("Menu")
                            self.configuracion = 4
                            run = False
                            return elapsed_time

                        if (self.width//2) <= mouse_x <= (self.width//2) + 130 and ((self.height//2)-70) <= mouse_y <= ((self.height//2)-70) + 45:
                            print("Reiniciar")
                            self.configuracion = self.nivel 
                            run = False
                            return elapsed_time
                            
                        if ((self.width//2)+150) <= mouse_x <= ((self.width//2)+150) + 120 and ((self.height//2)-70) <= mouse_y <= ((self.height//2)-70) + 45:
                            print("salir del juego")
                            nombre_archivo = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\volumen.json"
                            datos = {}
                            datos["volumen"] = 0.7
                            archivos = []
                            archivos.append(datos)
                            escribir_json(nombre_archivo, archivos)
                            run = False
                            pygame.quit()
                            sys.exit()
                        if ((self.width // 2) - 60) <= mouse_x <= ((self.width // 2) + 45) and 400 <= mouse_y <= 445:
                            if color == "green":
                                color = "red"
                                nombre_archivo = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\volumen.json"
                                datos = {}
                                datos["volumen"] = 0
                                archivos = []
                                archivos.append(datos)
                                escribir_json(nombre_archivo, archivos)

                            elif color == "red":
                                color = "green"
                                nombre_archivo = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\volumen.json"
                                datos = {}
                                datos["volumen"] = 0.7
                                archivos = []
                                archivos.append(datos)
                                escribir_json(nombre_archivo, archivos)
                            
            dibujar_cuadrado_con_texto(self.screen,((self.width//2)-300),((self.height//2)-70),140,45,3,(117, 233, 236),"despausar",None,35,"black")
            dibujar_cuadrado_con_texto(self.screen,((self.width//2)-130),((self.height//2)-70),100,45,3,(117, 233, 236),"Menu",None,35,"black")
            dibujar_cuadrado_con_texto(self.screen,((self.width//2)),((self.height//2)-70),130,45,3,(117, 233, 236),"reiniciar",None,35,"black")
            dibujar_cuadrado_con_texto(self.screen,((self.width//2)+150),((self.height//2)-70),120,45,3,(117, 233, 236),"cerrar juego",None,28,"black")
            dibujar_cuadrado_con_texto(self.screen,((self.width//2)-60),400,100,45,3,color,"musica",None,35,"purple")



            pygame.display.flip()
            pygame.time.Clock().tick(60)
            pygame.display.update()
    
    def ajustes(self):
        ajuste = self.configuracion
        return ajuste

# top5_screen = Pausa(1)
# top5_screen.iniciar()
# top5_screen.ajustes()

# import pygame
# import sys
# from funciones import *


# class Pausa:
#     def __init__(self,nivel):
#         pygame.init()

#         self.width, self.height = 984, 640
#         self.screen = pygame.display.set_mode((self.width, self.height))
#         pygame.display.set_caption("TOP 5")

#         self.background_image = pygame.image.load(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\pausa.jpg").convert()
#         self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
#         self.configuracion = -2
#         self.nivel = nivel

#         self.font = pygame.font.Font(None, 36)

#     def mostrar_texto(self, texto, x, y):
#         texto_renderizado = self.font.render(texto, True, "white")
#         self.screen.blit(texto_renderizado, (x, y))

#     def iniciar(self):
#         start_time = pygame.time.get_ticks()
#         run = True
#         if ajustes_de_volumen() == 0:
#             color = "red"
#         if ajustes_de_volumen() == 0.7:
#             color = "green"
#         while run:
#             self.screen.blit(self.background_image, (0, 0))
#             current_time = pygame.time.get_ticks() - start_time
#             elapsed_time = current_time // 1000  # Convertir de milisegundos a segundos
#             # print(elapsed_time)
#             if ajustes_de_volumen() == 0:
#                 pygame.mixer.music.set_volume(0)

#             if ajustes_de_volumen() == 0.7:
#                 pygame.mixer.music.set_volume(0.7)

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()

#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if event.button == 1:  # 1 representa el clic izquierdo del mouse
#                         mouse_x, mouse_y = event.pos      
                        
                        
#                         if ((self.width//2)-300) <= mouse_x <= ((self.width//2)-300) + 140 and ((self.height//2)-70) <= mouse_y <= ((self.height//2)-70) + 45:
#                             print("despausar") 
#                             run = False
#                             return elapsed_time  

#                         if ((self.width//2)-130) <= mouse_x <= ((self.width//2)-130) + 100 and ((self.height//2)-70) <= mouse_y <= ((self.height//2)-70) + 45:
#                             print("Menu")
#                             self.configuracion = 4
#                             run = False
#                             return elapsed_time

#                         if (self.width//2) <= mouse_x <= (self.width//2) + 130 and ((self.height//2)-70) <= mouse_y <= ((self.height//2)-70) + 45:
#                             print("Reiniciar")
#                             self.configuracion = self.nivel 
#                             run = False
#                             return elapsed_time
                            
#                         if ((self.width//2)+150) <= mouse_x <= ((self.width//2)+150) + 120 and ((self.height//2)-70) <= mouse_y <= ((self.height//2)-70) + 45:
#                             print("salir del juego")
#                             nombre_archivo = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\volumen.json"
#                             datos = {}
#                             datos["volumen"] = 0.7
#                             archivos = []
#                             archivos.append(datos)
#                             escribir_json(nombre_archivo, archivos)
#                             run = False
#                             pygame.quit()
#                             sys.exit()
#                         if ((self.width // 2) - 60) <= mouse_x <= ((self.width // 2) + 45) and 400 <= mouse_y <= 445:
#                             if color == "green":
#                                 color = "red"
#                                 nombre_archivo = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\volumen.json"
#                                 datos = {}
#                                 datos["volumen"] = 0
#                                 archivos = []
#                                 archivos.append(datos)
#                                 escribir_json(nombre_archivo, archivos)

#                             elif color == "red":
#                                 color = "green"
#                                 nombre_archivo = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\volumen.json"
#                                 datos = {}
#                                 datos["volumen"] = 0.7
#                                 archivos = []
#                                 archivos.append(datos)
#                                 escribir_json(nombre_archivo, archivos)
#                         if ((self.width//2)-82) <= mouse_x <= ((self.width//2)-82 + 22) and 400 <= mouse_y <= 445:
#                             # color = "green"
#                             nombre_archivo = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\volumen.json"
#                             datos = {}
#                             volumen = ajustes_de_volumen()
#                             if volumen <0 :
#                                 volumen = 0

#                             datos["volumen"] = volumen -0.1
#                             archivos = []
#                             archivos.append(datos)
#                             escribir_json(nombre_archivo, archivos)
#                             print("menos")
#                         if ((self.width//2)+43) <= mouse_x <= ((self.width//2)+40+ 22) and 400 <= mouse_y <= 445:
#                             # color = "green"
#                             nombre_archivo = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\volumen.json"
#                             datos = {}
#                             volumen = ajustes_de_volumen()
#                             if volumen >1 :
#                                 volumen = 1
                                
#                             datos["volumen"] = volumen +0.1
#                             archivos = []
#                             archivos.append(datos)
#                             escribir_json(nombre_archivo, archivos)
                        
#                             print("mas")
#                             pass
                            
#             dibujar_cuadrado_con_texto(self.screen,((self.width//2)-300),((self.height//2)-70),140,45,3,(117, 233, 236),"despausar",None,35,"black")
#             dibujar_cuadrado_con_texto(self.screen,((self.width//2)-130),((self.height//2)-70),100,45,3,(117, 233, 236),"Menu",None,35,"black")
#             dibujar_cuadrado_con_texto(self.screen,((self.width//2)),((self.height//2)-70),130,45,3,(117, 233, 236),"reiniciar",None,35,"black")
#             dibujar_cuadrado_con_texto(self.screen,((self.width//2)+150),((self.height//2)-70),120,45,3,(117, 233, 236),"cerrar juego",None,28,"black")
#             dibujar_cuadrado_con_texto(self.screen,((self.width//2)-60),400,100,45,3,color,"musica",None,35,"purple")
#             dibujar_cuadrado_con_texto(self.screen,((self.width//2)-82),400,25,45,3,"blue","-",None,45,"purple")
#             dibujar_cuadrado_con_texto(self.screen,((self.width//2)+40),400,25,45,3,"blue","+",None,45,"purple")




#             pygame.display.flip()
#             pygame.time.Clock().tick(60)
#             pygame.display.update()
    
#     def ajustes(self):
#         ajuste = self.configuracion
#         return ajuste

# top5_screen = Pausa(1)
# top5_screen.iniciar()
# top5_screen.ajustes()