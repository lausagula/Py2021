import PySimpleGUI as sg
import json
from menu import menuLog
from setting import regiSetting,iniSesionSetting    



def logeo():
    """ 
    
    Defina la funcional de los botones del menu de inico de sesion/registrarse. 
    """

    user = "User_Unknow"

    window = menuLog.iniciar_sesion()

    while True:

        event, value = window.read()

        if event == "Registro":
            regiSetting.registro()

        if event == "iniS":
            user = iniSesionSetting.log_in()
            if user != "User_Unknow":
                break

        if event == sg.WIN_CLOSED:
            break
    window.close()
    
    return user