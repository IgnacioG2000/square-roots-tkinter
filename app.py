from tkinter import *
import math
from tkinter.messagebox import *
from funciones_aux import *

main = Tk()

main.title("Formula Resolvente")

a = DoubleVar()
b = DoubleVar()
c = DoubleVar()
x1 = StringVar()
x2 = StringVar()


def calcular_raices():
    discriminante = b.get() ** 2 - 4 * a.get() * c.get()

    if discriminante > 0:
        raiz1 = (-b.get() + math.sqrt(discriminante)) / 2 * a.get()
        raiz2 = (-b.get() - math.sqrt(discriminante)) / 2 * a.get()
        round(raiz1, 3)
        round(raiz2, 3)

        x1.set(raiz1)
        x2.set(raiz2)

        showinfo("Raiz 1 y 2", str(x1.get()) + " y " + str(x2.get()))

    elif discriminante == 0:
        raiz1 = -b.get() / 2 * a.get()
        raiz2 = raiz1
        round(raiz1, 3)
        round(raiz2, 3)

        x1.set(raiz1)
        x2.set(raiz2)

        showinfo("Raiz 1 y 2", str(x1.get()))

    else:
        discriminante = abs(discriminante)
        parte_real = -b.get() / 2 * a.get()
        parte_imag = math.sqrt(discriminante) / 2 * a.get()

        raiz1 = (parte_real.__round__(3), parte_imag.__round__(3))
        raiz2 = (parte_real.__round__(3), -parte_imag.__round__(3))

        x1.set(raiz1)
        x2.set(raiz2)

        showinfo("Raiz 1 y 2", str(x1.get()) + " y " + str(x2.get()))


coef_a = Label(main, text="Ingrese el coeficiente a")
coef_a.grid(row=0, column=0, padx=100, pady=25)

coef_b = Label(main, text="Ingrese el coeficiente b")
coef_b.grid(row=1, column=0, padx=100, pady=25)

coef_c = Label(main, text="Ingrese el coeficiente c")
coef_c.grid(row=2, column=0, padx=100, pady=25)

entry_coef_a = Entry(main, textvariable=a, width=15)
entry_coef_a.grid(row=0, column=1)

entry_coef_b = Entry(main, textvariable=b, width=15)
entry_coef_b.grid(row=1, column=1)

entry_coef_c = Entry(main, textvariable=c, width=15)
entry_coef_c.grid(row=2, column=1)

boton_resolver = Button(
    main,
    text="Calcular raices x1 y x2",
    command=calcular_raices,
)
boton_resolver.grid(row=3, column=0, padx=50)

centrar_pantalla(main)

main.mainloop()
