
# En el parque de diversiones "Aventuras Extremas", un grupo de amigos ha decidido disfrutar
# del día probando las diferentes atracciones y luego se reúnen en un restaurante para compartir
# un delicioso almuerzo. Antes de que llegue la cuenta, deciden crear un programa para calcular
# y dividir los gastos de manera equitativa. Se pide ingresar los siguientes datos hasta que el
# usuario lo desee:
# Para cada amigo:
# - Nombre del amigo,
# - Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
# - Cantidad de platos principales pedidos (debe ser al menos 1).
# - Bebida elegida ("Refresco", "Agua", "Jugo").
# - Cantidad de bebidas pedidas (debe ser al menos 1).
# Se conocen los siguientes precios base:
# El precio unitario de cada plato principal es de $800.
# El precio unitario de cada bebida es de $200.
# Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente:
# A) El total gastado por el grupo (resultante del costo de los platos principales y las
# bebidas), y la propina sugerida para el personal del restaurante (esta corresponde al
# 10% del total gastado).
# B) Promedio del dinero gastado en “Jugo”, sobre el grupo de amigos en general.
# C) Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad).
# Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas]
# D) Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total
# (platos principales + bebidas) con una entrada gratuita para otra atracción del parque
# "Aventuras Extremas".
# E) REALIZAR DOS PUNTO; EL PRIMERO CORRESPONDIENTE AL ÚLTIMO NÚMERO
# DE SU DNI PERSONAL (Ejemplo 4) Y EL SEGUNDO RESTANDO A 9 EL ÚLTIMO
# NÚMERO DE SU DNI (Ejemplo 9 - 4 = 5):

# 0.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos
# principales del tipo "Pizza" y mostrar la lista completa por print.
# 1.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido
# platos principales del tipo "Hamburguesa" y mostrar la lista completa por print.
# 2.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos
# principales del tipo "Ensalada" y mostrar la lista completa por print.
# 3.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan pedido bebidas
# del tipo "Refresco" y mostrar la lista completa por print.
# 4.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan pedido bebidas
# del tipo "Agua" y mostrar la lista completa por print.
# 5.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
# de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
# 6.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
# de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
# 7.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
# de 7 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
# 8.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos
# de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
# 9.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos
# de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.

lista_nombre = ["Juan", "alex", "Pedro", "Laura", "Carlos","Ana", "Luis", "Elena", "Miguel", "Sofía"]
lista_plato_principal_elegido= ["Pizza", "Hamburguesa", "Ensalada", "Pizza","Hamburguesa", "Ensalada", "Pizza", "Hamburguesa", "Ensalada", "Pizza"]
lista_cantidad_de_platos =[20, 20, 3, 2, 2, 4, 3, 1, 1, 3]
lista_bebida_elegida= ["Refresco", "Agua", "Jugo", "Refresco","Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco"]
lista_cantidad_de_bebidas_pedidas= [1, 1, 5, 3, 2, 5, 1, 2, 1, 3]
#17600 precio de toda la comida pedida
#5000 es el precio de toda la bebida, pedida total 22600
precio_de_la_pizza =800
precio_de_la_hambuerguesa =800
precio_de_la_ensalada =800
precio_del_agua =200
precio_del_jugo=200
precio_de_los_refrescos=200

porcentaje_de_propina = 10

total_pizzas_pedidas =0 
total_de_hamburguesas_pedidas = 0
total_de_ensaladas_pedidas = 0

contador_de_pizza = 0
contador_de_hamburguesa = 0
contador_de_ensalada = 0

cantidad_de_aguas = 0
cantidad_de_jugos = 0
cantidada_de_refrescos = 0

contador_de_refrescos = 0
contador_de_Agua = 0
contador_de_Jugos = 0

maximo_comida = None
maximo_bebida = None
bebida_mas_comida_pedida = None
cantidad_de_bebidas_que_pidio = None
persona_que_compro_mas_comida = None
persona_que_compro_mas_bebida = None
comida_mas_bebida = None

personas_que_pidieron_pizza = []
personas_que_pidieron_ensalada = []
personas_que_pidieron_amburguesa = []
personas_que_pidieron_jugo = []
personas_que_pidieron_agua = []
personas_que_pidieron_refrescos = []

lista_personas_que_hiceron_mas_de_10_pedidos = []

