import pygame


imagen_de_disparo =  r"C:\Users\matia\OneDrive\Escritorio\UTN\Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\nave\disparo.png"
imagen_de_disparo_gigante = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\enemigos\disparo_madre.png"

class Disparo(pygame.sprite.Sprite):
    def __init__(self, x, y,positivo_negativo,imagen,tamaño:tuple):
        """
        el tamaño de mi bala normal es de (20,20)
        """
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(imagen).convert(), tamaño)
        self.image.set_colorkey((0, 0, 0))

        # Posicionamiento del disparo
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.signo = positivo_negativo.lower()

    def update(self):
        #velocidad de la vala y detruccion de sprite de la bala
        if self.signo == "positivo":
            self.rect.y += 5
            if self.rect.bottom < 0:
                self.kill()
        elif self.signo == "negativo":
            self.rect.y -= 5
            if self.rect.bottom < 0:
                self.kill()
        else:
            print("a ocurrido un error de tipeo asegurese de escribir una de las 2 opciones ") 
