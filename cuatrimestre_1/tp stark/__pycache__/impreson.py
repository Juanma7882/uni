# from stark_2 import *
# from stark_3 import *
# from stark_4 import *



# stark_marvel_app_2()
# stark_marvel_app_3()
# stark_marvel_app_4()


# numeros = 1, 2 , 3, 4,5,6,7,8,9,10,11,12
# print(numeros)
# for i in numeros:
#     if i < 2 and i % 





# def es_primo(numero):
#     if numero <= 1:
#         return False
#     if numero <= 3:
#         return True
#     if numero % 2 == 0 or numero % 3 == 0:
#         #si es divisible por 2 o 3 y el resto da 0 el numero no es primo de esta forma se omiten muchos numeros
#         return False

#     i = 5
#     print(i)
#     while i * i <= numero:
#         print(i)
#         if numero % i == 0 or numero % (i + 2) == 0:
#             print(i)
#             return False
#         i += 6

#     return True

# # Ejemplo de uso

# print(es_primo(7))





# numero = 10


# def numeros_primos(numero):
#     """
#     devuelve un bool si es primo true y si no 
#     false
#     """
#     mensaje = True

#     if numero <= 1:
#         mensaje = False
#     else:
#         for i in range(2 , numero):
#             resto = numero % i
#             if resto == 0:
#                 mensaje = False
#                 break
                
#     return mensaje 

# tipo = (numeros_primos())
# print(tipo)



# def navegar_fichas(lista_a_navegar):
#     """
#     se ingresa la lista de personajes 
#     """
#     total_fichas = len(lista_a_navegar)
#     if total_fichas == 0:
#         print("No hay fichas para mostrar.")
#         return

#     indice_actual = 0
#     while True:
#         print(lista_a_navegar[indice_actual])

#         if total_fichas > 1:
#             opcion = input(f"Selecciona una opción: [1] Anterior [2] Siguiente [S] Salir: ").strip().lower()
#             if opcion == '1':
#                 indice_actual = (indice_actual - 1)
#                 if indice_actual == -1:
#                     indice_actual == 24
#             elif opcion == '2':
#                 indice_actual = (indice_actual + 1) 
#                 if indice_actual == 25:
#                     indice_actual == 0
#             elif opcion == 's':
#                 break
#             else:
#                 print("Opción no válida. Por favor, selecciona una opción válida.")
#         else:
#             opcion = input(f"Selecciona una opción: [S] Salir: ").strip().lower()
#             if opcion == 's':
#                 break


# def navegar_fichas(lista_a_navegar):
#     """
#     se ingresa la lista de personajes 
#     """
#     total_fichas = len(lista_a_navegar)
#     if total_fichas == 0:
#         print("No hay fichas para mostrar.")
#         return

#     indice_actual = 0
#     while True:
#         print(lista_a_navegar[indice_actual])

#         if total_fichas > 1:
#             opcion = input(f"Selecciona una opción: [1] Anterior [2] Siguiente [S] Salir: ").strip().lower()
#             if opcion == '1':
#                 indice_actual = (indice_actual - 1) % total_fichas
#             elif opcion == '2':
#                 indice_actual = (indice_actual + 1) % total_fichas
#             elif opcion == 's':
#                 break
#             else:
#                 print("Opción no válida. Por favor, selecciona una opción válida.")
#         else:
#             opcion = input(f"Selecciona una opción: [S] Salir: ").strip().lower()
#             if opcion == 's':
#                 break







# n = ["10", "2", "2", "4"]
# n = list(set(n))
# print(n)
