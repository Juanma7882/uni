import json
import re




# Desafío #05: (crear biblioteca stark_desafio_5.py)
# Basándose en el desafío #01 deberás hacer la siguiente ejercitación, utilizando un
# menú que permita acceder a cada uno de los puntos por separado.

# IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
# escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
# un string, etc y que contendrá) y que es lo que retorna la función!

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia

# Para ello tendrás que seguir las siguientes directivas paso a paso.
# 1. Primera Parte
# 1.1. Crear la función "imprimir_menu_desafio_5" que imprima el menú de
# opciones por pantalla (las opciones son las que se van a utilizar para
# acceder a la funcionalidad de los puntos A hasta el O y Z para salir).
# Reutilizar la función 'imprimir_dato' realizada en una práctica anterior.
# 1.2. Crear la funcion 'stark_menu_principal_desafio_5' la cual se encargará
# de imprimir el menú de opciones y le pedirá al usuario que ingrese la
# letra de una de las opciones elegidas, deberá validar la letra usando
# RegEx y en caso de ser correcta tendrá que retornarla, Caso contrario
# retornará -1. El usuario puede ingresar tanto letras minúsculas como
# mayúsculas y ambas se deben tomar como válidas
# Reutilizar la función 'imprimir_menu_Desafio_5'
# 1.3. Crear la función 'stark_marvel_app_5' la cual recibirá por parámetro la
# lista de héroes y se encargará de la ejecución principal de nuestro
# programa. (usar if/elif o match según prefiera) Reutilizar las funciones
# con prefijo 'stark_' donde crea correspondiente.
# 1.4. Crear la función 'leer_archivo' la cual recibirá por parámetro un string
# que indicará el nombre y extensión del archivo a leer (Ejemplo:
# archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
# retornará la lista de héroes como una lista de diccionarios.
# 1.5. Crear la función 'guardar_archivo' la cual recibirá por parámetro un
# string que indicará el nombre con el cual se guardará el archivo junto
# con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
# tendrá un string el cual será el contenido a guardar en dicho archivo.
# Debe abrirse el archivo en modo escritura+, ya que en caso de no
# existir, lo creara y en caso de existir, lo va a sobreescribir La función
# debera retornar True si no hubo errores, caso contrario False, además
# en caso de éxito, deberá imprimir un mensaje respetando el formato:
# .Se creó el archivo: nombre_archivo.csv
# En caso de retornar False, el mensaje deberá decir: ‘Error al crear el
# archivo: nombre_archivo’

# Donde nombre_archivo será el nombre que recibirá el archivo a ser
# creado, conjuntamente con su extensión.
# 1.6. Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un
# string que puede contener una o muchas palabras. La función deberá
# retornar dicho string en el cual todas y cada una de las palabras que
# contenga, deberán estar capitalizadas (Primera letra en mayúscula).
# 1.7. Crear la función 'obtener_nombre_capitalizado' la cual recibirá por
# parámetro un diccionario el cual representará a un héroe y devolverá
# un string el cual contenga su nombre formateado de la siguiente
# manera:
# Nombre: Venom
# Reutilizar 'capitalizar_palabras'
# 1.8. Crear la función 'obtener_nombre_y_dato' la cual recibirá por
# parámetro un diccionario el cual representará a un héroe y una key
# (string) la cual representará la key del héroe a imprimir. La función
# devolverá un string el cual contenga el nombre y dato (key) del héroe a
# imprimir.
# El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.
# El string resultante debe estar formateado al estilo: (suponiendo que la
# key es fuerza)
# Nombre: Venom | Fuerza: 500
# Reutilizar 'obtener_nombre_capitalizado'

# 2. Segunda Parte
# 2.1. Crear la función 'es_genero' la cual recibirá por parámetro un
# diccionario que representará un héroe y un string el cual será usado
# para evaluar si el héroe coincide con el género buscado (El string
# puede ser M, F o NB). retornará True en caso de que cumpla, False
# caso contrario.
# 2.2. Crear la función 'stark_guardar_heroe_genero' la cual recibira por
# parámetro la lista de héroes y un string el cual representará el género
# a evaluar (puede ser M o F). Deberá imprimir solamente los héroes o
# heroínas que coincidan con el género pasado por parámetro y
# además, deberá guardar dichos nombres en un archivo con extensión

# csv (cada nombre deberá ir separado por una coma)
# Reutilizar las funciones 'es_genero', 'obtener_nombre_capitalizado',
# 'imprimir_dato' y 'guardar_archivo'.
# En el caso de 'guardar_archivo', cuando se llame a esta función el
# nombre de archivo a guardar deberá respetar el formato:
# heroes_M.csv, heroes_F.csv o heroes_NB según corresponda.
# La función retornará True si pudo guardar el archivo, False caso
# contrario.

# 3. Tercera Parte
# 3.1. Basandote en la función 'calcular_min', crear la función
# 'calcular_min_genero' la cual recibirá como parámetro extra un string
# que representa el género de la heroína/héroe a buscar. modificar un
# poco la lógica para que dentro no se traiga por defecto al primer héroe
# de la lista sino que mediante un flag, se traiga el primer héroe que
# COINCIDA con el género pasado por parámetro. A partir de allí, podrá
# empezar a comparar entre héroes o heroínas que coincidan con el
# género pasado por parámetro. La función retornará el héroe o heroína
# que cumpla la condición de tener el mínimo (peso, altura u otro dato)
# 3.2. Basandote en la función 'calcular_max', crear la función
# 'calcular_max_genero' la cual recibirá como parámetro extra un string
# que representará el género de la heroína/héroe a buscar. modificar un
# poco la lógica para que dentro no se traiga por defecto al primer héroe
# de la lista sino que mediante un flag, se traiga el primer héroe que
# COINCIDA con el género pasado por parámetro. A partir de allí, podrá
# empezar a comparar entre héroes o heroínas que coincidan con el
# género pasado por parámetro. La función retornará el héroe o heroína
# que cumpla la condición de tener el máximo (peso, altura u otro dato)
# 3.3. Basandote en la funcion 'calcular_max_min_dato', crear una funcion
# con la misma lógica la cual reciba un parámetro string que
# representará el género del héroe/heroína a buscar y renombrarla a
# 'calcular_max_min_dato_genero'. La estructura será similar a la ya
# antes creada, salvo que dentro de ella deberá llamar a
# 'calcular_max_genero' y 'calcular_min_genero', pasandoles el nuevo
# parámetro. Esta función retornará el héroe o heroína que cumpla con

