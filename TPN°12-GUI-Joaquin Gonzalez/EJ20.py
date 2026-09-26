import tkinter as tk


ventana = tk.Tk()

ventana.title("Ventana de preuba - EJ20")

ventana.geometry("400x300")


# Entrada
entrada = tk.Entry(
    ventana,
    width=30
)

entrada.place(x=40, y=20)


# Lista
lista = tk.Listbox(
    ventana,
    width=40,
    height=10
)

lista.place(x=40, y=60)


# Añadir tarea
def Añadir():
    tarea = entrada.get()

    lista.insert(tk.END, tarea)

    entrada.delete(0, tk.END)


# Eliminar tarea
def Eliminar():
    seleccion = lista.curselection()

    lista.delete(seleccion)


# Botones
boton1 = tk.Button(
    ventana,
    text="Añadir",
    command=Añadir
)

boton1.place(x=80, y=240)


boton2 = tk.Button(
    ventana,
    text="Eliminar",
    command=Eliminar
)

boton2.place(x=220, y=240)


ventana.mainloop()