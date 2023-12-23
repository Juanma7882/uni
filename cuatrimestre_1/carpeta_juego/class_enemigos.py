from typing import Any
import pygame
import random
import time
from musica import *
from ajustes_generales import *
from class_disparo import *
from funciones import ajustes_de_volumen

# ancho_screen = 984
# largo_screen = 630

class Enemigo(pygame.sprite.Sprite):
    # Manejo de rutas de archivos
    image_path = r"Curso_de_ingreso_PYTHON-main/ejercicios/cuatrimestre_1/carpeta_juego/imagenes/enemigos/enemigo_peque.png"
    original_image = pygame.image.load(image_path)
    
    def __init__(self,ancho_screen,largo_screen,grupo_disparo):
        super().__init__()
        self.ancho_screen = ancho_screen
        self.largo_screen = largo_screen
        # Escalar la imagen al tamaño deseado
        self.grupo_disparo = grupo_disparo
        self.image = pygame.transform.scale(self.original_image, (40, 60))
        self.image.set_colorkey((0, 0, 0))
        # Posicionamiento del enemigo
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange((largo_screen-self.rect.width)//6) 
        self.rect.x = random.randrange(ancho_screen-self.rect.height)
        self.velocidad_y = random.randint(1, 2)
        self.velocidad_x = random.randint(1, 2)
        self.vidas = 3
        self.start_time = time.time()


    def update(self) -> None:
        tiempo_de_disparo = random.randint(2, 3)
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x

        if self.rect.left < 0:
            self.velocidad_x += 1

        if  self.rect.right > self.ancho_screen:
            self.velocidad_x -= 1

        if self.rect.top < 0:
            self.velocidad_y += 1

        if self.rect.bottom > self.largo_screen:
            self.velocidad_y -= 1
        if self.vidas == 0:
            self.kill()

        if elapsed_time >= tiempo_de_disparo:
            bala = Disparo(self.rect.centerx-2, self.rect.top+50, "positivo",imagen_de_disparo,(20,20))
            self.grupo_disparo.add(bala)
            self.start_time = current_time
            reproducir_sonido(sonido_disparo,ajustes_de_volumen())

    def disparo(self):#centro
            bala = Disparo(self.rect.centerx-2, self.rect.top+50, "positivo",imagen_de_disparo,(20,20))
            self.grupo_disparo.add(bala)

    
    


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    



class Meterorito(pygame.sprite.Sprite):
    """
    los meteroritos son infinitos y si se destruye uno se crea otro su movieminto varia y pueden caer en difrentes direcciones
    """
    # Manejo de rutas de archivos
    image_path = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\enemigos\meterorito  2.jpg"
    original_image = pygame.image.load(image_path)

    # Rotar la imagen en 90 grados
    rotated_image = pygame.transform.rotate(original_image, 90)

    def __init__(self, ancho_screen, largo_screen):
        super().__init__()
        # Escalar la imagen al tamaño deseado
        self.image = pygame.transform.scale(self.rotated_image, (60, 40))
        self.image.set_colorkey((0, 0, 0))
        self.ancho_screen = ancho_screen
        self.largo_screen = largo_screen
        # Posicionamiento del enemigo
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randrange(ancho_screen - self.rect.height)

        self.velocidad_y = random.randint(1, 2)
        self.velocidad_x = random.randint(-1, 2)
        self.vidas = 2
        self.puntos = 0


    def update(self) -> None:
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x

        if self.rect.left < 0:
            self.rect.x = random.randint(200,600)
            self.rect.y = 0 
        if  self.rect.right > self.ancho_screen:
            self.rect.x = random.randint(200,600)
            self.rect.y = 0 
        if self.rect.top < 0:
            self.velocidad_y += 1

        if self.rect.bottom > self.largo_screen:
            self.rect.x = random.randint(200,600)
            self.rect.y = 0 

        if self.vidas <= 0:
            self.kill()


class Enemigo_boss(pygame.sprite.Sprite):
    # Manejo de rutas de archivos
    image_path = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\enemigos\nave_madre.png"
    original_image = pygame.image.load(image_path)
    rotated_image = pygame.transform.rotate(original_image, -90)
    
    def __init__(self,ancho_screen,largo_screen,grupo_disparo):
        super().__init__()
        self.ancho_screen = ancho_screen
        self.largo_screen = largo_screen
        # Escalar la imagen al tamaño deseado
        self.grupo_disparo = grupo_disparo
        self.image = pygame.transform.scale(self.rotated_image, (150, 200))
        self.image.set_colorkey((0, 0, 0))
        # Posicionamiento del enemigo
        self.rect = self.image.get_rect()
        self.rect.y = 0 #random.randrange((largo_screen-self.rect.width)//4) 
        self.rect.x = random.randrange(ancho_screen-self.rect.height)
        self.velocidad_y = 0 #random.randint(1, 2)
        self.velocidad_x = 1
        self.vidas = 25
        self.start_time = time.time()

    def disparo(self):  # centro
        bala = Disparo(self.rect.left + 12, self.rect.centery + 5, "positivo", imagen_de_disparo_gigante, (30, 40))
        self.grupo_disparo.add(bala)

    def disparo2(self):  # centro
        bala = Disparo(self.rect.right - 12, self.rect.centery + 5, "positivo", imagen_de_disparo_gigante, (30, 40))
        self.grupo_disparo.add(bala)
    
    def update(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x

        if self.rect.left < 0:
            self.velocidad_x += 1

        if  self.rect.right > self.ancho_screen:
            self.velocidad_x -= 1

        if self.vidas <= 0:
            self.kill()

        if elapsed_time >= 3:
            self.disparo()
            reproducir_sonido(sonido_disparo_mi_nave,ajustes_de_volumen())
            self.start_time = current_time


