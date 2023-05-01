import PySimpleGUI as sg

def menu_p():

    """Construye ventana con el menu principal del juego"""

    menuPrincipal = [[sg.Input("User_Unknow",disabled=True,key="usr")],
            [sg.Button(button_text="Ingresar",key="log",pad=((0,0),(30,0)),tooltip="Sobre el boton",border_width=2,size=(10,1))],
            [sg.Text("MemPy",font=("Helvetica",50),pad=((230,0),(100,160)))],
            [sg.Button(button_text="Iniciar Juego",key="play1",pad=((190,0),3),tooltip="Sobre el boton",border_width=2,size=(40,3))],
            [sg.Button(button_text="Configuración",key="config",pad=((190,0),3),tooltip="Sobre el boton",border_width=2,size=(40,3))],
            [sg.Button(button_text="Puntajes",key="puntos",pad=((190,0),3),tooltip="Sobre el boton",border_width=2,size=(40,3))],
            [sg.Button(button_text="Estadísticas",key="stats",pad=((190,0),3),tooltip="Sobre el boton",border_width=2,size=(40,3))]]

    window = sg.Window("Menu Principal",menuPrincipal,size=(700,700))

    return window