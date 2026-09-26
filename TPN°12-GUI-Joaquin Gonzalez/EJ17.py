#importamos tk
import tkinter as tk
from tkinter import messagebox
import random

#generamos un numero aleatorio del 1 al 10
numero = random.randint(1, 10)


#creamos la ventana y le otorgamos un titulo
ventana = tk.Tk()
ventana.title("Ventana de prueba-EJ17")

#definimos el tamaño de la ventana
ventana.geometry("400x110")

def Verificar():
    try:
        numero_user = int(texto1.get())

        if numero_user == numero:
            messagebox.showinfo("Ganaste", "Has acertado el numero correcto")

        elif numero_user > numero:
            messagebox.showerror("Incorrecto", "Pista: el numero es un poco mas chico")

        elif numero_user < numero:
            messagebox.showerror("Incorrecto", "Pista: el numero es un poco mas grande")

    except ValueError:
        messagebox.showwarning("Error", "Escribe un numero, no una letra... wachin")


###
titulo = tk.Label(
    text="Adivina el numero del 1 al 10:)",
    font=("Arial",18),
    fg="black",
    bg="aliceblue"
).place(x=5,y=8)

lb1 = tk.Label(
    text="Cual crees que es el numero?"
).place(x=10,y=50)

texto1 = tk.Entry(
    font=("Algerian",15),
    width=3
)
texto1.place(x=180,y=50)

boton = tk.Button(
    text="Verificar numero",
    command=Verificar
).place(width=110,x=15,y=80)


###
ventana.mainloop()