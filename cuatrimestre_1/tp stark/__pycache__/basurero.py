from data_stark import lista_personajes
from datos_stark import *


# Desafío #02:
# Usando como base lo realizado en el anterior desafío realizar los siguientes
# informes en un menú
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
#    género NB

# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia

# NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú
from data_stark import lista_personajes
from datos_stark import *


# Desafío #02:
# Usando como base lo realizado en el anterior desafío realizar los siguientes
# informes en un menú
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
#    género NB

# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia

# NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú
#def informe_de_menu ():


#A
#inpresion_de_datos("NB")

#B
#print(maximo_por_genero(lista_personajes,"F","altura"))

#C
#print(maximo_por_genero(lista_personajes,"M","altura"))

#D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
#print(minimo_por_genero(lista_personajes,"F","fuerza"))

# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
#print(minimo_por_genero(lista_personajes,"NB","poder"))

# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de 
# género NB
# print(promedio_por_genero(lista_personajes,"NB","fuerza"))

# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
#cantidad_color_de_ojos_o_pelo(lista_personajes,"ojos")

# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
#cantidad_color_de_ojos_o_pelo(lista_personajes,"pelo")

# I. Listar todos los superhéroes agrupados por color de ojos.
#print(agrupar_por_inteligenicia_color_de_ojos(lista_personajes,"color_ojos"))


# J. Listar todos los superhéroes agrupados por tipo de inteligencia
#print(agrupar_por_inteligenicia_color_de_ojos(lista_personajes,"inteligencia"))


# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
#    género NB
# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia





# def inpresion_de_datos (lista:list,GENERO:str):
#     """"
#     genros validos = F / M / NB /
#     """
#     for i in lista_personajes:
#         genero = i["genero"]
#         if GENERO != any:
#             if genero == GENERO :
#                 print(
#                         f'Nombre : {i["nombre"]}\n'
#                     )
#                 print("no hay datos")
#         else:
#             print("no hay datos")
            
#     print("sin mas datos")        
# inpresion_de_datos("NB")




# def obtener_dato()-> bool :
#     """
#     retorna false si no encuentra nombre o el dict esta vacio
#     """
#     for i in enciclopedia:
#         for clave, Valor in i.items():
#             #tamaño = clave+Valor
#             #print(len(tamaño))
#             if len(clave)>0 and "nombre" in clave:
#                 #print(clave,Valor)
#                 mensaje = f"sad{clave,Valor}"
#             else :
#                 mensaje =  f"dsk{clave,Valor}"
#                 #print(f"sad{clave,Valor}")
#         return mensaje

# print(obtener_dato(librito))

for personaje in lista_personajes:
    for clave, valor in personaje.items():
        if type(valor) == int or (type(valor) == float and valor.is_integer()) or (type(valor) == str and valor.replace('.', '', 1).isdigit()):
            valor_numerico = float(valor) if '.' in valor else int(valor)
            personaje[clave] = valor_numerico
def nombre_por_genero(lista,genero):
    mensaje_defecto = print("no hay ningun personaje con esas caracteristicas")

    if genero != any:
        for personaje in lista:
            if personaje["genero"] == genero:
                for i in personaje:
                    print(f"{i}:{personaje[i]}")
    else:
        return mensaje_defecto
nombre_por_genero(lista_personajes,"M")


#A
#inpresion_de_datos("NB")

#B
#print(maximo_por_genero(lista_personajes,"F","altura"))

#C
#print(maximo_por_genero(lista_personajes,"M","altura"))

#D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
#print(minimo_por_genero(lista_personajes,"F","fuerza"))

# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
#print(minimo_por_genero(lista_personajes,"NB","poder"))

# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de 
# género NB
# print(promedio_por_genero(lista_personajes,"NB","fuerza"))

# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
#cantidad_color_de_ojos_o_pelo(lista_personajes,"ojos")

# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
#cantidad_color_de_ojos_o_pelo(lista_personajes,"pelo")

# I. Listar todos los superhéroes agrupados por color de ojos.
#print(agrupar_por_inteligenicia_color_de_ojos(lista_personajes,"color_ojos"))


