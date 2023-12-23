# # Copyright (C) 2023 <UTN FRA>
# # 
# # This program is free software: you can redistribute it and/or modify
# # it under the terms of the GNU General Public License as published by
# # the Free Software Foundation, either version 3 of the License, or
# # (at your option) any later version.
# # 
# # This program is distributed in the hope that it will be useful,
# # but WITHOUT ANY WARRANTY; without even the implied warranty of
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# # GNU General Public License for more details.
# # 
# # You should have received a copy of the GNU General Public License
# # along with this program.  If not, see <http://www.gnu.org/licenses/>.

# import tkinter as tk
# from tkinter.messagebox import showinfo as alert
# from tkinter.messagebox import askyesno as question
# from tkinter.simpledialog import askstring as prompt
# import os
# #! No tocar
# command = 'py' if os.name in ['ce', 'nt', 'dos'] else 'python3'
# os.system(f'{command} -m pip install -r requirements.txt')
# #! No tocar
# import customtkinter

# '''
# #? El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con 
# #? algunos pokemones de prueba.

# Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
# Los datos que deberas pedir para los pokemones son:
#     * El nombre del pokemon
#     * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
#     * La cantidad de poder (validar que sea mayor a 50 y menor a 200)

# B) Al presionar el boton "Mostrar Pokedex" se deberan listar los pokemones y su posicion en la lista (por terminal) 
# y mostrar el informe del punto C.

# ACLARACION:
# Del punto C SOLO debera realizar DOS informes.
# Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
#     1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

#     2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
#         Realiza el informe correspondiente al numero obtenido.
    
# EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
# C)
#     #! 0) - Cantidad de pokemones de tipo Fuego
#     #! 1) - Cantidad de pokemones de tipo Electrico
#     #! 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
#     #! 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
#     #! 4) - Cantidad de pokemones, con mas de 100 de poder.
#     #! 5) - Cantidad de pokemones, con menos de 100 de poder
#     #! 6) - tipo de los pokemones del tipo que mas pokemones posea 
#     #! 7) - tipo de los pokemones del tipo que menos pokemones posea 
#     #! 8) - el promedio de poder de todos los ingresados
#     #! 9) - el promedio de poder de todos los pokemones de Electrico
# '''








# class App(customtkinter.CTk):
    
#     def __init__(self):
#         super().__init__()
        
#         self.title("UTN FRA - Pokedex")
#         self.minsize(320, 250)

#         self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", font=("Arial", 20, "bold"))
#         self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
#         self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
#         self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
#         self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

#         self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
#         self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

#         self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Pokedex", command=self.btn_mostrar_pokedex_on_click)
#         self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

#         # Cargar aca los pokemones
#         self.lista_nombre_pokemones = []
#         self.lista_poder_pokemones = []
#         self.lista_tipo_pokemones = []


#     def btn_mostrar_pokedex_on_click(self):
#         pokemon = len(self.lista_nombre_pokemones)
#         menos_poder = None
#         Agua = 0
#         Tierra =0
#         Psiquico=0
#         Fuego =0
#         Electrico =0
#         mayor_poder = None
        
#             #3
#         for i in range(pokemon):
#             if menos_poder == None or self.lista_poder_pokemones[i] < menos_poder:
#                 menos_poder = self.lista_nombre_pokemones[i]
#                 menos_poder = self.lista_poder_pokemones[i]
#                 menos_poder = self.lista_tipo_pokemones[i]
#             print(f"{menos_poder}")

#             if mayor_poder == None or self.lista_nombre_pokemones[i] > mayor_poder:
#                 mayor_poder = self.lista_nombre_pokemones[i]
#                 mayor_poder = self.lista_poder_pokemones[i]
#                 mayor_poder = self.lista_tipo_pokemones[i]
#                 print(f"{mayor_poder}")

            
#         match self.lista_tipo_pokemones[i]:
#             case "Agua":
#                 Agua +=1
#             case "Tierra":
#                 Tierra +=1
#             case "Psiquico":
#                 Psiquico +=1
#             case "Fuego":
#                 Fuego +=1
#             case _:
#                 Electrico +=1
        
#         if Agua > Tierra > Psiquico > Fuego > Electrico:
#             mensaje = "demasiada awa"
#         elif Tierra > Psiquico > Fuego > Electrico:
#             mensaje= "deamasiado barro"
#         elif  Psiquico > Fuego > Electrico:
#             mensaje = "demasiado siquici"
#         elif  Fuego > Electrico:
#             mensaje = "mucho calor"
#         else :
#             mensaje = "chispas"
#             print(f"{mensaje}")


#         pass

