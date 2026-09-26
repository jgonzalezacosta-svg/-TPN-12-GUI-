import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

opciones = ["Kilometros", "Metros"]

ventana = tk.Tk()

ventana.title("Calculadora - EJ14")

ventana.geometry("400x150")


texto = tk.Label(
    ventana,
    text="Valor:",
    font=("Algerian",15),
    fg="black",
    bg="aliceblue"
)

texto.place(x=40, y=1)


entrada = tk.Entry(
    ventana,
    font=("Algerian",15)
)

entrada.place(x=120, y=5)


opcion1 = ttk.Combobox(
    ventana,
    values=opciones
)

opcion1.place(x=40, y=50)


opcion2 = ttk.Combobox(
    ventana,
    values=opciones
)

opcion2.place(x=200, y=50)


def Convertir():

    numero = float(entrada.get())

    if opcion1.get() == "Metros" and opcion2.get() == "Kilometros":
        resultado = numero / 1000

    elif opcion1.get() == "Kilometros" and opcion2.get() == "Metros":
        resultado = numero * 1000

    else:
        resultado = numero

    messagebox.showinfo("Resultado", str(resultado))


boton = tk.Button(
    ventana,
    text="Convertir",
    width=8,
    height=2,
    command=Convertir
)

boton.place(x=160, y=80)


ventana.mainloop()