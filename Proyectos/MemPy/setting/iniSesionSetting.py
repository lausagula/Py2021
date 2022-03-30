import PySimpleGUI as sg
import json
from menu import menuInicioUser

def log_in():
    """ 
    
    Muestra la ventana de inicio de sesion, verificando que el usuario exista.
    :return user: retorna el nombre de usuario, el cual aparecera en el menu principal, para saber que usuario esta jugando.
    """

    window = menuInicioUser.iniSesion()
    
    
    user = "User_Unknow"

    while True:

        event, value = window.read()

        if event == "iniS":            
            try:
                with open ("user.json","r") as archivo:
                    datos  = json.load(archivo)
                if value["usr"] in datos.keys():           
                    infoUser = {value["usr"]:datos[value["usr"]]}
                    user = value["usr"]                 
                    
                else: 
                    sg.popup_no_buttons("Nombre de usuario no encontrado, vuelva a intentar.",title="Error",auto_close=True,auto_close_duration=2,background_color=("red"))
            except (FileExistsError,FileNotFoundError):
                sg.popup_no_buttons("Archivo no encontrado o inexistente.",title="ERROR",auto_close=True,auto_close_duration=3,background_color=("red"))

            break

        if event == sg.WIN_CLOSED:
            break
    window.close()
    return user
    

        


