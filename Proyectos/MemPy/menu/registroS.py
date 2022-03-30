import PySimpleGUI as sg


def regis():
    """ 
    
    Arma la ventana para registrar un nuevo usuario.
    """
    registroUsuario = [[sg.Text("Nombre de usuario:")],
        [sg.Input(key="user")],
        [sg.Text("Ingrese edad:")],
        [sg.Input(key="edad",size=(3,1))],
        [sg.Text("Genero")],
        [sg.Combo(["Masculino","Femenino","No binario","Prefieron no decir"],key="genero",default_value="---")],
        [sg.Button("ok",key="ok")]]

    window = sg.Window("Registrarse",registroUsuario)

    return window