import PySimpleGUI as sg
import json

def iniciar_sesion():
    
    """Menu para iniciar sesion o registrarse"""

    inicioSesion = [
        [sg.Text("Logueo:")],
        [sg.Button("Iniciar sesion",key="iniS")],
        [sg.Text("Es su primera vez? ",pad=((0,0),(20,0)))],
        [sg.Button("Registrarse",key="Registro")]]

    window = sg.Window("Logeo",inicioSesion)

    return window
