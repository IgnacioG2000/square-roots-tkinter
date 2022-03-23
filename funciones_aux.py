def centrar_pantalla(ventana):

    ancho_ventana = 700
    alto_ventana = 400

    x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = (
        str(ancho_ventana)
        + "x"
        + str(alto_ventana)
        + "+"
        + str(x_ventana)
        + "+"
        + str(y_ventana)
    )
    ventana.geometry(posicion)
    ventana.resizable(False, False)