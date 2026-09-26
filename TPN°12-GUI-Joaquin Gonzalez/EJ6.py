import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
# Ponemos un título en la ventana
ventana.title("Ventana de prueba-EJ6")
ventana.geometry("400x300")

opciones = ["hola, quiero estar en la consola", "puedo ser un elemento seleccionado?", "opcion 3", "opcion 4"]

lista = ttk.Combobox(
    ventana, 
    values=opciones,
    height=60,
    width=40
    )
lista.pack(pady=10)

def mostrar():
    if lista.get() == "puedo ser un elemento seleccionado?":
        print(lista.get())
        print("Gracias :)")
    else:
        print(lista.get())

boton = tk.Button(
    ventana, 
    text="ver elementos", 
    command=mostrar)
boton.pack()

ventana.mainloop()
