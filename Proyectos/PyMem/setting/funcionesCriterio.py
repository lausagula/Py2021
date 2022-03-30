import os
import csv
from PIL import Image
from random import sample

path_file = "dataset1"

def meme_avenger():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file2 = "images"
    arch_csv = "reference.csv"
    path_arch = os.path.join(os.getcwd(),path_file)


    with open(os.path.join(path_arch,arch_csv),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))

    meme_avengers = list(map(lambda x : x["image_name"],(filter(lambda y : y["original_name"].startswith("avengers"),data_set))))

    """ for n in sample(range(0,30),5):
        path_images = os.path.join(os.getcwd(),path_file,path_file2,meme_avengers[n])
        print (path_images)
        img = Image.open(path_images)
        img.show() """

    return meme_avengers

    
def meme_hilarious():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file2 = "images"
    arch_csv = "labels.csv"

    with open(os.path.join(os.getcwd(),path_file,arch_csv),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))

    meme_hilarious = list(map(lambda x : x["image_name"],(filter(lambda y : y["humour"] == "hilarious",data_set))))

    """ for n in sample(range(0,30),5):
        path_images = os.path.join(os.getcwd(),path_file,path_file2,meme_hilarious[n])
        print (path_images)
        img = Image.open(path_images)
        img.show() """
    
    return meme_hilarious



def airlines_america_sur():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_arch_airlines = "airlines.csv"

    path_arch = os.path.join(os.getcwd(),path_file)

    americaDelSur =  ["Argentina","Brazil","Colombian","Bolivia","Paraguay","Uruguay","Chile","Venezuela","Peru","Ecuador"]

    with open (os.path.join(path_arch,path_arch_airlines),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))

    aerolineasAmericaSur = list(map(lambda x : x["Name"],(filter(lambda x : x["Country"] in americaDelSur,data_set))))

    return aerolineasAmericaSur

