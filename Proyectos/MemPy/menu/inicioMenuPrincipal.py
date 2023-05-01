import PySimpleGUI as sg
from menu import menuPrincipal, menuInicioS
from setting import menuSetting, criterios, pedirDatos
from play import tablero
from puntuacion import puntos
from estadisticas import stats

def start():
    """ 
    
    Genera el menu principal del juego.
    Realiza las acciones correspondientes a cada boton.
    """

    window = menuPrincipal.menu_p()

    criterios.imprimir()


    while True:

        event, value = window.read()



        if event == "play1":
            if value["usr"] != "User_Unknow":
                window.hide()
                tablero.loop(value["usr"])
                window.un_hide()
            else:
                sg.popup_no_buttons("Necesita iniciar sesion primero.",title="Error",auto_close=True,auto_close_duration=2,background_color=("red"))

        if event == "log":
            user =  menuInicioS.logeo()
            if user != "User_Unknow":
                window["usr"].update(user)
        

        if event == "config":
            if value["usr"] == "User_Unknow":            
                sg.popup_no_buttons("Necesita iniciar sesion primero.",title="Error",auto_close=True,auto_close_duration=2,background_color=("red"))
            else:            
                window.hide()
                menuSetting.menu_config(value["usr"]) #DEVOLVER NOMBRE DEL USUARIO A ACTUALIZAR EN PANATLLA
                window.un_hide()

        if event == "puntos":
            puntos.loop(pedirDatos.pedir_archivo_tabla())

        if event == "stats":
            window.hide()
            stats.loop()
            window.un_hide()

        if event == sg.WINDOW_CLOSED:
            sg.popup_no_buttons("Gracias por jugar, saludos.",title="Adios",auto_close=True,auto_close_duration=1)
            break

