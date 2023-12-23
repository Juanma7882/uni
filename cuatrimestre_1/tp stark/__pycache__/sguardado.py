#los datos de los mas fuertes
# el_mas_fuerte = None
# los_mas_fuertes = []
# los_mas_fuertes_identidad = []
# los_mas_fuertes_peso = []
# #los datos de los mas deviles
# el_mas_devil = None
# los_mas_deviles = []
# los_mas_deviles_identidad = []
# los_mas_deviles_peso = []
# #D
# contadorM = 0
# peso_superheroe_masculios = 0
# #E
# fuerza_femenina_total = 0
# nombre_superheroes_mayor_al_promedio_femenino = []
# peso_superheroes_mayor_al_promedio_femenino = []
# contadorF = 0
# fuerza_femenina_promedio = 0

# for i in (lista_personajes):


#     # altura = float(i["altura"])
#     # peso = float(i["peso"])
#     # mensaje1 = "loz datos de todos los sperheroes son:\n"
#     # mensaje1 =     f'Nombre : {i["nombre"]}\n'
#     # mensaje1 =     f'Identidad : {i["identidad"]}\n'
#     # mensaje1 =     f'Empresa : {i["empresa"]}\n'
#     # mensaje1 =     f'Color de ojos : {i["color_ojos"]}\n'
#     # mensaje1 =     f'color de pelo : {i["color_pelo"]}\n'
#     # mensaje1 =     f'Fuerza : {i["fuerza"]}\n'
#     # mensaje1 =     f'Inteligencia : {i["inteligencia"]}'
#     # mensaje1 =     f'Altura : {altura}\n'
#     # mensaje1 =     f'peso : {peso}\n'
#     # mensaje1 =     f'{i["genero"]}\n'
    
# # print(mensaje1)


#     if el_mas_fuerte == None or int(el_mas_fuerte) < int(i["fuerza"]):
#         el_mas_fuerte = (i["fuerza"])

#     if el_mas_devil == None or int(el_mas_devil) > int(i["fuerza"]):
#         el_mas_devil = (i["fuerza"])

    # match  i["genero"]:
        # case "M":
        #     contadorM += 1
        #     peso_superheroe_masculios += float(i["peso"])
        # case "F":
        #     fuerza_femenina_total += int(i["fuerza"]) 
        #     contadorF += 1
    

# # #     print(i["genero"], i["fuerza"])
# peso_promedio = float(peso_superheroe_masculios / contadorM)
#fuerza_femenina_promedio= float(fuerza_femenina_total/contadorF)
# print(fuerza_femenina_total)
# print(fuerza_femenina_promedio)



# fuerza_femenina_total = 0
        # nombre_superheroes_mayor_al_promedio_femenino = []
        # peso_superheroes_mayor_al_promedio_femenino = []
        # contadorF = 0
        # fuerza_femenina_promedio = 0
        # for i in (lista_personajes):
        #     match  i["genero"]:
        #         case "F":
        #             fuerza_femenina_total += int(i["fuerza"]) 
        #             contadorF += 1
        # fuerza_femenina_promedio= float(fuerza_femenina_total/contadorF)
        # for i in (lista_personajes):
        #     if int(fuerza_femenina_promedio) < int(i["fuerza"]):
        #         peso = float(i["peso"])
        #         nombre_superheroes_mayor_al_promedio_femenino.append(i["nombre"])
        #         peso_superheroes_mayor_al_promedio_femenino.append(peso)

        # mensaje5 = f"nombre y peso de los super heroes que superen el promedio de fuerza femenina\n "
        # mensaje5 += f"Nombre : {nombre_superheroes_mayor_al_promedio_femenino}\n"
        # mensaje5 += f"peso : {peso_superheroes_mayor_al_promedio_femenino}\n"
        # print(mensaje5)


        
#for i in(lista_personajes):
# #     if el_mas_fuerte == i["fuerza"]:
# #         los_mas_fuertes.append(i["fuerza"])
# #         los_mas_fuertes_identidad.append(i["identidad"])
# #         peso_de_los_mas_fuertes = float(i["peso"])
# #         los_mas_fuertes_peso.append(peso_de_los_mas_fuertes)

# #     if el_mas_devil == i["fuerza"]:
# #         los_mas_deviles.append(i["fuerza"])
# #         los_mas_deviles_identidad.append(i["identidad"])
# #         peso_de_los_mas_deviles = float(i["peso"])
# #         los_mas_deviles_peso.append(peso_de_los_mas_deviles)

#Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
#género) los cuales su fuerza supere a la fuerza promedio de todas las
#superhéroes de género femenino
    # if float(fuerza_femenina_promedio) < int(i["fuerza"]):
    #     peso = float(i["peso"])
    #     nombre_superheroes_mayor_al_promedio_femenino.append(i["nombre"])
    #     peso_superheroes_mayor_al_promedio_femenino.append(peso)


