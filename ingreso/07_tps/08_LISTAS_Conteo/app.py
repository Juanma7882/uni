import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        ingrese_numero = prompt(title="",prompt="ingrese numero")
        







        # numeros = None
        # minimo = None
        # maximo = None
        # positivos = None     
        # contadorpositivos = 0
        # negativos = None
        # contador_negativo = 0
        # contador_ceros = 0
        # while True:
        #     numeros_ingresados =prompt(title="",prompt="ingresar numeros")
        #     if numeros_ingresados == None:
        #         break
        #     numeros_ingresados = int(numeros_ingresados)
        #     numeros += numeros_ingresados

        #     if numeros_ingresados == None or numeros_ingresados > maximo:
        #         maximo= numeros_ingresados
            
        #     if numeros_ingresados == None or numeros_ingresados < minimo:
        #         minimo =  numeros_ingresados
            
        #     if numeros_ingresados >0:
        #         positivos += numeros_ingresados
        #         contadorpositivos +=1
        #     elif numeros_ingresados <0:
        #         negativos += numeros_ingresados
        #         contador_negativo +=1
        #     else:
        #         contador_ceros +=1
        
        # promedio_negatito = negativos/contador_negativo
        # mensaje =  f"suma acumulada de los negativos {negativos}\n"
        # mensaje += f"suma acumulada de los positivos{positivos}\n"
        # mensaje += f"Cantidad de números positivos ingresados{contadorpositivos}\n"
        # mensaje += f"Cantidad de números negativos ingresados{contador_negativo}\n"
        # mensaje += f"Cantidad de ceros{contador_ceros}\n"
        # mensaje += f"minimo de los negativos{minimo}\n"
        # mensaje += f"maximo de los positivos{maximo}\n"
        # mensaje += f"promedio de los negativos{promedio_negatito}\n"
        # alert(title="",message=mensaje)
            pass

    def btn_mostrar_estadisticas_on_click(self):
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
