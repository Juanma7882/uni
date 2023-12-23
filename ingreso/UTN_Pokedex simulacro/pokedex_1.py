
import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import os
#! No tocar
# command = 'py' if os.name in ['ce', 'nt', 'dos'] else 'python3'
# os.system(f'{command} -m pip install -r requirements.txt')
#! No tocar
import customtkinter

'''
#? El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con 
#? algunos pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)

B) Al presionar el boton "Mostrar Pokedex" se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar el informe del punto C.

ACLARACION:
Del punto C SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C)
    #! 0) - Cantidad de pokemones de tipo Fuego
    #! 1) - Cantidad de pokemones de tipo Electrico
    #! 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    #! 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    #! 4) - Cantidad de pokemones, con mas de 100 de poder.
    #! 5) - Cantidad de pokemones, con menos de 100 de poder
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea 
    #! 8) - el promedio de poder de todos los ingresados
    #! 9) - el promedio de poder de todos los pokemones de Electrico
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)
        

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Pokedex", command=self.btn_mostrar_pokedex_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Cargar aca los pokemones
        self.lista_nombre_pokemones = []
        self.lista_poder_pokemones = []
        self.lista_tipo_pokemones = []


    def btn_mostrar_pokedex_on_click(self):
        pokemon = len(self.lista_nombre_pokemones)
        menos_poder = None
        Agua = 0
        Tierra =0
        Psiquico=0
        Fuego =0
        Electrico =0
        mayor_poder = None
        
            #3
        for i in range(pokemon):
            if menos_poder == None or self.lista_poder_pokemones[i] < menos_poder:
                menos_poder = self.lista_nombre_pokemones[i]
                menos_poder = self.lista_poder_pokemones[i]
                menos_poder = self.lista_tipo_pokemones[i]
            print(f"{menos_poder}")

            if mayor_poder == None or self.lista_nombre_pokemones[i] > mayor_poder:
                mayor_poder = self.lista_nombre_pokemones[i]
                mayor_poder = self.lista_poder_pokemones[i]
                mayor_poder = self.lista_tipo_pokemones[i]
                print(f"{mayor_poder}")

            
        match self.lista_tipo_pokemones[i]:
            case "Agua":
                Agua +=1
            case "Tierra":
                Tierra +=1
            case "Psiquico":
                Psiquico +=1
            case "Fuego":
                Fuego +=1
            case _:
                Electrico +=1
        
        if Agua > Tierra > Psiquico > Fuego > Electrico:
            mensaje = "demasiada awa"
        elif Tierra > Psiquico > Fuego > Electrico:
            mensaje= "deamasiado barro"
        elif  Psiquico > Fuego > Electrico:
            mensaje = "demasiado siquici"
        elif  Fuego > Electrico:
            mensaje = "mucho calor"
        else :
            mensaje = "chispas"
            print(f"{mensaje}")


        pass

    def btn_cargar_pokedex_on_click(self):
        for i in range(10):
            # nombre = prompt(title="utn",prompt="nombre del pokemon")
            # while nombre == None or not nombre.isalpha():
            #     nombre = prompt(title="utn",prompt="nombre del pokemon nuevamente")
            # self.lista_nombre_pokemones.append(nombre)

            # tipo = prompt(title="utn",prompt="ingrese tipo de pokemon")
            # while tipo != "Agua" and tipo != "Tierra" and tipo != "Psiquico" and tipo != "Fuego" and tipo != "Electrico":
            #     tipo = prompt(title="utn",prompt="ingrese tipo de pokemon nuevamente")
            # self.lista_nombre_pokemones.append(tipo)

            poder =prompt(title="utn",prompt="ingrese el poder del pokemon")
            while poder == int(poder.isdigit()) or int(poder) <50 or int(poder) >200 : 
                poder =prompt(title="utn",prompt="ingrese el poder del pokemon nuveamente")
            self.lista_poder_pokemones.append(poder)
        pass

    
if __name__ == "__main__":
    app = App()
    app.mainloop()