def airlines_USA():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """
    
    path_arch_airlines = "airlines.csv"

    path_arch = os.path.join(os.getcwd(),path_file)


    with open (os.path.join(path_arch,path_arch_airlines),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))

    aerolineasUsa = list(map(lambda x : x["Name"],(filter(lambda x : x["Country"] == "United States" and x["Active"] == "Y",data_set))))

    return aerolineasUsa

def forbes_mayores_de_95(): 
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_forbes = "forbes_billionaires_geo.csv"

    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_forbes),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))

    forbesMasViejos = list(set(map(lambda x : x["Source"],filter(lambda x : x["Age"] != "" and float(x["Age"]) > 95,data_set))))

    return forbesMasViejos

def forbes_mas_hijos():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_forbes = "forbes_billionaires_geo.csv"

    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_forbes),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))


    forbesMasHijos = list(set(map(lambda x : x["Country"],sorted(data_set, key=lambda x : x["Children"], reverse=True))))

    return forbesMasHijos

def forbes_en_Harvar():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_forbes = "forbes_billionaires_geo.csv"

    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_forbes),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))

    forbesEnHarvar = list(map(lambda x : x["Name"],filter(lambda x :"Harvar" in x["Education"] ,data_set)))

    return forbesEnHarvar

def forbes_residencia_solteros():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_forbes = "forbes_billionaires_geo.csv"

    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_forbes),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))



    forbesResidencia = list(set(map(lambda x : x["Residence"],filter(lambda x : x["Status"] == "Single",data_set))))

    return forbesResidencia

def circuitos_USA():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_f1C = "circuits.csv"

    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_f1C),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))

    circuitosCsv = list(set(map(lambda x : x["name"],filter(lambda x : x["country"] == "USA",data_set))))

    return circuitosCsv

def circuitos_USA2():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_f1C = "circuits.csv"

    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_f1C),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))

    circuitosCsv = list(set(map(lambda x : x["location"],filter(lambda x : x["country"] == "USA",data_set))))


    return circuitosCsv

def pilotos_españoles():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_f1D = "drivers.csv"

    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_f1D),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))
        

    driversCsv = list(map(lambda x : x["driverRef"],filter(lambda x : x["nationality"] == "Spanish",data_set)))

    return driversCsv

def piramides_mas_altas():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_pyra = "pyramids.csv"


    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_pyra),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))

    csvPiramides = list(map(lambda x : x["Pharaoh"],sorted(data_set,key= lambda x : x["Height (m)"])[:10]))

    return csvPiramides

def piramides_3_dinastia():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_pyra = "pyramids.csv"


    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_pyra),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))

    csvPiramides = list(map(lambda x : x["Modern name"],filter(lambda x : x["Dynasty"] == str(3),data_set)))

    return csvPiramides

def renta_autos_hibridos():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_rent = "CarRentalDataV1.csv"

    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_rent),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))


    csvAutosR = list(set(map(lambda x : x["vehicle.make"],filter(lambda x : x["fuelType"] == "HYBRID",data_set))))

    return csvAutosR

def renta_autos_suv():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_rent = "CarRentalDataV1.csv"

    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_rent),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))


    csvAutosR = list(set(map(lambda x : x["vehicle.model"],filter(lambda x : x["vehicle.type"] == "suv",data_set))))


    return csvAutosR[:16]


def compañia_ciudado_salud():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_logos = "companies.csv"
    path_arch = os.path.join(os.getcwd(),path_file)
    path_arch_logos = os.path.join(path_arch,"logos")
    

    with open(os.path.join(path_arch,path_file_logos),"r") as archivo:
            data_set = []

            for i in csv.DictReader(archivo):
                data_set.append(dict(i))

    csvLogos = list(map(lambda x : x["logo"],filter(lambda x : x["sector"] == "Healthcare" and x["logo"] != "",data_set)))
    
    """ for n in sample(range(0,30),5):
        path_images = os.path.join(path_arch_logos,csvLogos[n])
        print (path_images)
        img = Image.open(path_images)
        img.show() """

    return csvLogos

def pokemon_dragon():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_pok = "pokemon.csv"
    path_arch = os.path.join(os.getcwd(),path_file)
    path_arch_pok = os.path.join(path_arch,"pokemon")

    with open(os.path.join(path_arch,path_file_pok),"r") as archivo:
            data_set = []

            for i in csv.DictReader(archivo):
                data_set.append(dict(i))

    csvPok = list(map(lambda x : x["Name"],filter(lambda x : x["Type1"] == "Dragon" ,data_set)))

    """ for n in sample(range(0,20),5):
        path_images = os.path.join(path_arch_pok,csvPok[n]+".png")
        print(path_images)
        img = Image.open(path_images)
        img.show() """

    return csvPok

def zapatillas_hombre():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_wear = "fashion.csv"
    path_arch = os.path.join(os.getcwd(),path_file)
    path_arch_wear = os.path.join(path_arch,"imagesFootWear")

    with open(os.path.join(path_arch,path_file_wear),"r") as archivo:
            data_set = []

            for i in csv.DictReader(archivo):
                data_set.append(dict(i))

    csvWear = list(set(map(lambda x : x["Image"],filter(lambda x : x["Gender"] == "Men" and x["Category"] == "Footwear" ,data_set))))

    """ for n in sample(range(0,20),5):
        path_images = os.path.join(path_arch_wear,csvWear[n])
        print(path_images)
        img = Image.open(path_images)
        img.show()  """

    return csvWear

def ropa_mujeres():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_wear = "fashion.csv"
    path_arch = os.path.join(os.getcwd(),path_file)
    path_arch_wear = os.path.join(path_arch,"imagesApparel")

    with open(os.path.join(path_arch,path_file_wear),"r") as archivo:
            data_set = []

            for i in csv.DictReader(archivo):
                data_set.append(dict(i))

    csvWear = list(set(map(lambda x : x["Image"],filter(lambda x : x["Gender"] == "Girls" and x["Category"] == "Apparel" ,data_set))))

    """ for n in sample(range(0,10),5):
        path_images = os.path.join(path_arch_wear,csvWear[n])
        print(path_images)
        img = Image.open(path_images)
        img.show() """
    
    return csvWear

def jugadores_argentinos_zurdos():
    """ Abre el archivo csv, guarda una lista con los datos que cumplan con el criterio y retorna la lista. """

    path_file_juadoresF = "FullData.csv"
    path_arch = os.path.join(os.getcwd(),path_file)

    with open (os.path.join(path_arch,path_file_juadoresF),"r") as archivo:
        data_set = []

        for i in csv.DictReader(archivo):
            data_set.append(dict(i))


    csvjugadoresF = list(map(lambda x : x["Name"],filter(lambda x : x["Preffered_Foot"] == "Left" and x["Nationality"] == "Argentina",data_set)))


    return csvjugadoresF[:16]