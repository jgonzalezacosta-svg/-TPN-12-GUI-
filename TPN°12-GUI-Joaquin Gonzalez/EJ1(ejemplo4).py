from tkinter import *
import tkinter as tk
formu=Tk()
ventana = Frame(formu, width=300, height=220)
ventana.pack()#organiza los bloques en bloque por meedio del metodo pack
titulo = tk.Label (text="FORMULARIO DE INICIO", font=("Arial",18), fg="black", bg="aliceblue").place(x=5,y=8)
lb1= tk.Label( text="Nombre", fg="black", bg="ivory").place(x=10,y=50)
texto1= tk.Entry(font=("Algerian",15),width=10).place(x=90,y=50)
lb2= tk.Label( text="Contraseña", fg="black", bg="ivory").place(x=10,y=90)
texto2= tk.Entry(font=("Algerian",15),width=10).place(x=90,y=90)
boton = tk.Button(text="Aceptar").place(width=60,x=15,y=140)
tk.mainloop()