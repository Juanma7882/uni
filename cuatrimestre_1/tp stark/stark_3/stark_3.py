#from datos_stark import *
from data_stark import *
# NOMBRE: Juan 
#APELLIDO:Fernandez

# Desafío #03: (con biblioteca propia: stark_biblioteca)
# En base a lo resuelto en la parte 1, deberían crearse las siguientes funciones

# IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
# escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
# un string, etc y que contendrá) y que es lo que retorna la función!


# 0. Crear la función 'stark_normalizar_datos()' la cual recibirá por parámetro la
# lista de héroes. La función deberá:

# ● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
# las keys que representan datos numéricos) por ejemplo fuerza (int),
# altura (float), etc

# ● Validar primero que el tipo de dato no sea del tipo al cual será
# casteado. Por ejemplo si una key debería ser entero (ejemplo fuerza)
# verificar antes que no se encuentre ya en ese tipo de dato.

# ● Si al menos un dato fue modificado, la función deberá retornar el valor
# booleano True

# ● En caso de que la lista esté vacía o ya se hayan normalizado
# anteriormente los datos se deberá retornar el valor booleano False

# ● Crear una opción en el menú que me permita normalizar los datos (No
# se debería poder acceder a ninguna otra opción del menú hasta que
# los datos esten normalizados)

# ● En caso de que la llamada a la función retorne True mostrar un
# mensaje diciendo “Datos Normalizados” sino mostrar el mensaje
# “Hubo un error al normalizar los datos. Verifique que la lista no este
# vacía o que los datos ya no se hayan normalizado anteriormente”

#mensaje = True
# for i in lista_personajes:
#     if  (i["altura"]) is not float((i["altura"])):
#         mensaje = True
#         (i["altura"]) = float(i["altura"])
#     if  (i["peso"]) is not float(i["peso"]):
#         mensaje = True
#         (i["peso"]) = float(i["peso"])
#     if   (i["fuerza"]) is not int( (i["fuerza"])):
#         mensaje = True
#         (i["fuerza"]) = int(i["fuerza"])
# # vacia =[]

def stark_normalizar_datos(lista:list)->str:
    """
    recibe la lista de personajes y la devuelve con todos los datos casteados a 
    sus respectivos tipos ya sea int floot o str
    """
    mensaje = False
    if len(lista) == 0:
            mensaje = False
    elif mensaje == False:
        for i in lista:
            for clave, valor in i.items():
                if type(valor) == str and valor.replace('.', '',).isdigit() :
                    if '.' in valor:
                        valor = float(valor)
                        i[clave] = float(i[clave])
                        
                    else:
                        valor = int(valor)
                        i[clave] = int(i[clave])
                        
                    mensaje = True
                else:
                    #es str no se hace nada
                    pass
    if mensaje == True:
        mensaje = "Datos Normalizados"
    else :
        mensaje =  "Hubo un error al normalizar los datos. Verifique que la lista no este\n"
        mensaje +=  "vacía o que los datos ya no se hayan normalizado anteriormente\n "
        mensaje +=  f"{False}"

    return mensaje

(stark_normalizar_datos(lista_personajes))
# print(stark_normalizar_datos(lista_personajes))



#//////////////////////////////////////////////////////////////////////////////////////////////
# 1.1. Crear la función ”obtener_dato()” la cual recibirá por parámetro un
# diccionario el cual representara a un héroe y también recibirá un string que
# hace referencia a una “clave” del mismo
# Validar siempre que el diccionario no esté vacío y que el mismo tenga una key
# llamada “nombre”. Caso contrario la función retornara un False

vacio = {}
librito = {"nombre" : "picachu","edad":"23","peso":"5"}
# 
enciclopedia = [{"nombre" : "picachu"},
                {"    " : "charmander"}]

# def obtener_dato(diccionario:dict,clave:str)->bool:
#     """
#     retorna false si no encuentra nombre o el diccionario esta vacio
#     """
#     mensaje = False
#     if len(diccionario) > 0 and "nombre" in diccionario :
#         # mensaje = (f"{True}")
#         mensaje = (f"{True} {clave}: {diccionario[clave]}")

#     return mensaje
# print(obtener_dato(librito,"edad"))


