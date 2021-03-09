from tkinter import *

ventana= Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter | Pilar Goonzález")


# Texto Encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - Pilar G")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans",18),
    padx=10,
    pady=10
)
# Grid de 12 columnas(en el columnspan inicial)
encabezado.grid(row=0,column=0,columnspan=12,sticky=W)

# Label para el campo
label = Label(ventana, text="Nombre")
label.grid(row=1,column=0,sticky=W,padx=5, pady=5)

# Campo de texto
campo_texto = Entry(ventana)

# sticky fija el campo de texto a la izquierda
campo_texto.grid(row=1,column=1,sticky=W,padx=5,pady=5)

ventana.mainloop()