import pygame
pygame.init()
pygame.mixer.init()
from ajustes_generales import leer_json




pantalla_de_inicio_musica = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\inicio_juego.mp3"
primer_nivel_musica = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\Y2meta.app - Musica espacial. Galaxias. Relaxing music. Musica relajante. (128 kbps).mp3"
segundo_nivel_musica = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\among us .mp3"
tercer_nivel_musica = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\megalovania.mp3"


sonido_disparo = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\conido disparo.mp3"
sonido_choque = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\golpe_de_mi_nave.mp3"
sonido_disparo_mi_nave =r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\disparo_mi_nave.wav"
sonido_tanque = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\tanque_disparo.mp3"



# for i in leer_json(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\volumen.json"):
#     musica_volumen = float(i["volumen"])
#     print(musica_volumen)


def musica_de_fondo(ruta_musica,volumen):
        
    pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.play(-1)  # El argumento -1 hace que la música se repita indefinidamente
    pygame.mixer.music.set_volume(volumen)  # Establecer el volumen (0.0 - 1.0)


def parar_musica(opcion):
    """
    opcion_pausa   = pygame.mixer.music.pause() 
    opcion_reanudar   = pygame.mixer.music.unpause()  
    opcion_parar =  pygame.mixer.music.stop() 
    """
    if opcion == 1:
        e   = pygame.mixer.music.pause()  # Pausar la música
    if opcion == 2:
        e   = pygame.mixer.music.unpause()  # Reanudar la música
    if opcion == 3:
        e  = pygame.mixer.music.stop()  # Detener la música
    return e


def reproducir_sonido(ruta_sonido,volumen):
    sonido = pygame.mixer.Sound(ruta_sonido)
    sonido.set_volume(volumen)
    sonido.play()

# # Ejemplo de uso
# reproducir_sonido(r'ruta_del_sonido.wav', 0.8)

# sonidos = {
#     'sonido_colision_personaje': pygame.mixer.Sound(r'Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\golpe_de_mi_nave.mp3'),
#     "sonido_disparo_personaje":  pygame.mixer.Sound(r'Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\disparo_mi_nave.wav'),
#     "sonido_de_roca" : pygame.mixer.Sound(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\roca.mp3")
    
#     # Agrega más sonidos 
# }

# # Cargar un archivo de sonido
# sonido = pygame.mixer.Sound(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\conido disparo.mp3")
# sonido.set_volume(0.5)
# pygame.mixer.music.load("tu_musica.mp3")
# pygame.mixer.music.play(loops=-1)
# pygame.mixer.quit()
# pygame.quit()
