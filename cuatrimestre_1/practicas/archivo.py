


# import sqlite3

# conexion = sqlite3.connect("nombre de la base de datos.db")

# conexion.close()

# import sqlite3

# with sqlite3.connect() as conexion:

#     try: 
#         sentencia = """
                    

#                     """

#         conexion.execute(sentencia)




# def divide(x, y):
#     try:
#         resultado = x / y
#     except ZeroDivisionError:
#         print("No es posible dividir por cero!")
#     else:
#         print("El resultado es", resultado)

# divide(4,5)





# def numeros_iguales(numero_1,numero_2):
#     if numero_1 == numero_2:
#         print("entro aca")

#     assert 1 == 2, "El assert falló"
    
    

# numeros_iguales(1,2)



# def leer_entero(intentos):
#     retorno = None
#     for i in range(intentos):
#         valor = input("Ingrese un número entero: ")
#         try:
#             valor = int(valor)
#             retorno = valor
#             break
#         except ValueError:
#             print("Error se debe ingresar un número entero")
#     return retorno