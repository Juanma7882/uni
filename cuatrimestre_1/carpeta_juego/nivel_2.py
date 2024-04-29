import pygame
from funciones import *
from ajustes_generales import *
from class_enemigos import *

class Nivel2:
    def __init__(self):
        self.ancho_screen = 984
        self.largo_screen = 630
        self.fondo_nivel = r"cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\nivel2.png"
        self.nivel = Nivel(self.ancho_screen, self.largo_screen, 60, 35, self.fondo_nivel,1)
        self.sprite_nave_enemigo = pygame.sprite.Group()
        self.sprite_nave_enemigo_disparo = pygame.sprite.Group()
        self.sprite_meteorito = pygame.sprite.Group()
        self.cantidad_de_naves = 3
        self.cantidad_meteoritos = 10
        self.inicializar_nivel()

    def inicializar_nivel(self):
        mostrar_texto("nivel 2 ", self.ancho_screen // 2 -10, self.largo_screen // 2, 3000,self.fondo_nivel,self.ancho_screen,self.largo_screen)

        for i in range(self.cantidad_de_naves):
            nave_enemiga = Enemigo(self.ancho_screen, self.largo_screen, self.sprite_nave_enemigo_disparo)
            self.sprite_nave_enemigo.add(nave_enemiga)

        for i in range(self.cantidad_meteoritos):
            meti = Meterorito(self.ancho_screen, self.largo_screen)
            self.sprite_meteorito.add(meti)

    def ejecutar_nivel(self):
        musica_de_fondo(segundo_nivel_musica,ajustes_de_volumen()) 
        run = True
        while run:

            self.nivel.ejecutar()

            self.sprite_meteorito.update()
            self.sprite_meteorito.draw(self.nivel.screen)

            self.sprite_nave_enemigo.update()
            self.sprite_nave_enemigo.draw(self.nivel.screen)

            self.nivel.mis_disparos.update()
            self.nivel.mis_disparos.draw(self.nivel.screen)

            self.sprite_nave_enemigo_disparo.update()
            self.sprite_nave_enemigo_disparo.draw(self.nivel.screen)

            self.nivel.nave.colision_disparos(self.sprite_meteorito, self.nivel.mis_disparos)
            self.nivel.nave.colisiones_nave_normal(self.sprite_meteorito, 1)

            cantidad_de_meteoritos = len(self.sprite_meteorito)
            if cantidad_de_meteoritos < self.cantidad_meteoritos:
                meti = Meterorito(self.ancho_screen, self.largo_screen)
                self.sprite_meteorito.add(meti)

            self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo, 1)
            self.nivel.nave.colision_disparos(self.sprite_nave_enemigo, self.nivel.mis_disparos)
            self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo_disparo, 1)

            if self.nivel.nave.puntos > self.nivel.puntos or self.nivel.nave.puntos < self.nivel.puntos:
                self.nivel.puntos = self.nivel.nave.puntos

            self.nivel.nave.moverse(self.largo_screen, self.ancho_screen)
            self.nivel.nave.actualizar(self.nivel.screen)

            self.nivel.ejecusion_final()

            if self.nivel.nave.vidas <= 0:
                run = False #pierde
                parar_musica(3)
                return -1
            elif self.nivel.nave.vidas > 0 and self.nivel.controlador_tiempo() <= 0:
                parar_musica(3)
                run = False #gana
                return 2
            if self.nivel.interfas != -2:
                print(self.nivel.interfas)
                parar_musica(3)
                return self.nivel.interfas

            pygame.display.update()
    def puntos(self):
        puntos =  self.nivel.nave.puntos
        return puntos 

# nivel_2 = Nivel2()
# nivel_2.ejecutar_nivel()
