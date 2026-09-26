import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
# Ponemos un título en la ventana
ventana.title("Ventana de prueba-EJ7")
ventana.geometry("400x300")

progress = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=10)
progress["value"] = 0

def mostrar():
    progress["value"] = progress["value"] + 10
    

boton = tk.Button(
    ventana, 
    text="Aumentar valor de la barra de progreso", 
    command=mostrar)
boton.pack()

ventana.mainloop()
