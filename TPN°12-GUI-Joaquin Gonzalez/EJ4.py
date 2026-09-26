from tkinter import *
import tkinter as tk

# Creamos la ventana
ventana = Tk()

# Ponemos un título en la ventana
ventana.title("Ventana de prueba-EJ3")

# Cambiamos el tamaño de la ventana
ventana.geometry("500x300")


# Creamos un texto
texto = tk.Text(
    ventana,
    font=("Algerian", 15),
    width=15,
    height=1
)
texto.place(x=160, y=50)


# Creamos la acción del botón
def mostrar_mensaje():
    print(texto.get("1.0", "end"))


# Creamos un botón
boton = tk.Button(
    ventana,
    text="Mostrar mensaje en la consola",
    command=mostrar_mensaje
)
boton.pack()


ventana.mainloop()
