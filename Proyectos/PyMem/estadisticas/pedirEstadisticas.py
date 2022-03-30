import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

def buscar_archivo():
    """

    Busca la el archivo requerido y devuelve la ruta al archivo.
    """
    try:
        pathFile = os.path.join(os.getcwd(),"registroJugadas.csv")
        return pathFile
    except FileNotFoundError:
        print("Archivo no encontrado !")
        return ""
        

def pedir_top_10():
    """ 
    
    Busca el TOP 10 de las palabras que se encuientran primero en todas las partidas dentro del dataframe y muestra los datos en un grafico de torta.
    """

    df = pd.read_csv(buscar_archivo())

    df["Estado"].fillna("sin datos",inplace=True)

    df_ok = df[df["Estado"] == "ok"].groupby(["Partida"])["Palabra"].first().value_counts().head(10).plot(kind="pie",startangle=90)

    plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5), ncol=1)

    print(df_ok)

    plt.show()


def pedir_datos_por_estado():
    """ 
    
    Abre el dataframe, busca el procentaje de partidas por estado y muestra los datos en un grafico de torta.
    """
    
    df = pd.read_csv(buscar_archivo())

    df["Estado"].fillna("sin datos",inplace=True)

    df = (df[df["Nombre de evento"] == "Fin" ].groupby(["Estado"])["Estado"].count() * 100) / df[df["Nombre de evento"] == "Fin"].groupby(["Estado"])["Estado"].value_counts().sum()  
    dfGrafico = df.plot(kind="pie", legend=True,autopct='%1.1f%%') 

    print(df)

    plt.show()

def pedir_datos_por_genero():
    """ 
    
    Abre el dataframe, busca el procentaje de partidas finalizadas por genero y muestra los datos en un grafico de torta.
    """

    df = pd.read_csv(buscar_archivo())

    df["Estado"].fillna("sin datos",inplace=True)

    df = (df[df["Estado"] == "Finalizada"].groupby(["Usuarie -genero"])["Usuarie -genero"].count() * 100) / df[df["Estado"] == "Finalizada"].groupby(["Usuarie -genero"])["Usuarie -genero"].value_counts().sum() 
    
    dfGrafico = df.plot(kind="pie",autopct='%1.1f%%',shadow= True,labeldistance=1.4)
    
    print(df)                      

    plt.legend(loc= "center right",bbox_to_anchor=(1.30, 0.8))

    plt.show()


def pedir_datos_por_dia_de_semana():
    """ 
    
    Abre el dataframe, busca el procentaje de partidas finalizadas por genero y muestra los datos en un grafico de torta.
    """

    df = pd.read_csv(buscar_archivo())

    df = df[df["Nombre de evento"] == "Inicio Partida"]["Tiempo"].sort_index()


    df = ((df.apply(lambda x:datetime.fromtimestamp(x).weekday()).value_counts()*100) / df.apply(lambda x:datetime.fromtimestamp(x).weekday()).count()).sort_index()

    dfGrafico = df.plot(kind="pie",autopct='%1.1f%%')

    print(df)

    plt.legend(fontsize = 7, loc = (0, 1))

    plt.show()