# J. Listar todos los superhéroes agrupados por tipo de inteligencia
#print(agrupar_por_inteligenicia_color_de_ojos(lista_personajes,"inteligencia"))
# bandera = True
# while (bandera):
#     print(
#         "    (•-•)  (#_<)\n"
#         "    [> <]  /> <\  \n"
#         "A - Nombre de los super Heroes de genero NB\n"
#         "B - Personaje mas alto de Genero F\n"
#         "C - Personaje mas alto de Genero M\n"
#         "D - Personaje mas debil de genero M\n"
#         "E - Personaje mas devil de genero NB\n"
#         "F - Fuerza promedio de los super heroes NB\n"
#         "G - cantidad de super heroes que tienen cada tipo de color de ojos\n"
#         "H - cantidad de super heroes que tienen cada tipo de color de pelo \n"
#         "i - listado de todos los super heroes agrupados por color de ojos\n"
#         "J - Listado todos los superhéroes agrupados por tipo de inteligencia\n"
#     )
#     respuesta = input()
# ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     if  respuesta =="A":
        
# ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="B":

# ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#     elif respuesta =="C":
        
# ##////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="D":
    
# ##////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="E":
                
# ##////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="F":
    
# ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="G":

# ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#     elif respuesta =="H":
        
# ##////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="I":
    
# ##////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="J":
                
# ##////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     elif respuesta =="K":
#         bandera = False
# #////////////////////////    
#     else :
#         print("#####################################(´。＿。｀)#######")        
#         print("############ ERRORRRRRRRRRRRRRRRRRRR #################")       
#         print("######### INGRESE OPCION VALIDA  #####################")
#         print("######################################################")

#def informe_de_menu ():

# lista_color_de_ojos = []
# contador_color_de_ojos = {}

# for personaje in lista_personajes:
#     color_de_ojos = personaje["color_ojos"]
#     lista_color_de_ojos.append(color_de_ojos)

# for color in lista_color_de_ojos:
#     if color in contador_color_de_ojos:
#         contador_color_de_ojos[color] += 1
#     else:
#         contador_color_de_ojos[color] = 1

# for color, cantidad in contador_color_de_ojos.items():
#     print(f"Hay {cantidad} superhéroes con color de ojos '{color}'")


# lista_inteligencia = []
# contador_inteligencia = {}

# for personaje in lista_personajes:
#     inteligencia = personaje["inteligencia"]
#     lista_inteligencia.append(inteligencia)

# for nivel in lista_inteligencia:
#     if nivel in contador_inteligencia:
#         contador_inteligencia[nivel] += 1
#     else:
#         contador_inteligencia[nivel] = 1

# for nivel, cantidad in contador_inteligencia.items():
#     print(f"Hay {cantidad} superhéroes con nivel de inteligencia '{nivel}'")








#A
#inpresion_de_datos()

#B
#print(maximo_por_genero(lista_personajes,"F","altura"))

#C
#print(maximo_por_genero(lista_personajes,"M","altura"))

#D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
#print(minimo_por_genero(lista_personajes,"F","fuerza"))

# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
#print(minimo_por_genero(lista_personajes,"NB","poder"))

# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de 
# género NB
# print(promedio_por_genero(lista_personajes,"NB","fuerza"))

# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.


# # Tu lista de personajes
# lista_personajes = [
#     {
#         "nombre": "pacman",
#         "inteligencia": "low"
#     },
#     {
#         "nombre": "Rocket Raccoon",
#         "inteligencia": "average"
#     },
#     {
#         "nombre": "Wolverine",
#         "inteligencia": "good"
#     },
#     {
#         "nombre": "Howard the Duck",
#         "inteligencia": "low"
#     },
#     # ... otros personajes ...
# ]

# # Diccionario para agrupar personajes por nivel de inteligencia

# personajes_por_inteligencia = {}

# # Itera sobre la lista de personajes
# for personaje in lista_personajes:
#     inteligencia = personaje["inteligencia"]
#     nombre = personaje["nombre"]
#     # Verifica si el nivel de inteligencia ya es una clave en el diccionario
#     if inteligencia in personajes_por_inteligencia:
#         # Si existe, agrega el personaje a la lista existente
#         personajes_por_inteligencia[inteligencia]

#     else:
#         # Si no existe, crea una nueva clave con una lista que contiene el personaje
#         personajes_por_inteligencia[inteligencia] = [personaje]
# Ahora tienes un diccionario donde los personajes están agrupados por nivel de inteligencia
# print(personajes_por_inteligencia[""])

