from data_stark import *
"""
TP : 2  STARK  
NOMBRE :JUAN MANUEL
APELLIDO FERNANDEZ
# Desafío #02
AUTOCORREGIDO SI
"""
# ///////////////////////////////////////////////////////////////////////////////////////////////
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB


def nombre_por_genero(lista:list, genero:str):
    """"
    se ingresa una lista y el genero:
    genros validos : F / M / NB /
    """
    bandera = True
    for i in lista:
        if i["genero"] == genero:
            print(i["nombre"])
            bandera = False

    if  bandera == True:
        print("NO EXISTEN DATOS")    

# (nombre_por_genero(lista_personajes,"M"))


# /////////////////////////////////////////////////////////////////////////////////////////////////
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M


def maximo_por_genero_floot(lista:list,M_OR_F:str,variable_a_encontrar:float):
    """"
    EJEMPLO DE USO: maximo por genero(lista_hero,"M","altura")\n
    Tambien se puede usar para el genero NB experimental
    """
    el_mas_alto = None
    nombre = []
    bandera= False
    for i in (lista):
        variable_de_maximo_a_buscar = float(i[variable_a_encontrar])
        caracter_especifico = i["genero"]

        if caracter_especifico == M_OR_F :
            if (el_mas_alto) == None or float(el_mas_alto) < float(variable_de_maximo_a_buscar):
                el_mas_alto = variable_de_maximo_a_buscar
                bandera = True


    for i in lista:
        caracter_especifico = i["genero"]
        if caracter_especifico == M_OR_F : 
            if float(el_mas_alto) == float(i[variable_a_encontrar]):
                nombre.append(i["nombre"])

    if bandera == False:
        nombre.append("sin datos" )
    return nombre

# print(maximo_por_genero_floot(lista_personajes,"M","altura"))

# m = (maximo_por_genero_floot(lista_personajes,"M","altura"))
# for i in m:
#     print(i)

# f = (maximo_por_genero_floot(lista_personajes,"F","altura"))
# for i in f:
#     print(i)

# /////////////////////////////////////////////////////////////////////////////////////////////////
# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB

def minimo_por_genero(lista:list,M_OR_F:str,variable_a_encontrar)->str:
    """
    EJEMPLO DE USO: minimo por genero(lista_hero,"M","poder")\n
    Tambien se puede usar para el genero F Y NB experimental
    """
    el_mas_bajo = None
    nombre = []
    bandera= False
    for i in (lista):
        variable_de_maximo_a_buscar = float(i[variable_a_encontrar])
        caracter_especifico = i["genero"]

        if caracter_especifico == M_OR_F :
            if (el_mas_bajo) == None or int(el_mas_bajo) > int(variable_de_maximo_a_buscar):
                el_mas_bajo = variable_de_maximo_a_buscar
                bandera = True

    for i in lista:
        caracter_especifico = i["genero"]
        if caracter_especifico == M_OR_F : 
            if int(el_mas_bajo) == int(i[variable_a_encontrar]):
                nombre.append(i["nombre"])

    if bandera == False:
        nombre.append("sin datos" )
    return nombre

# print(minimo_por_genero_float(lista_personajes,"F","fuerza"))


# m = (minimo_por_genero_float(lista_personajes,"M","fuerza"))
# for i in m:
#     print(i)

# nb = (minimo_por_genero_float(lista_personajes,"NB","fuerza"))
# for i in nb:
#     print(i)



# def minimo_por_genero_int(lista:list,M_OR_F:str,variable_a_encontrar:int)->str:
#     """
#     EJEMPLO DE USO: minimo por genero(lista_hero,"M","poder")\n
#     Tambien se puede usar para el genero F Y NB experimental
#     """
#     el_mas_bajo = None
#     nombres = []
#     bandera = False
#     datos = []
#     for i in lista:
#         variable_de_minimo_a_buscar = (i[variable_a_encontrar])
#         caracter_especifico = i["genero"]
#         if caracter_especifico == M_OR_F :
#                 if (el_mas_bajo) == None or int(el_mas_bajo) > int(variable_de_minimo_a_buscar):
#                     variable_de_minimo_a_buscar = int(i[variable_a_encontrar])
#                     el_mas_bajo = variable_de_minimo_a_buscar
#                     nombre = (i["nombre"])
#                     nombres.append(nombre)
#                     bandera = True
#     for i in lista:
#         variable_de_minimo_a_buscar = (i[variable_a_encontrar])
#         caracter_especifico = i["genero"]
#         if caracter_especifico == M_OR_F :
#                 if int(el_mas_bajo) == int(variable_de_minimo_a_buscar):
#                     datos.append(str(i["nombre"]))

#     if bandera == True:
#         # mensaje = f"su {variable_a_encontrar} es {el_mas_bajo} "
        
#         for i in datos:
#             mensaje = i
#     if bandera == False:
#         mensaje = "NO hay datos "

#     return mensaje
# print(minimo_por_genero_int(lista_personajes,"F","fuerza"))