# las condiciones pasados por parámetro. Por ejemplo, si se le pasa 'F' y
# 'minimo', retornará la heroína que tenga el mínimo (altura, peso u otro
# dato)
# 3.4. Basandote en la función 'stark_calcular_imprimir_heroe' crear la
# función ‘stark_calcular_imprimir_guardar_heroe_genero’ que además
# reciba un string el cual representará el género a evaluar. El formato de
# mensaje a imprimir deberá ser estilo:
# Mayor Altura: Nombre: Gamora | Altura: 183.65
# Además la función deberá guardar en un archivo csv el resultado
# obtenido.
# Reutilizar: 'calcular_max_min_dato_genero', 'obtener_nombre_y_dato',
# 'imprimir_dato' y 'guardar_archivo'.
# En el caso de 'guardar_archivo' el nombre del archivo debe respetar el
# formato:
# heroes_calculo_key_genero.csv
# Donde:
# ● cálculo: representará el string máximo o mínimo
# ● key: representará cual es la key la cual se tiene que hacer el
# cálculo
# ● genero: representará el género a calcular.
# Ejemplo: para calcular el héroe más alto femenino, el archivo se
# deberá llamar:
# heroes_maximo_altura_F.csv
# Esta función retornará True si pudo guardar el archivo, False caso
# contrario

# 4. Cuarta Parte
# 4.1. Basandote en la función 'sumar_dato_heroe', crear la función llamada
# 'sumar_dato_heroe_genero' la cual deberá tener un parámetro extra
# del tipo string que representará el género con el que se va a trabajar.
# Esta función antes de realizar la suma en su variable sumadora,
# deberá validar lo siguiente:

# A. El tipo de dato del héroe debe ser diccionario.
# B. El héroe actual de la iteración no debe estar vacío (ser
# diccionario vacío)
# C. El género del héroe debe coincidir con el pasado por
# parámetro.

# Una vez que cumpla con las condiciones, podrá realizar la suma. La
# función deberá retornar la suma del valor de la key de los héroes o
# heroínas que cumplan las condiciones o -1 en caso de que no se
# cumplan las validaciones

# 4.2. Crear la función 'cantidad_heroes_genero' la cual recibirá por
# parámetro la lista de héroes y un string que representará el género a
# buscar. La función deberá iterar y sumar la cantidad de héroes o
# heroínas que cumplan con la condición de género pasada por
# parámetro, retornará dicha suma.
# 4.3. Basandote en la función 'calcular_promedio', crear la función
# 'calcular_promedio_genero' la cual tendrá como parámetro extra un
# string que representará el género a buscar. la lógica es similar a la
# función anteriormente mencionada en el enunciado. Reutilizar las
# funciones: 'sumar_dato_heroe_genero', 'cantidad_heroes_genero' y
# 'dividir'.
# retornará el promedio obtenido, según la key y género pasado por
# parámetro.
# 4.4. Basandote en la función ‘stark_calcular_imprimir_promedio_altura',
# desarrollar la función 'stark_calcular_imprimir_guardar_
# promedio_altura_genero' la cual tendrá como parámetro extra un string

# que representará el género de los héroes a buscar.
# La función antes de hacer nada, deberá validar que la lista no esté
# vacía. En caso de no estar vacía: calculará el promedio y lo imprimirá
# formateado al estilo:
# Altura promedio género F: 178.45
# En caso de estar vacía, imprimirá como mensaje:
# Error: Lista de héroes vacía.
# Luego de imprimir la función deberá guardar en un archivo los mismos
# datos. El nombre del archivo debe tener el siguiente formato:
# heroes_promedio_altura_genero.csv
# Donde:
# A. genero: será el género de los héroes a calcular, siendo M y F
# únicas opciones posibles.
# Ejemplos:
# heroes_promedio_altura_F.csv
# heroes_promedio_altura_M.csv

# Reutilizar las funciones: 'calcular_promedio_genero', 'imprimir_dato' y
# 'guardar_archivo'.
# Esta función retornará True si pudo la lista tiene algún elemento y pudo
# guardar el archivo, False en caso de que esté vacía o no haya podido
# guardar el archivo.

# 5. Quinta Parte
# 5.1. Crear la función 'calcular_cantidad_tipo' la cual recibirá por parámetro
# la lista de héroes y un string que representará el tipo de dato/key a
# buscar (color_ojos, color_pelo, etc)
# Antes de hacer nada, deberá validar que la lista no esté vacía. En caso
# de estarlo devolver un diccionario con la siguiente estructura:
# {
# "Error": “La lista se encuentra vacía”
# }
# La función deberá retornar un diccionario con los distintos valores del
# tipo de dato pasada por parámetro y la cantidad de cada uno (crear un
# diccionario clave valor).
# Por ejemplo, si el tipo de dato fuese color_ojos, devolverá un
# diccionario de la siguiente manera:
# {
# "Celeste": 4,
# "Verde": 8,
# "Marron": 6
# }
# Reutilizar la función 'capitalizar_palabras' para capitalizar los valores
# de las keys.

# 5.2. Crear la función 'guardar_cantidad_heroes_tipo' la cual recibirá como
# parámetro un diccionario que representará las distintas variedades del
# tipo de dato (distintos colores de ojos, pelo, etc) como clave con sus
# respectivas cantidades como valor. Como segundo parámetro recibirá
# el dato (color_pelo, color_ojos, etc) el cual tendrás que usarlo
# únicamente en el mensaje final formateado. Esta función deberá iterar
# cada key del diccionario y variabilizar dicha key con su valor para
# luego formatearlos en un mensaje el cual deberá guardar en archivo.
# Por ejemplo:

# "Caracteristica: color_ojos Blue - Cantidad de heroes: 9"
# Reutilizar la función 'guardar_archivo'. El nombre del archivo final
# deberá respetar el formato:
# heroes_cantidad_tipoDato.csv
# Donde:
# ● tipoDato: representará el nombre de la key la cual se está
# evaluando la cantidad de héroes.
# Ejemplo:
# heroes_cantidad_color_pelo.csv
# heroes_cantidad_color_ojos.csv
# La función retornará True si salió todo bien, False caso contrario.

# 5.3. Crear la función 'stark_calcular_cantidad_por_tipo' la cual recibirá por
# parámetro la lista de héroes y un string que representará el tipo de
# dato/key a buscar (color_ojos, color_pelo, etc). Dentro deberás
# reutilizar 'calcular_cantidad_tipo' y 'guardar_cantidad_heroes_tipo' con
# la lógica que cada una de esas funciones manejan.
# Esta función retornará True si pudo guardar el archivo, False caso
# contrario.
# 6. Sexta Parte
# 6.1. Crear la función 'obtener_lista_de_tipos' la cual recibirá por parámetro
# la lista de héroes y un string que representará el tipo de dato/key a
# buscar (color_ojos, color_pelo, etc).
# Esta función deberá iterar la lista de héroes guardando en una lista las
# variedades del tipo de dato pasado por parámetro (sus valores).
# En caso de encontrar una key sin valor (o string vacío), deberás
# hardcodear con el valor 'N/A' y luego agregarlo a la lista donde irás
# guardando todos los valores encontrados, si el valor del héroe no tiene
# errores, guardarlo tal cual viene.
# Finalmente deberás eliminar los duplicados de esa lista y retornarla

