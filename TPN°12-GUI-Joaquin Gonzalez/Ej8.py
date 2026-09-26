import tkinter as tk

# Creamos la ventana
ventana = tk.Tk()

# Ponemos un título en la ventana
ventana.title("Ventana de prueba-EJ8")
ventana.geometry("400x300")

# Variable que almacenará la opción seleccionada
opcion = tk.StringVar()

# Función que se ejecutará al seleccionar una opción
def mostrar_opcion():
    print(opcion.get())

# Creamos los botones de opción
radio1 = tk.Radiobutton(
    ventana,
    text="Rojo",
    variable=opcion,
    value="Rojo",
    command=mostrar_opcion
)
radio1.pack()

radio2 = tk.Radiobutton(
    ventana,
    text="Verde",
    variable=opcion,
    value="Verde",
    command=mostrar_opcion
)
radio2.pack()

radio3 = tk.Radiobutton(
    ventana,
    text="Azul",
    variable=opcion,
    value="Azul",
    command=mostrar_opcion
)
radio3.pack()

ventana.mainloop()
