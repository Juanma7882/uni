from data_stark import *
import re 




# Desafío #04:
# IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
# escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
# un string, etc y que contendrá) y que es lo que retorna la función!

# 1.1. Crear la función ‘extraer_iniciales’ que recibirá como parámetro:
# ● nombre_heroe: un string con el nombre del personaje
# La función deberá devolver a partir del parámetro recibido un nuevo string con
# las iniciales del nombre del personaje seguidos por un punto (.)
# ● En el caso que el nombre del personaje contenga el artículo ‘the’ se
# deberá omitir de las iniciales
# ● Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso
# que lo tenga se deberá reemplazar por un espacio en blanco
# La función deberá validar:
# ● Que el string recibido no se encuentre vacío
# Devolver ‘N/A’ en caso de no cumplirse la validación

# Ejemplo de la salida de la función para Howard the Duck:
# H.D.



def extraer_iniciales(lista:list):
    """
    Extrae las iniciales de los nombres de una lista de personas.
    Args:
        lista: Lista de personas.
    Returns:
        Lista de iniciales.
    """
    if len(lista) == 0:
        return  "N/A"

    # resultado = []
    for i in lista:
        cadena_a_procesar = (i["nombre"])
        palabra = cadena_a_procesar.lower()#normaliza todo a minuscula

        #proceso de eliminacion
        #Elimina todas las apariciones de "the" y el carácter "-"
        # palabra = palabra.replace("the", " ")#IMPORTANTE EL ESPACIO PARA QUE NO SE COMO LA PALABRA VECINA
        # palabra = palabra.replace("-", " ")

        palabra = re.sub(r"the"," ", palabra)#IMPORTANTE EL ESPACIO PARA QUE NO SE COMO LA PALABRA VECINA
        palabra = re.sub(r"-"," ", palabra)
        palabras = re.split(r'\s+', palabra) #sin el mas muestra hasta los espacios en blanco
        # palabras = palabra.split()#SEPARO LOS CARACTERES

        # Divide la cadena en palabras
        iniciales = []
        # Iterar a través de las palabras y tomar la primera letra
        for i in palabras:
                inicial = i[0].upper()# Tomar la primera letra y convertirla a mayúscula
                iniciales.append(inicial)
        puntuacion = "."
        puntuacion = puntuacion.join(iniciales)+ "."
        # resultado.append(puntuacion)
        
        resultado = puntuacion
        return(resultado)
    

(extraer_iniciales(lista_personajes))






# 1.2. Crear la función ‘definir_iniciales_nombre’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del personaje
# La función deberá agregar una nueva clave al diccionario recibido como
# parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de
# llamar a la función ‘extraer_iniciales’
# La función deberá validar:
# ● Que el dato recibido sea del tipo diccionario
# ● Que el diccionario contengan la clave ‘nombre’
# En caso de encontrar algún error retornar False, caso contrario retornar True



def definir_iniciales_nombre(lista:list)->bool:
    """
    agrega una clave "iniciales" a cada elemento de una 
    lista, con el valor de las iniciales del nombre del elemento
    """
    mensaje = False
    for  i in lista:
        tipo_de_dato = type(i)
        if tipo_de_dato == dict:
            for keys, values in i.items():
                if "nombre" in keys:
                    mensaje = True
                    
    if mensaje == True:
        for i in range(len(lista)):
            lista[i]["iniciales"]= extraer_iniciales([lista[i]])
    return mensaje
        
# print(definir_iniciales_nombre(lista_personajes))
# print(lista_personajes)
definir_iniciales_nombre(lista_personajes)
# 1.3. Crear la función ‘stark_imprimir_nombres_con_iniciales’ la cual recibirá
# como parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle
# las iniciales a los diccionarios contenidos en la lista_heroes
# Luego deberá imprimir la lista completa de los nombres de los personajes
# seguido de las iniciales encerradas entre paréntesis ()
# Se deberá validar:
# ● Que lista_heroes sea del tipo lista
# ● Que la lista contenga al menos un elemento
# Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de
# viñeta) seguido de un espacio.
# Ejemplo de salida:
# * Howard the Duck (H.D.)
# * Rocket Raccoon (R.R.)
# ...
# La función no retorna nada

def stark_imprimir_nombres_con_iniciales(lista:list):
    """
    recibe una lista y devuelve el nombre con sus iniciales: 
    * Howard the Duck (H.D.)
    """
    if (type(lista) == (list)) and (len(lista)>0):
        definir_iniciales_nombre(lista_personajes)
        for i in lista_personajes:
            mensaje = f" * {i['nombre']} ({i['iniciales']})"
            print(mensaje)
    else:
        pass
# stark_imprimir_nombres_con_iniciales(lista_personajes)