# como un set.
# Reutilizar 'capitalizar_palabras' para guardar cada uno de los datos
# con la primera letra mayúscula.
# 6.2. Crear la función 'normalizar_dato' la cual recibirá por parámetro un
# dato de héroe (el valor de una de sus keys, por ejemplo si la key fuese
# color_ojos y su valor fuese Verde, recibira este ultimo) y tambien una
# variable como string la cual representará el valor por defecto a colocar
# en caso de que el valor está vacío. Deberá validar que el dato no esté
# vacío, en caso de estarlo lo reemplazará con el valor default pasado
# por parámetro y lo retornará, caso contrario lo retornará sin
# modificaciones.
# 6.3. Crear la función 'normalizar_heroe' la cual recibirá dos parámetros. el
# primero será un diccionario que representará un solo héroe, el
# segundo parámetro será el nombre de la key de dicho diccionario la
# cual debe ser normalizada.
# La función deberá capitalizar las palabras que tenga dicha key como
# valor, luego deberá normalizar el dato (ya que si viene vacío, habrá
# que setearlo con N/A).
# Finalmente deberá capitalizar todas las palabras del nombre del héroe
# y deberá retornar al Hero con cada palabra de su nombre
# capitalizados, cada palabra del valor de la key capitalizadas y
# normalizadas (con N/A en caso de que estuviesen vacías por defecto).
# Reutilizar: 'capitalizar_palabras' y 'normalizar_dato'

# 6.4. Crear la funcion 'obtener_heroes_por_tipo' el cual recibira por
# parámetro:
# A. La lista de héroes
# B. Un set de tipos/variedades (colores de ojos, de pelo, etc)
# C. El tipo de dato a evaluar (la key en cuestion, color_ojos,
# color_pelo, etc)
# PRESTAR ATENCIÓN:

# A. Deberá iterar el set de tipos/variedades y por cada tipo tendrá evaluar
# si ese tipo existe como key en un diccionario el cual deberás armar.
# (contendrá cada variedad como key y una lista de nombres de héroes
# como valor de cada una de ellas).
# B. En caso de no existir dicha key en el diccionario, agregarla con una
# lista vacía como valor.
# C. Dentro de la iteración de variedades, iterar la lista de héroes (for
# anidado) 'normalizando' el posible valor que tenga la key evaluada, ya
# que podría venir vacía (qué función usarias aca? guiño guiño)
# D. Una vez normalizado el dato, evaluar si dicho dato coincide con el tipo
# pasado por parámetro.
# E. En caso de que coincida, agregarlo a la lista (inicialmente vacía) de la
# variedad iterada en el primer bucle.
# Esta función retornará un diccionario con cada variedad como key y
# una lista de nombres como valor.
# Por ejemplo:
# {
# "Celestes": ["Capitan America", "Tony Stark"],
# "Verdes": ["Hulk", "Viuda Negra"]
# ....
# }

# 6.5. Crear la funcion 'guardar_heroes_por_tipo' la cual recibira por
# parámetro un diccionario que representará los distintos tipos como
# clave y una lista de nombres como valor (Lo retorna la función anterior)
# y además como segundo parámetro tendrá un string el cual
# representará el tipo de dato a evaluar (color_pelo, color_ojos, etc).
# Deberá recorrer cada key y cada valor (lista) que esta contenga para
# finalmente crear un string el cual será un mensaje que deberás
# imprimir formateado.
# Por ejemplo:
# "color_ojos Green: Black Widow | Hulk"
# Reutilizar la función 'guardar_archivo'. El archivo final deberá respetar
# el formato:
# heroes_segun_TipoDato.csv
# Donde:
# ● TipoDato: es la key la cual indicará qué cosas se deben guardar
# en el archivo.
# Ejemplo:
# heroes_segun_color_pelo.csv (Agrupados por color de pelo)
# heroes_segun_color_ojos.csv (Agrupados por color de ojos)
# Esta función retorna True si salió todo bien, False caso contrario.
# 6.6. Crear la función 'stark_listar_heroes_por_dato' la cual recibirá por
# parámetro la lista de héroes y un string que representará el tipo de
# dato a evaluar (color_pelo, color_ojos, etc). Dentro deberás reutilizar
# las funciones:
# A. 'obtener_lista_de_tipos'
# B. 'obtener_heroes_por_tipo'
# C. 'guardar_heroes_por_tipo'
# Pasando por parámetro lo que corresponda según la lógica de las
# funciones usadas.

# Esta función retornará True si pudo guardar el archivo, False caso
# contrario.


def parce_json_stark(path:str)->list:
    archivo = open(path, "r")
    dic_json = json.load(archivo)
    archivo.close()
    return dic_json["heroes"]


lista_heroes = parce_json_stark("Curso_de_ingreso_PYTHON-main/ejercicios/cuatrimestre_1/tp stark/stark_5/data.json")





# print(lista_heroes)


# Curso_de_ingreso_PYTHON-main/ejercicios/cuatrimestre_1/tp stark/stark_5/data.json


# def parse_json_stark(path: str) -> list:
#     with open(path, "r") as archivo:
#         dic_json = json.load(archivo)
#     return dic_json["heroes"]

# lista_heroes = parse_json_stark("Curso_de_ingreso_PYTHON-main/ejercicios/cuatrimestre_1/tp stark/stark_5/data.json")
# print(lista_heroes)


##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#1.1
def imprimir_menu_desafio_5(menu:str):
    """
    recibe el menu y lo imprime 
    """
    print(menu)

##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#1.2
def stark_menu():
    """
    retona el menu a mostrar en la impresion
    """
    menu ="""
    
    A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
    C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
    F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
    G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
    H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
    I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
        indicadores anteriores (ítems C a F)
    J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
        no tener, Inicializarlo con No Tiene).
    M. Listar todos los superhéroes agrupados por color de ojos.
    N. Listar todos los superhéroes agrupados por color de pelo.
    O. Listar todos los superhéroes agrupados por tipo de inteligencia
    z. salir 
    """
    return menu

# imprimir_menu(stark_menu_principal_desafio_5())




