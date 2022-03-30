import csv
import datetime
from setting import funcionesCriterio as fun

def imprimir():
    """ Imprime la lista de criterios correspondiente al dia y horario. """

    x = datetime.datetime.now()
    hora = datetime.datetime.now().hour
    horaE = datetime.datetime.now().strftime("%H:%M:%S")
    dia = datetime.datetime.today().weekday()

    if int(hora) < 13:
        print("Hoy {}, en el horario de las {} toca el criterio {}".format(diasSemana[int(dia)],horaE,criteriosDataF[diasSemana[dia]]["mañana"]["criterio"]))
        print(criteriosDataF[diasSemana[dia]]["mañana"]["funcion"]())
        

    else:
        print("Hoy {}, en el horario de las {} toca el criterio {}".format(diasSemana[int(dia)],horaE,criteriosDataF[diasSemana[dia]]["tarde"]["criterio"]))
        print(criteriosDataF[diasSemana[dia]]["tarde"]["funcion"]())

def listaCriterios():
    """ Devuelve la lista de criterios correspondiente al dia y horario. """

    if hora < 13:
        return criteriosDataF[diasSemana[dia]]["mañana"]["funcion"]()
    else:
        return criteriosDataF[diasSemana[dia]]["tarde"]["funcion"]()
    


x = datetime.datetime.now()
hora = datetime.datetime.now().hour
horaE = datetime.datetime.now().strftime("%H:%M:%S")
dia = datetime.datetime.today().weekday()


diasSemana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

mañana,tarde = [(0, 12),(13, 23)]

criteriosDataF = {}
for d in diasSemana:
    criteriosDataF[d] = {mañana:{},tarde:{}}




criteriosDataF["Lunes"]["mañana"] = {"criterio":"Lugar de residencia de las 10 primeras personas con mayor cantidad de ingresos en el mundo, que su estado civil es soltero.","funcion":fun.forbes_residencia_solteros} #BIEN
criteriosDataF["Martes"]["mañana"] = {"criterio":"Nombre de las aerolineas ubicadas en sudamerica.","funcion":fun.airlines_america_sur} #BIEN
criteriosDataF["Miercoles"]["mañana"] = {"criterio":"Paises donde se encuentran las empresas de con mayores ingresos, y que su dueño tiene la mayor cantidad de hijos, basado en la lista de Forbes","funcion":fun.forbes_mas_hijos } #bien
criteriosDataF["Jueves"]["mañana"] = {"criterio":"Empresas dononde su dueño supera los 95 años.","funcion":fun.forbes_mayores_de_95}    #bien
criteriosDataF["Viernes"]["mañana"] = {"criterio":"Nombre de los circuitos de Formula 1 ubicados en USA","funcion":fun.circuitos_USA} #BIEN
criteriosDataF["Sabado"]["mañana"] = {"criterio":"El nombre de los faraones con las 10 piramides mas altas.","funcion":fun.piramides_mas_altas} #bien
criteriosDataF["Domingo"]["mañana"] = {"criterio":"Marca de los autos rentados de tipo hibrido.","funcion":fun.renta_autos_hibridos}    #bien

criteriosDataF["Lunes"]["tarde"] = {"criterio":"Personas que estan dentro de la lista de Forbes y estudiaron en Harvar.","funcion":fun.forbes_en_Harvar}    #bien
criteriosDataF["Martes"]["tarde"] = {"criterio":"Nombres de las piramides de las 3° dinastia.","funcion":fun.piramides_3_dinastia}  #bien
criteriosDataF["Miercoles"]["tarde"] = {"criterio":"Nombre de los pilotos de Formula 1 de nacionalidad Española.","funcion":fun.pilotos_españoles}  #bien
criteriosDataF["Jueves"]["tarde"] = {"criterio":"Lista de jugadores argentinos que su pie habil es el izquierdo.","funcion":fun.jugadores_argentinos_zurdos}    #bien
criteriosDataF["Viernes"]["tarde"] = {"criterio":"Ciudades de USA donde se encuentran circuitos de Formula 1","funcion":fun.circuitos_USA2} #BIEN
criteriosDataF["Sabado"]["tarde"] = {"criterio":"Modelo de los vehiculos rentados de tipo electricos y suv.","funcion":fun.renta_autos_suv} #bien
criteriosDataF["Domingo"]["tarde"] = {"criterio":"Nombre de las aerolineas ubicadas en Estados Unidos que estan activas.","funcion":fun.airlines_USA}   #bien