# 2.1. Crear la función ‘generar_codigo_heroe’ la cual recibirá como parámetros:
# ● id_heroe: un entero que representa el identificador del héroe.
# ○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
# 2.3. Para probar la función podes pasarle cualquier entero
# ● genero_heroe: un string que representa el género del héroe ( puede
# tomar los valores ‘M’, ‘F’ o ‘NB’)
# La función deberá generar un string con el siguiente formato:
# GENERO-000...000ID
# Es decir, el género recibido por parámetro seguido de un ‘-’ (guión) y por
# último el identificador recibido. Todos los códigos generados deben tener
# como máximo 10 caracteres (contando todos los caracteres, inclusive el
# guión). Se deberá completar con ceros para que todos queden del mismo
# largo
# Algunos ejemplos:
# F-00000001
# M-00000002
# NB-0000010
# La función deberá validar:
# ● El identificador del héroe sea numérico.
# ● El género no se encuentre vacío y este dentro de los valores esperados
# (‘M’, ‘F’ o ‘NB’)
# En caso de no pasar las validaciones retornar ‘N/A’. En caso de verificarse
# correctamente retornar el código generado

def asignar_iD(lista:list):
    contador = 1
    for i in range(len(lista)):
        lista[i]["id"]= f"{contador}" 
        contador += 1 
    
# print(asignar_iD(lista_personajes))
(asignar_iD(lista_personajes))





def validacion_entero(numeros):
    """
    recibe una cadena de numeros y valida que sean enteros
    devuelve true si son enteros false en caso contrario
    """
    validacion_numero_entero = r'^[1-9][0-9]*$' 
    if re.match(validacion_numero_entero, numeros):
        mensaje = True
    else:
        mensaje = False
    return mensaje
# prueba = "jk"
# print(validacion_entero(prueba))


def validacion_de_genero(generos):
    """
    devuelve tru si genero es uno de estos 3: M F NB
    y false en caso contrario
    """
    validacion_genero = r'^[M F NB]+$'
    if re.match(validacion_genero, generos):
        mensaje = True
    else:
        mensaje = False
    return mensaje
# pruebagenero = ""
# print(validacion_de_genero(pruebagenero))

def generar_codigo_heroe(lista:list):
    """
    recive una lista y devuelve un codigo generado 
    con su posicion en la lista y su genero 
    """
    mensajes = []
    for i in lista:
        numero = i["id"]
        genero = i["genero"]
        validar_numero = validacion_entero(numero)
        validar_genero = validacion_de_genero(genero)

        if validar_numero == True and validar_genero == True:
            longitud_total = 10
            mensaje = f'{str(i["genero"])}-'
            largo = int(len(mensaje))
            tamaño = (longitud_total - largo)
            mensaje_final = f'{str(i["genero"])}-{str(i["id"]).zfill(tamaño)}'
            mensajes.append(mensaje_final)
            # el str es para asegurarse que lo tome como str
        else:
            mensajes.append("N/A")

    return mensajes

(generar_codigo_heroe(lista_personajes))

# print(generar_codigo_heroe(lista_personajes))

# 2.2. Crear la función ‘agregar_codigo_heroe’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del personaje
# ● id_heroe: un entero que representa el identificador del héroe.
# ○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
# 2.3. Para probar la función podes pasarle cualquier entero
# La función deberá agregar una nueva clave llamada ‘codigo_heroe’ al
# diccionario ‘heroe’ recibido como parámetro y asignarle como valor un código
# utilizando la función ‘generar_codigo_heroe’
# La función deberá validar:
# ● Que el diccionario recibido como parámetro no se encuentre vacío.
# ● Que el código recibido mediante generar_codigo_heroe tenga
# exactamente 10 caracteres
# En caso de pasar las validaciones correctamente la función deberá retornar
# True, en caso de encontrarse un error retornar False

diccionario ={"nombre":"pablo"}
entero = "2"
    # for i in lista_personajes:
        # entrada_numero = i[numero]
# vaci =[]
def agregar_codigo_heroe(lista):
        """
        agrega una nueva calve a los diccionarios de la lista
        llamada codigo heroe (llama a generar codigo)
        """
        mensaje = False
        for i in range(len(lista)):
            codigo = generar_codigo_heroe(lista)
            for ico in  codigo:
                tamaño = len(ico)
                if tamaño == 10:
                    lista[i]["codigo_heroe"] = codigo[i]
                    mensaje = True
        
        return mensaje
(agregar_codigo_heroe(lista_personajes))