# print(nombre_superheroes_mayor_al_promedio_femenino)
# print(peso_superheroes_mayor_al_promedio_femenino)
# print(fuerza_femenina_promedio)



# # print("######################################################")        
# # print("############ EL PERSONAJE MAS FUERTE #################")       
# # print("######################################################")
# # mensaje = f'los datos del o el personaje mas fuerte son: \n'
# # mensaje += f"identidad {los_mas_fuertes_identidad}\n"
# # mensaje +=f"peso {los_mas_fuertes_peso}\n"
# # mensaje +=f"fuerza {los_mas_fuertes}\n"
# # mensaje += "\n"
# # mensaje += "##################################################\n"
# # mensaje += "############## EL PERSONAJE MAS DEVIL ############\n"
# # mensaje += "##################################################\n"
# # mensaje += f'los datos del o el personaje mas devil  son: \n'
# # mensaje += f"identidad {los_mas_deviles_identidad}\n"
# # mensaje +=f"peso {los_mas_deviles_peso}\n"
# # mensaje +=f"fuerza {los_mas_deviles}"
# # print(mensaje)




########################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# Desafío #02:
# Usando como base lo realizado en el anterior desafío realizar los siguientes
# informes en un menú
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia


# bandera = True
# while (bandera):
#     print(
#         "    (•-•)  (#_<)  \n"
#         "    [> <]  /> <\   \n"
#         "1  - Nombre de los super Heroes de genero NB\n"
#         "2  - Personaje mas alto de Genero F\n"
#         "3  - Personaje mas alto de Genero M\n"
#         "4  - Personaje mas debil de genero M\n"
#         "5  - Personaje mas devil de genero NB\n"
#         "6  - Fuerza promedio de los super heroes NB\n"
#         "7  - cantidad de super heroes que tienen cada tipo de color de ojos\n"
#         "8  - cantidad de super heroes que tienen cada tipo de color de pelo \n"
#         "9  - listado de todos los super heroes agrupados por color de ojos\n"
#         "10 - Listado todos los superhéroes agrupados por tipo de inteligencia\n"
#         "11 - SALIR DEL PROGRAMA"
#     )
#     respuesta = input()
# ##  A  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     if  respuesta =="1":
#         (nombre_por_genero(lista_personajes,"NB"))
# ##  B  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="2":
#         print(maximo_por_genero_floot(lista_personajes,"F","altura"))
# ##  C  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="3":
#         print(maximo_por_genero_floot(lista_personajes,"M","altura"))
# ##  D  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="4":
#         print(minimo_por_genero_int(lista_personajes,"M","fuerza"))
# ##  E  //////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="5":
#         print(minimo_por_genero_int(lista_personajes,"NB","fuerza"))
# ##  F  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="6":
#         print(promedio_por_genero(lista_personajes,"NB","fuerza"))
# ##  G  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="7":
#         cantidad_color_de_ojos_o_pelo(lista_personajes,"ojos")
# ##  H  //////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="8":
#         cantidad_color_de_ojos_o_pelo(lista_personajes,"pelo")
# ##  I  //////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="9":
#         print(agrupar_por_inteligenicia_color_de_ojos(lista_personajes,"color_ojos"))
# ##  J  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="10":
#         print(agrupar_por_inteligenicia_color_de_ojos(lista_personajes,"inteligencia"))
# ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////     
#     elif respuesta =="11":
#         bandera = False
# ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
#     else :
#         print("#####################################(´。＿。｀)#######")        
#         print("############ ERRORRRRRRRRRRRRRRRRRRR #################")       
#         print("######### INGRESE OPCION VALIDA  #####################")
#         print("######################################################")



##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# for i in lista_personajes:
#     print(type(i["peso"]))
    

# for i in lista_personajes:
#     (i["altura"]) = (i["altura"])
#     peso = (i["peso"])
#     fuerza = (i["fuerza"])
# # print(type("altura"))

#     if (i["altura"]) == float((i["altura"])):
#         mensaje_A = "NO se casteo a flotante\n"
#     elif (i["altura"]) is not float((i["altura"])):
#         (i["altura"]) = float(i["altura"])
#         mensaje_A = "se casteo altura a float\n"

#     if peso == float(peso):
#         mensaje_P = "peso NO se casteo a flotante\n"
#     elif peso is not float(peso):
#         (i["peso"]) = float(i["peso"])
#         mensaje_P = "peso se casteo peso a float\n"

#     if fuerza == int(fuerza):
#         mensaje_F = "NO se casteo a flotante\n"
#     elif fuerza is not int(fuerza):
#         (i["fuerza"]) = int(i["fuerza"])
#         mensaje_F = "se casteo fuerza a float\n"

# print (mensaje_A)
# print(type(i["altura"]))

# print(f"{mensaje_A}{mensaje_P}{mensaje_F}")