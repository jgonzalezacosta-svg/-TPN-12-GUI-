import tkinter as tk

ventana = tk.Tk()

ventana.title("Ventana de prueba-EJ9")
ventana.geometry("400x300")

empanada = tk.BooleanVar()
ensalada_de_frutas = tk.BooleanVar()
sanguches_de_miga = tk.BooleanVar()

check = tk.Checkbutton(
    ventana,
    text="Empanada",
    variable=empanada
)
check.pack()

check1 = tk.Checkbutton(
    ventana,
    text="Ensalada de fruta",
    variable=ensalada_de_frutas
)
check1.pack()

check2 = tk.Checkbutton(
    ventana,
    text="Sanguches de miga",
    variable=sanguches_de_miga
)
check2.pack()


def mostrar():
    print("Empanada:", empanada.get())
    print("Ensalada de fruta:", ensalada_de_frutas.get())
    print("Sanguches de miga:", sanguches_de_miga.get())


boton = tk.Button(
    ventana,
    text="Mostrar estado",
    command=mostrar
)
boton.pack()

ventana.mainloop()