import tkinter as tk
from datetime import datetime


ventana = tk.Tk()

ventana.title("Hora - EJ19")

ventana.geometry("400x150")


texto = tk.Label(
    ventana,
    font=("Algerian", 30),
    fg="black",
    bg="aliceblue"
)

texto.place(x=100, y=40)


def actualizar_hora():

    ahora = datetime.now()

    hora_actual = ahora.strftime("%H:%M:%S")

    texto.config(text=hora_actual)

    ventana.after(1000, actualizar_hora)


actualizar_hora()


ventana.mainloop()