# 2.3. Crear la función ‘stark_generar_codigos_heroes’ la cual recibirá como
# parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá iterar la lista de personajes y agregarle el código a cada
# uno de los personajes.
# El código del héroe (id_heore) surge de la posición del mismo dentro de la
# lista_heroes (comenzando por el 1).
# Reutilizar la función agregar_codigo_heroe pasándole como argumentos el
# héroe que se está iterando y el id_heroe
# Una vez finalizado imprimir por pantalla un mensaje como el siguiente:
# (## representa la cantidad de códigos generados):
# Se asignaron ## códigos
# * El código del primer héroe es: M-00000001
# * El código del del último héroe es: M-00001224
# La función deberá validar::
# ● La lista contenga al menos un elemento
# ● Todos los elementos de la lista sean del tipo diccionario
# ● Todos los elementos contengan la clave ‘genero’
# En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no
# contiene el formato correcto’
# La función no retorna ningún valor.


def stark_generar_codigos_heroes(lista:list):
    """
    genera un id que depende de su posicion en la lista
    """
    valor = True

    tamaño_lista = len(lista)
    if tamaño_lista == 0:
        mensaje = "El origen de datos no contiene el formato correcto"
        valor = False
    else:
        for i in lista:
            tipo_dato = type(i)
            if tipo_dato != dict or "genero" in lista:
                mensaje = "El origen de datos no contiene el formato correcto"
                valor = False

    if valor == True:
        contador = 1
        for i in range(len(lista)):
            lista[i]["id"]= f"{contador}" 
            contador += 1 
            mensaje = ""
    return mensaje

(stark_generar_codigos_heroes(lista_personajes))
# print(stark_generar_codigos_heroes(lista_personajes))


# 3.1. Crear la función ‘sanitizar_entero’ la cual recibirá como parámetro:
# ● numero_str: un string que representa un posible número entero
# La función deberá analizar el string recibido y determinar si es un número
# entero positivo. La función debe devolver distintos valores según el problema
# encontrado:
# ● Si contiene carácteres no numéricos retornar -1
# ● Si el número es negativo se deberá retornar un -2
# ● Si ocurren otros errores que no permiten convertirlo a entero entonces
# se deberá retornar -3
# También deberá quitar los espacios en blanco de atras y adelante del string
# en caso que los tuviese
# En caso que se verifique que el texto contenido en el string es un número
# entero positivo, retornarlo convertido en entero
cadena = "lDdDFSkjdsk"
negativo = "-23"
entero = "432 "
def sanitizar_entero(numero:str)->str:
    """
    recibe una cadena de numeros y valida que sean enteros 
    y lo convierete a entero
    """
    validacion_numero_entero = r'[0-9]+$'           #entero
    validacion_entero_negativo = r'^[-][1-9]+$'     #-1
    validacion_letras = r'[a-zA-Z]+$'               #-2
    if " " in numero:
        numero = re.sub(r" ","", numero)
    if re.match(validacion_numero_entero, numero):
        
        mensaje = f"convertido a entero"
    elif re.match(validacion_letras,numero):
        mensaje= "-1"
    elif re.match(validacion_entero_negativo,numero):
        mensaje = "-2"
    else:
        mensaje = "-3"

    return mensaje

# 3.2. Crear la función ‘sanitizar_flotante’ la cual recibirá como parámetro:
# ● numero_str: un string que representa un posible número decimal
# La función deberá analizar el string recibido y determinar si es un número
# flotante positivo. La función debe devolver distintos valores según el
# problema encontrado:
# ● Si contiene carácteres no numéricos retornar -1
# ● Si el número es negativo se deberá retornar un -2
# ● Si ocurren otros errores que no permiten convertirlo a entero entonces
# se deberá retornar -3
# También deberá quitar los espacios en blanco de atras y adelante del string
# en caso que los tuviese
# En caso que se verifique que el texto contenido en el string es un número
# flotante positivo, retornarlo convertido en flotante
cadena = "lDdDFSkjdsk"
negativo = "-23"
entero = "432 "
flotante = "93.9897798798987"
def sanitizar_flotante(numero):
    """
    recive un dato y si es flotante dice que fue convertido a flotante
    * si son caracteres no numericos -1
    * si son caracteres negativos -2
    * si es otro problema devuelve -3
    """
    validacion_numero_flotante = r'\d+\.\d{1,20}$'
    validacion_entero_negativo = r'^[-][0-9]+$'
    validacion_letras = r'[a-zA-Z]+$'
    if " " in numero:
        numero = re.sub(r" ","", numero)
    if re.match(validacion_numero_flotante, numero):
        
        mensaje = "convertido a flotante"
    elif re.match(validacion_letras,numero):
        mensaje= "-1 "
    elif re.match(validacion_entero_negativo,numero):
        mensaje = "-2 "
    else:
        mensaje = "-3"

    return mensaje
