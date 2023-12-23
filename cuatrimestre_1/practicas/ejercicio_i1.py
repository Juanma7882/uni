
lista_fabricante = []
lista_productos = []
lista_precios = []
cantidad_de_unidades = []
lista_de_marcas = []
#marca = m1 m2 m3 
#fabricantes f1 f2 f3 
for i in range(5):
    # producto = input("ingrese el elemento que desea llevar")
    # while producto != "jabon" and producto != "barbijo" and producto != "alcohol" :
    #     producto = input("producto no valido reingrese un producto VALIDO")
    # lista_productos.append(producto)

    precio = input("ingrese precio")
    while precio == None or not precio.isdigit() or int(precio) < 100 or int(precio) >300 :
        precio = input("EROR precio no valido")
    precio = int(precio)
    lista_precios.append(precio)
    print(precio)

    marca = input("marca del producto")
    while marca != "m1" and marca != "m2" and marca != "m3":
        marca = input("ERROR ingrese marca valida")
    lista_de_marcas.append(marca)

    fabricante = input("marca del producto")
    while fabricante != "f1" and fabricante != "f2" and fabricante != "f3":
        fabricante = input("ERROR ingrese marca valida")
    lista_fabricante.append(fabricante)