# for i in lista_personajes:
#     #print (i["color_ojos"])
#     print (i["color_pelo"])





# # Tu lista de personajes con datos adicionales
# lista_personajes = [
#     {
#         "nombre": "Howard the Duck",
#         "inteligencia": "low",
#         "identidad": "Howard T. Duck",
#         "empresa": "Marvel Comics",
#         "altura": "91.44",
#         "peso": "27.22",
#         "genero": "M",
#         "color_ojos": "Black",
#         "color_pelo": "White",
#         "fuerza": "28",
#     },
#     {
#         "nombre": "Rocket Raccoon",
#         "inteligencia": "average",
#         "identidad": "Subject 89P13",
#         "empresa": "Guardians of the Galaxy",
#         "altura": "71.12",
#         "peso": "25.4",
#         "genero": "M",
#         "color_ojos": "Brown",
#         "color_pelo": "Brown",
#         "fuerza": "30",
#     },
#     {
#         "nombre": "Wolverine",
#         "inteligencia": "good",
#         "identidad": "Logan",
#         "empresa": "X-Men",
#         "altura": "160.02",
#         "peso": "135.63",
#         "genero": "M",
#         "color_ojos": "Blue",
#         "color_pelo": "Black",
#         "fuerza": "55",
#     },
#     # ... otros personajes ...
# ]

# # Diccionario para agrupar personajes por nivel de inteligencia con nombre e inteligencia
# personajes_por_inteligencia = {}

# # Itera sobre la lista de personajes
# for personaje in lista_personajes:
#     nombre = personaje["nombre"]
#     inteligencia = personaje["inteligencia"]
    
#     # Crea un nuevo diccionario para cada personaje con nombre e inteligencia
#     personaje_resumido = {
#         "nombre": nombre,
#         "inteligencia": inteligencia
#     }

#     # Verifica si el nivel de inteligencia ya es una clave en el diccionario
#     if inteligencia in personajes_por_inteligencia:
#         # Si existe, agrega el personaje resumido a la lista existente
#         personajes_por_inteligencia[inteligencia].append(personaje_resumido)
#     else:
#         # Si no existe, crea una nueva clave con una lista que contiene el personaje resumido
#         personajes_por_inteligencia[inteligencia] = [personaje_resumido]

# # Ahora tienes un diccionario donde los personajes están agrupados por nivel de inteligencia con nombre e inteligencia
# print(personajes_por_inteligencia)





# # Tu lista de personajes con datos adicionales
# lista_personajes = [
#     {
#         "nombre": "Howard the Duck",
#         "inteligencia": "low",
#         "identidad": "Howard T. Duck",
#         "empresa": "Marvel Comics",
#         "altura": "91.44",
#         "peso": "27.22",
#         "genero": "M",
#         "color_ojos": "Black",
#         "color_pelo": "White",
#         "fuerza": "28",
#     },
#     {
#         "nombre": "Rocket Raccoon",
#         "inteligencia": "average",
#         "identidad": "Subject 89P13",
#         "empresa": "Guardians of the Galaxy",
#         "altura": "71.12",
#         "peso": "25.4",
#         "genero": "M",
#         "color_ojos": "Brown",
#         "color_pelo": "Brown",
#         "fuerza": "30",
#     },
#     {
#         "nombre": "Wolverine",
#         "inteligencia": "good",
#         "identidad": "Logan",
#         "empresa": "X-Men",
#         "altura": "160.02",
#         "peso": "135.63",
#         "genero": "M",
#         "color_ojos": "Blue",
#         "color_pelo": "Black",
#         "fuerza": "55",
#     },
#     # ... otros personajes ...
# ]

# # Diccionario para agrupar personajes por nivel de inteligencia con nombre e inteligencia
# personajes_por_inteligencia = {}

# # Itera sobre la lista de personajes
# for personaje in lista_personajes:
#     nombre = personaje["nombre"]
#     inteligencia = personaje["inteligencia"]
    
#     # Crea un nuevo diccionario para cada personaje con nombre e inteligencia
#     personaje_resumido = {
#         "nombre": nombre,
#         #"inteligencia": inteligencia
#     }

#     # Verifica si el nivel de inteligencia ya es una clave en el diccionario
#     if inteligencia in personajes_por_inteligencia:
#         # Si existe, agrega el personaje resumido a la lista existente
#         personajes_por_inteligencia[inteligencia].append(personaje_resumido)
#     else:
#         # Si no existe, crea una nueva clave con una lista que contiene el personaje resumido
#         personajes_por_inteligencia[inteligencia] = [personaje_resumido]

