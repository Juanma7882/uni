# import pygame


# pygame.init()

# running = True

# window = pygame.display.set_mode((500, 400), 0, 32)
# pygame.display.set_caption("vamos a hacer un juego!")
# while(running):
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			running = False

# 	window.fill((255, 255, 255)) # Se pinta el fondo de la ventana

# 	pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)
# 	pygame.display.flip()
	
    



#display

contadorU = 0
contadorD = 0

letras = ""

bandera_2 = True
while bandera_2:
    
    if contadorU < 10:
        concatenacion = str(contadorD) + str(contadorU)
        print(concatenacion)
    else:
        concatenacion = str(contadorD) + str(letras)
        print(concatenacion)
    
    if concatenacion == "63":
        break # en caso de arduino este deberia valer 0
        # contadorU = 0
        # contadorD = 0

    
    if contadorU < 10:
        contadorU += 1

    if letras == "F":
        letras = ""
        contadorU = 0
        contadorD  += 1
        
        
    if contadorU == 10:
        letras = "A"
        contadorU = 12
    elif letras == "A":
        letras = "B"
    elif letras == "B":
        letras = "C"
    elif letras == "C":
        letras = "D"
    elif letras == "D":
        letras = "E"
    elif letras == "E":
        letras = "F"