#     def btn_cargar_pokedex_on_click(self):
#         for i in range(10):
#             nombre = prompt(title="utn",prompt="nombre del pokemon")
#             while nombre == None or nombre == "" or nombre.isdigit():
#                 nombre = prompt(title="utn",prompt="nombre del pokemon nuevamente")
#             self.lista_nombre_pokemones.append(nombre)

#             tipo = prompt(title="utn",prompt="ingrese tipo de pokemon")
#             while tipo != "Agua" and tipo != "Tierra" and tipo != "Psiquico" and tipo != "Fuego" and tipo != "Electrico":
#                 tipo = prompt(title="utn",prompt="ingrese tipo de pokemon nuevamente")
#             self.lista_nombre_pokemones.append(tipo)

#             poder =prompt(title="utn",prompt="ingrese el poder del pokemon")
#             while poder == int(poder) <50 or poder >200 or poder == None: 
#                 poder =prompt(title="utn",prompt="ingrese el poder del pokemon nuveamente")
#             self.lista_poder_pokemones.append(poder)
#         pass

    
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()





















# # Copyright (C) 2023 <UTN FRA>
# # 
# # This program is free software: you can redistribute it and/or modify
# # it under the terms of the GNU General Public License as published by
# # the Free Software Foundation, either version 3 of the License, or
# # (at your option) any later version.
# # 
# # This program is distributed in the hope that it will be useful,
# # but WITHOUT ANY WARRANTY; without even the implied warranty of
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# # GNU General Public License for more details.
# # 
# # You should have received a copy of the GNU General Public License
# # along with this program.  If not, see <http://www.gnu.org/licenses/>.

# import tkinter as tk
# from tkinter.messagebox import showinfo as alert
# from tkinter.messagebox import askyesno as question
# from tkinter.simpledialog import askstring as prompt
# import customtkinter


# '''
# ################# INTRODUCCION #################
# #? El profesor OAK de pueblo paleta quiere que construyas un segundo modelo prototipico 
# #? de pokedex con 10 pokemones de prueba.
# '''
# NOMBRE = 'fernandez juan' # Completa tu nombre completo solo en esa variable
# '''
# #?################ ENUNCIADO #################
# Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
# Los datos que deberas pedir para los pokemones son:
#     * El nombre del pokemon.
#     * El tipo de color (azul , amarillo, blanco , otro).
#     * La altura del pokemon en centimetros (validar que sea mayor a 10 y menor a 200).
    
# B)  Al presionar el boton "Mostrar Pokedex" se deberan listar los pokemones y su posicion en la 
#     lista (por terminal), adicionalmente mostrar el informe del punto C.

# #!################ ACLARACION IMPORTANTE #################
# Del punto C SOLO debera realizar DOS informes.
# Para determinar que informe hacer, tenga en cuenta lo siguiente:

#     1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
#     2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
#         Realiza el informe correspondiente al numero obtenido.

# EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
# C)
#     #! 0) - Cantidad de pokemones de color amarillo.
#     #! 1) - Cantidad de pokemones de color blanco.
#     #! 2) - Nombre, color y altura del pokemon mas alto.
#     #! 3) - Nombre, color y altura del pokemon mas bajo.
#     #! 4) - Cantidad de pokemones con mas de 100 cm de altura.
#     #! 5) - Cantidad de pokemones con menos de 100 cm de altura.
#     #! 6) - color de los pokemones del color que mas pokemones posea.
#     #! 7) - color de los pokemones del color que menos pokemones posea.
#     #! 8) - el promedio de altura de todos los pokemones ingresados.
#     #! 9) - el promedio de altura de todos los pokemones azules.
# '''
# class App(customtkinter.CTk):
    
#     def __init__(self):
#         super().__init__()
        
#         self.title(f"UTN FRA - Pokedex de {NOMBRE}")
#         self.minsize(320, 250)

#         self.label_title = customtkinter.CTkLabel(master=self, text=f"Pokedex de {NOMBRE}", font=("Arial", 20, "bold"))
#         self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
#         self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
#         self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
#         self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

#         self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
#         self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

#         self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Pokedex", command=self.btn_mostrar_pokedex_on_click)
#         self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

#         # Cargar aca los pokemones
#         self.lista_nombre_pokemones = []
#         self.lista_altura_pokemones = []
#         self.lista_color_pokemones = []


#     def btn_mostrar_pokedex_on_click(self):
#         cantidad_de_pokemones = len(self.lista_altura_pokemones)

#         contador_color_amarillo = 0
#         contador_color_blanco = 0
#         contador_color_azul =0
#         contador_color_otro = 0

