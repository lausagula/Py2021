import PySimpleGUI as sg
from component import archComunas, archUni



layout = [[sg.Text("¿Que datos analizamos?",font=("Helvetica",30),pad=((0,0),(70,70)))],
    [sg.Button("Clubes de futbol",key="club",size=(40,3))],
    [sg.Button("Universidades",key="uni",size=(40,3))],
    [sg.Button("Salir",key="salir",size=(40,3),pad=((0,0),(40,40)))]]

window = sg.Window("Actividad 1 x Python Plus - TEORÍA -", layout,element_justification="c",size=(500,500),enable_close_attempted_event=True)


while True:

    event, _value = window.read()

    if event == "club":
        archComunas.comunas()

    if event == "uni":
        archUni.universidad()

    if event == "salir":
        break

window.close()



