from tkinter import *

# Crear ventana principal
ventana = Tk()
ventana.title("Calculadora")
ventana.configure(bg="#4c007d")

# Crear pantalla
pantalla = Entry(ventana, font=("Calibri 20"), bg="#7f00b2", fg='white', relief='flat')
pantalla.grid(row=0, column=0, columnspan=4, padx = 5, pady = 4)

# Funciones
def agregar_valor(valor):
    pantalla.insert(END, valor)
def borrar():
    pantalla.delete(0, END)
def evaluar():
    datos = pantalla.get()
    borrar()
    resultado = eval(datos)
    pantalla.insert(END, resultado)
def cambiar_color_on_enter(boton):
    boton.config(bg='#4c007d', fg="#bc4ed8")
def cambiar_color_on_leave(boton):
    boton.config(bg='#7f00b2', fg='white')
    
# Botones

boton_1 = Button(ventana, text="1", bg="#7f00b2", fg='white', relief='flat', width=5, height=2, command=lambda: agregar_valor(1))

boton_1.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_1))
boton_1.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_1))

boton_2 = Button(ventana, text="2", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor(2))

boton_2.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_2))
boton_2.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_2))

boton_3 = Button(ventana, text="3", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor(3))

boton_3.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_3))
boton_3.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_3))

boton_4 = Button(ventana, text="4", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor(4))

boton_4.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_4))
boton_4.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_4))

boton_5 = Button(ventana, text="5", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor(5))

boton_5.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_5))
boton_5.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_5))

boton_6 = Button(ventana, text="6", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor(6))

boton_6.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_6))
boton_6.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_6))

boton_7 = Button(ventana, text="7", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor(7))

boton_7.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_7))
boton_7.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_7))

boton_8 = Button(ventana, text="8", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor(8))

boton_8.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_8))
boton_8.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_8))

boton_9 = Button(ventana, text="9", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor(9))

boton_9.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_9))
boton_9.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_9))

boton_0 = Button(ventana, text="0", bg= "#7f00b2", fg='white', relief='flat', width=16, height=2, command=lambda :agregar_valor(0))

boton_0.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_0))
boton_0.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_0))

boton_borrar = Button(ventana, text="AC", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=borrar)

boton_borrar.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_borrar))
boton_borrar.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_borrar))

boton_parentesis1 = Button(ventana, text="(", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor("("))

boton_parentesis1.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_parentesis1))
boton_parentesis1.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_parentesis1))

boton_parentesis2 = Button(ventana, text=")", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor(")"))

boton_parentesis2.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_parentesis2))
boton_parentesis2.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_parentesis2))

boton_punto = Button(ventana, text=".", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor("."))

boton_punto.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_punto))
boton_punto.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_punto))

boton_div = Button(ventana, text="/", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor("/"))

boton_div.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_div))
boton_div.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_div))

boton_suma = Button(ventana, text="+", bg= "#7f00b2", fg='white', relief='flat', width=5, height=2, command=lambda :agregar_valor("+"))

boton_suma.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_suma))
boton_suma.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_suma))

boton_resta = Button(ventana, text="-", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor("-"))

boton_resta.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_resta))
boton_resta.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_resta))

boton_multiplicar = Button(ventana, text="X", bg= "#7f00b2", fg='white', relief='flat', width= 5, height=2, command=lambda :agregar_valor("*"))

boton_multiplicar.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_multiplicar))
boton_multiplicar.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_multiplicar))

boton_igual = Button(ventana, text="=", bg= "#7f00b2", fg='white', relief='flat', width=5, height=2, command=evaluar)

boton_igual.bind("<Enter>", lambda event: cambiar_color_on_enter(boton_igual))
boton_igual.bind("<Leave>", lambda event: cambiar_color_on_leave(boton_igual))

# Agregar botones en interfaz

boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton_7.grid(row= 2, column=0, padx=5, pady= 5)
boton_8.grid(row= 2, column=1, padx=5, pady= 5)
boton_9.grid(row= 2, column=2, padx=5, pady= 5)
boton_multiplicar.grid(row= 2, column=3, padx=5, pady= 5)

boton_4.grid(row= 3, column=0, padx=5, pady= 5)
boton_5.grid(row= 3, column=1, padx=5, pady= 5)
boton_6.grid(row= 3, column=2, padx=5, pady= 5)
boton_suma.grid(row= 3, column=3, padx=5, pady= 5)

boton_1.grid(row= 4, column=0, padx=5, pady= 5)
boton_2.grid(row= 4, column=1, padx=4, pady= 5)
boton_3.grid(row= 4, column=2, padx=5, pady= 5)
boton_resta.grid(row= 4, column=3, padx=5, pady= 5)

boton_0.grid(row= 5, column=0, columnspan=2, padx=5, pady= 5)
boton_punto.grid(row= 5, column=2, padx=5, pady= 5)
boton_igual.grid(row= 5, column=3, padx=5, pady= 5)

# Ejecutar la calculadora

ventana.mainloop()