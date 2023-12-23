# # import pygame
# # import sys

# # # Inicializar Pygame
# # pygame.init()

# # # Definir colores
# # blanco = (255, 255, 255)
# # negro = (0, 0, 0)

# # # Configurar la pantalla
# # ancho = 400
# # alto = 300
# # pantalla = pygame.display.set_mode((ancho, alto))
# # pygame.display.set_caption("Cuadrado con Texto")

# # # Configurar el reloj
# # reloj = pygame.time.Clock()

# # # Función para dibujar el cuadrado con texto
# # # def dibujar_cuadrado_con_texto(x, y, lado, texto):
# # #     pygame.draw.rect(pantalla, blanco, (x, y, lado, lado))
    
# # #     fuente = pygame.font.Font(None, 36)
# # #     texto_surface = fuente.render(texto, True, negro)
    
# # #     # Centrar el texto dentro del cuadrado
# # #     text_rect = texto_surface.get_rect(center=(x + lado // 2, y + lado // 2))
    
# # #     pantalla.blit(texto_surface, text_rect)

# # # Bucle principal
# # caligrafia = pygame.font.SysFont("calibri", 30)
# # while True:
# #     for evento in pygame.event.get():
# #         if evento.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()

# #     # Limpiar la pantalla
# #     pantalla.fill(negro)

# #     # Dibujar el cuadrado con texto
# #     x_cuadrado = 50
# #     y_cuadrado = 50
# #     lado_cuadrado = 200
# #     texto_cuadrado = "Hol"

# #     pygame.draw.rect(pantalla, blanco, (100, 100, 50, 50),0)
# #     texto = caligrafia.render("aceptar", True,220,220,220)
# #     pantalla.blit(texto,(10,10))
# #     pygame.display.flip

# #     # dibujar_cuadrado_con_texto(x_cuadrado, y_cuadrado, lado_cuadrado, texto_cuadrado)

# #     # Actualizar la pantalla
# #     pygame.display.flip()

# #     # Establecer la velocidad de fotogramas
# #     reloj.tick(30)



# # import pygame
# # import sys

# # # Inicializar Pygame
# # pygame.init()

# # # Configurar la pantalla
# # ancho = 400
# # alto = 300
# # pantalla = pygame.display.set_mode((ancho, alto))
# # pygame.display.set_caption("Cuadrado con Texto")

# # # Configurar colores
# # blanco = (255, 255, 255)
# # negro = (0, 0, 0)
# # nose = (50,50,50)

# # # Crear un objeto de fuente
# # caligrafia = pygame.font.SysFont("calibri", 30)

# # # Configurar el reloj
# # reloj = pygame.time.Clock()

# # # Bucle principal
# # while True:
# #     for evento in pygame.event.get():
# #         if evento.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()

# #     # Limpiar la pantalla

# #     # Dibujar el cuadrado
# #     x_cuadrado = 100
# #     y_cuadrado = 100
# #     lado_cuadrado = 50
# #     pygame.draw.rect(pantalla, blanco, (x_cuadrado, y_cuadrado, lado_cuadrado, lado_cuadrado))

# #     # Renderizar y dibujar el texto
# #     texto_cuadrado = "Aceptar"
# #     texto_surface = caligrafia.render(texto_cuadrado, True, nose)
# #     pantalla.blit(texto_surface, (x_cuadrado + 10, y_cuadrado + 10))

# #     # Actualizar la pantalla
# #     pygame.display.flip()

# #     pantalla.fill(negro)
# #     # Establecer la velocidad de fotogramas
# #     reloj.tick(30)



# # import pygame
# # import sys

# # Inicializar Pygame
# # pygame.init()

# # Configurar la pantalla
# # ancho = 400
# # alto = 300
# # pantalla = pygame.display.set_mode((ancho, alto))
# # pygame.display.set_caption("Cuadrado con Texto Dinámico")

# # Configurar colores
# # blanco = (255, 255, 255)
# # negro = (0, 0, 0)

# # Configurar el reloj
# # reloj = pygame.time.Clock()

# # def dibujar_cuadrado_con_texto(fondo, x, y, ancho_cuadrado, largo, ancho_del_cuadrado, color_del_cuadrado, texto, tipografia, tamaño_tipografia, color):
# #     pygame.draw.rect(fondo, color_del_cuadrado, (x, y, ancho_cuadrado, largo), ancho_del_cuadrado)

# #     fuente = pygame.font.Font(tipografia, tamaño_tipografia)
# #     texto_surface = fuente.render(texto, True, color)

# #     Centrar el texto dentro del cuadrado
# #     text_rect = texto_surface.get_rect(center=(x + ancho_cuadrado // 2, y + largo // 2))

# #     fondo.blit(texto_surface, text_rect)

# # Bucle principal
# # texto_ingresado = ""
# # while True:
# #     for evento in pygame.event.get():
# #         if evento.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()
# #         elif evento.type == pygame.KEYDOWN:
# #             if evento.key == pygame.K_BACKSPACE:
# #                 texto_ingresado = texto_ingresado[:-1]
# #             elif evento.key == pygame.K_RETURN:
# #                 Puedes manejar el evento de retorno si lo necesitas
# #                 pass
# #             else:
# #                 texto_ingresado += evento.unicode

# #     Limpiar la pantalla
# #     pantalla.fill(negro)

# #     Dibujar el cuadrado con texto usando la función
# #     dibujar_cuadrado_con_texto(pantalla, 50, 50, 200, 100, 0, (75,82,101), texto_ingresado, None, 30, blanco)

# #     Actualizar la pantalla
# #     pygame.display.flip()

# #     Establecer la velocidad de fotogramas
# #     reloj.tick(30)
# # import pygame
# # import re

# # pygame.init()

# # ancho_screen = 984
# # largo_screen = 650
# # screen = pygame.display.set_mode((ancho_screen, largo_screen))
# # pygame.display.set_caption("Mi Juego")

# # Carga la imagen del fondo
# # fondo = pygame.image.load(r"ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\iniciomod.png")
# # ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\iniciomod.png
# # Escala la imagen para que coincida con las dimensiones de la ventana
# # fondo = pygame.transform.scale(fondo, (ancho_screen, largo_screen))


# # nave = pygame.image.load("Curso_de_ingreso_PYTHON-main/ejercicios/cuatrimestre_1/carpeta_juego/imagenes/neon plus ps.png")
# # # Escala la imagen a un tamaño más pequeño
# # nave = pygame.transform.scale(nave, (200, 90))  #

# # nombre_x_y = 850,200 
# # running = True
# # clock = pygame.time.Clock()



# # Fuentes/font_title
# # fuente_titulo = "ejercicios/cuatrimestre_1/carpeta_juego/fuentes/4/airstrikehalf.ttf"
# # fuente = pygame.font.Font(fuente_titulo, 60)  #titulo
# # texto = "  space INVADERS"#invaders


# # Ruta a tu archivo de fuente (.ttf o .otf)
# # font_path = "ejercicios/cuatrimestre_1/carpeta_juego/fuentes/5/DS-DIGI.TTF"
# # Configurar la fuente del texto ingresado
# # fuente_nombre = pygame.font.Font(font_path,35) #texto ingreasado
# # texto2 =  "SPACE invaders!"
# # nombre_del_jugador = ""


# # def dibujar_cuadrado_con_texto(fondo,x, y,ancho_cuadrado,largo,ancho_del_cuadrado,color_del_cuadrado, texto,tipografia,tamaño_tipografia,color):
# #     pygame.draw.rect(fondo, color_del_cuadrado, (x, y,ancho_cuadrado,largo ),ancho_del_cuadrado)
    
# #     fuente = pygame.font.Font(tipografia, tamaño_tipografia)
# #     texto_surface = fuente.render(texto, True, color )
    
# #     # Centrar el texto dentro del cuadrado
# #     text_rect = texto_surface.get_rect(center=(x + ancho_cuadrado // 2, y + largo // 2))
    
# #     fondo.blit(texto_surface, text_rect)

# # def dibujar_cuadrado_con_texto(fondo, x, y, ancho_cuadrado, largo, ancho_del_cuadrado, color_del_cuadrado, texto, tipografia, tamaño_tipografia, color):
# #     pygame.draw.rect(fondo, color_del_cuadrado, (x, y, ancho_cuadrado, largo), ancho_del_cuadrado)

# #     fuente = pygame.font.Font(tipografia, tamaño_tipografia)
# #     texto_surface = fuente.render(texto, True, color)

# #     Centrar el texto dentro del cuadrado
# #     text_rect = texto_surface.get_rect(center=(x + ancho_cuadrado // 2, y + largo // 2))

# #     fondo.blit(texto_surface, text_rect)

# # while running:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
# #         elif event.type == pygame.KEYDOWN:
# #             Verifica si se presionó una tecla
# #             key_name = pygame.key.name(event.key)
# #             print(f"Tecla presionada: {key_name}")
# #             if key_name == "backspace":
# #                 nombre_del_jugador = nombre_del_jugador[:-1]
# #             elif key_name == "space":
# #                 nombre_del_jugador += " "
# #             else:
# #                 nombre_del_jugador += key_name 
            
# #         elif event.type == pygame.MOUSEBUTTONDOWN:
# #             Verifica si se hizo clic en el mouse
# #             button_name = pygame.mouse.get_pressed()
# #             print(f"Botón del mouse presionado: {button_name}")
# #     Dibuja el fondo en la screen
# #     screen.blit(fondo, (0, 0))
    

# #     centro_x = (ancho_screen - nave.get_width()) // 2
# #     centro_y = (largo_screen - nave.get_height()) // 3.2
    
# #     centro_x = (ancho_screen )//2

# #     titulo_del_inicio = fuente.render(texto, True, ("purple"))  # Color del texto (purple)
# #     rectangulo_texto = titulo_del_inicio.get_rect()
# #     ancho_texto = (rectangulo_texto.width)//2
# #     alto_texto = (rectangulo_texto.height)//2

# #     dibujar_cuadrado_con_texto(screen,((ancho_screen//2)-100),200,200,45,4,(117, 233, 236),nombre_del_jugador,font_path,35,"purple")
    
# #     screen.blit(titulo_del_inicio, (((ancho_screen//2)-ancho_texto), (largo_screen//5.4167))) 


# #     nombre_introducido = fuente_nombre.render(nombre_del_jugador, True, ("purple"))  # Color del texto (purple)
    
# #     screen.blit(nombre_introducido, (((ancho_screen//2)+100),(200-nombre_introducido.get_height())))


# #     Dibuja la superficie del texto en la screen
# #     Renderiza el resto de elementos del juego
# #     ...
# #     pygame.draw.line(fondo, "red", (50, 50), (200, 500), 5)
# #     pygame.draw.rect(fondo,(117, 233, 236), (((ancho_screen//2)-100),500,200,55), 5)

# #     pygame.display.flip()
# #     clock.tick(60)

# # pygame.quit()