def obtener_dato(diccionario:dict)->bool:
    """
    retorna false si no encuentra nombre o el dict esta vacio
    y no de vuelve nada en caso contrario
    """
    mensaje = False
    if len(diccionario) > 0 and "nombre" in diccionario :
        mensaje = " "
    return mensaje
# print(obtener_dato(librito))



#//////////////////////////////////////////////////////////////////////////////////////////////
# 1.2 Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el
# cual representara a un héroe y devolverá un string el cual contenga su nombre
# formateado de la siguiente manera:
# Nombre: Howard the Duck
# Validar siempre que el diccionario no este vacío y que la key que se pide exista. Caso
# contrario la función retornara un False
# NOTA: Reutilizar la función creada en el punto anterior


# diccionario_vacio = {}
# librito = {"nombre" : "picachu"}
# enciclopedia = [{"nombre" : "picachu"},
#                 {"    " : "charmander"},
#                 {"nombre" : "pichu"}]


def obtener_nombre(diccionario:dict)->str | bool:
    """
    retorna False si no encuentra nombre o el Nombre en caso que lo encuentre 
    """
    mensaje = False
    for clave, Valor in diccionario.items():
        if (len(clave) > 0) and ("nombre" in clave):
            mensaje = f"Nombre: {Valor}"
    return mensaje


# print(obtener_nombre(librito))
# print(obtener_nombre(librito))

# #beta
# def obtener_nombre(lista_diccionario)->str | bool:
#     """
#     retorna False si no encuentra nombre o el Nombre en caso que lo encuentre 
#     """
#     guardado = []
#     bandera = False
#     for i in lista_diccionario:
#         for clave, Valor in i.items():
#             if (len(clave) > 0) and ("nombre" in clave):
#                 bandera = True
#                 mensaje = f"Nombre: {Valor}"
#                 guardado.append(mensaje)

#     if bandera == True:
#             mostrar = guardado
#     else:
#         mostrar = False
#     return mostrar
# print(obtener_nombre(lista_personajes))


#//////////////////////////////////////////////////////////////////////////////////////////////

# 2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
# diccionario el cual representara a un héroe y una key (string) la cual
# representará el dato que se desea obtener.
# ● La función deberá devolver un string el cual contenga el nombre y dato
# (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O
# CUALQUIER OTRO DATO.
# ● El string resultante debe estar formateado de la siguiente manera:
# (suponiendo que la key es fuerza)
# Nombre: Venom | fuerza: 500
# ● Validar siempre que la lista no este vacía. Caso contrario la función
# retornara un False
#obtener_nombre_y_dato

diccionario_vacio = {}
librito = {"nombre" : "picachu", "peso": "20","altura": "22.4" }
enciclopedia = [{"nombre" : "picachu","peso":"54","altura":"35"},
                {"nombre" : "charmander","peso":"54","altura":"35"}]
cero = []
uno = [{}]

def obtener_nombre_y_dato(diccionario,key:str):
    """
    recibe como parametro un diccionario y una clave del mismo
    el diccionario debe contener la clave nombre y elda dato a
    buscar caso contrario devuelve false 
    """

    lista = (len(diccionario))
    #print(lista) 
    if lista == 0:
        mensaje = False
    else:
        for i in diccionario:
            tamño_dic = len(i)
            if tamño_dic >0 : 
                print(len(i))
                mensaje = print (f"nombre : {i['nombre']:18} | {key} : {i[key]:10} ")
                #print(mensaje)
            else: 
                mensaje = False
    return (mensaje)

# print(obtener_nombre_y_dato(lista_personajes,"peso"))


#//////////////////////////////////////////////////////////////////////////////////////////////
# 3.1 Crear la función “obtener_maximo()” la cual recibirá como parámetro una lista y
# una key (string) la cual representará el dato al cual se le debe calcular su cantidad
# MÁXIMA.
# ● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
# un int o un float. Caso contrario la función retornara un False
# ● En caso de que el dato que se está buscando en el diccionario es de tipo int o
# float retornar el mayor que haya encontrado en la búsqueda.


