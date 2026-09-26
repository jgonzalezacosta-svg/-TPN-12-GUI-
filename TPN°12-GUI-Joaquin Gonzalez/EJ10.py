import tkinter as tk

ventana = tk.Tk()

ventana.title("Ventana de prueba-EJ10")
ventana.geometry("400x300")


barra = tk.Scale(
    ventana,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
)
barra.pack()


def mostrar():
    print("Estado de la barra deslizante:", barra.get())


boton = tk.Button(
    ventana,
    text="Mostrar estado de la barra",
    command=mostrar
)
boton.pack()

ventana.mainloop()