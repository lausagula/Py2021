import PySimpleGUI as sg
from setting import pedirDatos
from menu import menuTablaPuntos


def loop(archivo):
    """ 
    
    Muestra la ventana de puntuacion.
    :Parametro archivo: list
    """

    window = menuTablaPuntos.table(archivo)

    while True:

        event, value = window.read()


        if event == sg.WIN_CLOSED:
            break

    window.close()