# print(sanitizar_flotante(flotante))



# 3.3. Crear la función ‘sanitizar_string’’ la cual recibirá como parámetro
# ● valor_str: un string que representa el texto a validar
# ● valor_por_defecto: un string que representa un valor por defecto
# (parámetro opcional, inicializarlo con ‘-’)
# La función deberá analizar el string recibido y determinar si es solo texto (sin
# números). En caso de encontrarse números retornar “N/A”
# En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada por un
# espacio
# El espacio es un caracter válido
# En caso que se verifique que el parámetro recibido es solo texto, se deberá
# retornar el mismo convertido todo a minúsculas
# En el caso que el texto a validar se encuentre vacío y que nos hayan pasado
# un valor por defecto, entonces retornar el valor por defecto convertido a
# minúsculas
# Quitar los espacios en blanco de atras y adelante de ambos parámetros en
# caso que los tuviese

letr= "                         zs dcf "
def sanitizar_string(string:str,valor_pordefecto="-"):
    """
    valida que lo que es igresado sea un str
    devuelve si son letras y numeros devuelve n/a
    en caso qye no se ni letras ni numeros o letras devuelve -3
    """
    validacion_letras_numeros = r'[a-zA-Z0-9]+$'
    validacion_letras = r'[a-z A-Z]*$'

    if "/" in string:
        string = re.sub(r"/"," ", string)

    if re.match(validacion_letras_numeros,string):
        mensaje= "N/A"
    elif re.match(validacion_letras,string):
        normalizar = string.lower()
        corte_espacios = normalizar.strip() 
        mensaje = f"{valor_pordefecto}{corte_espacios}"
    else:
        mensaje = "-3"

    return mensaje

# print(sanitizar_string(letr))

# 3.4. Crear la función ‘sanitizar_dato’ la cual recibirá como parámetros:
# ● heroe: un diccionario con los datos del personaje
# ● clave: un string que representa el dato a sanitizar (la clave del
# diccionario). Por ejemplo altura
# ● tipo_dato: un string que representa el tipo de dato a sanitizar. Puede
# tomar los valores: ‘string’, ‘entero’ y ‘flotante’
# La función deberá sanitizar el valor del diccionario correspondiente a la clave
# y al tipo de dato recibido
# Para sanitizar los valores se deberán utilizar las funciones creadas en los
# puntos 3.1, 3.2, 3.3 y 3.4

# Se deberá validar:
# ● Que tipo_dato se encuentre entre los valores esperados (‘string, ‘entero,
# ‘flotante)’ la validación debe soportar que nos lleguen mayúsculas o
# minúsculas. En caso de encontrarse un valor no válido informar por
# pantalla: ‘Tipo de dato no reconocido’

# ● Que clave exista como clave dentro del diccionario heroe. En caso de
# no encontrarse, informar por pantalla: ‘La clave especificada no
# existe en el héroe’. (en este caso la validación es sensible a
# mayúsculas o minúsculas)
# Ejemplo de llamada a la función válida:
# sanitizar_dato(dict_personaje, “altura”, “Flotante”)
# La función deberá devolver True en caso de haber sanitizado algún dato y
# False en caso contrario.
heroe = {
    "nombre": "Black Widow",
    "identidad": "Natasha Romanoff",
    "empresa": "Marvel Comics",
    "altura": "170.78999999999999",
    "peso": "59.340000000000003",
    "genero": "F",
    "color_ojos": "Green",
    "color_pelo": "Auburn",
    "fuerza": "15",
    "inteligencia": "good"
    }

# for i in heroe:
#     print(sanitizar_string(i["nombre"]))

def sanitizar_dato(diccionario,clave,tipo_de_dato):
    '''
    heroe:diccionario con los datos del personaje
    clave:un string que representa el dato a sanitizar
    tipo de dato : puede ser / string / flotante / entero
    '''
    if tipo_de_dato == "string":
        for claves,valor in diccionario.items():
            if claves == clave:
                print(sanitizar_string(valor))
    elif tipo_de_dato == "flotante" :
            for claves,valor in diccionario.items():
                if claves == clave:
                    print(sanitizar_flotante(valor))
        
    elif tipo_de_dato == "entero":
        for claves,valor in diccionario.items():
                if claves == clave:
                    print(sanitizar_entero(valor))
                    
# print(sanitizar_dato(heroe,"altura","flotante"))


# 3.5. Crear la función 'stark_normalizar_datos’ la cual recibirá como parámetros:
# ● lista_heroes: la listas personajes
# La función deberá recorrer la lista de héroes y sanitizar los valores solo de las
# siguientes claves: ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e
# ‘inteligencia’
# ● Un vez finalizado el proceso mostrar el mensaje ‘Datos normalizados’,
# ● Validar que la lista de héroes no esté vacía para realizar sus acciones,
# caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
# ● La función no retorna nada
# ● Reutilizar la función sanitizar_dato

