import tkinter as tk

ventana = tk.Tk()

ventana.title("Ventana de prueba-EJ12")

ventana.geometry("700x500")

Lienzo = tk.Canvas(
    ventana,
    width=700,
    height=700,
)

# Rectángulo
Lienzo.create_rectangle(50, 50, 200, 150)

# Círculo
Lienzo.create_oval(250, 50, 400, 200)

# Triángulo
Lienzo.create_polygon(500, 200, 600, 200, 550, 100)

# Imagen
imagen = tk.PhotoImage(file="yodespuesdeprogramar.png")
Lienzo.create_image(350, 450, image=imagen)

Lienzo.pack()

ventana.mainloop()