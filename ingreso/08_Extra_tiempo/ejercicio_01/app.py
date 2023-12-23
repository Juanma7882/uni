import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from datetime import time
import customtkinter


'''
Enunciado:
Al presionar el botón INICIAR se debe mostrar un mensaje de bienvenida "Bienvenidos a la UTN FRA" cada 3 segundos. 

'''

# class App(customtkinter.CTk):
    
#     def __init__(self):
#         super().__init__()

#         # configure window
#         self.title("UTN Fra")

#         self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
#         self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

#     def btn_mostrar_on_click(self):
#         pass
        

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
import time

# while True:
#     for i in range(1, 20):  # Imprimir hasta 5 veces
#         print("#" * i)
#         print("\n")
#         print("\n")
#         time.sleep(1)  # Pausa de 1 segundo
# import time

# for i in range(1, 21):  # Itera desde 1 hasta 20
#     # Calcula el porcentaje de carga
#     carga = i * 5  # 5% por iteración
    
#     # Crea una cadena de "#" según el porcentaje de carga
#     barra_de_carga = "#" * i
    
#     # Muestra el mensaje
#     mensaje = f"{barra_de_carga}\n"
#     mensaje += f"Carga: {carga}% "

#     print(mensaje)
#     print("\n")
#     print("\n")
#     time.sleep(1)  # Pausa de 1 segundo


import time

for i in range(1, 21):  # Itera desde 1 hasta 20
    # Calcula el porcentaje de carga
    carga = i * 5  # 5% por iteración
    
    # Crea una cadena de "#" según el porcentaje de carga
    barra_de_carga = "#" * i
    
    # Muestra el mensaje
    mensaje = f"{barra_de_carga}\n"
    mensaje += f"Carga: {carga}% "

    print(mensaje)
    print("\n")
    print("\n")
    print("\n")
    
    

    # Ajusta el tiempo de pausa en función de la carga
    if carga >= 80:
        time.sleep(3)  # Pausa de 2 segundos cuando la carga es 80%
    elif carga == 95:
        time.sleep(5)  # Pausa de 1 segundo cuando la carga es 95%
    else:
        time.sleep(2)  # Pausa de 1 segundo en otros casos
print("iniciando sistema")