def validacion_de_menu(respuesta:str):
    """
    valida lo que se puede ingresar en el menu
    devuelve:
    * -1 si es invalida
    * devuelve el str si es valido 
    """
    validacion = r'^[a-oA-OzZ]$'
    if re.match(validacion,respuesta):
        mensaje = respuesta
    else:
        mensaje = -1 
    return mensaje


def stark_menu_principal_desafio_5():
    """
    imprime el menu te permite ingresar un carcter lo valida y si es valido 
    retorna el mismo en caso contrario devuelve -1
    """
    menu = stark_menu()
    imprimir_menu_desafio_5(menu)
    respuesta = input()
    respuesta_normalizada = respuesta.upper()
    mensaje = validacion_de_menu(respuesta_normalizada)
    return mensaje

# print(stark_menu_principal_desafio_5())
# print(impresion)

##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# #1.3

                                        
def stark_marvel_app_5():
    bandera = True
    while bandera:
        impresion = stark_menu_principal_desafio_5()
        # print(impresion)A
        
        if impresion == "A":
            stark_guardar_heroe_genero(lista_heroes, "M")

            # print("entro aca")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "B":
            stark_guardar_heroe_genero(lista_heroes, "F")

        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "C":
            ALTURA = calcular_max_min_dato(lista_heroes, "M", "altura", "maximo")
            for I in ALTURA:
                print(I)
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "D":
            ALTURA = calcular_max_min_dato(lista_heroes, "F", "altura", "maximo")
            for I in ALTURA:
                print(I)
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "E":
            ALTURA = calcular_max_min_dato(lista_heroes, "M", "altura", "minimo")
            for I in ALTURA:
                print(I)
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "F":
            ALTURA = calcular_max_min_dato(lista_heroes, "F", "altura", "minimo")
            for I in ALTURA:
                print(I)
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "G":
            stark_calcular_imprimir_promedio_altura(lista_heroes, "M")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "H":
            stark_calcular_imprimir_promedio_altura(lista_heroes, "F")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "I":
                
                ALTURA = calcular_max_min_dato(lista_heroes, "M", "altura", "maximo")
                for I in ALTURA:
                    print(F"NOMBRE DE LA PERSONA MAS ALTA MASCULINA : {I}")
            ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////            

                ALTURA = calcular_max_min_dato(lista_heroes, "F", "altura", "maximo")
                for I in ALTURA:
                    print(F"NOMBRE DE LA PERSONA MAS ALTA FEMENINA  : {I}")
            ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////            

                ALTURA = calcular_max_min_dato(lista_heroes, "M", "altura", "minimo")
                for I in ALTURA:
                    print(F"NOMBRE DE LA PERSONA MAS BAJA MASCULINA : {I}")
            ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////            
                ALTURA = calcular_max_min_dato(lista_heroes, "F", "altura", "minimo")
                for I in ALTURA:
                    print(F"NOMBRE DE LA PERSONA MAS BAJA FEMENINA  : {I}")

        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "J":
            # for i in cantidad_color_de_ojos_o_pelo(lista_heroes, "ojos"):


            # print(cantidad_color_de_ojos_o_pelo(lista_heroes, "ojos"))
            f = cantidad_color_de_ojos_o_pelo(lista_heroes, "ojos")
            print("-" * 52)
            print(f"{'color de ojos':25}|  {'cantidad':23} ")
            for color, nombres in f.items():
                print("-" * 52)
                print(f" {color}: ")
                # for nombre in nombres:
                print(f" {'':23} |  - {nombres:20} |")
            print("-" * 52)
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "K":
            # print(cantidad_color_de_ojos_o_pelo(lista_heroes, "pelo"))
            f = cantidad_color_de_ojos_o_pelo(lista_heroes, "pelo")
            print("-" * 52)
            print(f"{'color de ojos':25}|  {'cantidad':23} ")
            for color, nombres in f.items():
                print("-" * 52)
                print(f" {color}: ")
                # for nombre in nombres:
                print(f" {'':23} |  - {nombres:20} |")
            print("-" * 52)
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "L":
            MENSAJE = normalizar_dato("NO TIENE")
            # print(cantidad_color_de_ojos_o_pelo(MENSAJE, "inteligencia"))

            f = cantidad_color_de_ojos_o_pelo(MENSAJE, "inteligencia")
            print("-" * 52)
            print(f"{'color de ojos':25}|  {'cantidad':23} ")
            for color, nombres in f.items():
                print("-" * 52)
                print(f" {color}: ")
                # for nombre in nombres:
                print(f" {'':23} |  - {nombres:20} |")
            print("-" * 52)
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "M":
            lista_de_tipos_set = obtener_lista_de_tipos(lista_heroes, "color_ojos")
            # print(obtener_heroes_por_tipo(lista_heroes, lista_de_tipos_set, "color_ojos"))
            f = obtener_heroes_por_tipo(lista_heroes, lista_de_tipos_set, "color_ojos")
            #  f =agrupar_por_inteligencia_color_de_ojos(lista_personajes, "color_ojos")
            print("-" * 52)
            print(f"{'color de ojos':25}|  {'nombres':23} ")
            for color, nombres in f.items():
                print("-" * 52)
                print(f" {color}: ")
                for nombre in nombres:
                    print(f" {'':23} |  - {nombre:20} |")
            print("-" * 52)
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "N":
            lista_de_tipos_set = obtener_lista_de_tipos(lista_heroes, "color_pelo")
            # print(obtener_heroes_por_tipo(lista_heroes, lista_de_tipos_set, "color_pelo"))

            f = obtener_heroes_por_tipo(lista_heroes, lista_de_tipos_set, "color_pelo")
            print("-" * 52)
            print(f"{'color de pelo':25}|  {'nombres':23} ")
            for color, nombres in f.items():
                print("-" * 52)
                print(f" {color}: ")
                for nombre in nombres:
                    print(f" {'':23} |  - {nombre:20} |")
            print("-" * 52)
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "O":
            lista_de_tipos_set = obtener_lista_de_tipos(lista_heroes, "inteligencia")
            # print(obtener_heroes_por_tipo(lista_heroes, lista_de_tipos_set, "inteligencia"))a
            
            f = obtener_heroes_por_tipo(lista_heroes, lista_de_tipos_set, "inteligencia")
            print("-" * 52)
            print(f"{'inteligencia':25}|  {'nombres':23} ")
            for color, nombres in f.items():
                print("-" * 52)
                print(f" {color}: ")
                for nombre in nombres:
                    print(f" {'':23} |  - {nombre:20} |")
            print("-" * 52)
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "Z":
            break
        else:
            print("COLOCAR ALGUNA LETRA VALIDA")

