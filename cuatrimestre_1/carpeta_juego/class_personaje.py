import pygame
from funciones import *
from class_enemigos import *
from musica import *
from class_disparo import *

class Personaje():
    def __init__(self, animaciones, pos_x, pos_y, tamaño: tuple, velocidad, que_hace, grupo_disparo):
        
        self.grupo_disparo = grupo_disparo
        self.animaciones = animaciones
        rescalar_imagenes(self.animaciones, tamaño)
        self.rect = pygame.Rect(pos_x, pos_y, *tamaño)
        self.rectangulo_x = pos_x
        self.rectangulo_y = pos_y
        self.velocidad = velocidad
        self.que_hace = que_hace
        self.contador_de_pasos = 0
        self.animacione_actuales = self.animaciones[self.que_hace]
        self.vidas = 3
        self.puntos = 0
        self.espacio_presionado = False

    def desplazar(self):
        velocidad_actual_x = 0
        velocidad_actual_y = 0
        if self.que_hace == "izquierda":
            velocidad_actual_x = -self.velocidad
        elif self.que_hace == "derecha":
            velocidad_actual_x = self.velocidad
        elif self.que_hace == "arriba":
            velocidad_actual_y = -self.velocidad
        elif self.que_hace == "abajo":
            velocidad_actual_y = self.velocidad
        self.rect.x += velocidad_actual_x
        self.rect.y += velocidad_actual_y

            
    # disparos de la bala
    def disparo(self):#centro
        bala = Disparo(self.rect.centerx-2, self.rect.top+50, "negativo",imagen_de_disparo,(20,20))
        self.grupo_disparo.add(bala)
    def disparo2(self):#derecha
        bala = Disparo(self.rect.centerx+7, self.rect.top+50, "negativo",imagen_de_disparo,(20,20))
        self.grupo_disparo.add(bala)
    def disparo3(self):#izquierda
        bala = Disparo(self.rect.centerx-10, self.rect.top+50, "negativo",imagen_de_disparo,(20,20))
        self.grupo_disparo.add(bala)
    

    def animacion(self, pantalla):
        largo = len(self.animacione_actuales)
        if self.contador_de_pasos >= largo:
            self.contador_de_pasos = 0
        pantalla.blit(self.animacione_actuales[self.contador_de_pasos], self.rect)
        self.contador_de_pasos += 1
        

    def moverse(self, pantalla_alto, pantalla_ancho):
        teclas_presionadas = pygame.key.get_pressed()
        espacio = False
        if teclas_presionadas[pygame.K_RIGHT] and self.rect.right < pantalla_ancho:
            self.que_hace = "derecha"
        elif teclas_presionadas[pygame.K_LEFT] and self.rect.left > 0:
            self.que_hace = "izquierda"
        elif teclas_presionadas[pygame.K_DOWN] and self.rect.bottom < pantalla_alto:
            self.que_hace = "abajo"
        elif teclas_presionadas[pygame.K_UP] and self.rect.top > 0:
            self.que_hace = "arriba"
        else:
            self.que_hace = "quieto"
        


        espacio = teclas_presionadas[pygame.K_SPACE]
        if espacio and not self.espacio_presionado:
            
            self.espacio_presionado = True
            if self.puntos <= 400:
                self.disparo()
                reproducir_sonido(sonido_disparo_mi_nave,ajustes_de_volumen())
            # sonidos['sonido_disparo_personaje'].play()
            if self.puntos > 400:
                self.disparo2()
                reproducir_sonido(sonido_disparo_mi_nave,ajustes_de_volumen())

            if self.puntos > 800:
                self.disparo3()
        elif not espacio:
            self.espacio_presionado = False

    def actualizar(self, pantalla):
        self.animacione_actuales = self.animaciones.get(self.que_hace, [])
        self.animacion(pantalla)
        self.desplazar()




# colisiones enemigos 
    def colisiones_nave_normal(self, sprite_meteorito, vida):
        """
        COLISION DE ALGUN SPRITE CONTRA LA NAVE
        sprite_meteorito: Lista de sprites que se desea analizar para detectar colisiones con la nave.
        vida: La cantidad de vidas que queremos que se le descuente a nuestra nave al colisionar.
        """
        colisiones_meteorito = pygame.sprite.spritecollide(self, sprite_meteorito, False)

        for enemigo in colisiones_meteorito:
            # Colisión detectada, toma las acciones necesarias
            sprite_meteorito.remove(enemigo)
            self.vidas -= vida
            reproducir_sonido(sonido_choque,ajustes_de_volumen())
            if self.puntos >= 100: 
                self.puntos -= 100

    def colision_disparos(self,sprite_nave_enemigo, nivel_mis_disparos):
        """
        
        """
        colisiones = pygame.sprite.groupcollide(sprite_nave_enemigo, nivel_mis_disparos, False,  True)
        for nave_enemiga, disparo in colisiones.items():
            nave_enemiga.vidas -= 1
            if nave_enemiga.vidas <= 0:
                self.puntos += 100
                print("colisiono")
                # sonidos['sonido_personaje'].play()

        