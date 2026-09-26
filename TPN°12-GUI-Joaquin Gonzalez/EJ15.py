#importamos tk
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

#creamos la ventana y le otorgamos un titulo
ventana = tk.Tk()
ventana.title("Ventana de prueba-EJ15")

#definimos el tamaño de la ventana
ventana.geometry("300x100")

#crear la variable numerica para el tamaño del texto
tamaño_texto = tk.IntVar()

file_path = filedialog.askopenfile()

#crear opcion para abrir y guardar archivos
def abir_guardar_archivos():
    file_path = filedialog.askopenfile()

def cambiar_texto():
    ventana_nueva = tk.Toplevel(ventana)
    ventana_nueva.title("configuraciones de texto")
    ventana_nueva.geometry("300x200")

    etiqueta = tk.Label(ventana_nueva, text="Elija un tamaño del texto")
    etiqueta.pack()
    scale= tk.Scale(ventana_nueva, from_=0, to=100, orient=tk.HORIZONTAL, variable=tamaño_texto, command=cambiar_tamaño)
    scale.pack()


def cambiar_tamaño(valor):
     text.config(font=("Arial", int(float(valor))))

#creamos un cuadro de texto para que la persona ingrese texto
text = tk.Text(
    ventana,
    height=5,
    width=30,
    font=("Arial",tamaño_texto.get()),
)
text.pack()

#Creamos un menú
menu= tk.Menu(ventana)
ventana.config(menu=menu)
submenu=tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=submenu)
submenu.add_command(label="Nuevo")
submenu.add_command(label="abrir/guardar archivo", command=abir_guardar_archivos)
submenu.add_command(label="Cambiar tamaño de texto", command=cambiar_texto)
submenu.add_command(label="Salir", command= ventana.quit)

###

###
ventana.mainloop()