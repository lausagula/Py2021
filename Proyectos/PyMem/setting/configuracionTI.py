import PySimpleGUI as sg
import json


def configurar(datosUser):
    """ 
    
    Arma las 2 ventanas de configuracion, armando la segunda en base al nivel seleccionado en la primer ventana.
    Algunas opciones estan restringidas, dependiendo del nivel seleccionado.
    El boton de cambio de color muestra el color seleccionado en tiempo real.
    """
    configNivel = [
        [sg.Text("Configuracion basica del juego: ")],
        [sg.Text("Seleccione nivel de juego: ",),sg.Spin(values=("Nivel 1","Nivel 2","Nivel 3","Nivel 4","Nivel 5"), initial_value=datosUser["Configuracion"]["Nivel"],key="lvl")],
        [sg.Button("Ok",key="ok")]]


    configN = sg.Window("Configuracion",configNivel)
           

    while True:

        event, values = configN.read()

        if event == "ok":
            
            configN.close()
        
            if values["lvl"] in ("Nivel 1","Nivel 2"):              
                configResto = [[sg.Text("Seleccione nivel de juego: "),sg.Spin(values=(values["lvl"],"0"),key="lvl",disabled=True)],
                        [sg.Text("Coincidencias: "),sg.Spin(values=(2,0), initial_value="2",key="cantC",disabled=True)],
                        [sg.Text("Seleccione tipo de elementos: ")],
                        [sg.Checkbox("Solo palabras.",size=(20,1),default=True,key="elemPlabra",disabled=True),sg.Checkbox("Imagenes.",key="elemImagenes",disabled=True)],
                        [sg.Text("Tiempo de juego")],
                        [sg.Text("Minutos"),sg.Spin(values=[i for i in range(1,6)],initial_value=datosUser["Configuracion"]["Tiempo"][0],key="min"),sg.Text("Segundos"),sg.Spin(values=[i for i in range(00,60)],initial_value=datosUser["Configuracion"]["Tiempo"][1],key="seg")],
                        [sg.Text("Seleccione un color:")],
                        [sg.In(datosUser["Configuracion"]["Color"],visible=False,enable_events=True,key="aux"),
                        sg.ColorChooserButton("Cambiar",target="aux",key="color",button_color=(datosUser["Configuracion"]["Color"]))],                        
                        [sg.Button("Enviar",pad=((100,0),(30,0)),key="env")]]
                        
            
            elif values["lvl"] in ("Nivel 2","Nivel 3"):
                configResto = [[sg.Text("Seleccione nivel de juego: "),sg.Spin(values=(values["lvl"],"0"),key="lvl",disabled=True)],
                        [sg.Text("Coincidencias: "),sg.Spin(values=(2,0), initial_value="2",key="cantC",disabled=True)],
                        [sg.Text("Seleccione tipo de elementos: ")],
                        [sg.Checkbox("Solo palabras.",size=(20,1),default=True,key="elemPlabra",disabled=True),sg.Checkbox("Imagenes.",key="elemImagenes",disabled=True)],
                        [sg.Text("Tiempo de juego")],
                        [sg.Text("Minutos"),sg.Spin(values=[i for i in range(0,2)],initial_value=datosUser["Configuracion"]["Tiempo"][0],key="min"),sg.Text("Segundos"),sg.Spin(values=[i for i in range(00,60)],initial_value=datosUser["Configuracion"]["Tiempo"][1],key="seg")],
                        [sg.Text("Seleccione un color:")],
                        [sg.In(datosUser["Configuracion"]["Color"],visible=False,enable_events=True,key="aux"),
                        sg.ColorChooserButton("Cambiar",target="aux",key="color",button_color=(datosUser["Configuracion"]["Color"]))],                        
                        [sg.Button("Enviar",pad=((100,0),(30,0)),key="env")]]
                

            else:
                configResto = [[sg.Text("Seleccione nivel de juego: "),sg.Spin(values=(values["lvl"],"0"),key="lvl",disabled=True)],
                        [sg.Text("Coincidencias: "),sg.Spin(values=(3,0),initial_value="3",key="cantC",disabled=True)],
                        [sg.Text("Seleccione tipo de elementos: ")],
                        [sg.Checkbox("Solo palabras.",size=(20,1),key="elemPlabra",disabled=True),sg.Checkbox("Imagenes.",default=True,key="elemImagenes",disabled=True)],
                        [sg.Text("Tiempo de juego")],
                        [sg.Text("Minutos"),sg.Spin(values=[i for i in range(00,2)],initial_value=datosUser["Configuracion"]["Tiempo"][0],key="min"),sg.Text("Segundos"),sg.Spin(values=[i for i in range(00,60)],initial_value=datosUser["Configuracion"]["Tiempo"][1],key="seg")],
                        [sg.Text("Seleccione un color:")],
                        [sg.In(datosUser["Configuracion"]["Color"],visible=False,enable_events=True,key="aux"),
                        sg.ColorChooserButton("Cambiar",target="aux",key="color",button_color=(datosUser["Configuracion"]["Color"]))],                        
                        [sg.Button("Enviar",pad=((100,0),(30,0)),key="env")]]
                
                
                
            

            window = sg.Window("config",configResto)

            '''if event == "aux":
                    configResto["color"].Update(button_color= (values[event],values[event]))
'''
            

        if event == sg.WINDOW_CLOSED:
            break



        return window