# # texto = ""
# # def validacion_de_menu(respuesta:str):
# #     """
# #     valida lo que se puede ingresar en el menu
# #     devuelve:
# #     * -1 si es invalida
# #     * devuelve el str si es valido 
# #     """
# #     validacion = r'[0-9A-Za-z]{1,5}$'
# #     #^(?=(?:[a-zA-Z]*[0-9]*){11}$)[a-zA-Z0-9]{11}$
# #     if re.match(validacion,respuesta):
# #         mensaje = respuesta
# #     else :
# #         mensaje = -1 
# #     return mensaje

# # print(validacion_de_menu(texto))

# # import pygame
# # import re

# # pygame.init()

# # ancho_screen = 984
# # largo_screen = 650
# # screen = pygame.display.set_mode((ancho_screen, largo_screen))
# # pygame.display.set_caption("Mi Juego")

# # Carga la imagen del fondo
# # fondo = pygame.image.load(r"ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\iniciomod.png")
# # ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\iniciomod.png
# # Escala la imagen para que coincida con las dimensiones de la ventana
# # fondo = pygame.transform.scale(fondo, (ancho_screen, largo_screen))


# # nave = pygame.image.load("Curso_de_ingreso_PYTHON-main/ejercicios/cuatrimestre_1/carpeta_juego/imagenes/neon plus ps.png")
# # # Escala la imagen a un tamaño más pequeño
# # nave = pygame.transform.scale(nave, (200, 90))  #

# # nombre_x_y = 850,200 
# # running = True
# # clock = pygame.time.Clock()



# # Fuentes/font_title
# # fuente_titulo = "ejercicios/cuatrimestre_1/carpeta_juego/fuentes/4/airstrikehalf.ttf"
# # fuente = pygame.font.Font(fuente_titulo, 60)  #titulo
# # texto = " space INVADERS"#invaders


# # Ruta a tu archivo de fuente (.ttf o .otf)
# # font_path = "ejercicios/cuatrimestre_1/carpeta_juego/fuentes/5/DS-DIGI.TTF"
# # Configurar la fuente del texto ingresado
# # fuente_nombre = pygame.font.Font(font_path,35) #texto ingreasado
# # texto2 =  "SPACE invaders!"
# # nombre_del_jugador = ""


# # def dibujar_cuadrado_con_texto(fondo,x, y,ancho_cuadrado,largo,ancho_del_cuadrado,color_del_cuadrado, texto,tipografia,tamaño_tipografia,color):
# #     pygame.draw.rect(fondo, color_del_cuadrado, (x, y,ancho_cuadrado,largo ),ancho_del_cuadrado)
    
# #     fuente = pygame.font.Font(tipografia, tamaño_tipografia)
# #     texto_surface = fuente.render(texto, True, color )
    
# #     # Centrar el texto dentro del cuadrado
# #     text_rect = texto_surface.get_rect(center=(x + ancho_cuadrado // 2, y + largo // 2))
    
# #     fondo.blit(texto_surface, text_rect)

# # def dibujar_cuadrado_con_texto(fondo, x, y, ancho_cuadrado, largo, ancho_del_cuadrado, color_del_cuadrado, texto, tipografia, tamaño_tipografia, color):
# #     pygame.draw.rect(fondo, color_del_cuadrado, (x, y, ancho_cuadrado, largo), ancho_del_cuadrado)

# #     fuente = pygame.font.Font(tipografia, tamaño_tipografia)
# #     texto_surface = fuente.render(texto, True, color)

# #     Centrar el texto dentro del cuadrado
# #     text_rect = texto_surface.get_rect(center=(x + ancho_cuadrado // 2, y + largo // 2))

# #     fondo.blit(texto_surface, text_rect)

# # while running:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
# #         elif event.type == pygame.KEYDOWN:
# #             Verifica si se presionó una tecla
# #             key_name = pygame.key.name(event.key)
# #             print(f"Tecla presionada: {key_name}")
# #             if key_name == "backspace":
# #                 nombre_del_jugador = nombre_del_jugador[:-1]
# #             elif key_name == "space":
# #                 nombre_del_jugador += " "
# #             else:
# #                 nombre_del_jugador += key_name 
            
# #         elif event.type == pygame.MOUSEBUTTONDOWN:
# #             Verifica si se hizo clic en el mouse
# #             button_name = pygame.mouse.get_pressed()
# #             print(f"Botón del mouse presionado: {button_name}")
# #     Dibuja el fondo en la screen
# #     screen.blit(fondo, (0, 0))
    

# #     centro_x = (ancho_screen - nave.get_width()) // 2
# #     centro_y = (largo_screen - nave.get_height()) // 3.2
    
# #     centro_x = (ancho_screen )//2

# #     titulo_del_inicio = fuente.render(texto, True, ("purple"))  # Color del texto (purple)
# #     screen.blit(titulo_del_inicio, (((ancho_screen//2)-ancho_screen//3.51), (largo_screen//5.4167))) 

# #     rectangulo_texto = titulo_del_inicio.get_rect()
# #     ancho_texto = (rectangulo_texto.width)//2
# #     alto_texto = (rectangulo_texto.height)//2
# #     dibujar_cuadrado_con_texto(screen,((ancho_screen//2)-100),200,200,45,4,(117, 233, 236),nombre_del_jugador,font_path,35,"purple")
    


# #     pygame.display.flip()
# #     clock.tick(60)

# # pygame.quit()



# # texto = ""
# # def validacion_de_menu(respuesta:str):
# #     """
# #     valida lo que se puede ingresar en el menu
# #     devuelve:
# #     * -1 si es invalida
# #     * devuelve el str si es valido 
# #     """
# #     validacion = r'[0-9A-Za-z]{1,5}$'
# #     #^(?=(?:[a-zA-Z]*[0-9]*){11}$)[a-zA-Z0-9]{11}$
# #     if re.match(validacion,respuesta):
# #         mensaje = respuesta
# #     else :
# #         mensaje = -1 
# #     return mensaje

# # print(validacion_de_menu(texto))

# # import pygame
# # import sys

# # # Inicializar Pygame
# # pygame.init()

# # # Definir colores
# # NEGRO = (0, 0, 0)
# # BLANCO = (255, 255, 255)

# # # Definir el tamaño de la pantalla
# # ANCHO, ALTO = 800, 600
# # pantalla = pygame.display.set_mode((ANCHO, ALTO))
# # pygame.display.set_caption("Ejemplo de Botón en Pygame")

# # # Definir las propiedades del botón
# # rectangulo_boton = pygame.Rect(300, 200, 200, 100)
# # color_boton_normal = BLANCO
# # color_boton_resaltado = (88, 214, 141)

# # # Bucle principal
# # while True:
# #     for evento in pygame.event.get():
# #         if evento.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()

# #     # Obtener la posición del mouse
# #     pos_mouse = pygame.mouse.get_pos()

# #     # Comprobar si el mouse está sobre el botón
# #     if rectangulo_boton.collidepoint(pos_mouse):
# #         color_actual = color_boton_resaltado
# #         # Aquí puedes agregar lógica adicional cuando el mouse está sobre el botón

# #     else:
# #         color_actual = color_boton_normal

# #     # Dibujar el fondo y el botón
# #     pantalla.fill(NEGRO)
# #     pygame.draw.rect(pantalla, color_actual, rectangulo_boton)

# #     # Actualizar la pantalla
# #     pygame.display.flip()
# # import pygame
# # import sys

# # def dibujar_cuadrado_con_texto(fondo, x, y, ancho_cuadrado, largo, ancho_del_cuadrado, color_del_cuadrado, texto, tipografia, tamaño_tipografia, color):
# #     # Obtener la posición del mouse
# #     pos_mouse = pygame.mouse.get_pos()

# #     # Crear un rectángulo que representa el cuadrado
# #     rectangulo_cuadrado = pygame.Rect(x, y, ancho_cuadrado, largo)

# #     # Verificar si el mouse está sobre el cuadrado
# #     if rectangulo_cuadrado.collidepoint(pos_mouse):
# #         color_del_cuadrado = (200, 200, 200)  # Cambiar el color cuando el mouse está sobre el cuadrado
# #         # Aquí puedes agregar lógica adicional cuando el mouse está sobre el cuadrado

# #     # Dibujar el cuadrado
# #     pygame.draw.rect(fondo, color_del_cuadrado, (x, y, ancho_cuadrado, largo), ancho_del_cuadrado)

# #     # Crear el texto
# #     fuente = pygame.font.Font(tipografia, tamaño_tipografia)
# #     texto_surface = fuente.render(texto, True, color)

# #     # Centrar el texto dentro del cuadrado
# #     text_rect = texto_surface.get_rect(center=(x + ancho_cuadrado // 2, y + largo // 2))

# #     # Dibujar el texto
# #     fondo.blit(texto_surface, text_rect)

# # # Inicializar Pygame
# # pygame.init()

# # # Definir colores
# # NEGRO = (0, 0, 0)
# # BLANCO = (255, 255, 255)

# # # Definir el tamaño de la pantalla
# # ANCHO, ALTO = 800, 600
# # pantalla = pygame.display.set_mode((ANCHO, ALTO))
# # pygame.display.set_caption("Ejemplo de Botón con Texto en Pygame")

# # # Bucle principal
# # while True:
# #     for evento in pygame.event.get():
# #         if evento.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()
            

# #     # Llamar a la función para dibujar el cuadrado con texto
# #     dibujar_cuadrado_con_texto(pantalla, 300, 200, 200, 100, 0, BLANCO, "Haz clic", None, 36, NEGRO)

# #     # Actualizar la pantalla
# #     pygame.display.flip()







# # # /////////////////////////////////////////////////////////////////////////////////
# # import pygame
# # import sys
# # import random
# # # Inicializar Pygame
# # pygame.init()

# # # Definir colores
# # NEGRO = (0, 0, 0)
# # BLANCO = (255, 255, 255)

# # # Configuración de la pantalla
# # ANCHO = 800
# # ALTO = 600
# # pantalla = pygame.display.set_mode((ANCHO, ALTO))
# # pygame.display.set_caption("Ejemplo de Disparo")

# # # Clase de Disparo
# # class Disparo(pygame.sprite.Sprite):
# #     def __init__(self, x, y, velocidad, owner):
# #         super().__init__()
# #         self.image = pygame.Surface((10, 10))
# #         self.image.fill(BLANCO)
# #         self.rect = self.image.get_rect()
# #         self.rect.center = (x, y)
# #         self.velocidad = velocidad
# #         self.owner = owner

# #     def update(self):
# #         if self.owner == "jugador":
# #             self.rect.y -= self.velocidad
# #         elif self.owner == "enemigo":
# #             self.rect.y += self.velocidad

# # # Grupos de sprites
# # todos_los_sprites = pygame.sprite.Group()
# # jugador_disparos = pygame.sprite.Group()
# # enemigo_disparos = pygame.sprite.Group()

