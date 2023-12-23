from data_stark import lista_personajes

"""""
TP : 1  STARK  
NOMBRE :JUAN MANUEL
APELLIDO FERNANDEZ
AUTOCORREGIDO SI

Luego de analizar el set de datos correspondiente resolver el Desafío #01:

A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino

NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
las opciones (A-E)
# """

# 1A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
# 2B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
#    fuerza (MÁXIMO)
# 3C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
#   (MÍNIMO)
# 4D. Recorrer la lista y determinar el peso promedio de los superhéroes
#   masculinos (PROMEDIO)
# 5E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
#   género) los cuales su fuerza supere a la fuerza promedio de todas las
#   superhéroes de género femenino

bandera = True
while (bandera):
    print(
        " \n"
        " 🚀 stark 1#\n"
        "              \n"
        "    (•-•)  (#_<)\n"
        "    [> <]  /> <\  \n"
        "1 - Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe 📋\n"
        "2 - Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza maxima💪\n"
        "3 - Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo mas bajo\n"
        "4 - Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)\n"
        "5 - Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier\n"
        "    género) los cuales su fuerza supere a la fuerza promedio de todas las\n"
        "    superhéroes de género femenino\n"
        "6 - salir del programa")
    respuesta = input()
##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if  respuesta =="1":
        patron = "_"
        largo = 146
        print(patron*largo)
        print(f'|{" ":4}{"Nombre":16}| {" ":6}{"Identidad":24}|{" ":3}{"Empresa":13}|{" ":6}{"Color de ojos":19}| {"Fuerza":7}| {"Inteligencia":12}|{"Altura":7}|{"peso":8}|{"Genero":7} |')
        print(patron*largo)
        for i in (lista_personajes):
            altura = float(i["altura"])
            peso =float(i["peso"])
            mensaje1=f'| {i["nombre"]:19}| {i["identidad"]:30}| {i["empresa"]:15}| {i["color_ojos"]:24}| {i["fuerza"]:7}| {i["inteligencia"]:12}| {altura:6}| {peso:7}| {i["genero"]:7}|'
            print(mensaje1)
            print(patron*largo)
##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif respuesta =="2":
            el_mas_fuerte = None
            datos = []

            for i in (lista_personajes):
                if el_mas_fuerte == None or int(el_mas_fuerte) < int(i["fuerza"]):
                    el_mas_fuerte = (i["fuerza"])

            for i in(lista_personajes):
                if el_mas_fuerte == i["fuerza"]:
                    datos.append(i)

            print(("-"*29))
            print(f'| {"identidad":13}|{"":3}{"peso:":8} |')
            print(("-"*29))
            for i in datos:
                print(f'| {i["identidad"]:10} | {float(i["peso"]):10} |')
            print(("-"*29))

##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#3C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo(MÍNIMO)
    elif respuesta =="3":
        el_mas_bajo = None
        datos = []
        
        for i in (lista_personajes):
            if el_mas_bajo == None or float(el_mas_bajo) > float(i["altura"]):
                el_mas_bajo = (i["altura"])

        for i in(lista_personajes):
            if el_mas_bajo == i["altura"]:
                datos.append(i)
        
        print(("-"*51))
        print(f'| {"nombre":13}{" ":6}{"Identidad":29}|')
        print(("-"*51))
        for i in datos:
            print(f'| {i["nombre"]:10} | {i["identidad"]:30}|')
        print(("-"*51))

##////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif respuesta =="4":
        contadorM = 0
        peso_superheroe_masculios = 0
        for i in (lista_personajes):
            match  i["genero"]:
                case "M":
                    contadorM += 1
                    peso_superheroe_masculios += float(i["peso"])

        peso_promedio = float(peso_superheroe_masculios / contadorM)
        mensaje4  =  "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        mensaje4 += f"El peso promedio de los super heroes masculinos es de {peso_promedio}\n"
        mensaje4 +=  "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        print(mensaje4)

##////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif respuesta =="5":
                
        fuerza_femenina_total = 0
        contadorF = 0
        fuerza_femenina_promedio = 0
        datos = []
        for i in (lista_personajes):
            match  i["genero"]:
                case "F":
                    fuerza_femenina_total += int(i["fuerza"]) 
                    contadorF += 1

        fuerza_femenina_promedio= float(fuerza_femenina_total/contadorF)
        
        for i in (lista_personajes):
            if int(fuerza_femenina_promedio) < int(i["fuerza"]):
                peso = float(i["peso"])
                nombre = i["nombre"]
                pesos = peso
                datos.append(f"| {nombre:19} |  {pesos:8}|")
        mensaje_5  = "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        mensaje_5 += "+ nombre y peso de los super heroes que superen el promedio de fuerza femenina +\n"
        mensaje_5 += "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        print(mensaje_5)
        print(34*"-")
        print(f'|{" ":4}{"Nombre":16} |{" ":2}{"Peso":8}|')
        print(34*"-")
        for item in datos:
                print(item) 
        print(34*"-")
        
##////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif respuesta == "6":
        bandera = False
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    else :
        print("#####################################(´。＿。｀)#######")        
        print("############ OPCION INCORRECTA #######################")       
        print("######### INGRESE OPCION VALIDA  #####################")
        print("######################################################")