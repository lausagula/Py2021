from tkinter import Event
import PySimpleGUI as sg
import json

from menu import registroS

def registro():
    """ 
    
    Esta funcion crea un nuevo usario, con una configuracion basica y lo guarda en un archivo json, que puede no existir.
    """
    
    window = registroS.regis()

    event, value = window.read()

    if event == "ok":
        try:
            with open ("user.json","r+") as archivo:
                datos = json.load(archivo)
            with open ("user.json","w") as archivo:          
                datos[value["user"]] = {"Edad":value["edad"],
                        "Genero":value["genero"],
                        "Configuracion":{
                        "Nivel":"Nivel 1",
                        "Coincidencias":2,
                        "Elementos":(True,False),         
                        "Tiempo":(4,59),
                        "Color":"#d9d9d9"}}
                json.dump(datos,archivo)

        except (FileExistsError,FileNotFoundError):
            archivo = open("user.json","w+")
            datos = {value["user"]:{"Edad":value["edad"],
                    "Genero":value["genero"],
                    "Configuracion":{
                    "Nivel":"Nivel 1",
                    "Coincidencias":2,
                    "Elementos":(True,False),         
                    "Tiempo":(4,59),
                    "Color":"#d9d9d9"}}}
            json.dump(datos,archivo)
            archivo.close()
    
            
        sg.popup_no_buttons("Usted se ha registrado con exito.",title="Enhorabuena !!",auto_close=True,auto_close_duration=3)
        
        window.close()
        