# # # Clase de Nave
# # class Nave(pygame.sprite.Sprite):
# #     def __init__(self, x, y):
# #         super().__init__()
# #         self.image = pygame.Surface((50, 50))
# #         self.image.fill(BLANCO)
# #         self.rect = self.image.get_rect()
# #         self.rect.center = (x, y)

# #     def disparar(self):
# #         if self == jugador_nave:
# #             disparo = Disparo(self.rect.centerx, self.rect.y, 5, "jugador")
# #             jugador_disparos.add(disparo)
# #             todos_los_sprites.add(disparo)
# #         elif self == enemigo_nave:
# #             disparo = Disparo(self.rect.centerx, self.rect.bottom, 5, "enemigo")
# #             enemigo_disparos.add(disparo)
# #             todos_los_sprites.add(disparo)

# # # Crear instancias de naves
# # jugador_nave = Nave(ANCHO // 2, ALTO - 50)
# # enemigo_nave = Nave(ANCHO // 2, 50)

# # todos_los_sprites.add(jugador_nave, enemigo_nave)

# # reloj = pygame.time.Clock()

# # # Bucle principal
# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()
# #         elif event.type == pygame.KEYDOWN:
# #             if event.key == pygame.K_SPACE:
# #                 jugador_nave.disparar()

# #     # Movimiento del enemigo
# #     enemigo_nave.rect.x += 5  # Ajusta la velocidad según sea necesario

# #     # Cambia la dirección cuando alcanza los bordes
# #     if enemigo_nave.rect.right > ANCHO or enemigo_nave.rect.left < 0:
# #         enemigo_nave.rect.x *= -1

# #     # Disparo del enemigo (puedes ajustar la frecuencia de disparo)
# #     if random.randint(0, 100) < 2:
# #         enemigo_nave.disparar()

# #     todos_los_sprites.update()

# #     # Lógica de colisiones (puedes agregar más lógica según sea necesario)
# #     colisiones_jugador = pygame.sprite.spritecollide(jugador_nave, enemigo_disparos, True)
# #     colisiones_enemigo = pygame.sprite.spritecollide(enemigo_nave, jugador_disparos, True)

# #     pantalla.fill(NEGRO)
# #     todos_los_sprites.draw(pantalla)

# #     pygame.display.flip()
# #     reloj.tick(60)
# # import pygame
# # import sys

# # # Inicializar Pygame
# # pygame.init()

# # # Configuración de la pantalla
# # ANCHO = 800
# # ALTO = 600
# # pantalla = pygame.display.set_mode((ANCHO, ALTO))
# # pygame.display.set_caption("Movimiento del Cuadrado")

# # # Colores
# # NEGRO = (0, 0, 0)
# # BLANCO = (255, 255, 255)

# # # Clase del Cuadrado
# # class Cuadrado(pygame.sprite.Sprite):
# #     def __init__(self, x, y, tamaño, velocidad):
# #         super().__init__()
# #         self.image = pygame.Surface(tamaño)
# #         self.image.fill(BLANCO)
# #         self.rect = self.image.get_rect()
# #         self.rect.topleft = (x, y)
# #         self.velocidad = velocidad

# #     def mover(self, direccion):
# #         if direccion == "izquierda" and self.rect.left > 0:
# #             self.rect.x -= self.velocidad
# #         elif direccion == "derecha" and self.rect.right < ANCHO:
# #             self.rect.x += self.velocidad
# #         elif direccion == "arriba" and self.rect.top > 0:
# #             self.rect.y -= self.velocidad
# #         elif direccion == "abajo" and self.rect.bottom < ALTO:
# #             self.rect.y += self.velocidad

# # # Crear un cuadrado
# # cuadrado = Cuadrado(ANCHO // 2, ALTO // 2, (50, 50), 5)

# # # Bucle principal
# # reloj = pygame.time.Clock()

# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()

# #     teclas_presionadas = pygame.key.get_pressed()

# #     if teclas_presionadas[pygame.K_LEFT]:
# #         cuadrado.mover("izquierda")
# #     elif teclas_presionadas[pygame.K_RIGHT]:
# #         cuadrado.mover("derecha")
# #     elif teclas_presionadas[pygame.K_UP]:
# #         cuadrado.mover("arriba")
# #     elif teclas_presionadas[pygame.K_DOWN]:
# #         cuadrado.mover("abajo")

# #     # Limpiar la pantalla
# #     pantalla.fill(NEGRO)

# #     # Dibujar el cuadrado en la nueva posición
# #     pantalla.blit(cuadrado.image, cuadrado.rect)

# #     # Actualizar la pantalla
# #     pygame.display.flip()

# #     # Controlar la velocidad de actualización
# # #     reloj.tick(60)

# # import pygame
# # import sys

# # # Inicializar Pygame
# # pygame.init()

# # # Configuración de la pantalla
# # ANCHO = 800
# # ALTO = 600
# # pantalla = pygame.display.set_mode((ANCHO, ALTO))
# # pygame.display.set_caption("Movimiento del Cuadrado con Disparo")

# # # Colores
# # NEGRO = (0, 0, 0)
# # BLANCO = (255, 255, 255)

# # # Clase del Cuadrado
# # class Cuadrado(pygame.sprite.Sprite):
# #     def __init__(self, x, y, tamaño, velocidad):
# #         super().__init__()
# #         self.image = pygame.Surface(tamaño)
# #         self.image.fill(BLANCO)
# #         self.rect = self.image.get_rect()
# #         self.rect.topleft = (x, y)
# #         self.velocidad = velocidad

# #     def mover(self, direccion):
# #         if direccion == "izquierda" and self.rect.left > 0:
# #             self.rect.x -= self.velocidad
# #         elif direccion == "derecha" and self.rect.right < ANCHO:
# #             self.rect.x += self.velocidad
# #         elif direccion == "arriba" and self.rect.top > 0:
# #             self.rect.y -= self.velocidad
# #         elif direccion == "abajo" and self.rect.bottom < ALTO:
# #             self.rect.y += self.velocidad

# # # Clase del Disparo

# # class Disparo(pygame.sprite.Sprite):
# #     def __init__(self, x, y, velocidad):
# #         super().__init__()
# #         self.image = pygame.Surface((10, 10))
# #         self.image.fill(BLANCO)
# #         self.rect = self.image.get_rect()
# #         self.rect.center = (x, y)
# #         self.velocidad = velocidad

# #     def update(self):
# #         self.rect.y -= self.velocidad
# #         if self.rect.bottom < 0:
# #             self.kill()  # Eliminar el disparo cuando sale de la pantalla

# # # Crear un cuadrado y un grupo de sprites para los disparos
# # cuadrado = Cuadrado(ANCHO // 2, ALTO // 2, (50, 50), 5)
# # disparos = pygame.sprite.Group()

# # # Bucle principal
# # reloj = pygame.time.Clock()

# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()
# #         elif event.type == pygame.KEYDOWN:
# #             if event.key == pygame.K_SPACE:
# #                 # Crear un nuevo disparo en la posición actual del cuadrado
# #                 disparo = Disparo(cuadrado.rect.centerx, cuadrado.rect.top, 10)
# #                 disparos.add(disparo)

# #     teclas_presionadas = pygame.key.get_pressed()

# #     if teclas_presionadas[pygame.K_LEFT]:
# #         cuadrado.mover("izquierda")
# #     elif teclas_presionadas[pygame.K_RIGHT]:
# #         cuadrado.mover("derecha")
# #     elif teclas_presionadas[pygame.K_UP]:
# #         cuadrado.mover("arriba")
# #     elif teclas_presionadas[pygame.K_DOWN]:
# #         cuadrado.mover("abajo")

# #     # Actualizar la posición de los disparos
# #     disparos.update()

# #     # Limpiar la pantalla
# #     pantalla.fill(NEGRO)

# #     # Dibujar el cuadrado en la nueva posición
# #     pantalla.blit(cuadrado.image, cuadrado.rect)

# #     # Dibujar los disparos
# #     disparos.draw(pantalla)

# #     # Actualizar la pantalla
# #     pygame.display.flip()

# #     # Controlar la velocidad de actualización
# #     reloj.tick(60)


# import pygame
# import sys
# from funciones import *
# # Supongamos que esta función ajusta el tamaño de las imágenes
# # def rescalar_imagenes(animaciones, tamaño):
#     # Implementa la lógica para ajustar el tamaño de las imágenes
#     # pass

# # Definir la clase Disparo
# # class Disparo(pygame.sprite.Sprite):
# #     def __init__(self, animaciones, pos_x, pos_y, tamaño, velocidad):
# #         # super().__init__()
# #         self.animaciones = animaciones
# #         rescalar_imagenes(self.animaciones, tamaño)
# #         self.image = self.animaciones[0]  # Asegúrate de tener imágenes en tu lista de animaciones
# #         self.rect = self.image.get_rect()
# #         self.rect.x = pos_x
# #         self.rect.y = pos_y
# #         self.velocidad = velocidad

# #     def actualizar_disparo(self):
# #         self.rect.y -= self.velocidad
# #         if self.rect.bottom < 0:
# #             self.kill()




# # def animacion_disparo():
# #     diccionario_de_animaciones = {}
# #     diccionario_de_animaciones["normal"] = disparos
# # corazones = [pygame.image.load(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\objetos\vida.png")]

# # class Disparo(pygame.sprite.Sprite):

# #     def __init__(self,animaciones,pos_x,pos_y,tamaño,velocidad,que_hace) :
# #         self.animaciones = animaciones
# #         rescalar_imagenes(self.animaciones,tamaño)  
# #         self.rectangulo = pygame.Rect(pos_x,pos_y,*tamaño)
# #         self.rectangulo_x = pos_x
# #         self.rectangulo_y = pos_y
# #         self.velocidad = velocidad
# #         self.que_hace = que_hace
# #         self.contador_de_pasos = 0
# #         self.animacione_actuales = self.animaciones[self.que_hace]

# #     def actualizar_disparo(self):
# #             self.rectangulo.y -= self.velocidad
# #             if self.rectangulo.bottom < 0:
# #                 self.kill()


# # # Inicializar Pygame
# # pygame.init()

# # # Configuración de la pantalla
# # ANCHO = 800
# # ALTO = 600
# # pantalla = pygame.display.set_mode((ANCHO, ALTO))
# # pygame.display.set_caption("Ejemplo de Disparo")

# # # Colores
# # NEGRO = (0, 0, 0)
# # BLANCO = (255, 255, 255)

# # # Crear un objeto Disparo
# # dic = animacion_corazon()
# # disparo = Disparo(dic,200,200,(20,20),1,"normal")

# # # Bucle principal
# # reloj = pygame.time.Clock()

# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()

# #     # Actualizar el disparo en cada cuadro

# #     # Limpiar la pantalla
# #     pantalla.fill(NEGRO)

# #     disparo.actualizar_disparo()
# #     # Dibujar el disparo en la nueva posición
# #     pantalla.blit(disparo.animacione_actuales, disparo.rectangulo)