def stark_normalizar_datos(lista:list):
    """
    recive la lista de personajes y se asegura de que cada uno sea 
    de cada tipo correspodiente
    """
    tamaño = len(lista)
    if tamaño == 0:
        mensaje ="Error: Lista de héroes vacía"
        print(mensaje)
    for i in lista:
        for claves,valores in i.items():
            match claves:
                case "altura":
                    (sanitizar_flotante(valores))
                    mensajeA = "altura normalizada"
                case "peso":
                    (sanitizar_flotante(valores))
                    mensajeB = "peso normalizada"
                case "color_ojos":
                    sanitizar_string(valores)
                    mensajeC = "color de ojos normalizada"
                case "color_pelo":
                    sanitizar_string(valores)
                    mensajeD = "color de pelo normalizada"
                case "fuerza":
                    sanitizar_entero(valores)
                    mensajeE = "fuerza normalizada"
                case "inteligencia":
                    sanitizar_string(valores)
                    mensajeF = "inteligencia normalizada"
    print("datos normalizados")

# stark_normalizar_datos(lista_personajes)

# 4.1. Crear la función ‘generar_indice_nombres’ la cual recibirá como parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá iterar la lista de personajes y generar una lista donde cada
# elemento es cada palabra que componen el nombre de los personajes.

# Por ejemplo la lista que se deberá retornar tiene la siguiente forma:
# [‘Howard’, ‘the’, ‘Duck’, ‘Rocket’, ‘Raccoon’, ‘Wolverine’, ... ]
# La función deberá validar que:
# ● La lista contenga al menos un elemento
# ● Todos los elementos de lista_heroes sean del tipo diccionario
# ● Todos los elementos contengan la clave ‘nombre’
# En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no
# contiene el formato correcto’

vacio = []
def generar_indice_nombres(lista:list):
    """
    recorre la lista de personajes y agarra todos los nombre  
    y los retorna en una lista con todos los nombre
    """
    lista_nombres = []
    lista_ingresada = lista
    tamaño = len(lista_ingresada)
    bandera = False
    if tamaño == 0:
        bandera = False
    for i in lista_ingresada:
        tipo_dato = type(i)
        if tipo_dato != dict:
            mensaje = False
        for clave,valor in i.items():
            if clave == "nombre":
                bandera = True

    for i in lista_ingresada:
        if bandera == True:
            personaje = i["nombre"]
            lista_nombres.append(personaje)
    if bandera == True:
        mensaje = lista_nombres
    else:
        mensaje = "El origen de datos no contiene el formato correcto"
    return mensaje

(generar_indice_nombres(lista_personajes))




# 4.2. Crear la función ‘stark_imprimir_indice_nombre’ la cual recibirá como
# parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá mostrar por pantalla el índice generado por la función
# generar_indice_nombres con todos los nombres separados con un guión.
# Por ejemplo:
# Howard-the-duck-Rocket-Raccoon-Wolverine...

def stark_imprimir_indice_nombre(lista_personajes: list):
    """
    genera un str que tiene todos los nombres de la lista 
    unidos por guiones
    """
    lista = (generar_indice_nombres(lista_personajes))
    texto_unido = "-".join(lista)
    indice = re.sub(r" ","-", texto_unido)
    return indice
# print(stark_imprimir_indice_nombre(lista_personajes))
(stark_imprimir_indice_nombre(lista_personajes))


# 5.1. Crear la función ‘convertir_cm_a_mtrs’ la cual recibirá como parámetro:
# ● valor_cm: Un número que representa una medida en centímetros
# La función deberá retornar el número recibido, pero convertido a la unidad
# metros. La función deberá validar que el número recibido sea un número
# flotante positivo, en caso de no serlo retornar -1
numero_en_cms = "3.4"
def convertir_cm_a_mtrs(valor_en_cm:float):
    """
    recibe el str de un numero y que se desea pasar a Metros 
    el numero apasar se debe ingresar en cm
    """
    validacion_numero_flotante = r'\d+\.\d{1,20}$'
    if re. match(validacion_numero_flotante,valor_en_cm):
        numero_flotante = float(valor_en_cm)
        resultado = numero_flotante/100
    else:
        resultado = "-1"
    return resultado
# print(convertir_cm_a_mtrs(numero_en_cms))
(convertir_cm_a_mtrs(numero_en_cms))


