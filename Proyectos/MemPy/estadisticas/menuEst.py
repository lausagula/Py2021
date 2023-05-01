import PySimpleGUI as sg

def menu():
    """ 
    
    Arma la ventana de Estadisticas.
    """

    layout = [[sg.Button("Top 10",size=(8,4),key="-Top10-"),sg.Button("Estado",size=(8,4),key="-Estado-"),sg.Button("Genero",size=(8,4),key="-Genero-"),sg.Button("Dias",size=(8,4),key="-Dias-")]]

    window = sg.Window("Estadisticas",layout,element_justification="center")

    return window