# #     # Actualizar la pantalla
# #     pygame.display.flip()

# #     # Controlar la velocidad de actualización
# #     reloj.tick(60)



# # import pygame
# # import sys

# # def rescalar_imagenes(animaciones, tamaño):
# #     # Implementa la lógica para ajustar el tamaño de las imágenes
# #     pass

# # def animacion_disparo():
# #     diccionario_de_animaciones = {}
# #     diccionario_de_animaciones["normal"] = corazones  # Así asumo que 'corazones' es una lista válida de imágenes
# #     return diccionario_de_animaciones

# # class Disparo(pygame.sprite.Sprite):

# #     def __init__(self, animaciones, pos_x, pos_y, tamaño, velocidad, que_hace):
# #         super().__init__()
# #         self.animaciones = animaciones
# #         rescalar_imagenes(self.animaciones["normal"], tamaño)
# #         self.image = self.animaciones["normal"][0]  # Tomamos la primera imagen de la lista
# #         self.rect = self.image.get_rect()
# #         self.rect.x = pos_x
# #         self.rect.y = pos_y
# #         self.velocidad = velocidad
# #         self.que_hace = que_hace

# #     def actualizar_disparo(self):
# #         self.rect.y -= self.velocidad
# #         if self.rect.bottom < 0:
# #             self.kill()

# # # Inicializar Pygame
# # pygame.init()

# # # Configuración de la pantalla
# # ANCHO = 800
# # ALTO = 600
# # pantalla = pygame.display.set_mode((ANCHO, ALTO))
# # pygame.display.set_caption("Ejemplo de Disparo")

# # # Colores
# # NEGRO = (0, 0, 0)

# # # Crear un objeto Disparo
# # dic = animacion_disparo()
# # disparo = Disparo(dic, 200, 200, (20, 20), 1, "normal")
# # grupo_disparos = pygame.sprite.Group()
# # # Bucle principal
# # reloj = pygame.time.Clock()

# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()
# #     # for event in pygame.event.get():
# #     #     if event.type == pygame.QUIT:
# #     #         running = False
# #         elif event.type == pygame.KEYDOWN:
# #             # Verifica si se presionó una tecla
# #             key_name = pygame.key.name(event.key)
# #             print(f"Tecla presionada: {key_name}")
           
# #             if key_name == "space" :
# #                 # if  r'[0-9A-Za-z ]+$' == key_name:  
# #                 print(f"Tecla presionada: {key_name}")
# #             if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
# #                 disparo = Disparo(dic, 200, 200, (20, 20), 1, "normal")

# #     grupo_disparos.update()

# #     # Limpiar la pantalla
# #     # nivel.screen.fill(NEGRO)

# #     # Dibujar todos los disparos en el grupo
# #     grupo_disparos.draw(pantalla)

# #     # Actualizar el disparo en cada cuadro

# #     # Limpiar la pantalla
# #     pantalla.fill(NEGRO)

# #     disparo.actualizar_disparo()
# #     # Dibujar el disparo en la nueva posición
# #     pantalla.blit(disparo.image, disparo.rect)

# #     # Actualizar la pantalla
# #     pygame.display.flip()

# #     # Controlar la velocidad de actualización
# #     reloj.tick(60)






#  # def actualizar_disparo(self, pantalla):
#     #     for disparo in self.disparos_activos:
#     #         disparo['rect'].y -= disparo['velocidad']
#     #         pantalla.blit(self.animacione_actuales["normal"],self.rectangulo) 
#     #         # pygame.draw.rect(pantalla, (255, 255, 255), disparo['rect'])
#     #         # print("actuañlizo")

#     #         if disparo['rect'].bottom < 0:
#     #             self.disparos_activos.remove(disparo)


# # import pygame
# # import sys

# # # Inicializar Pygame
# # pygame.init()

# # # Configuración de la pantalla
# # width, height = 800, 600
# # screen = pygame.display.set_mode((width, height))
# # pygame.display.set_caption("Contador de Puntos")

# # # Definir colores
# # white = (255, 255, 255)
# # black = (0, 0, 0)

# # # Configuración del objeto
# # object_size = 50
# # object_x = width // 2 - object_size // 2
# # object_y = height - 2 * object_size
# # object_speed = 5

# # # Inicializar el contador de puntos
# # score = 0

# # # Configurar la fuente para el marcador
# # font = pygame.font.Font(None, 36)

# # # Función para mostrar el contador de puntos en la pantalla
# # def display_score():
# #     score_text = font.render("Puntos: {}".format(score), True, white)
# #     screen.blit(score_text, (10, 10))

# # # Bucle principal del juego
# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()

# #     keys = pygame.key.get_pressed()
# #     if keys[pygame.K_LEFT] and object_x > 0:
# #         object_x -= object_speed
# #     if keys[pygame.K_RIGHT] and object_x < width - object_size:
# #         object_x += object_speed

# #     # Lógica de colisión (en este caso, simplemente verifica si el objeto ha alcanzado la parte superior)
# #     if object_y < 0:
# #         object_y = height - 2 * object_size
# #         score += 1  # Incrementa el contador de puntos cuando el objeto es "destruido"

# #     # Dibujar en la pantalla
# #     screen.fill(black)
# #     pygame.draw.rect(screen, white, (object_x, object_y, object_size, object_size))

# #     # Mostrar el contador de puntos
# #     display_score()

# #     # Actualizar la pantalla
# #     pygame.display.flip()

# #     # Controlar la velocidad del bucle
# #     pygame.time.Clock().tick(60)









# """
# import pygame ,sys
# import random
# from pygame.locals import  QUIT
# import sqlite3
# from musica_sonidos import *
# from colores import *
# from objetos import *
# from funciones import *
# from fondos import *
# from constantes import *

# pygame.init()

# abrir_base_de_datos()

# player = Jugador()
# grupo_balas_jugador.add(player)
# grupo_jugador.add(player)
# pantalla_inicial(ventana_ppal)

# player_name = nombre_en_menu(ventana_ppal)
# pantalla_nivel(ventana_ppal, 1, "Tu misión es eliminar la estrella de la muerte! Ten mucho cuidado")
# nivel_actual = 1
# primer_nivel =True
# segundo_nivel = False
# tercer_nivel = False

# tiempo_inicial = pygame.time.get_ticks()

# nivel_uno()

# while run:
#     Reloj.tick(fps)
#     cronometro_iniciado = True
    
#     movimiento_fondo(fondo)
#     if nivel_actual == 2:
#         movimiento_fondo(fondo_nivel_dos)
#     elif nivel_actual == 3:
#         movimiento_fondo(fondo_nivel_tres)
    
#     # Manejo de eventos
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 player.disparar()
#             elif event.key == pygame.K_ESCAPE:
#                 juego_en_pausa = not juego_en_pausa
            
                
#     while juego_en_pausa:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     juego_en_pausa = not juego_en_pausa   
                    
#         ventana_ppal.blit(mensaje_pausa, (ANCHO_VENTANA // 2 - mensaje_pausa.get_width() // 2, ALTO_VENTANA // 2 - mensaje_pausa.get_height() // 2))  
#         pygame.display.flip()  

#     for enemigo in grupo_enemigos:
#             if enemigo.rect.top > ALTO_VENTANA:
#                 enemigo.rect.y = -10
#                 enemigo.rect.x = random.randint(1, ANCHO_VENTANA - 50)
                
#     for monedas in grupo_monedas:
#             if monedas.rect.top > ALTO_VENTANA:
#                 monedas.rect.y = -10
#                 monedas.rect.x = random.randint(1, ANCHO_VENTANA - 50)
                
#     ###################################cronometro################################
#     tiempo_transcurrido = pygame.time.get_ticks() - tiempo_inicial

#     if tiempo_inicial is not None and cronometro_iniciado:
#         tiempo_restante = max(0, DURACION_NIVEL - tiempo_transcurrido // 1000)
    
#     ########################### COLISIONES #######################################
# #CHOQUE ENTRE METEORO Y JUGADOR  
#     choque_entre_meteoro_y_nave = pygame.sprite.spritecollide(player,grupo_meteoros,True)
#     for choque in choque_entre_meteoro_y_nave:
#         player.vidas   -= 30
#         sonido_colision.play()
#         piedras = Meteoros(random.randint(0, ANCHO_VENTANA), 0)
#         grupo_jugador.add(piedras)
#         grupo_meteoros.add(piedras)
#         explo_meteorito = Explosion(choque.rect.center,(10,10))
#         grupo_jugador.add(explo_meteorito)
        
#         if player.vidas <=0:
#             explo_meteorito = Explosion(choque.rect.center,(10,10))
#             grupo_jugador.add(explo_meteorito)
#             run = False
#             conn = sqlite3.connect("puntuacion.db")
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO puntuacion (nombre, score) VALUES (?, ?)", (player_name, score))
#             conn.commit()
#             conn.close()
#             pantalla_game_over(score)

# #CHOQUE ENTRE NAVES
#     choque_entre_naves = pygame.sprite.spritecollide(player,grupo_enemigos,True)
#     for choque in choque_entre_naves:
#         explo_3 = Explosion(choque.rect.center,(10,10))
#         grupo_jugador.add(explo_3)
#         player.vidas   -= 30
#         sonido_colision.play()
#         enemigos = nave_enemiga(10,10)
#         grupo_jugador.add(enemigos)
#         grupo_enemigos.add(enemigos)
#         if player.vidas <=0:
#             explo_3 = Explosion(choque.rect.center,(10,10))
#             grupo_jugador.add(explo_3)
#             run = False
#             conn = sqlite3.connect("puntuacion.db")
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO puntuacion (nombre, score) VALUES (?, ?)", (player_name, score))
#             conn.commit()
#             conn.close()
#             pantalla_game_over(score)
            
# #LASER NAVE ENEMIGA A JUGADOR
#     laser_nave_enemiga_a_rebelde = pygame.sprite.spritecollide(player,grupo_balas_enemigos,True)
#     for j in laser_nave_enemiga_a_rebelde:
#         player.vidas -= 20
#         explo_1 = Explosion(j.rect.center,(10,10))
#         grupo_jugador.add(explo_1)
#         if player.vidas <=0:
#             run = False
#             conn = sqlite3.connect("puntuacion.db")
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO puntuacion (nombre, score) VALUES (?, ?)", (player_name, score))
#             conn.commit()
#             conn.close()
#             pantalla_game_over(score)
            
# #LASER REBELDE A NAVES ENEMIGAS
#     laser_rebelde_a_enemigos = pygame.sprite.groupcollide(grupo_enemigos,grupo_balas_jugador,True,True)
#     for i in laser_rebelde_a_enemigos:
#         score+=100
#         enemigo.disparos_enemigos()
#         enemigo = nave_enemiga(300,10)
#         grupo_enemigos.add(enemigo)
#         grupo_jugador.add(enemigo)

#         explo = Explosion(i.rect.center,(10,10))
#         grupo_jugador.add(explo)
#         sonido_explosion.play()
        