# # Ahora tienes un diccionario donde los personajes están agrupados por nivel de inteligencia con nombre e inteligencia

# #print(personajes_por_inteligencia["good"])



# Tu lista de personajes con datos adicionales


# Crear un diccionario con listas vacías como valores iniciales
# The above code is creating a dictionary called `personajes_por_inteligencia` that groups the names
# of characters by their intelligence level. It iterates over a list of characters and for each
# character, it retrieves the name and intelligence level. If the intelligence level is not already a
# key in the dictionary, it creates an empty list. Then, it appends the character's name to the
# corresponding list in the dictionary. Finally, it prints the `personajes_por_inteligencia`
# dictionary.
# The above code is creating a dictionary called `personajes_por_inteligencia` that groups the names
# of characters by their intelligence level. It iterates over a list of characters and for each
# character, it retrieves the name and intelligence level. If the intelligence level is not already a
# key in the dictionary, it creates an empty list. Then, it appends the character's name to the
# corresponding list in the dictionary. Finally, it prints the `personajes_por_inteligencia`
# dictionary.
# The above code is creating a dictionary called `personajes_por_inteligencia` that groups the names
# of characters by their intelligence level. It iterates over a list of characters and for each
# character, it retrieves the name and intelligence level. If the intelligence level is not already a
# key in the dictionary, it creates an empty list. Then, it appends the character's name to the
# corresponding list in the dictionary. Finally, it prints the `personajes_por_inteligencia`
# dictionary.
# personajes_por_inteligencia = {}

# # Itera sobre la lista de personajes
# for personaje in lista_personajes:
#     nombre = personaje["nombre"]
#     inteligencia = personaje["inteligencia"]
    
#     # Si la inteligencia no es una clave en el diccionario, crea una lista vacía
#     if inteligencia not in personajes_por_inteligencia:
#         personajes_por_inteligencia[inteligencia] = []
    
#     # Agrega el nombre del personaje a la lista correspondiente
#     personajes_por_inteligencia[inteligencia].append(nombre)

# # Ahora tienes un diccionario donde los nombres de los personajes están agrupados por nivel de inteligencia
# print(personajes_por_inteligencia)







# # for i in personaje_resumido:
# #     print(i["nombre"])

# for i in lista_personajes:
#     nombre = i["nombre"]
#     inteligencia = i ["inteligencia"]





# # Crear un diccionario con listas vacías como valores iniciales
# mi_diccionario = {
#     "clave1": ["batman","superman"],
#     "clave2": ["luffi","zoro"],
#     "clave3": ["picachu","charmander"],
#     # Puedes agregar más claves si es necesario
# }

# # Puedes agregar elementos a las listas en el diccionario de la siguiente manera
# mi_diccionario["clave1"].append("elemento1")
# mi_diccionario["clave1"].append("elemento2")

# mi_diccionario["clave2"].append("elemento3")

# # Ahora el diccionario contiene listas con elementos

# candena = "\n"
# mi_diccionario = mi_diccionario.values() 
# print(mi_diccionario)

















# for personaje in lista_personajes:
#     inteligencia = personaje["inteligencia"]
#     inteligencia == "good"
#     nombre = personaje["nombre"]
#     peso = personaje["peso"]
    
#     ##Imprime la inteligencia, el nombre y el peso del personaje
#     print(f"Nombre: {nombre}, Inteligencia: {inteligencia}, Peso: {peso}")

    

# Este código recorre la lista de personajes y, en cada iteración, accede a la inteligencia, 
# el nombre y el peso del personaje. Luego, utiliza print() para imprimir estos valores en el formato 
# deseado, que muestra el nombre, la inteligencia y el peso de cada personaje.






# mas_devil_femenino = None
# lista_mas_devil_femenino =[]
# for personaje in lista_personajes:
#     if personaje['genero'] == "F":
#         if mas_devil_femenino == None or float(personaje['fuerza']) > mas_devil_femenino:
#             mas_devil_femenino = float(personaje['fuerza'])
#             lista_mas_devil_femenino = [personaje]
#         elif mas_devil_femenino == float(personaje['fuerza']):
#             lista_mas_devil_femenino.append(personaje)
# for i in lista_mas_devil_femenino:
#     print(i["nombre"])