def obtener_maximo(lista:list,variable_a_encontrar:float|int):
    """
    recive como parametro una lista y un dato al que se desea encontrar
    el maximo debe ser de tipo float o int 
    """
    maximo = None
    tamaño = len(lista)
    if tamaño == 0:
        mensaje = False
    else:
        for i in lista:
            buscar = variable_a_encontrar
            if type(i[ buscar]) is int:
                if (maximo) == None or int(maximo) < int(i[ buscar]):
                    maximo = i[ buscar]
                    mensaje = maximo
        
            elif type(i[ buscar]) is float:
                if (maximo) == None or float(maximo) < float(i[ buscar]):
                    maximo = i[ buscar]
                    mensaje = maximo
            else: #type(i["fuerza"]) is str:
                mensaje = False
    return mensaje 

#print(obtener_maximo(lista_personajes,"altura"))
        
        
#//////////////////////////////////////////////////////////////////////////////////////////////
# 3.2 Crear la función “obtener_minimo()” la cual recibirá como parámetro una lista y
# una key (string) la cual representará el dato al cual se le debe calcular su cantidad
# MÍNIMA.
# ● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
# un int o un float. Caso contrario la función retornara un False
# ● En caso de que el dato que se está buscando en el diccionario es de tipo int o
# float retornar el menor que haya encontrado en la búsqueda.

def obtener_minimo(lista:list,variable_a_encontrar:float|int):
    """
    recive como parametro una lista y un dato al que se desea encontrar
    el maximo debe ser de tipo float o int 
    """
    mimino = None
    tamaño = len(lista)
    if tamaño == 0:
        mensaje = False
    else:
        for i in lista:
            buscar = variable_a_encontrar
            if type(i[ buscar]) is int:
                if (mimino) == None or int(mimino) > int(i[ buscar]):
                    mimino = i[ buscar]
                    mensaje = mimino
        
            elif type(i[ buscar]) is float:
                if (mimino) == None or float(mimino) > float(i[ buscar]):
                    mimino = i[ buscar]
                    mensaje = mimino
            else: #type(i["fuerza"]) is str:
                mensaje = False
    return mensaje 

#print(obtener_maximo(lista_personajes,"altura"))

#//////////////////////////////////////////////////////////////////////////////////////////////
# 3.3 Crear la función 'obtener_dato_cantidad()' la cual recibira tres parámetros:
# ● La lista de héroes
# ● Un número que me indique el valor a buscar (puede ser la altura
# máxima, la altura mínima o cualquier otro dato)
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
# ‘peso’, ‘edad’, etc.
# La función deberá retornar una lista con el héroe o los heroes que cumplan
# con la condición pedida. Reutilizar las funciones hechas en los puntos 3.1 y 3.2
# Ejemplo de llamada:
# mayor_altura = obtener_maximo(lista_heroes,”altura”)
# lista_heroes_max_altura = 'obtener_dato_cantidad(lista_heroes,mayor_altura,”altura”)
# El objetivo de estás llamadas es obtener todos los superhéroes que tengan la altura
# correspondiente a la altura máxima, y la misma función me podria servir tanto como
# para altura menor, como la mayor o alguna altura que yo le especifique también.



def obtener_dato_cantidad(lista:list, numero:int, buscar:str):
    """
    puede buscar un minimo o un maximo o cualquier otro dato que se desea
    la opcion 0 busca maximos el 1 busca minimo y la opcion 2 busca cualquier otro dato

    """
    minimo_maximo = None
    if numero == "0":
        minimo_maximo = obtener_minimo(lista,buscar)
        print(f"El mínimo valor de '{buscar}' es {minimo_maximo} en:")
        for i in lista:
            if minimo_maximo == i[buscar]:
                print(i["nombre"])

    elif numero == "1":
        minimo_maximo = obtener_maximo(lista,buscar)
        print(f"El máximo valor de '{buscar}' es {minimo_maximo} en:")
        for i in lista:
            if minimo_maximo == i[buscar]:
                print(i["nombre"])

    elif numero == "2":
        dato_a_buscar = buscar
        encontrado = False
        dnis = []
        for i in lista:
            for clave, valor in i.items():
                if dato_a_buscar == clave or dato_a_buscar == str(valor):
                    dnis.append(i)#al guardar el indice se guarda el diccionario tambien 
                    encontrado = True
                    break
        if encontrado:
            print(f"{dato_a_buscar} está en la lista.")
            for dni in dnis:#entonces con dni.get extraemos los datos de forma segura del diccionario que esta en una lista 
                print(f"Nombre: {dni['nombre']}")#agarrar el o los datos que deseamos guardar y luego mostrar
        else:#talvez con una key ,clave.item(podamos hacer lo mismo)
            print(f"{dato_a_buscar} no está en la lista.")