# #LASER REBELDE A METEORITOS
#     laser_rebelde_a_meteoritos = pygame.sprite.groupcollide(grupo_meteoros,grupo_balas_jugador,True,True)
#     for i in laser_rebelde_a_meteoritos:
#         score+=100
        
#         piedras = Meteoros(random.randint(0, ANCHO_VENTANA), 0)
#         grupo_meteoros.add(piedras)
#         grupo_jugador.add(piedras)

#         explo_meteorito = Explosion(i.rect.center,(10,10))
#         grupo_jugador.add(explo_meteorito)

#         explo = Explosion(i.rect.center,(10,10))
#         grupo_jugador.add(explo)
#         sonido_explosion.play()
    
# #LASER REBELDE A ESTRELLA
#     laser_rebelde_a_estrella = pygame.sprite.groupcollide(grupo_estrella,grupo_balas_jugador, False, True)
#     for estrella, balas in laser_rebelde_a_estrella.items():
#         for bala in balas:
#             score += 300
#             estrella.vidas -= 50
            
#             explo_estrella = Explosion(bala.rect.center,(100,100))
#             grupo_jugador.add(explo_estrella)
#             sonido_explosion.play()

#             if estrella.vidas <= 0:
#                 run = False
#                 conn = sqlite3.connect("puntuacion.db")
#                 cursor = conn.cursor()
#                 cursor.execute("INSERT INTO puntuacion (nombre, score) VALUES (?, ?)", (player_name, score))
#                 conn.commit()
#                 conn.close()
#                 video.preview()
#                 pantalla_victoria(player_name,score)
                
# #HIPER RAYO ESTRELLA DE LA MUERTE A REBELDE
#     hiperrayo_a_rebelde = pygame.sprite.spritecollide(player, grupo_balas_estrella, True)
#     for i in hiperrayo_a_rebelde:
#             player.vidas -= 50
            
#             explo = Explosion(i.rect.center,(10,10))
#             grupo_jugador.add(explo)
#             if player.vidas <=0:
#                 run = False
#                 conn = sqlite3.connect("puntuacion.db")
#                 cursor = conn.cursor()
#                 cursor.execute("INSERT INTO puntuacion (nombre, score) VALUES (?, ?)", (player_name, score))
#                 conn.commit()
#                 conn.close()
#                 pantalla_game_over(score)
                
                
# #MONEDA CON REBELDE 
#     colisiones_monedas = pygame.sprite.spritecollide(player, grupo_monedas, True)
#     for moneda in colisiones_monedas:
#         if player.vidas < 100:
#             incremento_vidas = min(20, 100 - player.vidas)
#             player.vidas += incremento_vidas
#             burbuja_moneda = Burbuja(moneda.rect.center, (20, 20))
#             grupo_jugador.add(burbuja_moneda)
#             sonido_energia.play()
        
            
#         nueva_moneda_vida = Moneda(random.randint(0, ANCHO_VENTANA), 0)
#         grupo_monedas.add(nueva_moneda_vida)  
#         grupo_jugador.add(nueva_moneda_vida )
            
# ####################################################################################
# #NIVELES:
#     if tiempo_restante == 0 and player.vidas >= 1:
#         if nivel_actual == 1 and not segundo_nivel:
#             # Cambio al NIVEL 2
#             nivel_actual += 1
#             segundo_nivel = True
#             primer_nivel = False
#             tercer_nivel = False
#             pantalla_nivel(ventana_ppal, 2, "Ya saben que llegamos, cuidado el enemigo abrió fuego!")
            
#             tiempo_inicial = pygame.time.get_ticks()
#             player.vidas = 100    
#             nivel_dos()           
#         elif nivel_actual == 2 and not tercer_nivel:
#             # Cambio al NIVEL 3
#             nivel_actual += 1
#             tercer_nivel = True
#             segundo_nivel = False
#             primer_nivel = False
#             pantalla_nivel(ventana_ppal, 3, "Destruye la estrella de la muerte!")
#             tiempo_inicial = pygame.time.get_ticks()
#             player.vidas = 100 
#             nivel_tres()
#         elif tercer_nivel:
#             if tiempo_restante == 0:
#                 segundo_nivel = False
#                 tercer_nivel = False
#                 primer_nivel = False
#                 pantalla_game_over(score)
                
#     grupos_update()

#     texto_puntuacion(ventana_ppal,('score: '+ str(score)+' '),20,ANCHO_VENTANA-75,2)
#     barra_vida(ventana_ppal,texto_puntuacion(ventana_ppal,'  vida: ',20,ANCHO_VENTANA-970,2),ANCHO_VENTANA-930,10,player.vidas)
#     mostrar_nivel(nivel_actual)
#     mostrar_cronometro(tiempo_restante)
    
#     pygame.display.update()  
#     Reloj.tick(fps) 

#     pygame.display.flip()
# pygame.quit()
# sys.exit()

# """

# import json
# import os

# # def actualizar_datos_jugadores(datos_nuevos):
# #     # Ruta del archivo JSON
# #     ruta_archivo = r'Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\datos_jugadores.json'

# #     # Verificar si el archivo ya existe
# #     if os.path.exists(ruta_archivo):
# #         # Si el archivo existe, cargar los datos existentes
# #         with open(ruta_archivo, 'r') as archivo_existente:
# #             datos_existente = json.load(archivo_existente)
        
# #         # Agregar los nuevos datos al archivo existente
# #         datos_existente["jugadores"].extend(datos_nuevos["jugadores"])

# #         # Escribir todos los datos de nuevo al archivo JSON
# #         with open(ruta_archivo, 'w') as archivo_json:
# #             json.dump(datos_existente, archivo_json, indent=2)
# #     else:
# #         # Si el archivo no existe, simplemente escribir los datos
# #         with open(ruta_archivo, 'w') as archivo_json:
# #             json.dump(datos_nuevos, archivo_json, indent=2)

# #     print(f"Se ha actualizado el archivo JSON en {ruta_archivo}")
# #     # Ejemplo de datos nuevos a agregar
# # nuevos_jugadores = {
# #     "jugadores": [
# #         {"juaam": "Nuevo Jugador"},
       
# #     ]
# # }

# # # Llamada a la función para actualizar el archivo
# # actualizar_datos_jugadores(nuevos_jugadores)

# # Aplicar temas vistos en clases:
# # ● Tipos de datos avanzados: listas, tuplas, diccionarios, sets.
# # ● Funciones. El código debe estar debidamente modularizado y documentado. Tengan
# # en cuenta los objetivos de la programación con funciones. Realizar módulos.py para la
# # correcta organización de las mismas.
# # ● Manejo de strings: para normalizar datos, realizar validaciones, etc.
# # ● Archivos csv o Json. Deberá contar con un archivo de configuración que se utilizará
# # con todas los datos para inicializar el juego.
# # ● Manejo de excepciones. Deberán controlar por lo menos cuatro tipos de excepciones.
# # ● Base de datos. Deberá contar con una base de datos que guarde el score y el nombre
# # del jugador
# # ● POO. Deberá contar con al menos tres clases en el trabajo práctico.
# # ● Expresiones regulares. Deberá contar con al menos el uso de alguna expresión
# # regular.

# # Pygame:
# # ● Imágenes. Según la temática del juego a desarrollar, habrá imágenes estáticas y/o
# # dinámicas (que van cambiando con cada acción del jugador)
# # ● Fuentes: toda interacción con el jugador implica que esos mensajes se muestran por la
# # ventana del juego. Por ejemplo: el texto de los botones, las vidas, score, etc.
# # ● Rectángulos: para representar botones, o cualquier elemento del juego que necesiten.
# # ● Manejo de eventos: teclas, mouse, eventos propios y temporizadores para la
# # interacción con el usuario.
# # ● Colisiones: entre el jugador principal y los objetos del juego (obstáculos, vidas, objetos
# # especiales).

# # ● Botones: por ejemplo para el manejo del menú principal
# # ● Sonidos y música: debe haber una música de fondo y ante distintas acciones, un
# # efecto de sonido distinto.
# # Consideraciones:
# # ● Aplicar las técnicas de programación vistas en clase.
# # ● Todo código que les hayamos compartido o que hayan obtenido de las clases, debe ser
# # reelaborado (intenten darle una impronta propia). No abusen del copy-paste.
# # ● La temática del juego no podrá ser la misma que la explicada en clases.
# # ● El código debe estar modularizado, contando con distintos archivos, cada uno referente
# # a lo que contiene. (Main, configuración, base de datos, clase_tal)

# # TEMA: GALAXIA
# # Descripción
# # El juego debe incluir un jugador principal que puede moverse en la zona de juego sin salir de
# # los límites de la pantalla, una variedad de obstáculos o enemigos, la capacidad de disparar o
# # realizar acciones para defenderse, un sistema de vidas y puntuación, y la opción de incluir un
# # elemento especial o poderes. Deberán crear una pantalla de inicio con botones de opciones y
# # una pantalla de fin para mostrar la puntuación final del jugador.

# # Requisitos del Juego:
# # Pantalla de Inicio:
# # Debe haber una pantalla de inicio con un título y botones para comenzar el juego, ver las
# # opciones y salir del mismo. En la cual, se deberá ingresar el nombre del jugador, este NO
# # puede ser por consola, sino en la misma pantalla.
# # Jugador Principal:
# # El jugador debe controlar un personaje o entidad que puede moverse en el espacio de juego.
# # El personaje debe ser capaz de interactuar de alguna manera con el entorno disparando,
# # saltando o realizando acciones para defenderse.
# # Niveles:
# # El juego debe contar con 3 niveles distintos, cada uno debe agregar una dificultad respecto al
# # nivel anterior (más enemigos, objetos que se mueven a mayor velocidad, etc).

# # Obstáculos o Enemigos:
# # Debe haber una variedad de obstáculos o enemigos en la zona de juego que representen
# # desafíos para el jugador.
# # Los obstáculos o enemigos pueden ser de diferentes tipos y comportarse de manera única.

# # Modalidad de juego:
# # La nave propia solo podrá moverse de izquierda a derecha o viceversa, nunca hacia adelante
# # o hacia atrás. Las naves deben efectuar disparos, tanto la propia como las enemigas.Utilizar
# # movimientos aleatorios para las naves enemigas.
# # Al final de cada partida se deberá guardar el SCORE junto con el nombre de usuario. En tal
# # sentido, se deberá elaborar un ranking ordenado de mayor a menor puntuación, mostrando
# # su respectivo nombre y puntuación.
# # Elemento Especiales o Poderes:
# # Incluir un elemento especial o poderes que otorguen beneficios temporales al jugador.
# # Tiempo:
# # Tiene que contar con un cronómetro.

# # def leer_datos_jugadores(ruta_archivo):
# #     """
# #     Lee los datos de jugadores desde un archivo JSON.

# #     Parameters:
# #     - ruta_archivo (str): La ruta del archivo JSON.

