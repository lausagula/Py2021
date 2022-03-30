import PySimpleGUI as sg
from estadisticas import menuEst
from estadisticas import pedirEstadisticas


def loop():
    """ 
    
    Muestra la ventana de estadisticas.
    """

    window =  menuEst.menu()

    while True:

        event, _value = window.read()

        if event == "-Top10-":
            pedirEstadisticas.pedir_top_10()

        if event == "-Estado-":
            try:
                pedirEstadisticas.pedir_datos_por_estado()
            except IndexError:
                print("No hay datos suficientes para generar el grafico.")

        if event == "-Genero-":
            try:
                pedirEstadisticas.pedir_datos_por_genero()
            except IndexError:
                print("No hay datos suficientes para generar el grafico.")

        if event == "-Dias-":
            try:
                pedirEstadisticas.pedir_datos_por_dia_de_semana()
            except IndexError:
                print("No hay datos suficientes para generar el grafico.")


        if event == sg.WIN_CLOSED:
            break


    window.close()
