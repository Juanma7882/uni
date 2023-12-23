'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador_votos = 0
        contador_nombres = ""
        bandera = True
        while bandera == True:  
            nombre = prompt(title="",prompt="Nombre")
            while nombre == None or nombre.isdigit() or nombre == "":
                nombre = prompt(title="nombre invalido",prompt="ingrese nombre")

            edad = int(prompt(title="",prompt="edad"))
            while edad == None or not edad <25 or edad.isdigit():
                edad = prompt(title="",prompt="edad") 
        
            votos = prompt(title="seleccione",prompt="candidato")
            while votos == None or not votos.isdigit() or votos == "":
                votos = prompt(title="reingrese voto",prompt="seleccione candidato")
        
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
