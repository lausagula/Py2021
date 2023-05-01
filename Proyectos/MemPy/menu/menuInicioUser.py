import PySimpleGUI as sg


def iniSesion():
    """ 

    Arma la ventana para ingresar el nombre de usuario almomento de iniciar sesion.
    """

    layout = [[sg.Text("Ingrese nombre de usuario:")],
        [sg.Input(key="usr")],
        [sg.Button("Ingresar",key="iniS")]]

    window = sg.Window("Log In", layout)

    return window