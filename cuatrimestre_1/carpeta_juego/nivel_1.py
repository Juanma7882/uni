import pygame
from funciones import *
from ajustes_generales import *
from class_disparo import *
from class_enemigos import *

class Nivel1:
    def __init__(self):
        self.ancho_screen = 984
        self.largo_screen = 640
        
        self.fondo_nivel = r"cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\nivel1.jpg"
        self.nivel = Nivel(self.ancho_screen, self.largo_screen, 60, 45, self.fondo_nivel,0)
        self.sprite_nave_enemigo = pygame.sprite.Group()
        self.cantidad_enemigos = 12
        self.sprite_meteorito = pygame.sprite.Group()
    
    def ejecutar_nivel(self):
        musica_volumen = ajustes_de_volumen()

        musica_de_fondo(primer_nivel_musica,musica_volumen)

        # mostrar_texto("sobrevive", self.ancho_screen // 2 -30, self.largo_screen // 2, 3000,self.fondo_nivel,self.ancho_screen,self.largo_screen)
        # mostrar_texto("los 3 niveles", self.ancho_screen // 2 -30, self.largo_screen // 2, 3000,self.fondo_nivel,self.ancho_screen,self.largo_screen)
        # mostrar_texto("hasta que el tiempo se agote", self.ancho_screen // 2 -30, self.largo_screen // 2, 3000,self.fondo_nivel,self.ancho_screen,self.largo_screen)
        # mostrar_texto("evita perder las 3 vidas", self.ancho_screen // 2 -30, self.largo_screen // 2, 3000,self.fondo_nivel,self.ancho_screen,self.largo_screen)
        # mostrar_texto("nivel 1 ", self.ancho_screen // 2 -10, self.largo_screen // 2, 3000,self.fondo_nivel,self.ancho_screen,self.largo_screen)
        
        for i in range(self.cantidad_enemigos):
            meti = Meterorito(self.ancho_screen, self.largo_screen)
            self.sprite_meteorito.add(meti)

        run = True
        while run:
            self.nivel.ejecutar()
        
            self.sprite_meteorito.update()
            self.sprite_meteorito.draw(self.nivel.screen)

            self.nivel.mis_disparos.update()
            self.nivel.mis_disparos.draw(self.nivel.screen)

            self.nivel.nave.colision_disparos(self.sprite_meteorito, self.nivel.mis_disparos)
            self.nivel.nave.colisiones_nave_normal(self.sprite_meteorito, 1)

            cantidad_de_meteoritos = len(self.sprite_meteorito)
            if cantidad_de_meteoritos < self.cantidad_enemigos:
                meti = Meterorito(self.ancho_screen, self.largo_screen)
                self.sprite_meteorito.add(meti)

            if self.nivel.nave.puntos > self.nivel.puntos or self.nivel.nave.puntos < self.nivel.puntos:
                self.nivel.puntos = self.nivel.nave.puntos

            self.nivel.nave.moverse(self.largo_screen, self.ancho_screen)
            self.nivel.nave.actualizar(self.nivel.screen)
            self.nivel.ejecusion_final()

            if self.nivel.nave.vidas <= 0 or self.nivel.teclas == "escape":
                run = False #pierde
                return -1

            elif self.nivel.nave.vidas > 0 and self.nivel.controlador_tiempo() <= 0:
                parar_musica(3)
                self.bandera = True #gana
                return 1
            if self.nivel.interfas != -2:
                parar_musica(3)
                print(self.nivel.interfas)
                return self.nivel.interfas
            pygame.display.update()

    def puntos(self):
        puntos =  self.nivel.nave.puntos
        return puntos 


# nivel_1 = Nivel1()
# nivel_1.ejecutar_nivel() 