# #     Returns:
# #     - list: Una lista de diccionarios que representan los datos de los jugadores.
# #     """
# #     # Verificar si el archivo existe
# #     if not os.path.exists(ruta_archivo):
# #         print(f"El archivo {ruta_archivo} no existe.")
# #         return []

# #     # Leer los datos del archivo JSON
# #     with open(ruta_archivo, 'r') as archivo_json:
# #         datos_jugadores = json.load(archivo_json)

# #     # Obtener la lista de jugadores del diccionario
# #     jugadores = datos_jugadores.get("jugadores", [])

# #     return jugadores

# # # Ejemplo de uso
# # ruta_archivo_ejemplo = r'Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\datos_jugadores.json'
# # jugadores_ejemplo = leer_datos_jugadores(ruta_archivo_ejemplo)
# # print(jugadores_ejemplo)
# # # Imprimir los datos de cada jugador
# # for jugador in jugadores_ejemplo:
# #     nombre = jugador.get("nombre", "")
# #     puntos = jugador.get("puntos", 0)
# #     nivel = jugador.get("nivel", 1)
# #     print(f"Nombre: {nombre}, Puntos: {puntos}, Nivel: {nivel}")

# import pygame
# import sys

# pygame.init()

# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# clock = pygame.time.Clock()

# font = pygame.font.Font(None, 36)
# text_color = (255, 255, 255)
# background_color = (0, 0, 0)

# def mostrar_texto(texto, x, y, duracion):
#     texto_surface = font.render(texto, True, text_color)
#     rect = texto_surface.get_rect(center=(x, y))
#     screen.blit(texto_surface, rect)

#     pygame.display.flip()

#     tiempo_inicial = pygame.time.get_ticks()

#     while pygame.time.get_ticks() - tiempo_inicial < duracion:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#     # Limpiar la pantalla después de la duración
#     screen.fill(background_color)
#     pygame.display.flip()

# # Uso del ejemplo
# mostrar_texto("Hola, esto desaparecerá en 3 segundos", width // 2, height // 2, 3000)

# # Bucle principal
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
# sys.exit()
# """
# import pygame
# from funciones import *
# from ajustes_generales import *
# from class_disparo import *
# from class_enemigos import *

# # class Nivel1:
# #     def __init__(self):
# #         self.ancho_screen = 984
# #         self.largo_screen = 630
# #     def ejecutar_nivel(self):
# #         ancho_screen = 984
# #         largo_screen = 630
# #         #llamamos a los ajustes generales ya hechos en nivel para no estar duplicando codigo
# #         fondo_nivel = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\nivel1.jpg"

# #         nivel = Nivel(self.ancho_screen,self.largo_screen,60,30,fondo_nivel)

# #         cantidad_enemigos = 12
# #         # definimos al enemigo meteorito
# #         sprite_meteorito = pygame.sprite.Group()

# #         for i in range(cantidad_enemigos):
# #                 meti = meterorito(self.ancho_screen,self.largo_screen)
# #                 sprite_meteorito.add(meti)


# #         sonido_inicial(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\We Will Rock .mp3",0.1)

# #         run = True
# #         while run:

            
            
# #             # dibujamos y actualizamos a los meteritos en la pantalla 
# #             sprite_meteorito.update()
# #             sprite_meteorito.draw(nivel.screen)
# #             # se dibujan y actualizan mis disparos y los dibujos 
# #             nivel.mis_disparos.update()
# #             nivel.mis_disparos.draw(nivel.screen)

# #             nivel.nave.colision_disparos(sprite_meteorito, nivel.mis_disparos)
# #             # colision entre mi nave y los disparos enemigos
# #             nivel.nave.colisiones_nave_normal(sprite_meteorito,1)

# #             cantidad_de_meteoritos = len(sprite_meteorito)
# #             if cantidad_de_meteoritos < cantidad_enemigos:
# #                 meti = meterorito(ancho_screen,largo_screen)
# #                 sprite_meteorito.add(meti)

# #             if nivel.nave.puntos > nivel.puntos or nivel.nave.puntos <  nivel.puntos:
# #                     nivel.puntos =  nivel.nave.puntos

# #             nivel.nave.moverse(largo_screen,ancho_screen)
# #             nivel.nave.actualizar(nivel.screen)
            
        
# #             nivel.ejecusion_final()

# #             if nivel.nave.vidas == 0 or nivel.controlador_tiempo()  <=0:
# #                 run = False
# #             pygame.display.update()


# class Nivel1:
#     def __init__(self):
#         self.ancho_screen = 984
#         self.largo_screen = 630
#         self.fondo_nivel = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\nivel1.jpg"
#         self.nivel = Nivel(self.ancho_screen, self.largo_screen, 60, 6, self.fondo_nivel)
#         self.sprite_nave_enemigo = pygame.sprite.Group()
#         self.cantidad_enemigos = 12
#         self.sprite_meteorito = pygame.sprite.Group()
       
            
    
#     def ejecutar_nivel(self):
#         # mostrar_texto("nivel 1")
#         mostrar_texto("nivel 1 ", width // 2, height // 2, 3000,self.fondo_nivel,self.ancho_screen,self.largo_screen)

#         for i in range(self.cantidad_enemigos):
#             meti = meterorito(self.ancho_screen, self.largo_screen)
#             self.sprite_meteorito.add(meti)
#         run = True
#         while run:
#             self.nivel.ejecutar()
           
#             self.sprite_meteorito.update()
#             self.sprite_meteorito.draw(self.nivel.screen)

#             self.nivel.mis_disparos.update()
#             self.nivel.mis_disparos.draw(self.nivel.screen)

#             self.nivel.nave.colision_disparos(self.sprite_meteorito, self.nivel.mis_disparos)
#             self.nivel.nave.colisiones_nave_normal(self.sprite_meteorito, 1)

#             cantidad_de_meteoritos = len(self.sprite_meteorito)
#             if cantidad_de_meteoritos < self.cantidad_enemigos:
#                 meti = meterorito(self.ancho_screen, self.largo_screen)
#                 self.sprite_meteorito.add(meti)

#             if self.nivel.nave.puntos > self.nivel.puntos or self.nivel.nave.puntos < self.nivel.puntos:
#                 self.nivel.puntos = self.nivel.nave.puntos

#             self.nivel.nave.moverse(self.largo_screen, self.ancho_screen)
#             self.nivel.nave.actualizar(self.nivel.screen)
#             self.nivel.ejecusion_final()

#             if self.nivel.nave.vidas <= 0:
#                 run = False #pierde
#                 return -1

#             elif self.nivel.nave.vidas > 0 and self.nivel.controlador_tiempo() <= 0:
#                 self.bandera = True #gana
#                 return 1

#             pygame.display.update()
#     def puntos(self):
#         puntos =  self.nivel.nave.puntos
#         return puntos 



    
# # from nivel_2 import * 
# # from nivel_3 import * 


# nivel_1 = Nivel1()
# nivel_1.ejecutar_nivel()


# # class Nivel1:
# #     def __init__(self):
# #         self.ancho_screen = 984
# #         self.largo_screen = 630
# #         self.fondo_nivel = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\nivel1.jpg"

# #         self.nivel = Nivel(self.ancho_screen, self.largo_screen, 60, 30, self.fondo_nivel)
# #         self.sprite_meteorito = pygame.sprite.Group()
# #         self.cantidad_enemigos = 12

# #     def cargar_enemigos(self):
# #         for i in range(self.cantidad_enemigos):
# #             meti = meterorito(self.ancho_screen, self.largo_screen)
# #             self.sprite_meteorito.add(meti)

# #     def ejecutar_nivel(self):
# #         self.cargar_enemigos()
# #         # sonido_inicial(r"ruta/a/tu/sonido.mp3", 0.1)
# #         run = True
# #         while run:
# #             self.nivel.ejecutar()
# #             self.actualizar_sprites()

# #     def actualizar_sprites(self):
# #         self.sprite_meteorito.update()
# #         self.sprite_meteorito.draw(self.nivel.screen)
# #         self.nivel.mis_disparos.update()
# #         self.nivel.mis_disparos.draw(self.nivel.screen)
# #         self.nivel.nave.colision_disparos(self.sprite_meteorito, self.nivel.mis_disparos)
# #         self.nivel.nave.colisiones_nave_normal(self.sprite_meteorito, 1)
# #         cantidad_de_meteoritos = len(self.sprite_meteorito)
# #         if cantidad_de_meteoritos < self.cantidad_enemigos:
# #             self.cargar_enemigos()
# #         if self.nivel.nave.puntos > self.nivel.puntos or self.nivel.nave.puntos < self.nivel.puntos:
# #             self.nivel.puntos = self.nivel.nave.puntos
# #         self.nivel.nave.moverse(self.largo_screen, self.ancho_screen)
# #         self.nivel.nave.actualizar(self.nivel.screen)
# #         self.nivel.ejecusion_final()


# """
# import pygame
# from funciones import *
# from ajustes_generales import *
# from class_enemigos import *


# # # class nivel_2:
# # ancho_screen = 984
# # largo_screen = 630
# # #llamamos a los ajustes generales ya hechos en nivel para no estar duplicando codigo
# # fondo_nivel = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\nivel2.png"

# # nivel = Nivel(ancho_screen,largo_screen,60,30,fondo_nivel)

# # # aca se define las naves ennemigas
# # sprite_nave_enemigo = pygame.sprite.Group()
# # sprite_nave_enemigo_disparo = pygame.sprite.Group()

# # # SE generan tantos enemigos como queramos
# # cantidad_de_naves = 3
# # for i in range(cantidad_de_naves):
# #     nave_enemiga = Enemigo(ancho_screen,largo_screen,sprite_nave_enemigo_disparo)
# #     sprite_nave_enemigo.add(nave_enemiga)


# # # definimos al enemigo meteorito
# # cantidad_meteroritos = 10
# # sprite_meteorito = pygame.sprite.Group()
# # for i in range(cantidad_meteroritos):
# #         meti = meterorito(ancho_screen,largo_screen)
# #         sprite_meteorito.add(meti)


# # sonido_inicial(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\We Will Rock .mp3",0.1)

# # # diccionario para almacenar sonidos
# # sonidos = {
# #     'sonido_personaje': pygame.mixer.Sound(r'Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\golpe_de_mi_nave.mp3'),
# #     # Agrega más sonidos 
# # }

# # puntos_meterorito = 0
# # run = True
# # while run:

# #     nivel.ejecutar()
    
# #     # dibujamos y actualizamos a los meteritos en la pantalla 
# #     sprite_meteorito.update()
# #     sprite_meteorito.draw(nivel.screen)

# #     # dibujamos y actualizamos a las naves enemigas en la pantalla 
# #     sprite_nave_enemigo.update()
# #     sprite_nave_enemigo.draw(nivel.screen)

# #     # estos son los disparos de la nave 
# #     nivel.mis_disparos.update()
# #     nivel.mis_disparos.draw(nivel.screen)