# obtener_dato_cantidad(lista_personajes, "0", "fuerza")
# obtener_dato_cantidad(lista_personajes, "1", "fuerza")
# obtener_dato_cantidad(lista_personajes, "2", "79.35")#"79.349999999999994
# obtener_dato_cantidad(lista_personajes, "2", "100")#"79.349999999999994

#//////////////////////////////////////////////////////////////////////////////////////////////
# 3.4 Crear la función 'stark_imprimir_heroes' la cual recibirá un parametro:
# ● La lista de héroes
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
# contrario no hará nada y retornara False

# En caso de que la lista no este vacia imprimir la información completa de
# todos los heroes de la lista que se le pase#
#  3.4 Crear la función 'stark_imprimir_heroes' la cual recibirá un parametro:

# ● La lista de héroes
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
# contrario no hará nada y retornara False
# En caso de que la lista no este vacia imprimir la información completa de
# todos los heroes de la lista que se le pase

# Ejemplo de llamada:
# mas_pesado = obtener_maximo(lista_heroes,”peso”)
# lista_mas_pesados = 'obtener_dato_cantidad(lista_heroes,mas_pesado ,”peso”)
# stark_imprimir_heroes(lista_mas_pesados) -> Imprimo sólo los héroes más pesados
# stark_imprimir_heroes(lista_heroes) -> Imprimo todos los héroes

def stark_imprimir_heroes(lista:list):
    """
    recive una lista e imprime todos los datos y todos los personajes
    """
    tamaño = len(lista)
    if  tamaño == 0:
        mensaje1 = False
    else:
        for i in (lista_personajes):
            
            mensaje1  =     f'Nombre : {i["nombre"]}\n'
            mensaje1 +=     f'Identidad : {i["identidad"]}\n'
            mensaje1 +=     f'Empresa : {i["empresa"]}\n'
            mensaje1 +=     f'Color de ojos : {i["color_ojos"]}\n'
            mensaje1 +=     f'color de pelo : {i["color_pelo"]}\n'
            mensaje1 +=     f'Fuerza : {i["fuerza"]}\n'
            mensaje1 +=     f'Inteligencia : {i["inteligencia"]}'
            mensaje1 +=     f'Altura : {i["altura"]}\n'
            mensaje1 +=     f'peso : {i["peso"]}\n'
            mensaje1 +=     f'genero : {i["genero"]}\n'
            print(mensaje1)
#print(stark_imprimir_heroes(lista_personajes))

#//////////////////////////////////////////////////////////////////////////////////////////////
# 4.1 Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de
# héroes y un string que representara el dato/key de los héroes que se requiere sumar.
# Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes
# de hacer la suma. La función deberá retorna la suma de todos los datos según la key
# pasada por parámetro

def sumar_dato_heroe(lista:list,key:int|float):
    """
    recive una lista con diccionarios  y una clave en donde se busca
    el dato que se desea sumar 
    """
    acumulador = 0
    for personaje in lista:
        for c , v in personaje.items():
            tamaño = len(c)
            if key in personaje and tamaño > 1:
                acumulador += personaje[key]
    return acumulador
print(sumar_dato_heroe(lista_personajes,"fuerza"))


#//////////////////////////////////////////////////////////////////////////////////////////////
# 4.2 Crear la función ‘dividir’ la cual recibirá como parámetro dos números (dividendo
# y divisor). Se debe verificar si el divisor es 0, en caso de serlo, retornar False, caso
# contrario realizar la división entre los parámetros y retornar el resultado

def dividir(dividendo, divisor):
    """
    recibe dos parametros un dividendo y un divisor se divide y devuelve
    el resultado en caso que el divisor sea 0 devuelve false
    """
    if divisor == 0:
        resultado=  False
    else:
        resultado = dividendo / divisor

    return resultado

# resultado = dividir(10, 2)
# print(resultado)  