# for i in range(10):
#     nombre = input("nombre")
#     while nombre == None or nombre == "" or nombre.isdigit(): 
#         nombre = input("reingrese su nombre")
#     lista_nombre.append(nombre)
#     print(nombre)

#     plato_principal_elegido  =  input("plato principal")
#     while plato_principal_elegido != "pizza" and plato_principal_elegido != "amburguesa" and plato_principal_elegido !="ensalada":
#         plato_principal_elegido = input("plato principal")
#     lista_plato_principal_elegido.append(plato_principal_elegido)
#     print(plato_principal_elegido)

#     cantidad_de_plato = input("cantidad de platos")
#     while cantidad_de_plato == None or int(cantidad_de_plato) <1:
#         cantidad_de_plato = input("cantidad de platos")
#     cantidad_de_plato = int(cantidad_de_plato)
#     lista_cantidad_de_platos.append(cantidad_de_plato)
#     print(cantidad_de_plato)

#     tipo_de_bebida  =  input("tipo de bebida")
#     while tipo_de_bebida != "Refresco" and tipo_de_bebida != "agua" and tipo_de_bebida !="jugo":
#         tipo_de_bebida = input("tipo de bebida")
#     lista_bebida_elegida.append(tipo_de_bebida)
#     print(tipo_de_bebida)

#     bebida = input("cantidad de bebidas")
#     while bebida == None or int(bebida) <1:
#         bebida = input("cantidad de bebidas")
#     bebida = int(bebida)
#     lista_cantidad_de_bebidas_pedidas.append(bebida)
#     print(bebida)

for i in range(len(lista_nombre)):
    # nombre = lista_nombre[i]
    # comida_elegida = lista_plato_principal_elegido [i]
    # cantidad_de_platos_pedidos = lista_cantidad_de_platos [i]
    # bebida_elegida = lista_bebida_elegida[i]
    # cantidad_bebidas_pedidas = lista_cantidad_de_bebidas_pedidas[i]
    # print(f" nombre {nombre} comida elegida {comida_elegida} cantidad de platos {cantidad_de_platos_pedidos} bebida elegida {bebida_elegida} cantidad de bebidas {cantidad_bebidas_pedidas}")

    if lista_bebida_elegida[i] == "Refresco":
        cantidada_de_refrescos += lista_cantidad_de_bebidas_pedidas[i]
        personas_que_pidieron_refrescos.append(lista_nombre[i])
        contador_de_refrescos += 1
    elif lista_bebida_elegida[i] == "Agua":
        cantidad_de_aguas += lista_cantidad_de_bebidas_pedidas[i]
        personas_que_pidieron_agua.append(lista_nombre[i])
        contador_de_Agua += 1
    elif lista_bebida_elegida[i]== "Jugo":
        cantidad_de_jugos += lista_cantidad_de_bebidas_pedidas[i]
        personas_que_pidieron_jugo.append(lista_nombre[i])
        contador_de_Jugos += 1
        
    if  lista_plato_principal_elegido [i] == "Pizza":
        total_pizzas_pedidas += lista_cantidad_de_platos[i]
        personas_que_pidieron_pizza.append(lista_nombre[i])
        contador_de_pizza +=1
    elif  lista_plato_principal_elegido [i] == "Hamburguesa":
        total_de_hamburguesas_pedidas += lista_cantidad_de_platos[i]
        personas_que_pidieron_amburguesa.append(lista_nombre[i])
        contador_de_hamburguesa+=1 
    elif  lista_plato_principal_elegido [i] == "Ensalada":
        total_de_ensaladas_pedidas += lista_cantidad_de_platos[i]
        personas_que_pidieron_ensalada.append(lista_nombre[i])
        contador_de_ensalada+=1
    
#print(f"total de comida {total_pizzas_pedidas} {personas_que_pidieron_pizza}")
    
    if 10 <lista_cantidad_de_bebidas_pedidas[i] + lista_cantidad_de_platos[i]:
        lista_personas_que_hiceron_mas_de_10_pedidos.append(lista_nombre[i])
# print(lista_personas_que_hiceron_mas_de_10_pedidos)

    if maximo_comida == None or lista_cantidad_de_platos[i] > maximo_comida:
        persona_que_compro_mas_comida = lista_nombre[i]
        maximo_comida = lista_cantidad_de_platos[i]
        cantidad_de_bebidas_que_pidio = lista_cantidad_de_bebidas_pedidas[i]
        comida_mas_bebida = maximo_comida + cantidad_de_bebidas_que_pidio 
