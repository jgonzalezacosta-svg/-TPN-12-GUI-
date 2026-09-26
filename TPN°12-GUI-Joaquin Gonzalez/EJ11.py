import tkinter as tk

ventana = tk.Tk()

ventana.title("Ventana de prueba-EJ11")
ventana.geometry("400x300")


Lienzo = tk.Canvas(
    ventana,
    width=200,
    height=200,
)
Lienzo.create_rectangle(50, 100, 200, 200)
Lienzo.pack()

ventana.mainloop()