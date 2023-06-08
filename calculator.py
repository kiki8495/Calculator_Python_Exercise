from tkinter import *

# Crear ventana principal
ventana = Tk()
ventana.title("Calculadora")

# Crear pantalla
pantalla = Entry(ventana, font=("Calibri 20"))
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

# Botones

boton_1 = Button(ventana, text="1", width= 5, height=2, command=lambda :agregar_valor(1))
boton_2 = Button(ventana, text="2", width= 5, height=2, command=lambda :agregar_valor(2))
boton_3 = Button(ventana, text="3", width= 5, height=2, command=lambda :agregar_valor(3))
boton_4 = Button(ventana, text="4", width= 5, height=2, command=lambda :agregar_valor(4))
boton_5 = Button(ventana, text="5", width= 5, height=2, command=lambda :agregar_valor(5))
boton_6 = Button(ventana, text="6", width= 5, height=2, command=lambda :agregar_valor(6))
boton_7 = Button(ventana, text="7", width= 5, height=2, command=lambda :agregar_valor(7))
boton_8 = Button(ventana, text="8", width= 5, height=2, command=lambda :agregar_valor(8))
boton_9 = Button(ventana, text="9", width= 5, height=2, command=lambda :agregar_valor(9))
boton_0 = Button(ventana, text="0", width=18, height=2, command=lambda :agregar_valor(0))

boton_borrar = Button(ventana, text="AC", width= 5, height=2, command=borrar)
boton_parentesis1 = Button(ventana, text="(", width= 5, height=2, command=lambda :agregar_valor("("))
boton_parentesis2 = Button(ventana, text=")", width= 5, height=2, command=lambda :agregar_valor(")"))
boton_punto = Button(ventana, text=".", width= 5, height=2, command=lambda :agregar_valor("."))

boton_div = Button(ventana, text="/", width= 5, height=2, command=lambda :agregar_valor("/"))
boton_suma = Button(ventana, text="+", width=5, height=2, command=lambda :agregar_valor("+"))
boton_resta = Button(ventana, text="-", width= 5, height=2, command=lambda :agregar_valor("-"))
boton_multiplicar = Button(ventana, text="X", width= 5, height=2, command=lambda :agregar_valor("*"))
boton_igual = Button(ventana, text="=", width= 5, height=2, command= evaluar)

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