# stark_marvel_app_5()
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 1.4

def leer_archivo(arch:str)->list:
    """
    recibe como parametro un json y te devuelve 
    un diccionario
    """
    archivo = open(arch, "r")
    dic_json = json.load(archivo)
    archivo.close()
    return dic_json["heroes"]


##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 1.5



def validacion_archivos(validar):
    """
    se asegura que el tipo de archivo recivido
    sea (CSV|py|txt|pdf)devuelve true si es corrrecto
    y false si no 
    """
    validacion = r'^.+\.(CSV|py|txt|pdf|json)$'

    if re.match(validacion,validar):
        mensaje  = True
    else:
        mensaje=  False
    return mensaje

def guardar_archivo(nombre_del_archivo_y_su_tipo,contenido)->bool:
    """
    esta funcion es capaz de crear archivos se le debe pasar el nombre del archivo y el tipo
    tambien lo que desea que contenga
    guardar_archivo(archivo.py,practica_n2)
    tipos de archicos validos = CSV / py / txt / pdf/json
    """
    # ubicasion relativa del archivo en donde se va crear o guardar 
    ubicasion_relativa_de_la_carpeta = r"Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\tp stark\stark_5"
    
    tamaño = len(contenido)
    validacion = validacion_archivos(nombre_del_archivo_y_su_tipo)

    if tamaño == 0 or validacion == False:
        mensaje = False
        print(f"Error al crear el archivo: {nombre_del_archivo_y_su_tipo}" )
    else :
        # el archivo se abre se le pasa la ubicacion se le suma el archivo. la w es de write para escribir el archivo              
        archivo = open(ubicasion_relativa_de_la_carpeta + nombre_del_archivo_y_su_tipo, "w")
        archivo.write(contenido)
        archivo.close()
        print("archivo creado con exito")
        mensaje = True

    return mensaje
# Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\tp stark\stark_5\prueba.CSV
# Curso_de_ingreso_PYTHON-main\ejercicios\cuatrimestre_1\tp stark\stark_5

# mensaje = "todo funciona bien reparafdo"
# # lis = ['sda']
# nombre = "prueba.CSV"
# guardar_archivo(nombre,mensaje)
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#1.6


diccionario = [{"calev": "alor"},{"nalev": "palor"},{"hsdhjalev": "sdkjlor"}]
librito = {"nombre" : "picachu", "peso": "20","altura": "22.4","apellido" : "ject hsu" }

def palabras_capitalizado(diccionario:dict):
    """
    recive un diccionario y le coloca en mayuscula 
    la primer letra a todos los caracateres
    """
    diccionario_mayusculas = {}
    #split cortar separar ponerle la mayuscula y juntar todo devuelta
    for clave, valor in diccionario.items():
                                    #.title otra forma de hacerlo con todo
        if type(clave) == str and type(valor) == str:
            diccionario_mayusculas[clave.capitalize()] = valor.title()
        else:
            diccionario_mayusculas[clave.capitalize()] = valor

    return diccionario_mayusculas

# lu = palabras_capitalizado(librito)
# print(lu)

# for i in lu:
#     print(i["nombre"])

##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#1.7

def obtener_nombre_capitalizado(diccionario:dict):
    """
    recive un diccionario y le coloca en mayuscula a todos los caracteres encontrados
    retorna el diccionario ya con todo en mayusculas 
    """
    # buscar = clave.capitalize()
    resultado = palabras_capitalizado(diccionario)
    mensaje =  (f'Nombre: {resultado["Nombre"]} ' )
    return mensaje

# print(obtener_nombre_capitalizado(librito))



##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 1.8



librito = {"nombre" : "picachu", "peso": "20","altura": "22.4" }

def obtener_nombre_y_dato(diccionario:dict,dato:str):
    """
    recibe un dicionario y el dato a buscar luego lo formatea
    para que se vea de la siguiente forma:
    Nombre: Picachu  | Peso: 20
    """
    # dato = dato.capitalize()
    dato = dato.capitalize()
    datos_capitalizados = obtener_nombre_capitalizado(diccionario)
    # print(datos_capitalizados)
    datos = palabras_capitalizado(diccionario)
    mensaje = f"{datos_capitalizados} | {dato}: {datos[dato]}"
    return mensaje

# print(obtener_nombre_y_dato(librito,"peso"))



##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#2.1

librito = {"nombre" : "picachu", "peso": "20","altura": "22.4","genero":"f" }



def es_genero(diccionario:dict):
    """
    recive un diccionario y valida que contenga la key genero
    y que contenga uno de los siguientes 3 generos
    | M | F | NB |
    """
    if "genero" in diccionario and diccionario["genero"] == "F" or diccionario["genero"]  == "M" or diccionario["genero"]  == "NB":
        mensaje = True
    else:
        mensaje = False
    
    return mensaje
# print(es_genero(librito))

##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 2.2

        

def stark_guardar_heroe_genero(lista_heroes:list, genero_M_OR_F:str,):
    """
    recive la lista de heroes un genero y la busca en caso de 
    encontrarlo lo guarda un archivo CSV y devuelve True
    caso contrario devuelve False
    """

    genero = genero_M_OR_F
    contenido = ""
        
    lista = []
    for i in lista_heroes:
        validacion_de_genero = es_genero(i)
        if validacion_de_genero and i["genero"] == genero:
            lista.append(f"{i["nombre"]}")

    cadena_nombres = ", \n".join(lista)
    # print(cadena_nombres)
    contenido += f"{cadena_nombres}"

    nombre_del_archivo_y_su_tipo = f"HEROES_{genero}.CSV"
    true_false = (guardar_archivo(nombre_del_archivo_y_su_tipo,contenido))
    print(contenido)

    return true_false

# print(stark_guardar_heroe_genero(lista_heroes, "F"))


##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 3.1.

def minimo_por_genero_floot(lista:list,M_OR_F:str,variable_a_encontrar:float):
    """"
    EJEMPLO DE USO: minimo por genero(lista_hero,"M","altura")\n
    Tambien se puede usar para el genero NB experimental
    """
    el_mas_bajo = None
    nombre = []
    bandera= False
    for i in (lista):
        variable_de_minimo_a_buscar = float(i[variable_a_encontrar])
        caracter_especifico = i["genero"]

        if caracter_especifico == M_OR_F :
            if (el_mas_bajo) == None or float(el_mas_bajo) > float(variable_de_minimo_a_buscar):
                el_mas_bajo = variable_de_minimo_a_buscar
                bandera = True


    for i in lista:
        caracter_especifico = i["genero"]
        if caracter_especifico == M_OR_F : 
            if float(el_mas_bajo) == float(i[variable_a_encontrar]):
                nombre.append(i["nombre"])

    if bandera == False:
        nombre.append("sin datos" )
    return nombre

