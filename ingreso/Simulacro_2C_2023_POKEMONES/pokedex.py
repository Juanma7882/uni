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

from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import warnings

'''
#!################ INTRODUCCION #################
# Nos encargan el desarrollo de una aplicación que le permita a sus usuarios inscribirse a 
    un listado de viajeros para un nuevo transbordador de SpaceX:
'''
NOMBRE = 'juan manuel fernandez' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
A) Para ello deberás programar el botón 'Cargar Viajeros' para poder cargar los siguientes datos de 5 personas:
    * Nombre
    * Altura (entre 60 cm y 200 cm)
    * Peso (entre 40 kilos y 250 kilos)
    * Edad (entre 1 y 100 ) 

B) Al presionar el botón "Mostrar Datos Crudo" se deberán listar todos los datos de los usuarios y 
    su posición en la lista (por terminal) 

#!################ ACLARACION IMPORTANTE #################
Del punto C solo deberá realizar 2 informes. Para determinar que informe hacer, 
    tenga en cuenta lo siguiente:
    
    Informe 1- Tome el último número de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)
    Informe 2- el promedio de altura entre todos los usuarios ingresados que sean mayores de 18 años

Realizar los informes correspondientes a los números obtenidos. 
    EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) 
        A- El nombre de la persona con el menor peso ingresado
        B- La cantidad de personas de más de 50 años
    #! 1) 
        A- El nombre de la persona con el mayor peso ingresado
        B- La cantidad de personas de menos de 50 años
    #! 2)
        A- El nombre de la persona con la mayor altura ingresada
        B- La cantidad de personas de más de 80 kilos
    #! 3)
        A- El nombre de la persona con la menor altura ingresada
        B- La cantidad de personas de menos de 100 kilos
    #! 4) 
        A- El nombre de la persona con la mayor edad ingresada
        B- La cantidad de personas de más de 100 cm de altura
    #! 5) 
        A- El nombre de la persona con la menor edad ingresada
        B- La cantidad de personas de menos de 170 cm de altura 
    #! 6) 
        A- El nombre de las personas que NO superen la edad promedio
        B- La cantidad de personas de menos de 160 cm de altura
    #! 7) 
        A- El nombre de las personas que NO superen la altura promedio
        B- La cantidad de personas de menos de 80 kilos
    #! 8)
        A- El nombre de las personas que NO superen el peso promedio
        B- La cantidad de personas de más  de 50 kilos
    #! 9) 
        A- El nombre de las personas que SI superen el peso promedio
        B- La cantidad de personas de menos de 18 años
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - ◄TravelCode Agency► coded by {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"◄TravelCode Agency► coded by {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Viajeros", command=self.btn_cargar_viajeros_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Datos Crudo", command=self.btn_mostrar_datos_crudo_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para el boton mostrar
        # Cargar aca los pokemones
        self.lista_nombres = [
            "Pepe", "Moni", "Paola", "Fatiga", "Dardo",
            "Maria", "Añanga", "Goku", "Vegeta", "Roshi"
        ]
        self.lista_alturas_cm = [
            174, 165, 155, 60, 180, 159, 60, 175, 170, 150
        ]
        self.lista_pesos = [
            80, 70, 65, 41, 90, 66, 150, 75, 70, 60
        ]
        
        self.lista_edades = [
            55, 46, 18, 12, 47, 42, 99, 35, 37, 90
        ]


    def btn_cargar_viajeros_on_click(self):
        for i in range(1):
            nombre = prompt(title="utn",prompt="nombre")
            while nombre == None or not nombre.isalpha():
                nombre = prompt(title="utn",prompt="nombre")
            self.lista_nombres.append(nombre)
#  A- El nombre de la persona con la menor altura ingresada
#         B- La cantidad de personas de menos de 100 kilos
            altura = None
            while altura == None or not altura.isdigit() or int(altura)<=60 or int(altura) >=200:
                altura = prompt(title="utn",prompt="altura en cm")
            altura = int(altura)
            self.lista_alturas_cm.append(altura)

            peso = prompt(title="utn",prompt="peso")
            while peso == None or not peso.isdigit() or int(peso)<=40 or int(peso) >=250:
                peso = prompt(title="utn",prompt="peso")
            peso = int(peso)
            self.lista_pesos.append(peso)

            edad = prompt(title="utn",prompt="edad")
            while edad == None or not edad.isdigit() or int(edad)<0 and int(edad) >=100:
                edad = prompt(title="utn",prompt="edad")
            edad = int(edad)
            self.lista_alturas_cm.append(edad)

        pass
        

    def btn_mostrar_informe_1_on_click(self):
        #! 3)
        menor_altura = len(self.lista_alturas_cm)
        mas_bajo = None
        contador = 0
        for i in range(menor_altura):
            if mas_bajo == None or self.lista_alturas_cm[i] < mas_bajo:
                mas_bajo = self.lista_alturas_cm[i]
                nombre_mas_bajo = self.lista_nombres[i]
        print(f"la persona mas baja es {nombre_mas_bajo} ")
        # A- El nombre de la persona con la menor altura ingresada
        # B- La cantidad de personas de menos de 100 kilos
        #menos_100kilos = len(self.lista_pesos)
        
        # #for i in range(menos_100kilos):
        #     if self.lista_pesos[i] < 100:
        #         contador+= 1
        # print(f"la cantidad de perosnas con menos de 100kg son {contador}")
        # pass

    def btn_mostrar_informe_2_on_click(self):
        edad = len(self.lista_edades)
        suma_de_edades = 0
        contador = 0
        for i in range(edad):
            if self.lista_edades[i]>18:
                contador +=1
                suma_de_edades += self.lista_edades[i]
        promedio = suma_de_edades / contador
        print(f"promedio de las personas con mas de 18 años es {promedio}")
        
        pass

    
    def btn_mostrar_datos_crudo_on_click(self):
        nombres = len(self.lista_nombres)
        for i in range(nombres):
            nombres1 = self.lista_nombres[i]
            edad = self.lista_edades[i]
            altura = self.lista_alturas_cm[i]
            peso = self.lista_pesos[i]
            print (f"lugar en la lista {i:10} nombre {nombres1:15} edad {edad:10} altura {altura:14} peso {peso}")
        pass

    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()