# 5.2. Crear la función ‘generar_separador’ la cual recibirá como parámetro
# ● patron: un carácter que se utilizará como patrón para generar el
# separador
# ● largo: un número que representa la cantidad de caracteres que va
# ocupar el separador.
# ● imprimir: un parámetro opcional del tipo booleano (por default definir
# en True)
# La función deberá generar un string que contenga el patrón especificado
# repitiendo tantas veces como la cantidad recibida como parámetro (uno junto
# al otro, sin salto de línea)
# Si el parámetro booleano recibido se encuentra en False se deberá solo
# retornar el separador generado. Si se encuentra en True antes de retornarlo,
# imprimirlo por pantalla
# La función deberá validar:
# ● Que el parámetro patrón tenga al menos un carácter y como máximo
# dos
# ● Que el parámetro largo sea un entero entre 1 y 235 inclusive
# En caso de no verificarse las validaciones devolver ‘N/A’
# Ejemplo de llamada:
# generar_separador(‘*’, 10)
# Ejemplo de salida:
# **********


def generar_separador(patron, largo, imprimir=True):
    """
    recibe el patron un largo a imprimir 
    """
    tamaño_patron = len(patron)
    if not (1 <= tamaño_patron <= 2) or not (1 <= largo <= 235):
        return "N/A"
    
    separador = patron * largo
    
    if imprimir == True:
        (separador)
    else :
        print(separador)

    return separador

# resultado = generar_separador('*$', 10)
# print(resultado) 



# 5.3. Crear la función ‘generar_encabezado’ la cual recibirá como parámetro
# ● titulo: un string que representa el título de una sección de la ficha
# La función deberá devolver un string que contenga el título envuelto entre dos
# separadores (estimar el largo requerido para tu pantalla).
# Ejemplo de salida:
# ********************************************************************************
# PRINCIPAL
# ********************************************************************************
# La función deberá convertir el titulo recibido en todas letras mayúsculas
def generar_encabezado(titulo:str):
    """
    recibe un str para el titulo al cual sera encerrado con simbolos 
    """
    palabra = titulo.upper()
    resultado = generar_separador('//', 30)
    mensaje = f"{resultado}\n"
    mensaje += f"{palabra}\n"
    mensaje += f"{resultado}\n"
    return mensaje


# print(generar_encabezado("titulo"))




# 5.4. Crear la función ‘imprimir_ficha_heroe’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del héroe
# La función deberá a partir los datos del héroe generar un string con el
# siguiente formato e imprimirlo por pantalla::
# ***************************************************************************************
# PRINCIPAL
# ***************************************************************************************
# NOMBRE DEL HÉROE: Spider-Man (S.M.)
# IDENTIDAD SECRETA: Peter Parker
# CONSULTORA: Marvel Comics
# CÓDIGO DE HÉROE : M-00000001
# ***************************************************************************************
# FISICO
# ***************************************************************************************

# ALTURA: 1,78 Mtrs.
# PESO: 74,25 Kg.
# FUERZA: 55 N
# ***************************************************************************************
# SEÑAS PARTICULARES
# ***************************************************************************************
# COLOR DE OJOS: Hazel
# COLOR DE PELO: Brown

# print(lista_personajes)
def imprimir_ficha_heroe(lista):
    """
    recibe la lista de personajes y lo imprime con sierto formato
    """
    lista_datos =[]
    for i in lista:
        (i["altura"]) = (convertir_cm_a_mtrs(i["altura"]))
        m = generar_encabezado("principal") 
        m += f"NOMBRE DEL HÉROE: {i['nombre']} ({i['iniciales']})\n"
        m += f"IDENTIDAD SECRETA: {i['identidad']}\n"
        m += f"CONSULTORA: {i['empresa']}\n"
        m += f"CÓDIGO DE HÉROE: {i['codigo_heroe']}\n"
        m += generar_encabezado("fisico") 
        m += f"ALTURA: {float(i['altura'])} Mtrs\n"
        m += f"PESO: {float(i['peso'])} Kg\n"
        m += f"FUERZA: {int(i['fuerza'])} N\n"
        m += generar_encabezado("SEÑAS PARTICULARES") 
        m += f"COLOR DE OJOS: {i['color_ojos']}\n"
        m += f"COLOR DE PELO: {i['color_pelo']}\n"
        lista_datos.append(m)

    # print(lista_datos)
    #for i in lista_datos:
        #print(i) i
    return lista_datos

# print(imprimir_ficha_heroe(lista_personajes))

# dato = (imprimir_ficha_heroe(lista_personajes))
# for i in dato:
# print(dato[1])


