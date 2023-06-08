from tkinter import *

def on_enter(event):
    boton.config(bg='#4c007d', fg='white')

def on_leave(event):
    boton.config(bg='#7f00b2', fg='black')

ventana = Tk()
ventana.title("Eliminación de bordes de los botones")

ventana.configure(bg="#4c007d")  # Cambiar el fondo de la ventana principal

boton = Button(ventana, text="Pasa el mouse aquí", bg='#7f00b2', fg='black', relief='flat')
boton.pack()

boton.bind("<Enter>", on_enter)  # Evento cuando el mouse entra al botón
boton.bind("<Leave>", on_leave)  # Evento cuando el mouse sale del botón

ventana.mainloop()