# print(minimo_por_genero_floot(lista_heroes,"F","fuerza"))


##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#3.2


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

# print(maximo_por_genero_floot(lista_heroes,"M","fuerza"))


##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#3.3

def calcular_max_min_dato(lista:list,M_OR_F:str,variable_a_encontrar:float,minimo_o_maximo:str):
    """
    calcula en min o el max de algun genero especifico y una variable especifica 
    returna una lista con los mismos
    """
    normalizar_genero = M_OR_F.upper()
    normalizar_variable_a_encontrar = variable_a_encontrar.lower()
    normalizar_minimo_o_maximo = minimo_o_maximo.lower()

    if normalizar_minimo_o_maximo == "maximo":
        mensaje = maximo_por_genero_floot(lista,normalizar_genero,normalizar_variable_a_encontrar)

    elif normalizar_minimo_o_maximo == "minimo":
        mensaje = minimo_por_genero_floot(lista,normalizar_genero,normalizar_variable_a_encontrar)
    
    return mensaje


# print(calcular_max_min_dato(lista_heroes,"M","fuerza","Maximo"))

##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#3.4


def stark_calcular_imprimir_guardar_heroe_genero(calculos:str,keys:str,genero:str):
    """
    calculo = maximo o minimo
    key = variable a buscar ya sea fuerza o otra caracteristica
    genero = PUEDE SER M o F 
    """

    calculo = calculos
    key = keys
    nuevo = ""
    M_o_F = genero.upper()
    lista = lista_heroes 

    dato = calcular_max_min_dato(lista,M_o_F,key,calculo)
    
    for i in lista:
        for j in dato:
            if j == i["nombre"]:
                archivo = obtener_nombre_y_dato(i,key)
                if "maximo" == calculo:
                    nuevo += f"Mayor {key}: {archivo}\n"
                else:
                    nuevo += f"Menor {key}: {archivo}\n"
                break

    print(nuevo)

    nombre_del_archivo = f"heroes_{calculo}_{key}_{M_o_F}.CSV"
    True_false = guardar_archivo(nombre_del_archivo,nuevo)
    
    return True_false

# stark_calcular_imprimir_guardar_heroe_genero("maximo","fuerza","M")


##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#4.1


# def sumar_dato_heroe(lista:list,key:int|float):
#     """
#     recive una lista con diccionarios  y una clave en donde se busca
#     el dato que se desea sumar 
#     """
#     acumulador = 0
#     for personaje in lista:
#         tamaño = len(personaje)
#         if key in personaje and tamaño > 1:
#             print(personaje)
#             acumulador += personaje
#     return acumulador

# print(sumar_dato_heroe(lista_heroes,"fuerza"))


for i in lista_heroes:
    i["fuerza"]  = int(i["fuerza"])
    i["altura"] = float(i["altura"])

def sumar_dato_heroe(lista:list,key:int|float,genero):
    """
    recive una lista con diccionarios  y una clave en donde se busca
    el dato que se desea sumar 
    """
    acumulador = -1
    for personaje in lista:
        tamaño = len(personaje)
        if tamaño > 0 and key in personaje and personaje["genero"] == genero:
            if acumulador == -1:
                acumulador = 0
            acumulador += i[key]
    # print(i[key])

    return acumulador

# print(sumar_dato_heroe(lista_heroes,"altura","M"))






def cantidad_heroes_genero(lista:list,key:int|float,genero):
    """
    recive una lista con diccionarios  y una clave en donde se busca
    el dato que se desea sumar 
    """
    acumulador = 0
    for personaje in lista:
        tamaño = len(personaje)
        if tamaño > 0 and key in personaje and personaje["genero"] == genero:
            acumulador += 1

    return acumulador

# print(cantidad_heroes_genero(lista_heroes,"fuerza","F"))



for i in lista_heroes:
    i["fuerza"]  = int(i["fuerza"])
    # print(i)

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

def calcualar_promedio(lista:list,calcular:str,genero):
    """
    recibe una lista y un parametro al cual se desea calcular el promedio
    """
    for i in lista:
        tamaño = len(i)
    suma = (sumar_dato_heroe(lista,calcular,genero))
    promedio = dividir(suma,tamaño)
    return promedio

# print(calcualar_promedio(lista_heroes,"fuerza","M"))




##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#

# def stark_calcular_imprimir_promedio_altura():

def stark_calcular_imprimir_promedio_altura(lista_heroes:list,genero:str):
    """
    calculo = maximo o minimo
    key = variable a buscar ya sea fuerza o otra caracteristica
    genero = PUEDE SER M o F 
    """

    mensaje = ""
    M_o_F = genero.upper()

    tamaño = len(lista_heroes)
    if tamaño > 0:
        dato = calcualar_promedio(lista_heroes,"altura",genero)
        # datos = dato:.2f
        mensaje = f"Altura promedio genero {genero} : {dato:.2f}"

    print(mensaje)

    nombre_del_archivo = f"heroes_promedio_altura_{M_o_F}.CSV"
    True_false = guardar_archivo(nombre_del_archivo,mensaje)
    
    return True_false



# stark_calcular_imprimir_promedio_altura(lista_heroes,"M")


##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////




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

# print(agrupar_por_inteligencia_color_de_ojos(lista_heroes,""))



def cantidad_color_de_ojos_o_pelo(lista, color_de):

    color_de = color_de.lower()
    if color_de == "ojos":
        ojos_o_pelo = "color_ojos"
    elif color_de == "pelo":
        ojos_o_pelo = "color_pelo"
    elif color_de == "inteligencia":
        ojos_o_pelo = "inteligencia"

    lista_color_de_pelo = []
    contador_color_de_pelo = {}
    nombre = []

    tamaño = len(lista)
    if tamaño > 0:
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
        
    else:
        contador_color_de_pelo["ERROR"] = "la lista se encuentra vacia"



    return contador_color_de_pelo

# lista_vacioa = []


# print(cantidad_color_de_ojos_o_pelo(lista_heroes,"inteligencia"))



##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////





def guardar_cantidad_heroes_tipo(diccionario:dict,tipo_de_dato:str):

    texto =""
    for clave , valor in diccionario.items():

        texto += f"Caracteristica: {tipo_de_dato} {clave} - cantidad de heroes {valor}\n"

    nombre_del_archivo = f"heroes_cantidad_{tipo_de_dato}.CSV"
    true_or_false = guardar_archivo(nombre_del_archivo,texto)

    return true_or_false