# resultado = dividir(5, 0)
# print(resultado) 

#//////////////////////////////////////////////////////////////////////////////////////////////
# 4.3 Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de
# héroes y un string que representa el dato del héroe que se requiere calcular el
# promedio. La función debe retornar el promedio del dato pasado por parámetro
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 4.1 y 4.2
def calcualar_promedio(lista:list,calcular:str):
    """
    recibe una lista y un parametro al cual se desea calcular el promedio
    """
    for i in lista:
        tamaño = len(i)
    suma = (sumar_dato_heroe(lista,calcular))
    promedio = dividir(suma,tamaño)
    return promedio

# print(calcualar_promedio(lista_personajes,"fuerza")) 


#//////////////////////////////////////////////////////////////////////////////////////////////
# 4.4 Crear la función ‘mostrar_promedio_dato’ la cual recibirá como parámetro una
# lista de héroes y un string que representa la clave del dato
# ● Se debe validar que el dato que se encuentra en esa clave sea de tipo int o
# float. Caso contrario retornaria False
# ● Se debe validar que la lista a manipular no esté vacía , en caso de que esté
# vacía se retornaria también False
def mostrar_promedio_dato(lista:list,clave:str):
    """
    recibe una lista de heros y un str que representa una clave
    """
    tamaño = len(lista)
    if tamaño == 0:
        print(False)
    if clave == int or float:
        promedio = calcualar_promedio(lista,clave)
        print(promedio)
    else:
        print (False)

mostrar_promedio_dato(lista_personajes,"fuerza")

#//////////////////////////////////////////////////////////////////////////////////////////////
# 5.1 Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla,
# el cual permite utilizar toda la funcionalidad ya programada.
def imprimir_menu(menu:str):
    """
    recibe el menu y lo imprime 
    """
    print(menu)

#//////////////////////////////////////////////////////////////////////////////////////////////
# 5.2 Crear la función “validar_entero” la cual recibirá por parámetro un string de
# número el cual deberá verificar que sea sea un string conformado únicamente por
# dígitos. Retornara True en caso de serlo, False caso contrario
#numero2 = "155315"
def validar_entero(string:str)->bool:
    """
    recibe un str y devuelve false al encontrarlo y tru si no 
    """
    if string.isdigit():
        mensaje = False
    else:
        mensaje = True
    return mensaje

#print(validar_entero(numero2))


#//////////////////////////////////////////////////////////////////////////////////////////////
# 5.3 Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú
# de opciones y le pedirá al usuario que ingrese el número de una de las opciones
# elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara
# casteado a int , caso contrario retorna False. Reutilizar las funciones del ejercicio 5.1
# y 5.2

#5.3
def stark_menu_principal():
    '''
    Imprime menú, pide al usuario que ingrese número.
    Si es correcto retorna el numero casteado a "int", caso contrario False
    '''
    imprimir_menu()
    opcion_elegida = input("Seleccione un numero: ")
    validacion = validar_entero(opcion_elegida)
    if validacion == True:
        opcion_elegida_int = int(opcion_elegida)
        mensaje =  f"{opcion_elegida_int}"
    else:
        mensaje = "False"
    return mensaje
# print(stark_menu_principal(3))

#//////////////////////////////////////////////////////////////////////////////////////////////
# 7. Una vez realizadas y probadas las funciones resolver en un menú los siguientes
# puntos del desafio anterior.
# A 1. Normalizar datos (No se debe poder acceder a los otros puntos)
# B 2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
# C 3 . Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# D 4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# E 5 . Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# F 6 . Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# G 7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
# género NB
# H 8 . Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# I 9 . Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# J 10 . Listar todos los superhéroes agrupados por color de ojos.
# K 11 . Listar todos los superhéroes agrupados por tipo de inteligencia




# B

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
# (nombre_por_genero(lista_personajes,"NB"))

# C
def maximo_por_genero(lista:list,M_OR_F:str,variable_a_encontrar:float):
    """"
    EJEMPLO DE USO: maximo por genero(lista_hero,"M","altura")\n
    Tambien se puede usar para el genero NB experimental
    """
    el_mas_alto = None
    nombre = []
    for i in (lista):
        variable_de_maximo_a_buscar = float(i[variable_a_encontrar])
        caracter_especifico = i["genero"]
        if caracter_especifico == M_OR_F :
            if (el_mas_alto) == None or float(el_mas_alto) < float(variable_de_maximo_a_buscar):
                el_mas_alto = variable_de_maximo_a_buscar
                nombre = (i["nombre"])
    return(nombre,el_mas_alto)
