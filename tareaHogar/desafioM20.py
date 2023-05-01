import csv
from collections import Counter

with open("appstore_games.csv","r",encoding="utf-8") as archivo_csv:

    csvReader = csv.reader(archivo_csv, delimiter=',')
    next(csvReader)
    
    dicc = {}
    
    for i in csvReader:
        try:
            dicc[i[4]] = int(i[6])
        except ValueError:
            ()

    max = Counter(dicc).most_common(10)

    print(dict(max))


with open("appstore_games.csv","r",encoding="utf-8") as archivo_csv:

    csvReader = csv.reader(archivo_csv, delimiter=',')
    next(csvReader)
    '''for i in csvReader:
        if (i[7] == "0") and ("ES" in i[12]):
            print(i[2])'''


    listaGratuitosEspañol = list(filter(lambda x : (x[7] == "0") and ("ES" in x[12]), csvReader))

    print(listaGratuitosEspañol)