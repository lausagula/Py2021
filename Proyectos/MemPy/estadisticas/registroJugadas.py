import csv
import os
import pandas as pd
from setting import pedirDatos

columnas = ["Tiempo","Partida","Cantidad total de palabras a adivinar","Nombre de evento","usuarie -nick","Usuarie -genero","usuarie -edad","Estado","Palabra","nivel"]


def traer_archivo():
    """ Retorna la ruta del archivo del parametro "arch" """
    arch = "registroJugadas.csv"
    path_file = os.path.join(os.getcwd(),arch)
    return path_file


def registrar_jugada(*datos):
    """ 
    
    Recibe una lista como parametro y carga los datos a un archivo csv ya existente.
    :Parametro datos: lista
    """
    archivo = traer_archivo()
    df = pd.DataFrame(datos,columns=columnas)
    df.to_csv(archivo,index=None,mode="a",header=False)
