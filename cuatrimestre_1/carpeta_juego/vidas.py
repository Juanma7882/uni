import pygame

class Vidas(pygame.sprite.Sprite):
    # Manejo las rutas de archivos
    image_path = r"Curso_de_ingreso_PYTHON-main/ejercicios/cuatrimestre_1/carpeta_juego/imagenes/objetos/vida.png"
    original_image = pygame.image.load(image_path)
    
    def __init__(self, x, y):
        super().__init__()

        # Escalar la imagen al tamaño deseado
        self.image = pygame.transform.scale(self.original_image, (30, 30))
        self.image.set_colorkey((0, 0, 0))

        # Posicionamiento del enemigo
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