#print(persona_que_compro_mas_comida , maximo_comida, bebida_mas_comida_pedida)

    if maximo_bebida == None or lista_cantidad_de_bebidas_pedidas[i] > maximo_bebida:
        persona_que_compro_mas_bebida= lista_nombre[i]
        maximo_bebida =  lista_cantidad_de_bebidas_pedidas[i]
        bebida_mas_comida = lista_cantidad_de_bebidas_pedidas[i] + lista_cantidad_de_platos[i]

    if bebida_mas_comida < comida_mas_bebida:
        mensaje_aventura_extrema = f"la persona que pidio mas platos y bebidas es {persona_que_compro_mas_comida}"
    elif comida_mas_bebida < bebida_mas_comida:
        mensaje_aventura_extrema = f"la persona que compro mas bebidas y platos es {persona_que_compro_mas_bebida}"
    else :
        mensaje_aventura_extrema = f"ustedes 2 se ganaron un vije a aventuras extremas {persona_que_compro_mas_comida} y {persona_que_compro_mas_bebida}"
# print(mensaje_aventura_extrema)






precio_total_de_las_pizzas = (precio_de_la_pizza * total_pizzas_pedidas)
precio_total_de_la_ensaladas = (precio_de_la_ensalada * total_de_ensaladas_pedidas)
precio_total_de_la_hambuerguesas = (precio_de_la_hambuerguesa * total_de_hamburguesas_pedidas)
total_de_la_comida = (precio_total_de_las_pizzas + precio_total_de_la_hambuerguesas + precio_total_de_la_ensaladas)

precio_total_de_aguas_pedidas = (precio_del_agua * cantidad_de_aguas)
precio_total_de_jugo_pedidas = (precio_del_jugo * cantidad_de_jugos)
precio_total_de_refrescos_pedidas = (precio_de_los_refrescos * cantidada_de_refrescos)
total_bebidas = (precio_total_de_aguas_pedidas + precio_total_de_jugo_pedidas + precio_total_de_refrescos_pedidas)

precio_de_bebidas_mas_la_comida = (total_de_la_comida + total_bebidas)
total_de_propina= (porcentaje_de_propina * precio_de_bebidas_mas_la_comida / 100)
precio_final = (total_de_propina + precio_de_bebidas_mas_la_comida) 

porcentaje_de_comidas = total_pizzas_pedidas + total_de_hamburguesas_pedidas + total_de_ensaladas_pedidas
porcentaje_ensalada = (total_de_ensaladas_pedidas * 100 / porcentaje_de_comidas )
porcentaje_amburguesa = (total_de_hamburguesas_pedidas *100/ porcentaje_de_comidas )
porcentaje_pizza = (total_pizzas_pedidas * 100 / porcentaje_de_comidas )

mensaje = f"el precio de su comida es de {precio_de_bebidas_mas_la_comida} mas la propina de {total_de_propina} "
mensaje += f"que les deja un precio final a pagar de {precio_final} \n"

mensaje += f"el porcentaje de ensalada pedida es {porcentaje_ensalada:.2f}% \n"
mensaje += f"el porcentaje de amburguesa pedida es {porcentaje_amburguesa:.2f}% \n" 
mensaje += f"el porcentaje de pizza pedida es de {porcentaje_pizza:.2f}%\n"

mensaje +=f"nombre de las personas que pidieron ensalada {personas_que_pidieron_ensalada}\n"
mensaje +=f"nombre de las personas que pidieron amburgurguesa {personas_que_pidieron_amburguesa}\n"
mensaje +=f"nombre de las personas que pidieron pizza {personas_que_pidieron_pizza}\n"
mensaje +=f"nombre de las personas que pidieron jugo {personas_que_pidieron_jugo}\n"
mensaje +=f"nombre de las personas que pidieron agua {personas_que_pidieron_agua}\n"
mensaje +=f"nombre de las personas que pidieron refresco {personas_que_pidieron_refrescos}\n"
mensaje += f"personas que hiceron un pedido de mas de 10 productos {lista_personas_que_hiceron_mas_de_10_pedidos}\n"

print(f"{mensaje} {mensaje_aventura_extrema}")
