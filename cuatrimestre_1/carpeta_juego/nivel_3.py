import pygame
from funciones import *
from ajustes_generales import *
from class_enemigos import *

class Nivel3:
    def __init__(self):
        self.ancho_screen = 984
        self.largo_screen = 630
        self.fondo_nivel = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\nivel3.jpg"
        self.nivel = Nivel(self.ancho_screen, self.largo_screen, 60, 45, self.fondo_nivel,2)
        self.sprite_nave_enemigo = pygame.sprite.Group()
        self.sprite_nave_enemigo_disparo = pygame.sprite.Group()
        self.sprite_meteorito = pygame.sprite.Group()
        self.sprite_boss = pygame.sprite.Group()
        self.sprite_boss_disparo = pygame.sprite.Group()

        self.cantidad_de_naves = 3
        self.cantidad_meteoritos = 7

        self.inicializar_nivel()
    
    def inicializar_nivel(self):
        mostrar_texto("nivel 3 ", self.ancho_screen // 2 -10, self.largo_screen // 2, 3000,self.fondo_nivel,self.ancho_screen,self.largo_screen)

        for i in range(self.cantidad_de_naves):
            nave_enemiga = Enemigo(self.ancho_screen, self.largo_screen, self.sprite_nave_enemigo_disparo)
            self.sprite_nave_enemigo.add(nave_enemiga)

        for i in range(self.cantidad_meteoritos):
            meti = meterorito(self.ancho_screen, self.largo_screen)
            self.sprite_meteorito.add(meti)

        boss = Enemigo_boss(self.ancho_screen, self.largo_screen, self.sprite_boss_disparo)
        self.sprite_boss.add(boss)


    def ejecutar_nivel(self):
        musica_de_fondo(segundo_nivel_musica,ajustes_de_volumen()) 

        # puntos_meteorito = 0
        run = True
        while run:
            self.nivel.ejecutar()

            self.sprite_nave_enemigo.update()
            self.sprite_nave_enemigo.draw(self.nivel.screen)

            self.sprite_nave_enemigo_disparo.update()
            self.sprite_nave_enemigo_disparo.draw(self.nivel.screen)

            self.nivel.mis_disparos.update()
            self.nivel.mis_disparos.draw(self.nivel.screen)

            self.sprite_boss_disparo.update()
            self.sprite_boss_disparo.draw(self.nivel.screen)

            self.sprite_boss.update()
            self.sprite_boss.draw(self.nivel.screen)

            self.sprite_meteorito.update()
            self.sprite_meteorito.draw(self.nivel.screen)

            self.nivel.nave.colision_disparos(self.sprite_boss, self.nivel.mis_disparos)
            self.nivel.nave.colisiones_nave_normal(self.sprite_boss_disparo, 2)

            self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo, 1)
            self.nivel.nave.colision_disparos(self.sprite_nave_enemigo, self.nivel.mis_disparos)
            self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo_disparo, 1)

            self.nivel.nave.colision_disparos(self.sprite_meteorito, self.nivel.mis_disparos)
            self.nivel.nave.colisiones_nave_normal(self.sprite_meteorito, 1)

            cantidad_de_meteoritos = len(self.sprite_meteorito)
            if cantidad_de_meteoritos < self.cantidad_meteoritos:
                meti = meterorito(self.ancho_screen, self.largo_screen)
                self.sprite_meteorito.add(meti)

            if self.nivel.nave.puntos > self.nivel.puntos or self.nivel.nave.puntos < self.nivel.puntos:
                self.nivel.puntos = self.nivel.nave.puntos

            self.nivel.nave.moverse(self.largo_screen, self.ancho_screen)
            self.nivel.nave.actualizar(self.nivel.screen)

            self.nivel.ejecusion_final()
        
            if self.nivel.nave.vidas <= 0:
                run = False #pierde
                return -1

            elif self.nivel.nave.vidas > 0 and self.nivel.controlador_tiempo() <= 0:
                parar_musica(3)
                self.bandera = True #gana

                return 3
            if self.nivel.interfas != -2:
                parar_musica(3)
                print(self.nivel.interfas)
                return self.nivel.interfas

            pygame.display.update()
    def puntos(self):
        puntos =  self.nivel.nave.puntos
        return puntos             

# nivel_3 = Nivel3()
# nivel_3.ejecutar_nivel()

