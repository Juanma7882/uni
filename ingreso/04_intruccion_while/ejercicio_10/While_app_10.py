import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
while 10
Nombre: Juan Manuel
Fernandez: Fernandez
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivos = 0
        contador_positivo = 0
        suma_negativos = 0
        contador_negativo = 0
        contador_0 = 0
        while True:
            numeros_ingresados = prompt(title="utn",prompt="ingrese numeros")
            if numeros_ingresados == None:
                break
            numeros_ingresados=float(numeros_ingresados)
            if numeros_ingresados >0:
                suma_positivos += numeros_ingresados
                contador_positivo += 1
            elif numeros_ingresados <0:
                suma_negativos += numeros_ingresados
                contador_negativo +=1
            else :
                contador_0 +=1
        
        diferencia = abs(suma_positivos + suma_negativos)
        mensaje =  f" positivos ingresados {suma_positivos}\n "
        mensaje += f" contador de positivos ingresados {contador_positivo}\n "
        mensaje += f" contador de negativos ingresados {contador_negativo}\n "
        mensaje += f" contador de cero ingresados {contador_0}\n "
        mensaje += f" diferencia de positivos y negativos ingresados en absoluto {diferencia}\n "
        alert(title="utn",message=mensaje)
        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
