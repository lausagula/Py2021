import os
from PIL import Image
import csv


path_arch = os.path.join(os.getcwd(),"dataset1")


def procesar_imagen(listaImg, pathCompleto):
    """ 
    
    Recibe una lista de imagenes y la direccion donde se encuentran, formatea las imagenes y devuelve una lista con las imagenes formateadas.
    :Parametro listaImg: list
    :Parametro pathCompleto: String
    """

    nuevaListaImg = []

    for i in listaImg:
        aux = os.path.join(pathCompleto,i)
        if i.endswith(".jpg"):
            im = Image.open(aux)
            aux = aux.replace(".jpg",".png")
        else:
            im = Image.open(aux)
        im = im.resize((1200,1000))
        im.save(aux)
        nuevaListaImg.append(aux)

    print(nuevaListaImg)


    return nuevaListaImg

def ropa_mujer():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """    

    csv_ropa = "fashion.csv"

    path_arch_ropa = os.path.join(path_arch,"imagesApparel")

    with open(os.path.join(path_arch,csv_ropa),"r") as archivo:
            data_set = []

            for i in csv.DictReader(archivo):
                data_set.append(dict(i))

    listaCsvRopa = list(set(map(lambda x : x["Image"],filter(lambda x : x["Gender"] == "Girls" and x["Category"] == "Apparel" ,data_set))))

    listaNuevaImg = procesar_imagen(listaCsvRopa[:16],path_arch_ropa)

    return listaNuevaImg

def zapatillas_hombre():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    csv_zapatillas = "fashion.csv"

    path_arch_zapatillas = os.path.join(path_arch,"imagesFootWear")

    with open(os.path.join(path_arch,csv_zapatillas),"r") as archivo:
            data_set = []

            for i in csv.DictReader(archivo):
                data_set.append(dict(i))

    listCsvZapatillas = list(set(map(lambda x : x["Image"],filter(lambda x : x["Gender"] == "Men" and x["Category"] == "Footwear" ,data_set))))

    listaNuevaImg = procesar_imagen(listCsvZapatillas[:16],path_arch_zapatillas)

    return listaNuevaImg


def pokemons():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    csvPok = "pokemon.csv"

    path_arch_pok = os.path.join(path_arch,"pokemon")

    with open(os.path.join(path_arch,csvPok),"r") as archivo:
            data_set = []

            for i in csv.DictReader(archivo):
                data_set.append(dict(i))

    csvPok = list(map(lambda x : x["Name"],filter(lambda x : x["Type1"] == "Dragon" ,data_set)))

    csvPokMod = []

    for nom in csvPok:
        aux =  nom + ".png"
        csvPokMod.append(aux)

    print(csvPokMod[:16])

    listaNuevaImg = procesar_imagen(csvPokMod[:16],path_arch_pok)

    return listaNuevaImg


def logos_empresas():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    csvLogos = "companies.csv"

    path_arch_logos = os.path.join(path_arch,"logos")

    with open(os.path.join(path_arch,csvLogos),"r") as archivo:
            data_set = []

            for i in csv.DictReader(archivo):
                data_set.append(dict(i))

    listCsvLogos = list(set(map(lambda x : x["logo"],filter(lambda x : x["sector"] == "Healthcare" and x["logo"] != "",data_set))))

    listaNuevaImg = procesar_imagen(listCsvLogos[:16],path_arch_logos)

    return listaNuevaImg
