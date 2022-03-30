import csv
from setting import pedirDatos

def tabla_puntos(user,puntos):
    """ 
    
    Registra la puntuacion de las partidas.
    :Parametro user: String
    :Parametro puntos: int
    """

    lvl = pedirDatos.pedirLvl(user)

    if lvl == "Nivel 1":
        archivo = "tablaPuntosLvl1.csv"
    elif lvl == "Nivel 2":
        archivo = "tablaPuntosLvl2.csv"
    elif lvl == "Nivel 3":
        archivo = "tablaPuntosLvl3.csv"
    elif lvl == "Nivel 4":
        archivo = "tablaPuntosLvl4.csv"
    else:
        archivo = "tablaPuntosLvl5.csv"

    try:
        with open(archivo,"x") as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(["Nombre","Nivel","Puntos"])
            writer.writerow([user,lvl,puntos])
    except FileExistsError:
        with open(archivo,"a") as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow([user,lvl,puntos])
        

    
        