#         pokemon_mas_alto = None
#         indice_mas_peque = None
#         contador_mas_100 = 0
#         contador_menos_100 = 0
#         acumulador_de_altura_azul = 0
#         acumulador_de_altura = 0
#         contador_de_pokemones =0 

#         for i in range(cantidad_de_pokemones):
            
#             nombre = self.lista_nombre_pokemones[i]
#             altura = self.lista_altura_pokemones[i]
#             color = self.lista_color_pokemones[i]
#             print (f"{i} {nombre:15} {altura:10} {color:10}")


#             if self.lista_color_pokemones[i] == "amarillo":
#                 contador_color_amarillo +=1
#             if self.lista_color_pokemones[i] == "blanco":
#                 contador_color_blanco += 1
#             # if self.lista_color_pokemones[i] == "azul":
#             #     f=f
#             # if self.lista_color_pokemones[i] == "otro":
#             #     f=f
            
            if pokemon_mas_alto == None or self.lista_altura_pokemones [i] > pokemon_mas_alto:
                pokemon_mas_alto = self.lista_nombre_pokemones[i]
                pokemon_mas_alto = self.lista_color_pokemones[i]
                pokemon_mas_alto = self.lista_altura_pokemones[i]
                print (f"{pokemon_mas_alto}")

            if indice_mas_peque == None or self.lista_altura_pokemones[i] < self.lista_nombre_pokemones[indice_mas_peque]:
                indice_mas_peque = i
            if self.lista_altura_pokemones[i] > 100:
                contador_mas_100 += 1 
            elif self.lista_altura_pokemones[i]<100:
                contador_menos_100 +=1
            
#             match self.lista_color_pokemones[i]:
#                 case "amarillo":
#                     contador_color_amarillo +=1
#                 case "blanco":
#                     contador_color_blanco +=1
#                 case "azul":
#                     contador_color_azul +=1 
#                     acumulador_de_altura_azul += self.lista_altura_pokemones[i]
#                 case _:
#                     contador_color_otro +=1
#             acumulador_de_altura += self.lista_altura_pokemones[i] 
            
#             if contador_color_blanco > contador_color_amarillo and contador_color_blanco> contador_color_azul and contador_color_blanco > contador_color_otro:
#                 mensaje = "hay muchos pokemon blanco"
#             elif contador_color_amarillo>contador_color_azul and contador_color_amarillo > contador_color_otro:
#                 mensaje = "hay muchos pokemon pikachu"
#             elif contador_color_otro > contador_color_azul:
#                 mensaje = "hay colores varios"
#             else :
#                 mensaje="hay muchos pokemon azules"
            
#             if contador_color_blanco < contador_color_amarillo and contador_color_blanco< contador_color_azul and contador_color_blanco < contador_color_otro:
#                 mensaje = "hay pocos pokemon blanco"
#             elif contador_color_amarillo<contador_color_azul and contador_color_amarillo < contador_color_otro:
#                 mensaje = "hay pocos pokemon pikachu"
#             elif contador_color_otro < contador_color_azul:
#                 mensaje = "hay colores varios"
#             else :
#                 mensaje ="hay pocos pokemon azules"

#         if(cantidad_de_pokemones > 0):
#             promedio = acumulador_de_altura / cantidad_de_pokemones
        
#         if(contador_color_azul > 0):
#             promedio_azul = acumulador_de_altura_azul / contador_color_azul




#             pass

#     def btn_cargar_pokedex_on_click(self):
#         for i in range(2):
#             nombre_del_pokemon = prompt(title="",prompt="nombre del pokemon")
#             while nombre_del_pokemon == None or nombre_del_pokemon == "" or nombre_del_pokemon.isdigit() or len(nombre_del_pokemon)<3:
#                 nombre_del_pokemon = prompt(title="",prompt="reingrese nombre del puchamon")
#             self.lista_nombre_pokemones.append(nombre_del_pokemon)

#             color_del_pokemon  = prompt(title="",prompt="color del pokemon")
#             while color_del_pokemon != "azul" and color_del_pokemon != "amarillo" and color_del_pokemon != "blanco" and color_del_pokemon != "otro":
#                 color_del_pokemon = prompt(title="",prompt="ingrese su verdadero color")
#             self.lista_color_pokemones.append(color_del_pokemon)

#             altura_del_pokemon = prompt(title="",prompt="altura del pokemon")
#             while altura_del_pokemon == None or int(altura_del_pokemon) <10 or int(altura_del_pokemon) >200:
#                 altura_del_pokemon = prompt(title="",prompt="ingrese la verdadera altura")
#             altura_del_pokemon = int(altura_del_pokemon)
#             self.lista_altura_pokemones.append(altura_del_pokemon)
        



