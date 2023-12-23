# Desafío #02
# FERNANDEZ JUAN MANUEL 

from data_stark import lista_personajes
from datos_stark_2 import *

"""
TP : 2  STARK  
NOMBRE :JUAN MANUEL
APELLIDO FERNANDEZ
# Desafío #02
AUTOCORREGIDO SI
"""

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


def stark_marvel_app_2():
    bandera = True
    while (bandera):
        print(
            " \n"
            " 🚀 stark 2# 🚀\n"
            "                \n"
            "    (•-•)  (#_<)  \n"
            "    [> <]  /> <\   \n"
            "1  - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de genero NB📃\n"
            "2  - Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n"
            "3  - Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n"
            "4  - Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n"
            "5  - Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n"
            "6  - Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n"
            "7  - Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
            "8  - Determinar cuántos superhéroes tienen cada tipo de color de pelo. ✂\n"
            "9  - Listar todos los superhéroes agrupados por color de ojos. 👀\n"
            "10 - Listar todos los superhéroes agrupados por tipo de inteligencia🧠\n"
            "11 - SALIR DEL PROGRAMA"
        )
        respuesta = input()
        match respuesta:
    ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "1":
                (nombre_por_genero(lista_personajes,"NB"))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "2":
                print(maximo_por_genero_floot(lista_personajes,"F","altura"))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "3":
                print(maximo_por_genero_floot(lista_personajes,"M","altura"))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case  "4":
                print(minimo_por_genero(lista_personajes,"M","fuerza"))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case  "5":
                print(minimo_por_genero(lista_personajes,"NB","fuerza"))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case  "6":
                print(promedio_por_genero(lista_personajes,"NB","fuerza"))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case  "7":
                cantidad_color_de_ojos_o_pelo(lista_personajes,"ojos")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case  "8":
                cantidad_color_de_ojos_o_pelo(lista_personajes,"pelo")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case  "9":

                f =agrupar_por_inteligencia_color_de_ojos(lista_personajes, "color_ojos")
                print("-" * 52)
                print(f"{'color de ojos':25}|  {'nombres':23} ")
                for color, nombres in f.items():
                    print("-" * 52)
                    print(f" {color}: ")
                    for nombre in nombres:
                        print(f" {'':23} |  - {nombre:20} |")
                print("-" * 52)

        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case  "10":
                f =agrupar_por_inteligencia_color_de_ojos(lista_personajes, "inteligencia")
                print("-" * 52)
                print(f"{'inteligencia':25}|  {'nombres':23} ")
                for color, nombres in f.items():
                    print("-" * 52)
                    print(f" {color}: ")
                    for nombre in nombres:
                        print(f" {'':23} |  - {nombre:20} |")
                print("-" * 52)

        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////     
            case  "11":
                bandera = False
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
            case _:
                print("#####################################(´。＿。｀)#######")        
                print("############ ERRORRRRRRRRRRRRRRRRRRR #################")       
                print("######### INGRESE OPCION VALIDA  #####################")
                print("######################################################")

stark_marvel_app_2()