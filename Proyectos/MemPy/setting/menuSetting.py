import json
from tkinter import TclError
import PySimpleGUI as sg
from setting import configuracionTI
from setting import pedirDatos

def menu_config(user):
    """ 
    
    Esta funcion se encarga de guarda en un archivo json ya existente la nueva configuracion del usuario.

    :parametro user: es un string, el cual se va a usar para buscar al usuario en el archivo json y asignarle la nueva configuracion.
    """
    datos = pedirDatos.devolverDatos()
    window = configuracionTI.configurar(datos[user])

    while True:

            event, value = window.read()

            if event == "aux":
                try:
                    window["color"].Update(button_color= (value[event],value[event]))
                except TclError:
                    pass


            if event == "env":
                
                infoConfig = {
                        "Nivel":value["lvl"],
                        "Coincidencias":value["cantC"],
                        "Elementos":(value["elemPlabra"],value["elemImagenes"]),         #(PALABRAS,IMAGENES)
                        "Tiempo":(int(value["min"]),int(value["seg"])),
                        "Color":value["aux"]}


                with open("user.json","r") as archivo:
                    datos = json.load(archivo)
                with open ("user.json","w") as archivo:
                    datos[user]["Configuracion"] = infoConfig
                    json.dump(datos,archivo)               
                break
                
            if event == sg.WIN_CLOSED:
                break

    window.close()
    