# vamos = (cantidad_color_de_ojos_o_pelo(lista_heroes,"inteligencia"))

# print(guardar_cantidad_heroes_tipo(vamos,"inteligencia"))



##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 5.3




def stark_calcular_cantidad_por_tipo(lista_heroes:list,tipo_de_dato_a_buscar):


    vamos = (cantidad_color_de_ojos_o_pelo(lista_heroes,tipo_de_dato_a_buscar))

    capitalize = palabras_capitalizado(vamos)

    True_or_false = (guardar_cantidad_heroes_tipo(capitalize,tipo_de_dato_a_buscar))

    return True_or_false


# print(stark_calcular_cantidad_por_tipo(lista_heroes,"Inteligencia"))



##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 6.1.

# Crear la función 'obtener_lista_de_tipos' la cual recibirá por parámetro
# la lista de héroes y un string que representará el tipo de dato/key a
# buscar (color_ojos, color_pelo, etc).
# Esta función deberá iterar la lista de héroes guardando en una lista las
# variedades del tipo de dato pasado por parámetro (sus valores).
# En caso de encontrar una key sin valor (o string vacío), deberás
# hardcodear con el valor 'N/A' y luego agregarlo a la lista donde irás
# guardando todos los valores encontrados, si el valor del héroe no tiene
# errores, guardarlo tal cual viene.
# Finalmente deberás eliminar los duplicados de esa lista y retornarla

# como un set.
# Reutilizar 'capitalizar_palabras' para guardar cada uno de los datos
# con la primera letra mayúscula.


def obtener_lista_de_tipos(lista_heroes:list,key:str):

    lista_de_datos_nuevos = []
    for i in lista_heroes:
        if  key in i:
            if i[key] == "" or i[key] == " ":
                i[key] = 'N/a'
            lista_de_datos_nuevos.append((i[key]).title())

    lista_seteada = set(lista_de_datos_nuevos)

    return lista_seteada

# print(obtener_lista_de_tipos(lista_heroes,"inteligencia"))



##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#6.2

# Crear la función 'normalizar_dato' la cual recibirá por parámetro un
# dato de héroe (el valor de una de sus keys, por ejemplo si la key fuese
# color_ojos y su valor fuese Verde, recibira este ultimo) y tambien una
# variable como string la cual representará el valor por defecto a colocar
# en caso de que el valor está vacío. Deberá validar que el dato no esté
# vacío, en caso de estarlo lo reemplazará con el valor default pasado
# por parámetro y lo retornará, caso contrario lo retornará sin
# modificaciones.


def normalizar_dato(reemplazar):
    lista_de_datos_nuevos = []

    for i in lista_heroes:
        for clave, valor in i.items():
            if " " ==  valor or valor == "" :
                i[clave] = reemplazar
    lista_de_datos_nuevos.append(i)

    return lista_heroes

# MENSAJE = (normalizar_dato("NO TIENE"))
# print(MENSAJE)


##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 6.3.

# Crear la función 'normalizar_heroe' la cual recibirá dos parámetros. el
# primero será un diccionario que representará un solo héroe, el
# segundo parámetro será el nombre de la key de dicho diccionario la
# cual debe ser normalizada.
# La función deberá capitalizar las palabras que tenga dicha key como
# valor, luego deberá normalizar el dato (ya que si viene vacío, habrá
# que setearlo con N/A).
# Finalmente deberá capitalizar todas las palabras del nombre del héroe
# y deberá retornar al Hero con cada palabra de su nombre
# capitalizados, cada palabra del valor de la key capitalizadas y
# normalizadas (con N/A en caso de que estuviesen vacías por defecto).
# Reutilizar: 'capitalizar_palabras' y 'normalizar_dato'


def normalizar_heroe(diccionario,key):
    for clave, valor in diccionario.items():
        if key in clave:
            if " " ==  valor or valor == "" :
                diccionario[clave] = "N/a"
    diccionario_capitalizado = palabras_capitalizado(diccionario)
    return diccionario_capitalizado

# dicci = {"nuevo":"lor","inteligencia":""}
# print(normalizar_heroe(dicci,"inteligencia"))

##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Crear la funcion 'obtener_heroes_por_tipo' el cual recibira por
# parámetro:
# A. La lista de héroes
# B. Un set de tipos/variedades (colores de ojos, de pelo, etc)
# C. El tipo de dato a evaluar (la key en cuestion, color_ojos,
# color_pelo, etc)
# PRESTAR ATENCIÓN:
# A. Deberá iterar el set de tipos/variedades y por cada tipo tendrá evaluar
# si ese tipo existe como key en un diccionario el cual deberás armar.
# (contendrá cada variedad como key y una lista de nombres de héroes
# como valor de cada una de ellas).
# B. En caso de no existir dicha key en el diccionario, agregarla con una
# lista vacía como valor.
# C. Dentro de la iteración de variedades, iterar la lista de héroes (for
# anidado) 'normalizando' el posible valor que tenga la key evaluada, ya
# que podría venir vacía (qué función usarias aca? guiño guiño)
# D. Una vez normalizado el dato, evaluar si dicho dato coincide con el tipo
# pasado por parámetro.
# E. En caso de que coincida, agregarlo a la lista (inicialmente vacía) de la
# variedad iterada en el primer bucle.
# Esta función retornará un diccionario con cada variedad como key y
# una lista de nombres como valor.
# Por ejemplo:
# {
# "Celestes": ["Capitan America", "Tony Stark"],
# "Verdes": ["Hulk", "Viuda Negra"]
# ....
# }



def normalizar_lista(lista_heroes,dato_a_evaluar):
    nueva_lista = []
    for i in lista_heroes:
        dato_normlaizado = normalizar_heroe(i,dato_a_evaluar)
        nueva_lista.append(dato_normlaizado)
    return nueva_lista


def obtener_heroes_por_tipo(lista_heroes:list,lista_de_tipos_set:set,dato_a_evaluar):

    lista_normalizada = normalizar_lista(lista_heroes,dato_a_evaluar)
    # lista_de_tipos_set = obtener_lista_de_tipos(lista_heroes,"inteligencia")

    diccionario_inteligente = {}

    for i in lista_de_tipos_set:
        if lista_de_tipos_set != diccionario_inteligente:
            diccionario_inteligente[i] = []

    for heroe in lista_normalizada:
        for clave , valor in heroe.items():
            if valor in lista_de_tipos_set:
                diccionario_inteligente[valor].append(heroe["Nombre"])

    return diccionario_inteligente

# lista_de_tipos_set = obtener_lista_de_tipos(lista_heroes,"inteligencia")

