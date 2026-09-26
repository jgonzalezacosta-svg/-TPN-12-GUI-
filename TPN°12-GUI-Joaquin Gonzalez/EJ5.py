from tkinter import *
import tkinter as tk
from tkinter import colorchooser

# Creamos la ventana
ventana = Tk()

# Ponemos un título en la ventana
ventana.title("Ventana de prueba-EJ5")

# Cambiamos el tamaño de la ventana
ventana.geometry("500x300")

# Creamos la acción del botón
def elegir_color():
    # Abre el selector de color
    # Devuelve una tupla: ((rgb), "#hexadecimal")
    resultado = colorchooser.askcolor(title="Elige un color")
    
    # El segundo elemento de la tupla (índice 1) es el código hexadecimal
    color_hex = resultado[1]
    
    # Si el usuario selecciona un color y no cancela, cambia el fondo
    if color_hex:
        ventana.configure(bg=color_hex)

# Creamos un botón
boton = tk.Button(
    ventana,
    text="Seleccionar un color",
    command=elegir_color
)
boton.pack()



ventana.mainloop()
