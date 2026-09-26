import tkinter as tk

ventana = tk.Tk()

ventana.title("Calculadora - EJ13")
ventana.geometry("300x400")

entrada = tk.Entry(ventana)
entrada.grid(row=0, column=0, columnspan=4, pady=20)

botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]


def mostrar(boton):
    if boton == "C":
        entrada.delete(0, tk.END)

    elif boton == "=":
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)

    else:
        entrada.insert(tk.END, boton)


fila = 1
columna = 0

for boton in botones:

    tk.Button(
        ventana,
        text=boton,
        width=5,
        height=2,
        command=lambda b=boton: mostrar(b)
    ).grid(row=fila, column=columna)

    columna = columna + 1

    if columna == 4:
        columna = 0
        fila = fila + 1


ventana.mainloop()