# Crear un diccionario con listas vacías como valores iniciales
#personajes_por_inteligencia = {}

# # Itera sobre la lista de personajes
# for personaje in lista_personajes:
#     inteligencia = personaje["inteligencia"]
    
#     # Si la inteligencia no es una clave en el diccionario, crea una lista vacía
#     if inteligencia not in personajes_por_inteligencia:
#         personajes_por_inteligencia[inteligencia] = []
    
#     # Agrega el personaje completo a la lista correspondiente
#     personajes_por_inteligencia[inteligencia].append(personaje)

# # Ahora tienes un diccionario donde los personajes están agrupados por nivel de inteligencia
# print(personajes_por_inteligencia)

# def contar_color_ojos_y_pelo(personajes):
#     # Inicializa diccionarios para contar color de ojos y color de pelo
#     color_ojos_count = {}
#     color_pelo_count = {}

#     # Itera sobre la lista de personajes
#     for personaje in personajes:
#         color_ojos = personaje.get("color_ojos", "Desconocido")
#         color_pelo = personaje.get("color_pelo", "Desconocido")

#         # Contar el color de ojos
#         if color_ojos in color_ojos_count:
#             color_ojos_count[color_ojos] += 1
#         else:
#             color_ojos_count[color_ojos] = 1

#         # Contar el color de pelo
#         if color_pelo in color_pelo_count:
#             color_pelo_count[color_pelo] += 1
#         else:
#             color_pelo_count[color_pelo] = 1

#     return color_ojos_count, color_pelo_count

# # Llama a la función con la lista de personajes
# resultados_color_ojos, resultados_color_pelo = contar_color_ojos_y_pelo(lista_personajes)

# # Imprime los resultados
# print("Número de superhéroes por color de ojos:")
# print(resultados_color_ojos)
# print("\nNúmero de superhéroes por color de pelo:")
# print(resultados_color_pelo)




# lista_color_de_pelo = []
# contador_color_de_pelo = {}

# for personaje in lista_personajes:
#     color_de_pelo = personaje["color_ojos"]
#     lista_color_de_pelo.append(personaje["color_ojos"])

# for color in lista_color_de_pelo:

#     if color in contador_color_de_pelo:
#         contador_color_de_pelo[color] += 1

#     else:
#         contador_color_de_pelo[color] = 1 

# #print(f"lista color de pelo {lista_color_de_pelo}" )

# for color ,cantidad in contador_color_de_pelo.items():
#     print(f"hay {cantidad} superheroes con el color de pelo {color}")


# lista_color_pelo = []
# conteo_colores_pelo = {}
# for personaje in lista_personajes:
#     color_pelo = personaje['color_pelo']
#     lista_color_pelo.append(color_pelo)

# for color in lista_color_pelo:
#     if color in conteo_colores_pelo:
#         conteo_colores_pelo[color] += 1
#     else:
#         conteo_colores_pelo[color] = 1

# for color, cantidad in conteo_colores_pelo.items():
#     print(f'CON COLOR DE PELO {color} HAY {cantidad} SUPERHEROES')

                                
    # print("sin mas datos")        
#inpresion_de_datos("NB")
# def impresion_de_datos(genero):
#     """
#     Géneros válidos: F (Femenino), M (Masculino), NB (No binario)
#     """
#     for personaje in lista_personajes:
#         gen = personaje["genero"]
#         altura = float(personaje["altura"])
#         peso = float(personaje["peso"])
        
#         if gen == "":
#             print("Sin datos de género")
#         elif gen == genero:
#             print(
#                 f'Nombre: {personaje["nombre"]}\n'
#                 f'Peso: {peso}\n'
#                 f'Fuerza: {personaje["fuerza"]}\n'
#                 f'Altura: {altura}\n'
#                 f'Género: {gen}\n'
#                 f'Empresa: {personaje["empresa"]}\n'
#                 f'Identidad: {personaje["identidad"]}\n'
#                 f'Inteligencia: {personaje["inteligencia"]}\n'
#                 f'Color de ojos: {personaje["color_ojos"]}\n'
#                 f'Color de pelo: {personaje["color_pelo"]}\n'
#             )
    
# # Llama a la función para imprimir datos de personajes con género "NB"
# impresion_de_datos("NB")


