import tkinter as tk
import random


ventana = tk.Tk()

ventana.title("Piedra, Papel o Tijera - EJ21")

ventana.geometry("400x200")


opciones = ["Piedra", "Papel", "Tijera"]


def jugar(eleccion):

    computadora = random.choice(opciones)

    if eleccion == computadora:
        resultado = "Empate"

    elif (eleccion == "Piedra" and computadora == "Tijera") or \
         (eleccion == "Papel" and computadora == "Piedra") or \
         (eleccion == "Tijera" and computadora == "Papel"):
        resultado = "Ganaste"

    else:
        resultado = "Perdiste"

    computadora_label.config(text="la computadora eligió: " + computadora)
    resultado_label.config(text="resutlado: " + resultado)


# Texto
titulo = tk.Label(
    ventana,
    text="Elije una opcion:",
    font=("Arial", 16)
)

titulo.pack()


# Botones horizontales
boton1 = tk.Button(
    ventana,
    text="Piedra",
    command=lambda: jugar("Piedra")
)

boton1.place(x=50, y=50)


boton2 = tk.Button(
    ventana,
    text="Papel",
    command=lambda: jugar("Papel")
)

boton2.place(x=165, y=50)


boton3 = tk.Button(
    ventana,
    text="Tijera",
    command=lambda: jugar("Tijera")
)

boton3.place(x=275, y=50)


# Resultados
computadora_label = tk.Label(
    ventana,
    text="La computadora eligió:"
)

computadora_label.place(x=100, y=100)


resultado_label = tk.Label(
    ventana,
    text="Resultado:"
)

resultado_label.place(x=150, y=130)


ventana.mainloop()