# print(obtener_heroes_por_tipo(lista_heroes,lista_de_tipos_set,"inteligencia"))




##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Crear la funcion 'guardar_heroes_por_tipo' la cual recibira por
# parámetro un diccionario que representará los distintos tipos como
# clave y una lista de nombres como valor (Lo retorna la función anterior)
# y además como segundo parámetro tendrá un string el cual
# representará el tipo de dato a evaluar (color_pelo, color_ojos, etc).
# Deberá recorrer cada key y cada valor (lista) que esta contenga para
# finalmente crear un string el cual será un mensaje que deberás
# imprimir formateado.
# Por ejemplo:
# "color_ojos Green: Black Widow | Hulk"
# Reutilizar la función 'guardar_archivo'. El archivo final deberá respetar
# el formato:
# heroes_segun_TipoDato.csv
# Donde:
# ● TipoDato: es la key la cual indicará qué cosas se deben guardar
# en el archivo.
# Ejemplo:
# heroes_segun_color_pelo.csv (Agrupados por color de pelo)
# heroes_segun_color_ojos.csv (Agrupados por color de ojos)
# Esta función retorna True si salió todo bien, False caso contrario.


def guardar_heroes_por_tipo(diccionario:dict,agrupar):
    nombre = None
    mensaje = ""
    color_a_agrupar = []
    guardar = ""
    for  clave , valor in diccionario.items():
        nombre = valor
        color_a_agrupar.append(clave)

    for i in nombre:
        mensaje += f" {i} |"

    for i in color_a_agrupar:
        guardar += f"{agrupar} {i}:{mensaje}\n"

    nombre_del_archivo = f"Heroes_segun_{agrupar}.CSV"
    True_false =guardar_archivo(nombre_del_archivo,guardar)

    return True_false

# agrupar = "inteligencia"
# lista_de_tipos_set = obtener_lista_de_tipos(lista_heroes,agrupar)
# diccionario = obtener_heroes_por_tipo(lista_heroes,lista_de_tipos_set,agrupar)
# print(guardar_heroes_por_tipo(diccionario,agrupar))





##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Crear la función 'stark_listar_heroes_por_dato' la cual recibirá por
# parámetro la lista de héroes y un string que representará el tipo de
# dato a evaluar (color_pelo, color_ojos, etc). Dentro deberás reutilizar
# las funciones:
# A. 'obtener_lista_de_tipos'
# B. 'obtener_heroes_por_tipo'
# C. 'guardar_heroes_por_tipo'
# Pasando por parámetro lo que corresponda según la lógica de las
# funciones usadas.

# Esta función retornará True si pudo guardar el archivo, False caso
# contrario.




def stark_listar_heroes_por_dato(lista_heroes,color_key_a_agrupar):

    lista_de_tipos_set = obtener_lista_de_tipos(lista_heroes,color_key_a_agrupar)
    diccionario = obtener_heroes_por_tipo(lista_heroes,lista_de_tipos_set,color_key_a_agrupar)
    True_or_false = guardar_heroes_por_tipo(diccionario,color_key_a_agrupar)

    return True_or_false

# print(stark_listar_heroes_por_dato(lista_heroes,"color_pelo"))



# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F

# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)

# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia
# S. SALIR



                                        
# def stark_marvel_app_5():
#     bandera = True
#     while bandera:
#         impresion = stark_menu_principal_desafio_5()
#         print(impresion)
#         if impresion == "A":
#             stark_guardar_heroe_genero(lista_heroes, "M")
#             print("entro aca")
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "B":
#             stark_guardar_heroe_genero(lista_heroes, "F")
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "C":
#             ALTURA = calcular_max_min_dato(lista_heroes, "M", "altura", "maximo")
#             for I in ALTURA:
#                 print(I)
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "D":
#             ALTURA = calcular_max_min_dato(lista_heroes, "F", "altura", "maximo")
#             for I in ALTURA:
#                 print(I)
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "E":
#             ALTURA = calcular_max_min_dato(lista_heroes, "M", "altura", "minimo")
#             for I in ALTURA:
#                 print(I)
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "F":
#             ALTURA = calcular_max_min_dato(lista_heroes, "F", "altura", "minimo")
#             for I in ALTURA:
#                 print(I)
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "G":
#             stark_calcular_imprimir_promedio_altura(lista_heroes, "M")
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "H":
#             stark_calcular_imprimir_promedio_altura(lista_heroes, "M")
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "I":
                
#                 ALTURA = calcular_max_min_dato(lista_heroes, "M", "altura", "maximo")
#                 for I in ALTURA:
#                     print(F"NOMBRE DE LA PERSONA MAS ALTA MASCULINA : {I}")
#             ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////            

#                 ALTURA = calcular_max_min_dato(lista_heroes, "F", "altura", "maximo")
#                 for I in ALTURA:
#                     print(F"NOMBRE DE LA PERSONA MAS ALTA FEMENINA  : {I}")
#             ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////            

#                 ALTURA = calcular_max_min_dato(lista_heroes, "M", "altura", "minimo")
#                 for I in ALTURA:
#                     print(F"NOMBRE DE LA PERSONA MAS BAJA MASCULINA : {I}")
#             ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////            
#                 ALTURA = calcular_max_min_dato(lista_heroes, "F", "altura", "minimo")
#                 for I in ALTURA:
#                     print(F"NOMBRE DE LA PERSONA MAS BAJA FEMENINA  : {I}")

#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "J":
#             print(cantidad_color_de_ojos_o_pelo(lista_heroes, "ojos"))
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "K":
#             print(cantidad_color_de_ojos_o_pelo(lista_heroes, "pelo"))
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "L":
#             MENSAJE = normalizar_dato("NO TIENE")
#             print(cantidad_color_de_ojos_o_pelo(MENSAJE, "inteligencia"))
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "M":
#             lista_de_tipos_set = obtener_lista_de_tipos(lista_heroes, "color_ojos")
#             print(obtener_heroes_por_tipo(lista_heroes, lista_de_tipos_set, "color_ojos"))
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "N":
#             lista_de_tipos_set = obtener_lista_de_tipos(lista_heroes, "color_pelo")
#             print(obtener_heroes_por_tipo(lista_heroes, lista_de_tipos_set, "color_pelo"))
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "O":
#             lista_de_tipos_set = obtener_lista_de_tipos(lista_heroes, "inteligencia")
#             print(obtener_heroes_por_tipo(lista_heroes, lista_de_tipos_set, "inteligencia"))
#         ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         elif impresion == "Z":
#             break
#         else:
#             print("COLOCAR ALGUNA LETRA VALIDA")

stark_marvel_app_5()
