import PySimpleGUI as sg
import pandas as pd


def table(archivos):
    """ 
    
    Arma la ventana con las tablas de puntuacion para cada nivel de juego.
    :Parametro archivos: list
    """

    layout = []

    for a in archivos:
        df = pd.read_csv(a,encoding="utf-8")
        #df = pd.read_csv(a,header=None,encoding="utf-8")
        df = df.sort_values("Puntos",ascending=False)
        #header = df.iloc[0].tolist()
        header = df.columns.tolist()
        data = df.values.tolist()
    
        layout += [
            [sg.Text("Tabla Nivel " + str(archivos.index(a) + 1 ))],
            [sg.Table(
                values=data,
                headings=header,
                display_row_numbers=True,
                auto_size_columns=False,
                num_rows=min(25, len(data)))]
        ]

    window = sg.Window('Tabla de Puntos', layout, grab_anywhere=False,element_justification="center")

    return window