import csv
import json
import PySimpleGUI as sg

def comunas():
    """

    Esta funcion crea un archivo y muestra las 20 primeros clubes de CABA pertenecientes a las Comuna 11.
    """

    with open("clubes.csv","r",encoding="utf-8") as archivo_csv:
        csvReader = csv.reader(archivo_csv, delimiter=",")

        next(csvReader)
        
        '''for i in csvReader:
            if (i[17] == "Comuna 11"):
                print ("Nombre: {}".format(i[1]))'''

        listaComunasCABA = list(filter(lambda x : x[17] == "Comuna 11",csvReader))

        for l in (listaComunasCABA[:20]):
            print("Nombre: {}, del barrio de {}.".format(l[1],l[16]))
            



    with open("archivo.json","w") as archivo:            
        json.dump(listaComunasCABA[:20],archivo)

    sg.popup_no_buttons("Archivo generado con exito.",title="Exito",auto_close=True,auto_close_duration=3)




    
    