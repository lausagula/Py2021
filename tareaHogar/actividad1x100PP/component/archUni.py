import json
import csv
import PySimpleGUI as sg


def universidad():
    """

    Esta funcion crea un archivo y muestra las 20 primeras universidades de CABA ubicadas en al barrio de San Nicolas.
    """

    with open ("universidades.csv","r",encoding="utf-8") as archivo_csv:
        csvreader = csv.reader(archivo_csv, delimiter=",")

        next(csvreader)
        
        listaUni = list(filter(lambda x : x[15] == "San Nicolas", csvreader))

        listaUni = listaUni[:20]

        for l in listaUni:
            print("NOMBRE: {}. UBICACION {}".format(l[3],l[11]))

    with open("archUni.json","w") as archivo:

        json.dump(listaUni,archivo)

    sg.popup_no_buttons("Archivo generado con exito.",title="Exito",auto_close=True,auto_close_duration=3)


