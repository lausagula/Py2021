import PySimpleGUI as sg



def board(user,lvl,color): 
    """ 
    
    Genera el tablero de juego dependiento del nivel de juego.
    :Parametro user: String
    :Parametro lvl: String
    :Parametro color: String
    """

    if lvl == "Nivel 1":
        layout = [
                [sg.Text("Usuario:"),sg.Text(user)],
                [sg.Text("Nivel: "),sg.Text(lvl)],
                [sg.Button("Comenzar",pad=((80,0),(0,0)),size=(8,2),key="start"),sg.Text(pad=((0,50),(30,0)),justification="center",size=(8,2),font=("Halvetica",20),key="-Timer-",background_color=color)],
                [sg.Button(size=(10,5),key="B1",image_size=(100,80)),sg.Button(size=(10,5),key="B2",image_size=(100,80))],
                [sg.Button(size=(10,5),key="B3",image_size=(100,80)),sg.Button(size=(10,5),key="B4",image_size=(100,80))],
                [sg.Button(size=(10,5),key="B5",image_size=(100,80)),sg.Button(size=(10,5),key="B6",image_size=(100,80))],
                [sg.Button(size=(10,5),key="B7",image_size=(100,80)),sg.Button(size=(10,5),key="B8",image_size=(100,80))]
            
            ]

    elif (lvl == "Nivel 2") or (lvl == "Nivel 4"):
        layout = [
            [sg.Text("Usuario:"),sg.Text(user)],
            [sg.Text("Nivel: "),sg.Text(lvl)],
            [sg.Button("Comenzar",pad=(80,0),size=(8,2),key="start"),sg.Text(pad=((0,50),(30,0)),size=(8,2),justification="center",font=("Halvetica",20),key="-Timer-",background_color=color)],
            [sg.Button(size=(10,5),key="B1",image_size=(100,80)),sg.Button(size=(10,5),key="B2",image_size=(100,80)),sg.Button(size=(10,5),key="B3",image_size=(100,80))],
            [sg.Button(size=(10,5),key="B4",image_size=(100,80)),sg.Button(size=(10,5),key="B5",image_size=(100,80)),sg.Button(size=(10,5),key="B6",image_size=(100,80))],
            [sg.Button(size=(10,5),key="B7",image_size=(100,80)),sg.Button(size=(10,5),key="B8",image_size=(100,80)),sg.Button(size=(10,5),key="B9",image_size=(100,80))],
            [sg.Button(size=(10,5),key="B10",image_size=(100,80)),sg.Button(size=(10,5),key="B11",image_size=(100,80)),sg.Button(size=(10,5),key="B12",image_size=(100,80))]
        ]
    
    else:
        layout = [
            [sg.Text("Usuario:"),sg.Text(user)],
            [sg.Text("Nivel: "),sg.Text(lvl)],
            [sg.Button("Comenzar",pad=(80,0),size=(8,2),key="start"),sg.Text(pad=((0,50),(30,0)),size=(8,2),justification="center",font=("Halvetica",20),key="-Timer-",background_color=color)],
            [sg.Button(size=(10,5),key="B1",image_size=(100,80)),sg.Button(size=(10,5),key="B2",image_size=(100,80)),sg.Button(size=(10,5),key="B3",image_size=(100,80)),sg.Button(size=(10,5),key="B4",image_size=(100,80))],
            [sg.Button(size=(10,5),key="B5",image_size=(100,80)),sg.Button(size=(10,5),key="B6",image_size=(100,80)),sg.Button(size=(10,5),key="B7",image_size=(100,80)),sg.Button(size=(10,5),key="B8",image_size=(100,80))],
            [sg.Button(size=(10,5),key="B9",image_size=(100,80)),sg.Button(size=(10,5),key="B10",image_size=(100,80)),sg.Button(size=(10,5),key="B11",image_size=(100,80)),sg.Button(size=(10,5),key="B12",image_size=(100,80))],
            [sg.Button(size=(10,5),key="B13",image_size=(100,80)),sg.Button(size=(10,5),key="B14",image_size=(100,80)),sg.Button(size=(10,5),key="B15",image_size=(100,80)),sg.Button(size=(10,5),key="B16",image_size=(100,80))]
        ]


    window = sg.Window("Tablero de juego",layout,element_justification="c",background_color=color)

    return window