# #     sprite_nave_enemigo_disparo.update()
# #     sprite_nave_enemigo_disparo.draw(nivel.screen)


# #     nivel.nave.colision_disparos(sprite_meteorito, nivel.mis_disparos)
# #     # colision entre mi nave y los disparos enemigos
# #     nivel.nave.colisiones_nave_normal(sprite_meteorito,1)
# #     cantidad_de_meteoritos = len(sprite_meteorito)
# #     if cantidad_de_meteoritos < cantidad_meteroritos:
# #         meti = meterorito(ancho_screen,largo_screen)
# #         sprite_meteorito.add(meti)

    
# #     # colisones entre la nave enemiga y los disparos
# #     nivel.nave.colisiones_nave_normal(sprite_nave_enemigo,1)
# #     # colision entre mis disparos y la nave enemiga
# #     nivel.nave.colision_disparos(sprite_nave_enemigo, nivel.mis_disparos)
# #     # colision entre mi nave y los disparos enemigos
# #     nivel.nave.colisiones_nave_normal(sprite_nave_enemigo_disparo,1)

# #     if nivel.nave.puntos > nivel.puntos or nivel.nave.puntos <  nivel.puntos:
# #         nivel.puntos =  nivel.nave.puntos

    
# #     #actualizacion de mi nave 
# #     nivel.nave.moverse(largo_screen,ancho_screen)
# #     nivel.nave.actualizar(nivel.screen)
    
# #     # aca se ejecuta el timer los conadores y las vidas
# #     nivel.ejecusion_final()
# #     if nivel.nave.vidas == 0 or nivel.controlador_tiempo()  <=0:
# #         run = False
# #     pygame.display.update()

# class Nivel2:
#     def __init__(self):
#         self.ancho_screen = 984
#         self.largo_screen = 630
#         self.fondo_nivel = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\nivel2.png"
#         self.nivel = Nivel(self.ancho_screen, self.largo_screen, 60, 35, self.fondo_nivel)
#         self.sprite_nave_enemigo = pygame.sprite.Group()
#         self.sprite_nave_enemigo_disparo = pygame.sprite.Group()
#         self.sprite_meteorito = pygame.sprite.Group()

#         self.cantidad_de_naves = 3
#         self.cantidad_meteoritos = 10

#         self.inicializar_nivel()
#         self.sonidos = {
#             'sonido_personaje': pygame.mixer.Sound(r'Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\golpe_de_mi_nave.mp3'),
#             # Agrega más sonidos 
#         }

#     def inicializar_nivel(self):
#         mostrar_texto("nivel 2 ", width // 2, height // 2, 3000,self.fondo_nivel,self.ancho_screen,self.largo_screen)

#         for i in range(self.cantidad_de_naves):
#             nave_enemiga = Enemigo(self.ancho_screen, self.largo_screen, self.sprite_nave_enemigo_disparo)
#             self.sprite_nave_enemigo.add(nave_enemiga)

#         for i in range(self.cantidad_meteoritos):
#             meti = meterorito(self.ancho_screen, self.largo_screen)
#             self.sprite_meteorito.add(meti)

#         sonido_inicial(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\We Will Rock .mp3", 0.1)

#     def ejecutar_nivel(self):
#         puntos_meteorito = 0
#         run = True
#         while run:
#             self.nivel.ejecutar()

#             # Lógica específica del nivel 2 aquí
#             # ...

#             self.sprite_meteorito.update()
#             self.sprite_meteorito.draw(self.nivel.screen)

#             self.sprite_nave_enemigo.update()
#             self.sprite_nave_enemigo.draw(self.nivel.screen)

#             self.nivel.mis_disparos.update()
#             self.nivel.mis_disparos.draw(self.nivel.screen)

#             self.sprite_nave_enemigo_disparo.update()
#             self.sprite_nave_enemigo_disparo.draw(self.nivel.screen)

#             self.nivel.nave.colision_disparos(self.sprite_meteorito, self.nivel.mis_disparos)
#             self.nivel.nave.colisiones_nave_normal(self.sprite_meteorito, 1)

#             cantidad_de_meteoritos = len(self.sprite_meteorito)
#             if cantidad_de_meteoritos < self.cantidad_meteoritos:
#                 meti = meterorito(self.ancho_screen, self.largo_screen)
#                 self.sprite_meteorito.add(meti)

#             self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo, 1)
#             self.nivel.nave.colision_disparos(self.sprite_nave_enemigo, self.nivel.mis_disparos)
#             self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo_disparo, 1)

#             if self.nivel.nave.puntos > self.nivel.puntos or self.nivel.nave.puntos < self.nivel.puntos:
#                 self.nivel.puntos = self.nivel.nave.puntos

#             self.nivel.nave.moverse(self.largo_screen, self.ancho_screen)
#             self.nivel.nave.actualizar(self.nivel.screen)

#             self.nivel.ejecusion_final()

           
#             if self.nivel.nave.vidas <= 0:
#                 run = False #pierde
#                 return -1

#             elif self.nivel.nave.vidas > 0 and self.nivel.controlador_tiempo() <= 0:
#                 run = False #gana
#                 return 2

#             pygame.display.update()
#     def puntos(self):
#         puntos =  self.nivel.nave.puntos
#         return puntos 

# nivel_2 = Nivel2()
# nivel_2.ejecutar_nivel()




# # class Nivel2:
# #     def __init__(self):
# #         self.ancho_screen = 984
# #         self.largo_screen = 630

# #         self.fondo_nivel = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\nivel2.png"
# #         self.nivel = Nivel(self.ancho_screen, self.largo_screen, 60, 30, self.fondo_nivel)
# #         self.sprite_meteorito = pygame.sprite.Group()
# #         self.sprite_nave_enemigo = pygame.sprite.Group()
# #         self.sprite_nave_enemigo_disparo = pygame.sprite.Group()
# #         self.cantidad_meteroritos = 10
# #         self.cantidad_de_naves = 3
# #         self.sonidos = {
# #             'sonido_personaje': pygame.mixer.Sound(r'ruta/a/tu/sonido.mp3'),
# #             # Agrega más sonidos 
# #         }

# #     def cargar_meteoritos(self):
# #         for i in range(self.cantidad_meteroritos):
# #             meti = meterorito(self.ancho_screen, self.largo_screen)
# #             self.sprite_meteorito.add(meti)

# #     def cargar_naves_enemigas(self):
# #         for i in range(self.cantidad_de_naves):
# #             nave_enemiga = Enemigo(self.ancho_screen, self.largo_screen, self.sprite_nave_enemigo_disparo)
# #             self.sprite_nave_enemigo.add(nave_enemiga)

# #     def ejecutar_nivel(self):
# #         self.cargar_meteoritos()
# #         self.cargar_naves_enemigas()
# #         # sonido_inicial(self.sonidos['sonido_personaje'], 0.1)
# #         run = True
# #         while run:
# #             self.nivel.ejecutar()
# #             self.actualizar_sprites()
# #             self.nivel.ejecusion_final()

# #     def actualizar_sprites(self):
# #         self.sprite_meteorito.update()
# #         self.sprite_meteorito.draw(self.nivel.screen)
# #         self.sprite_nave_enemigo.update()
# #         self.sprite_nave_enemigo.draw(self.nivel.screen)
# #         self.nivel.mis_disparos.update()
# #         self.nivel.mis_disparos.draw(self.nivel.screen)
# #         self.sprite_nave_enemigo_disparo.update()
# #         self.sprite_nave_enemigo_disparo.draw(self.nivel.screen)
# #         self.nivel.nave.colision_disparos(self.sprite_meteorito, self.nivel.mis_disparos)
# #         self.nivel.nave.colisiones_nave_normal(self.sprite_meteorito, 1)
# #         cantidad_de_meteoritos = len(self.sprite_meteorito)
# #         if cantidad_de_meteoritos < self.cantidad_meteroritos:
# #             self.cargar_meteoritos()
# #         self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo, 1)
# #         self.nivel.nave.colision_disparos(self.sprite_nave_enemigo, self.nivel.mis_disparos)
# #         self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo_disparo, 1)
# #         if self.nivel.nave.puntos > self.nivel.puntos or self.nivel.nave.puntos < self.nivel.puntos:
# #             self.nivel.puntos = self.nivel.nave.puntos
# #         self.nivel.nave.moverse(self.largo_screen, self.ancho_screen)
# #         self.nivel.nave.actualizar(self.nivel.screen)


# import pygame
# from funciones import *
# from ajustes_generales import *
# from class_enemigos import *

# # # class nivel_3:
# # ancho_screen = 984
# # largo_screen = 630
# # #llamamos a los ajustes generales ya hechos en nivel para no estar duplicando codigo
# # fondo_nivel = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\nivel3.jpg"

# # nivel = Nivel(ancho_screen,largo_screen,60,45,fondo_nivel)

# # # aca se define las naves ennemigas

# # sprite_boss = pygame.sprite.Group()
# # sprite_boss_disparo = pygame.sprite.Group()

# # for i in range(1):
# #     boss = Enemigo_boss(ancho_screen,largo_screen,sprite_boss_disparo)
# #     sprite_boss.add(boss)

# # # SE generan tantos enemigos como queramos
# # sprite_nave_enemigo = pygame.sprite.Group()
# # sprite_nave_enemigo_disparo = pygame.sprite.Group()
# # cantidad_de_naves = 3
# # for i in range(cantidad_de_naves):
# #     nave_enemiga = Enemigo(ancho_screen,largo_screen,sprite_nave_enemigo_disparo)
# #     sprite_nave_enemigo.add(nave_enemiga)


# # # definimos al enemigo meteorito
# # cantidad_meteroritos = 7
# # sprite_meteorito = pygame.sprite.Group()
# # for i in range(cantidad_meteroritos):
# #         meti = meterorito(ancho_screen,largo_screen)
# #         sprite_meteorito.add(meti)


# # sonido_inicial(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\We Will Rock .mp3",0.1)

# # # diccionario para almacenar sonidos
# # sonidos = {
# #     'sonido_personaje': pygame.mixer.Sound(r'Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\golpe_de_mi_nave.mp3'),
# #     # Agrega más sonidos 
# # }

# # puntos_meterorito = 0
# # run = True
# # while run:

# #     nivel.ejecutar()
    
# #     # dibujamos y actualizamos a los meteritos en la pantalla 
    
# #     # # dibujamos y actualizamos a las naves enemigas en la pantalla 
# #     sprite_nave_enemigo.update()
# #     sprite_nave_enemigo.draw(nivel.screen)

# #     # estos son los disparos de la nave enemiga
# #     sprite_nave_enemigo_disparo.update()
# #     sprite_nave_enemigo_disparo.draw(nivel.screen)
    
# #     nivel.mis_disparos.update()
# #     nivel.mis_disparos.draw(nivel.screen)

# #     sprite_boss_disparo.update()
# #     sprite_boss_disparo.draw(nivel.screen)
    
