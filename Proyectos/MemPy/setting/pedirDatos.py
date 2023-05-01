import json
import os
import pandas as pd

def devolverDatos():
    """ Retorna la ubicacion de archivo de usuarios. """

    path_arch = "user.json"
    path_file = os.path.join(os.getcwd(),path_arch)

    with open(path_file,"r") as archivo:
        datos = json.load(archivo)
    return datos


def pedir_edad(user):
    """ 
    
    Retorna la edad del usuario.
    :Parametro user: String
    """

    datos = devolverDatos()
    edad = datos[user]["Edad"]
    return edad

def pedir_genero(user):
    """ 
    
    Retorna el genero del usuario.
    :Parametro user: String
    """
    
    datos = devolverDatos()
    genero = datos[user]["Genero"]
    return genero
    

def pedirColor(user):
    """ 
    
    Retorna el color seleccionado por el usuario.
    :Parametro user: String
    """

    datos = devolverDatos()
    color = datos[user]["Configuracion"]["Color"]
    return color

def pedirTiempo(user):
    """ 
    
    Retorna el tiempo seleccionado por el usuario.
    :Parametro user: String
    """

    datos = devolverDatos()
    tiempo = datos[user]["Configuracion"]["Tiempo"]
    return tiempo

def pedirLvl(user):
    """ 
    
    Retorna el nivel del usuario.
    :Parametro user: String
    """

    datos = devolverDatos()
    lvl = datos[user]["Configuracion"]["Nivel"]
    return lvl

def pedir_archivo_tabla():
    """ Retorna una lista con el nombre de los distintos archivos donde se guarda la puntuacion. """

    arch = ["tablaPuntosLvl1.csv","tablaPuntosLvl2.csv","tablaPuntosLvl3.csv","tablaPuntosLvl4.csv","tablaPuntosLvl5.csv"]
    nueva_lista = []
    for a in arch: 
        nueva_lista.append(os.path.join(os.getcwd(),a))

    return nueva_lista
        

def pedir_num_Partida():
    """ Retorna el numero de la proxima partida a jugar. """

    archivo = os.path.join(os.getcwd(),"registroJugadas.csv")
    try:
        df = pd.read_csv(archivo,encoding="utf-8")
        try:
            numPartida = df["Partida"].values[-1]
        except IndexError:
            numPartida = 0
        #return numPartida +1
    except FileNotFoundError:
        columnas = ["Tiempo","Partida","Cantidad total de palabras a adivinar","Nombre de evento","usuarie -nick","Usuarie -genero","usuarie -edad","Estado","Palabra","nivel"]
        df = pd.DataFrame(columns=columnas)
        df.to_csv(archivo,mode="x",header=True,encoding="utf-8",index=False)
        numPartida = 0

    return numPartida +1


def pedir_coincidencias(lvl):
    """ Retorna la cantidad de palabras a adivinar por nivel. """

    if lvl == "Nivel 1":
        return 4
    elif lvl == "nivel 2" or lvl == "Nivel 4":
        return 6
    else:
        return 8