# 5.5. Crear la función 'stark_navegar_fichas’ la cual recibirá como parámetros:
# ● lista_heroes: la listas personajes
# La función deberá comenzar imprimiendo la ficha del primer personaje de la
# lista y luego solicitar al usuario que ingrese alguna de las siguientes opciones:
# [ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir
# ● Si el usuario ingresa ‘1’: se debe mostrar el héroe que se encuentra en
# la posición anterior en la lista (en caso de estar en el primero, ir al
# último)

# ● Si el usuario ingresa ‘2’: se debe mostrar el héroe que se encuentra en
# la posición siguiente en la lista (en caso de estar en el último, ir al
# primero)

# ● Si ingresa ‘S’: volver al menú principal

# ● Si ingresa cualquier otro valor, volver a mostrar las opciones hasta que
# ingrese un valor válido




# lista_fichas = imprimir_ficha_heroe(lista_personajes)
# primer_ficha = lista_fichas[0]
# print(primer_ficha)



def navegar_fichas(lista_a_navegar):
    """
    se ingresa la lista de personajes 
    """
    total_fichas = len(lista_a_navegar)
    if total_fichas == 0:
        print("No hay fichas para mostrar.")
        return

    indice_actual = 0
    while True:
        print(lista_a_navegar[indice_actual])

        if total_fichas > 1:
            opcion = input(f"Selecciona una opción: [1] Anterior [2] Siguiente [S] Salir: ").strip().lower()
            if opcion == '1':
                indice_actual = (indice_actual - 1)
                if indice_actual == -1:
                    indice_actual += total_fichas
            elif opcion == '2':
                indice_actual = (indice_actual + 1) 
                if indice_actual == total_fichas:
                    indice_actual = 0
            elif opcion == 's':
                break
            else:
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                print("Opción no válida. Por favor, selecciona una opción válida.\n")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        else:
            opcion = input(f"Selecciona una opción: [S] Salir: ").strip().lower()
            if opcion == 's':
                break

# lista_fichas = imprimir_ficha_heroe(lista_personajes)
# navegar_fichas(lista_fichas)
# navegar_fichas(imprimir_ficha_heroe(lista_personajes))


# 6.1. Crear la función ‘imprimir_menu’ que imprima las siguientes opciones por
# pantalla:
# """

# 1 - Imprimir la lista de nombres junto con sus iniciales
# 2 - Generar códigos de héroes
# 3 - Normalizar datos
# 4 - Imprimir índice de nombres
# 5 - Navegar fichas
# S - Salir

# ____________________________________________________________
# """

def imprimir_menu():
    """
    imprime el menu
    """
    menu ="""    

        🚀 stark 4# 🚀
        
        (•-•)  (#_<)  
        [> <]  /> <\   
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Generar códigos de héroes
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    6 - Salir
    """
    print(menu)

# imprimir_menu()

# 6.2. Crear la función ‘stark_menu_principal'. No recibe parámetros.
# La función deberá imprimir el menú de opciones y le pedirá al usuario que
# ingrese una.
# La función deberá retornar la respuesta del usuario


def stark_menu_principal():
    """
    imprime el menu 
    y recibe una opcion
    """
    imprimir_menu()  # Llama a la función para imprimir el menú
    
    # ingrese una opción
    respuesta = input()
    
    return respuesta  # Retorna la respuesta del usuario

# opcion_elegida = stark_menu_principal()
# print(f"Opción elegida: {opcion_elegida}")

# 6.3. Crear la función ‘stark_marvel_app_3’ la cual recibirá como parámetro:
# ● lista_heroes: la lista de personajes
# La función se encargará de la ejecución principal de nuestro programa.
# Utilizar if/elif o match según prefiera (match solo para los que cuentan con

# python 3.10+).
# Debe informar por consola en caso de seleccionar una opción incorrecta y
# volver a pedir el dato al usuario.
# Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.

    """
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Generar códigos de héroes
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    6 - Salir
    """
    
def stark_marvel_app_4(lista_personajes):
    """
    imprime el marvel app
    """
    bandera = True
    while bandera:
        respuesta = stark_menu_principal()
        match respuesta:
            case "1":
                stark_imprimir_nombres_con_iniciales(lista_personajes)
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "2":
                print(generar_codigo_heroe(lista_personajes))
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "3":
                stark_normalizar_datos(lista_personajes)
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "4":
                print(stark_imprimir_indice_nombre(lista_personajes))
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "5":
                lista_fichas = imprimir_ficha_heroe(lista_personajes)
                navegar_fichas(lista_fichas)
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case "6":
                bandera = False  
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            case _:
                print("Opción no válida. Por favor, ingrese una opción válida.")
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

stark_marvel_app_4(lista_personajes)





































































































































# lista_numeros = [8, 5, 1, 4, 6, 9, 2, 10, 3, 7]
# print(lista_numeros)