# #     sprite_boss.update()
# #     sprite_boss.draw(nivel.screen)

# #     sprite_meteorito.update()
# #     sprite_meteorito.draw(nivel.screen)


# #     # colisones entre la nave enemiga y los disparos
# #     # nivel.nave.colisiones_nave_normal(sprite_boss,1)
# #     # colision entre mis disparos y la nave enemiga
# #     nivel.nave.colision_disparos(sprite_boss, nivel.mis_disparos)
# #     # colision entre mi nave y los disparos enemigos
# #     nivel.nave.colisiones_nave_normal(sprite_boss_disparo,1)

    
# #     # colisones entre la nave enemiga y los disparos
# #     nivel.nave.colisiones_nave_normal(sprite_nave_enemigo,1)
# #     # colision entre mis disparos y la nave enemiga
# #     nivel.nave.colision_disparos(sprite_nave_enemigo, nivel.mis_disparos)
# #     # colision entre mi nave y los disparos enemigos
# #     nivel.nave.colisiones_nave_normal(sprite_nave_enemigo_disparo,1)


# #     nivel.nave.colision_disparos(sprite_meteorito, nivel.mis_disparos)
# #     # colision entre mi nave y los disparos enemigos
# #     nivel.nave.colisiones_nave_normal(sprite_meteorito,1)
# #     cantidad_de_meteoritos = len(sprite_meteorito)
# #     if cantidad_de_meteoritos < cantidad_meteroritos:
# #         meti = meterorito(ancho_screen,largo_screen)
# #         sprite_meteorito.add(meti)

    

# #     if nivel.nave.puntos > nivel.puntos or nivel.nave.puntos <  nivel.puntos:
# #         nivel.puntos =  nivel.nave.puntos

    
# #     #actualizacion de mi nave 
# #     nivel.nave.moverse(largo_screen,ancho_screen)
# #     nivel.nave.actualizar(nivel.screen)
    
# #     # aca se ejecuta el timer los conadores y las vidas
# #     nivel.ejecusion_final()
# #     if nivel.nave.vidas == 0 or nivel.controlador_tiempo()  <=0:
# #         run = False
# #     pygame.display.update()

# class Nivel3:
#     def __init__(self):
#         self.ancho_screen = 984
#         self.largo_screen = 630
#         self.fondo_nivel = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\imagenes\fondos de pantalla\nivel3.jpg"
#         self.nivel = Nivel(self.ancho_screen, self.largo_screen, 60, 45, self.fondo_nivel)
#         self.sprite_nave_enemigo = pygame.sprite.Group()
#         self.sprite_nave_enemigo_disparo = pygame.sprite.Group()
#         self.sprite_meteorito = pygame.sprite.Group()
#         self.sprite_boss = pygame.sprite.Group()
#         self.sprite_boss_disparo = pygame.sprite.Group()

#         self.cantidad_de_naves = 3
#         self.cantidad_meteoritos = 7

#         self.inicializar_nivel()
#         self.sonidos = {
#             'sonido_personaje': pygame.mixer.Sound(r'Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\golpe_de_mi_nave.mp3'),
#             # Agrega más sonidos 
#         }

#     def inicializar_nivel(self):
#         mostrar_texto("nivel 3 ", width // 2, height // 2, 3000,self.fondo_nivel,self.ancho_screen,self.largo_screen)

#         for i in range(self.cantidad_de_naves):
#             nave_enemiga = Enemigo(self.ancho_screen, self.largo_screen, self.sprite_nave_enemigo_disparo)
#             self.sprite_nave_enemigo.add(nave_enemiga)

#         for i in range(self.cantidad_meteoritos):
#             meti = meterorito(self.ancho_screen, self.largo_screen)
#             self.sprite_meteorito.add(meti)

#         boss = Enemigo_boss(self.ancho_screen, self.largo_screen, self.sprite_boss_disparo)
#         self.sprite_boss.add(boss)

#         sonido_inicial(r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\sonidos\We Will Rock .mp3", 0.1)

#     def ejecutar_nivel(self):
#         # puntos_meteorito = 0
#         run = True
#         while run:
#             self.nivel.ejecutar()

           

#             self.sprite_nave_enemigo.update()
#             self.sprite_nave_enemigo.draw(self.nivel.screen)

#             self.sprite_nave_enemigo_disparo.update()
#             self.sprite_nave_enemigo_disparo.draw(self.nivel.screen)

#             self.nivel.mis_disparos.update()
#             self.nivel.mis_disparos.draw(self.nivel.screen)

#             self.sprite_boss_disparo.update()
#             self.sprite_boss_disparo.draw(self.nivel.screen)

#             self.sprite_boss.update()
#             self.sprite_boss.draw(self.nivel.screen)

#             self.sprite_meteorito.update()
#             self.sprite_meteorito.draw(self.nivel.screen)

#             self.nivel.nave.colision_disparos(self.sprite_boss, self.nivel.mis_disparos)
#             self.nivel.nave.colisiones_nave_normal(self.sprite_boss_disparo, 1)

#             self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo, 1)
#             self.nivel.nave.colision_disparos(self.sprite_nave_enemigo, self.nivel.mis_disparos)
#             self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo_disparo, 1)

#             self.nivel.nave.colision_disparos(self.sprite_meteorito, self.nivel.mis_disparos)
#             self.nivel.nave.colisiones_nave_normal(self.sprite_meteorito, 1)

#             cantidad_de_meteoritos = len(self.sprite_meteorito)
#             if cantidad_de_meteoritos < self.cantidad_meteoritos:
#                 meti = meterorito(self.ancho_screen, self.largo_screen)
#                 self.sprite_meteorito.add(meti)

#             if self.nivel.nave.puntos > self.nivel.puntos or self.nivel.nave.puntos < self.nivel.puntos:
#                 self.nivel.puntos = self.nivel.nave.puntos

#             self.nivel.nave.moverse(self.largo_screen, self.ancho_screen)
#             self.nivel.nave.actualizar(self.nivel.screen)

#             self.nivel.ejecusion_final()

           
#             if self.nivel.nave.vidas <= 0:
#                 run = False #pierde
#                 return -1

#             elif self.nivel.nave.vidas > 0 and self.nivel.controlador_tiempo() <= 0:
#                 self.bandera = True #gana
#                 return 3

#             pygame.display.update()
#     def puntos(self):
#         puntos =  self.nivel.nave.puntos
#         return puntos             


# nivel_3 = Nivel3()
# nivel_3.ejecutar_nivel()



# # class Nivel3:
# #     def __init__(self):
# #         self.ancho_screen = 984
# #         self.largo_screen = 630
# #         self.fondo_nivel = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\nivel_3.py"
# #         self.nivel = Nivel(self.ancho_screen, self.largo_screen, 60, 45, self.fondo_nivel)
# #         self.sprite_meteorito = pygame.sprite.Group()
# #         self.sprite_nave_enemigo = pygame.sprite.Group()
# #         self.sprite_nave_enemigo_disparo = pygame.sprite.Group()
# #         self.sprite_boss = pygame.sprite.Group()
# #         self.sprite_boss_disparo = pygame.sprite.Group()
# #         self.cantidad_meteroritos = 7
# #         self.cantidad_de_naves = 3
# #         self.sonidos = {
# #             'sonido_personaje': pygame.mixer.Sound(r'ruta/a/tu/sonido.mp3'),
# #             # Agrega más sonidos 
# #         }

# #     def cargar_meteoritos(self):
# #         for i in range(self.cantidad_meteroritos):
# #             meti = meterorito(self.ancho_screen, self.largo_screen)
# #             self.sprite_meteorito.add(meti)

# #     def cargar_naves_enemigas(self):
# #         for i in range(self.cantidad_de_naves):
# #             nave_enemiga = Enemigo(self.ancho_screen, self.largo_screen, self.sprite_nave_enemigo_disparo)
# #             self.sprite_nave_enemigo.add(nave_enemiga)

# #     def cargar_boss(self):
# #         for i in range(1):
# #             boss = Enemigo_boss(self.ancho_screen, self.largo_screen, self.sprite_boss_disparo)
# #             self.sprite_boss.add(boss)

# #     def ejecutar_nivel(self):
# #         self.cargar_meteoritos()
# #         self.cargar_naves_enemigas()
# #         self.cargar_boss()
# #         # sonido_inicial(self.sonidos['sonido_personaje'], 0.1)
# #         run = True
# #         while run:
# #             self.nivel.ejecutar()
# #             self.actualizar_sprites()
# #             self.nivel.ejecusion_final()

# #     def actualizar_sprites(self):
# #         self.sprite_nave_enemigo.update()
# #         self.sprite_nave_enemigo.draw(self.nivel.screen)
# #         self.sprite_nave_enemigo_disparo.update()
# #         self.sprite_nave_enemigo_disparo.draw(self.nivel.screen)
# #         self.sprite_boss_disparo.update()
# #         self.sprite_boss_disparo.draw(self.nivel.screen)
# #         self.sprite_boss.update()
# #         self.sprite_boss.draw(self.nivel.screen)
# #         self.nivel.mis_disparos.update()
# #         self.nivel.mis_disparos.draw(self.nivel.screen)
# #         self.sprite_meteorito.update()
# #         self.sprite_meteorito.draw(self.nivel.screen)
# #         self.nivel.nave.colision_disparos(self.sprite_boss, self.nivel.mis_disparos)
# #         self.nivel.nave.colisiones_nave_normal(self.sprite_boss_disparo, 1)
# #         self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo, 1)
# #         self.nivel.nave.colision_disparos(self.sprite_nave_enemigo, self.nivel.mis_disparos)
# #         self.nivel.nave.colisiones_nave_normal(self.sprite_nave_enemigo_disparo, 1)
# #         self.nivel.nave.colision_disparos(self.sprite_meteorito, self.nivel.mis_disparos)
# #         self.nivel.nave.colisiones_nave_normal(self.sprite_meteorito, 1)
# #         cantidad_de_meteoritos = len(self.sprite_meteorito)
# #         if cantidad_de_meteoritos < self.cantidad_meteroritos:
# #             self.cargar_meteoritos()
# #         if self.nivel.nave.puntos > self.nivel.puntos or self.nivel.nave.puntos < self.nivel.puntos:
# #             self.nivel.puntos = self.nivel.nave.puntos
# #         self.nivel.nave.moverse(self.largo_screen, self.ancho_screen)
# #         self.nivel.nave.actualizar(self.nivel.screen)
import json

def escribir_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo)

def leer_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos_leidos = json.load(archivo)
    return datos_leidos

# Ejemplo de uso
nombre_archivo = "Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\mini.json"
nombre = "juan"
puntos = "1532"

datos = {}
datos["nombre"] = nombre
datos["puntos"] = puntos

archivos = []
archivos.append(datos)




escribir_json(nombre_archivo, archivos)

print(leer_json("Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\mini.json"))
for i in leer_json("Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\carpeta_juego\mini.json"):
    print(i["nombre"])
