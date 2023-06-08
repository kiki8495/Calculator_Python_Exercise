from tkinter import *

# Crear ventana principal
ventana = Tk()
ventana.title("Calculadora")

# Crear pantalla
pantalla = Entry(ventana, font=("Calibri 20"))
pantalla.grid(row=0, column=0, columnspan=4, padx = 5, pady = 4)

# Funciones
def agregar_uno():
    pantalla.insert(END, "1")
def agregar_dos():
    pantalla.insert(END, "2")
def agregar_tres():
    pantalla.insert(END, "3")
def agregar_cuatro():
    pantalla.insert(END, "4")
def agregar_cinco():
    pantalla.insert(END, "5")
def agregar_seis():
    pantalla.insert(END, "6")
def agregar_siete():
    pantalla.insert(END, "7")
def agregar_ocho():
    pantalla.insert(END, "8")
def agregar_nueve():
    pantalla.insert(END, "9")
def agregar_cero():
    pantalla.insert(END, "0")
def borrar():
    pantalla.selection_clear

#Botones
#boton_ = Button(ventana, text="", width= 5, height=2)

boton_1 = Button(ventana, text="1", width= 5, height=2, command=agregar_uno)
boton_2 = Button(ventana, text="2", width= 5, height=2, command=agregar_dos)
boton_3 = Button(ventana, text="2", width= 5, height=2, command=agregar_tres)
boton_4 = Button(ventana, text="2", width= 5, height=2, command=agregar_cuatro)
boton_5 = Button(ventana, text="2", width= 5, height=2, command=agregar_cinco)
boton_6 = Button(ventana, text="2", width= 5, height=2, command=agregar_seis)
boton_7 = Button(ventana, text="2", width= 5, height=2, command=agregar_siete)
boton_8 = Button(ventana, text="2", width= 5, height=2, command=agregar_ocho)
boton_9 = Button(ventana, text="2", width= 5, height=2, command=agregar_nueve)
boton_0 = Button(ventana, text="2", width= 14, height=2, command=agregar_cero)

boton_borrar = Button(ventana, text="AC", width= 5, height=2)
boton_parentesis1 = Button(ventana, text="(", width= 5, height=2)
boton_parentesis2 = Button(ventana, text=")", width= 5, height=2)
boton_punto = Button(ventana, text=".", width= 5, height=2)

boton_div = Button(ventana, text="/", width= 5, height=2)
boton_suma = Button(ventana, text="+", width=5, height=2)
boton_resta = Button(ventana, text="-", width= 5, height=2)
boton_multiplicar = Button(ventana, text="*", width= 5, height=2)
boton_igual = Button(ventana, text="=", width= 5, height=2)

#Agregar botones en pantalla
#boton_.grid(row= , column= , padx=5, pady=5)
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_punto.grid(row=1, column=3, padx=5, pady=5)
boton_1.grid(row= 2, column=0 , padx=5, pady= 5)


# Ejecutar la calculadora
ventana.mainloop()