# for i in range(len(lista_numeros)-1):
#     for j in range(i+1, len(lista_numeros)):
#         if lista_numeros[i] > lista_numeros[j]:
            
#             aux = lista_numeros[i]
#             lista_numeros[i] = lista_numeros[j]                      
#             lista_numeros[j] = aux               
# print(lista_numeros)

    

# lista_numeros = [8, 5, 1, 4, 6, 9, 2, 10, 3, 7]
# print(lista_numeros)

# for i in range(len(lista_numeros)-1):

#         if lista_numeros[i] > lista_numeros[i+1]:
            
#             aux = lista_numeros[i]
#             lista_numeros[i] = lista_numeros[i+1]                      
#             lista_numeros[i+1] = aux               
# print(lista_numeros)

# lista_numeros = [8, 5, 1, 4, 6, 9, 2, 10, 3, 7]
# print("Lista original:", lista_numeros)

# for i in range(len(lista_numeros)-1):
#     if lista_numeros[i] > lista_numeros[i+1]:
#         aux = lista_numeros[i]
#         lista_numeros[i] = lista_numeros[i+1]
#         lista_numeros[i+1] = aux

# print("Lista ordenada:", lista_numeros)


# lista_numeros = [8, 5, 1, 4, 6, 9, 2, 10, 3, 7]
# print("Lista original:", lista_numeros)

# n = len(lista_numeros)
# bandera = True

# while bandera:
#     bandera = False
#     for i in range(n-1):
#         if lista_numeros[i] > lista_numeros[i+1]:
#             lista_numeros[i], lista_numeros[i+1] = lista_numeros[i+1], lista_numeros[i]
#             bandera = True
#             print(lista_numeros)

# print("Lista ordenada:", lista_numeros)

# lista_palabras = ["perro", "gato", "manzana", "banana", "elefante","abeja",]
# print("Lista original:", lista_palabras)

# n = len(lista_palabras)
# bandera = True

# while bandera:
#     bandera = False
#     for i in range(n-1):
#         if lista_palabras[i] > lista_palabras[i+1]:
#             lista_palabras[i], lista_palabras[i+1] = lista_palabras[i+1], lista_palabras[i]
#             bandera = True

# print("Lista ordenada:", lista_palabras)

# import time

# lista_numeros = [8, 5, 1, 4, 6, 9, 2, 10, 3, 7]
# print("Lista original:", lista_numeros)

# # Registra el tiempo de inicio
# inicio = time.time()

# n = len(lista_numeros)
# bandera = True

# while bandera:
#     bandera = False
#     for i in range(n-1):
#         if lista_numeros[i] > lista_numeros[i+1]:
#             lista_numeros[i], lista_numeros[i+1] = lista_numeros[i+1], lista_numeros[i]
#             bandera = True

# # Registra el tiempo de finalización
# fin = time.time()

# print("Lista ordenada:", lista_numeros)

# # Calcula el tiempo transcurrido en segundos
# tiempo_transcurrido = fin - inicio
# print("Tiempo de ejecución:", tiempo_transcurrido, "segundos")

# for i in lista_personajes:
#     i["fuerza"] = int(i["fuerza"])
#     lista_numeros = i["fuerza"]
    

#     n = len(lista_personajes)
#     swapped = True
            
#     while swapped:
#         swapped = False
#         for i in range(n-1):
#             if lista_numeros[i] > lista_numeros[i+1]:
#                 lista_numeros[i], lista_numeros[i+1] = lista_numeros[i+1], lista_numeros[i]
#                 swapped = True

#     print("Lista ordenada:", lista_numeros)



# Supongamos que tienes una lista de personajes en formato de diccionarios
# lista_personajes = [
#     {"nombre": "Aragorn", "fuerza": 95},
#     {"nombre": "Gandalf", "fuerza": 100},
#     {"nombre": "Frodo", "fuerza": 60},
#     {"nombre": "Legolas", "fuerza": 85},
# ]

# Convierte la fuerza de cada personaje a un entero
# for personaje in lista_personajes:
#     personaje["fuerza"] = int(personaje["fuerza"])

# Ordena la lista de personajes por fuerza de manera ascendente
# n = len(lista_personajes)
# intercambio = True

# while intercambio:
#     intercambio = False
#     for i in range(n - 1):
#         if lista_personajes[i]["fuerza"] > lista_personajes[i + 1]["fuerza"]:
#             lista_personajes[i], lista_personajes[i + 1] = lista_personajes[i + 1], lista_personajes[i]
#             intercambio = True

# # Imprime la lista ordenada de personajes por fuerza
# for personaje in lista_personajes:
#     print("Nombre:", personaje["nombre"], "| Fuerza:", personaje["fuerza"])



