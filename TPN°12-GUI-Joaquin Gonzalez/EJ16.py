#importamos tk
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

#creamos la ventana y le otorgamos un titulo
ventana = tk.Tk()
ventana.title("Ventana de prueba-EJ16")

#definimos el tamaño de la ventana
ventana.geometry("400x450")
###
### Definición de las columnas
tree = ttk.Treeview(ventana)

# Definición de las columnas
tree["columns"] = ("uno", "#0")
tree.column("#0", width=100, minwidth=100)
tree.column("uno", width=100, minwidth=100)

# Definición de los encabezados
tree.heading("#0", text="Nombre")
tree.heading("uno", text="Telefono")

# Empaquetado y ejecución
tree.place(width=240,x=15,y=200)

###
def Añadir_contacto():
    tree.insert("", "end", text=texto1.get(), values=texto2.get())

###
titulo = tk.Label (text="Agenda de contactos telefonicos", font=("Arial",18), fg="black", bg="aliceblue").place(x=5,y=8)
lb1= tk.Label( text="Nombre:", fg="black", bg="ivory").place(x=10,y=50)
texto1= tk.Entry(font=("Algerian",15),width=15)
texto1.place(x=90,y=50)
lb2= tk.Label( text="Telefono:", fg="black", bg="ivory").place(x=10,y=90)
texto2= tk.Entry(font=("Algerian",15),width=15)
texto2.place(x=90,y=90)
boton = tk.Button(text="Añadir",command=Añadir_contacto).place(width=60,x=15,y=140)

###
ventana.mainloop()