#print(maximo_por_genero(lista_personajes,"M","altura"))
# D 

# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M

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

# E 

# F

# G 
# Recorrer la lista y determinar la fuerza promedio de los superhéroes de 
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
# H
# I 


# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

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

#cantidad_color_de_ojos_o_pelo(lista_personajes,"ojos")



# 1ro cargamos los datos una lista y lo que se quiera agrupar ya sea inteligencia o color de ojos 


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


# 6.Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes
# y se encargará de la ejecución principal de nuestro programa.
# Utilizar if/elif o match según prefiera. Debe informar por consola en caso de
# seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las
# funciones con prefijo 'stark_' donde crea correspondiente.

def imprimir_menu():
    """
    imprime el menu
    """
    menu = """
    
        🚀 stark 3# 🚀
        🚀             
        (•-•)  (#_<)  
        [> <]  /> <\   
    1  - Normalizar datos
    2  - Nombre de los super Heroes de genero NB
    3  - Personaje mas alto de Genero F
    4  - Personaje mas alto de Genero M
    5  - Personaje mas debil de genero M
    6  - Personaje mas devil de genero NB
    7  - Fuerza promedio de los super heroes NB
    8  - cantidad de super heroes que tienen cada tipo de color de ojos
    9  - cantidad de super heroes que tienen cada tipo de color de pelo 
    10 - listado de todos los super heroes agrupados por color de ojos
    11 - Listado todos los superhéroes agrupados por tipo de inteligencia
    12 - SALIR DEL PROGRAMA
    """
    print(menu)
# imprimir_menu()



def stark_marvel_app_3(lista_personajes):
    """
    imprime el menu y hace funcionar las funciones 
    """
    bandera = True
    normalizacion = True
    while (normalizacion):
        imprimir_menu()
        respuesta = input()
        match respuesta:
            case "1":
                print(stark_normalizar_datos(lista_personajes))
                normalizacion = False
            case  _:
                print("debe normalizar los datos 1ro")

    while (bandera):
        print(
            " \n "
            " 🚀 stark 3# 🚀\n"
            "  🚀             \n"
            "    (•-•)  (#_<)  \n"
            "    [> <]  /> <\   \n"
            "1  - Normalizar datos (No se debe poder acceder a los otros puntos)\n"
            "2  - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de genero NB\n"
            "3  - Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n"
            "4  - Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n"
            "5  - Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n"
            "6  - Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n"
            "7  - Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n"
            "8  - Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
            "9  - Determinar cuántos superhéroes tienen cada tipo de color de pelo. \n"
            "10 - Listar todos los superhéroes agrupados por color de ojos.\n"
            "11 - Listar todos los superhéroes agrupados por tipo de inteligencia\n"
            "12 - SALIR DEL PROGRAMA"
        )
        respuesta = input()
        
        match respuesta:
    ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "1":
                print(stark_normalizar_datos(lista_personajes))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "2":
                (nombre_por_genero(lista_personajes,"NB",))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "3":
                print(maximo_por_genero(lista_personajes,"F","altura"))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "4":
                print(maximo_por_genero(lista_personajes,"M","altura"))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "5":
                print(minimo_por_genero(lista_personajes,"M","fuerza"))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "6":
                print(minimo_por_genero(lista_personajes,"NB","fuerza"))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case  "7":
                print(promedio_por_genero(lista_personajes,"NB","fuerza"))
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case  "8":
                cantidad_color_de_ojos_o_pelo(lista_personajes,"ojos")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case  "9":
                cantidad_color_de_ojos_o_pelo(lista_personajes,"pelo")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case  "10":
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
            case  "11":
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
            case  "12":
                bandera = False
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
            case _:
                print("#####################################(´。＿。｀)#######")        
                print("############ OPCION INCORRECTA #######################")       
                print("######### INGRESE OPCION VALIDA  #####################")
                print("######################################################")

stark_marvel_app_3(lista_personajes)






