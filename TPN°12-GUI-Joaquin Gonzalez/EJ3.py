from tkinter import *
import tkinter as tk

# Creamos la ventana
ventana = Tk()

# Ponemos un título en la ventana
ventana.title("Ventana de prueba-EJ3")

# Cambiamos el tamaño de la ventana
ventana.geometry("300x30")

# Creamos la acción del botón
def mostrar_mensaje():
    print("Wow, se mostró un texto en la consola")

# Creamos un botón
boton = tk.Button(
    ventana,
    text="Mostrar un mensaje en la consola...",
    command=mostrar_mensaje
)
boton.pack()

ventana.mainloop()