# /////////////////////////////////////////////////////////////////////////////////////////////////
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de 
# género NB
def promedio_por_genero (lista:list,generos:str,Variable_promedio:int):
    """
    generos puede ser: "M", "F" o "NB" UNICAMENETE
    """
    acumulador = 0
    contador = 0
    bandera = False
    for i in lista:
        genero = i["genero"]
        poder =  int(i[Variable_promedio])
        if generos == genero:
                contador +=1
                acumulador +=  poder
                bandera = True
        else :
            pass

    if contador >0:
        promedio = float(acumulador / contador) 
        mensaje = F"El promedio de poder es {(promedio):.2f}"
    elif bandera == False:
        mensaje = "NO hay datos"
    return(mensaje)
# print(promedio_por_genero(lista_personajes,"NB","fuerza"))


# /////////////////////////////////////////////////////////////////////////////////////////////////
# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.


# def cantidad_color_de_ojos_o_pelo(lista:list,color_de:str):
    
#     """
#     ojos/pelo
#     """
#     if color_de == "ojos":
#         ojos_o_pelo = "color_ojos"
#     elif color_de == "pelo":
#         ojos_o_pelo = "color_pelo"

#     lista_color_de_pelo = []
#     contador_color_de_pelo = {}

#     for i in lista:
        
#         color_de_pelo = i[ojos_o_pelo]
#         lista_color_de_pelo.append(color_de_pelo)

#     for color in lista_color_de_pelo:
#         color_de_pelo = i[ojos_o_pelo]
#         if color_de_pelo == "" or color_de_pelo == " ":
#             pass
#         else:
#             if color in contador_color_de_pelo:
#                 contador_color_de_pelo[color] += 1
#             else:
#                 contador_color_de_pelo[color] = 1 

#     print(37*"_")
#     print(f"| {'cantidad':5}|color de {color_de:15} |")
#     print(37*"_")
#     for color ,cantidad in contador_color_de_pelo.items():
#         print(f"| {cantidad:7} |{color:24} |")
#     print(37*"_")
# cantidad_color_de_ojos_o_pelo(lista_personajes,"ojos")


def cantidad_color_de_ojos_o_pelo(lista, color_de):
    
    if color_de == "ojos":
        ojos_o_pelo = "color_ojos"
    elif color_de == "pelo":
        ojos_o_pelo = "color_pelo"

    lista_color_de_pelo = []
    contador_color_de_pelo = {}
    nombre = []
    for i in lista:
        color_de_pelo = i[ojos_o_pelo]
        if color_de_pelo == "" or color_de_pelo == " ":
            nombre.append(i["nombre"])

        if i["nombre"] != nombre:
            color_de_pelo = i[ojos_o_pelo]
            color_de_pelo = color_de_pelo.capitalize()
            lista_color_de_pelo.append(color_de_pelo)

    for color in lista_color_de_pelo:
        if color == "" or color == " ":
            pass
        else:
            if color in contador_color_de_pelo:
                contador_color_de_pelo[color] += 1
            else:
                contador_color_de_pelo[color] = 1 

    print(37*"_")
    print(f"| {'cantidad':5}|color de {color_de:15} |")
    print(37*"_")
    for color ,cantidad in contador_color_de_pelo.items():
        print(f"| {cantidad:7} |{color:24} |")
    print(37*"_")

cantidad_color_de_ojos_o_pelo(lista_personajes, "pelo")

cantidad_color_de_ojos_o_pelo(lista_personajes,"ojos")




# /////////////////////////////////////////////////////////////////////////////////////////////////
# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia



def agrupar_por_inteligencia_color_de_ojos(lista, agrupar):
    """
    agrupar = color_ojos / inteligencia
    """
    diccionario_color_de_ojos_inteligencia = {}
    for personaje in lista:
        color_de_ojos_inteligencia = personaje[agrupar].capitalize()
        nombre = personaje["nombre"]

        if color_de_ojos_inteligencia == "" or color_de_ojos_inteligencia == "No hair":
            pass
        elif color_de_ojos_inteligencia in diccionario_color_de_ojos_inteligencia:
            diccionario_color_de_ojos_inteligencia[color_de_ojos_inteligencia].append(nombre)
        else:
            diccionario_color_de_ojos_inteligencia[color_de_ojos_inteligencia] = [nombre]

    return diccionario_color_de_ojos_inteligencia


# /////////////////////////////////////////////////////////////////////////////////////////////////






# f =agrupar_por_inteligencia_color_de_ojos(lista_personajes, "inteligencia")
# f =agrupar_por_inteligencia_color_de_ojos(lista_personajes, "color_ojos")

# print("-" * 52)
# print(f"{'color de ojos':25}|  {'nombres':23} ")


# print("-" * 52)
# print(f"{'inteligencia':25}|  {'nombres':23} ")
# for color, nombres in f.items():
#     print("-" * 52)
#     print(f" {color}: ")
#     # print("-" * 52)
#     for nombre in nombres:
#         print(f" {'':23} |  - {nombre:20} |")
# print("-" * 52)