#         pass









    
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "" # Nombre del alumno

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

B) Al presionar el botón mostrar 
    
    Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal) 

# IMPORTANTE:
Del punto C solo deberá realizar SOLAMENTE 2 informes. 
(PRESUPONER QUE CADA CLIENTE INGRESADO ES UN CLIENTE DISTINTO, NINGUNO SE REPITE, 
no es necesario validar que no haya nombres repetidos)

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 2 - Tome el último número de su DNI Personal (Ej 4) 
        y realice ese informe (Ej, Realizar informe 4)

    Informe 3 - Tome el último número de su DNI Personal (Ej 4), 
        y restarle al número 9 (Ej 9-4 = 5). En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.

    Realizar los informes correspondientes a los números obtenidos. 
        EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)


        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
    
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        self.lista_nombre=["juan", "manuel" , "fernandez","alexander"]
        self.lista_tipo_de_intrumento=["mep", "cedear", "mep","bonos"]
        self.lista_monto_en_pesos= ["10000", "20000", "10000","15000" ]
        self.lista_cantidad_de_ontrumentos = ["3","6","3","50"]

    def btn_mostrar_todos_on_click(self):
        nombres = len(self.lista_nombre)
        for i in range(nombres):
            nombre = self.lista_nombre[i]
            instrumento =self.lista_tipo_de_intrumento[i]
            monto= self.lista_monto_en_pesos[i]
            print (f"lugar en la lista {i:10} nombre {nombre:15} tipo {instrumento:10} {monto:14}")
            
        pass
#3
    def btn_mostrar_informe_1(self):
        contador = 0
        for i in range(len(self.lista_tipo_de_intrumento)):
            if self.lista_tipo_de_intrumento[i] != "cedear":
                contador +=1
        print(f"personas que no inviertieron en cedear {contador}")
        pass
#6
    def btn_mostrar_informe_2(self):
        monto = len(self.lista_monto_en_pesos)
        menos_dinero = None
        lugar_de_la_persona = None
        menos_dinero_pesos = None
        menos_dinero_tipo = None
        for i in range (monto):
            if menos_dinero == None or self.lista_monto_en_pesos [i] > menos_dinero:            
                menos_dinero = self.lista_nombre[i]
                menos_dinero_tipo = self.lista_tipo_de_intrumento[i]     
                menos_dinero_pesos= self.lista_monto_en_pesos[i] 
                lugar_de_la_persona = i
        print (f"posiscion {lugar_de_la_persona} nombre {menos_dinero} tipo de instrumento {menos_dinero_tipo} pesos {menos_dinero_pesos}")
        
###### 2 ######
        # datos = len(self.lista_tipo_de_intrumento)
        # contador = 0
        # for i in range(datos):
        #     if self.lista_tipo_de_intrumento[i] == "mep" and self.lista_cantidad_de_ontrumentos[i] >=50 and self.lista_cantidad_de_ontrumentos[i] <=200:
        #         contador+=1
        # print(f"mep 50 y 100 {contador}")
        pass

    def btn_mostrar_informe_3(self):
        pass 

    def btn_cargar_datos_on_click(self):
        for i in range(3): 
            nombre = prompt(title="",prompt="nombre")
            while nombre == None or nombre == "" or nombre.isdigit():
            # while nombre == none or not nombre.isalpha 
                nombre = prompt(title="",prompt="reingrese su nombre")
            self.lista_nombre.append(nombre)

            tipo_de_intrumento  = prompt(title="",prompt="tipo de intrumento")
            while tipo_de_intrumento != "cedear" and tipo_de_intrumento != "bonos" and tipo_de_intrumento != "mep":
                tipo_de_intrumento = prompt(title="",prompt="ingrese lo que desea operar")
            self.lista_tipo_de_intrumento.append(tipo_de_intrumento)

            monto_en_pesos = prompt(title="",prompt="monto_en_pesos")
            while monto_en_pesos == None or monto_en_pesos.isdigit or int(monto_en_pesos) <10000:
                monto_en_pesos = prompt(title="",prompt="ingrese monto en pesos")
            monto_en_pesos = int(monto_en_pesos)
            self.lista_monto_en_pesos.append(monto_en_pesos)

            cantidad_de_ontrumentos = None
            while cantidad_de_ontrumentos == None or not cantidad_de_ontrumentos.isdigit():# or int(cantidad_de_ontrumentos):<0
                    cantidad_de_ontrumentos = prompt("utn",prompt = "cantidad de instrumentos")
            cantidad_de_ontrumentos = int(cantidad_de_ontrumentos)
            self.lista_cantidad_de_ontrumentos.append(cantidad_de_ontrumentos)

        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
