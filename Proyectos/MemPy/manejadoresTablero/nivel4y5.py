import PySimpleGUI as sg
import time as t
import random
from play import menuTablero
from setting import pedirDatos
from puntuacion import registrarPuntos
from estadisticas import registroJugadas


lista_comparo = [] #Lista para comparar parejas de palabras/imagenes.

combinaciones = [] #Lista con las palabras/imagenes ye encontradas.

puntuacion = 0

def evaluar():
    """ Evalua que los datos de la lista sean iguales (los datos son las palabras o nombre de las imagenes). """
    if lista_comparo[0][1] == lista_comparo[1][1]:
        return True

def comparar(window,event,lista,datosJ,tiempo):
    """ 
    
    Evalua que hallan apretado 2 botones y se fija si los datos de estos son iguales o diferentes.
    En el caso de ser iguales, suma la puntuacion, registra la jugada y verifica si hay mas convinaciones posibles, en caso que no halla retorna un True.
    En el caso de que sean distintas, muestra los 2 botones durante 1 segundo, registra la jugada y vuelve a ocultar los botones.
    En ambos casos al final limpia la lista de comparaciones.
    :Parametro window: tupla
    :Parametro event: String
    :Parametro lista: list
    :Parametro datosJ: dict
    :Parametro tiempo: float
    """
    global puntuacion
    if len(lista_comparo) == 2:
        datosJ["Tiempo"] = int(tiempo)
        datosJ["Palabra"] = lista_comparo[0][1]
        datosJ["Evento"] = "intento"
        window.refresh()
        if evaluar():
            puntuacion += 2
            combinaciones.append(lista_comparo[0][1])
            datosJ["Estado"] = "ok"
            registroJugadas.registrar_jugada(datosJ.values())
            print("-----------")
            print(puntuacion)
            print("-----------")
            if len(combinaciones) == (len(lista))/2: #Comparo si las palabras ya encontradas son la misma cantidad que las ingresadas en la lista
                sg.popup("GANASTE")
                lista_comparo.clear()
                combinaciones.clear()
                return True
            lista_comparo.clear()
        else:
            t.sleep(1)
            datosJ["Estado"] = "error"
            registroJugadas.registrar_jugada(datosJ.values())
            window[lista_comparo[0][0]].update(disabled=False)
            window[lista_comparo[1][0]].update(disabled=False)                 
            window[lista_comparo[0][0]].update(image_filename="",image_size=(93,80))
            window[lista_comparo[1][0]].update(image_filename="",image_size=(93,80))
            lista_comparo.clear()
            puntuacion -= 1


def play(user,list_criterios):
    """ 
    
    Inicializa la puntuacion en 0, completa los datos de las jugadas que no van a varirar durante la partida y genera el tablero de juego.
    Va a realizar las distintas acciones correspondientes a los distintos botones e ira registrando las distintas jugadas, a la vez mostrara un cronometro.
    :Parametro user: String
    :Parametro list_criterios: list
    """

    datosJugada = {
        "Tiempo":0,
        "Partida":0,
        "cantPalabras":0,
        "Evento":"",
        "Nick":"",
        "Genero":"",
        "Edad":0,
        "Estado":"",
        "Palabra":"",
        "Nivel":""
    }

    global puntuacion
    puntuacion = 0

    list_criterios.extend(list_criterios)
   
    random.shuffle(list_criterios)  

    print(len(list_criterios))


    ok = False

    tiempo = pedirDatos.pedirTiempo(user)

    tiempo = (tiempo[0] * 60) +  tiempo[1]

    lvl = pedirDatos.pedirLvl(user)
    color = pedirDatos.pedirColor(user)
    datosJugada["Nivel"] = lvl
    datosJugada["Nick"] = user
    datosJugada["Edad"] = pedirDatos.pedir_edad(user)
    datosJugada["Genero"] = pedirDatos.pedir_genero(user)
    datosJugada["Partida"] = pedirDatos.pedir_num_Partida()
    datosJugada["cantPalabras"] = pedirDatos.pedir_coincidencias(lvl)
    
    window = menuTablero.board(user,lvl,color)


    while True:

        
        event, value = window.read(timeout=10)


        if event ==  "start":
            star_time = t.time()
            current_time = t.time() - star_time
            ok = True
            datosJugada["Tiempo"] = int(star_time)
            datosJugada["Evento"] = "Inicio Partida"
            registroJugadas.registrar_jugada(datosJugada.values())            
            window["start"].update(disabled= True)

        if event == sg.WIN_CLOSED:
            datosJugada["Evento"] = "Fin"
            datosJugada["Estado"] = "abandonada"
            registroJugadas.registrar_jugada(datosJugada.values())   
            break
        

        if event.startswith("B"):

            if ok:
                img = list_criterios[int(event[1:])-1]
                window[event].update(image_filename=img,image_subsample=13)
                #window[event].update(palabras[botones.index(event)])
                window[event].update(disabled=True)
                lista_comparo.append((event,img[102:]))
                print(lista_comparo)

                if comparar(window,event,list_criterios,datosJugada,t.time()):
                    registrarPuntos.tabla_puntos(user,puntuacion)
                    datosJugada["Tiempo"] = int(t.time())
                    datosJugada["Evento"] = "Fin"
                    datosJugada["Estado"] = "Finalizada"
                    registroJugadas.registrar_jugada(datosJugada.values())
                    break
            else:
                sg.popup_no_buttons("Inicie el juego primero.",title="ATENCIÓN !!",auto_close=True,auto_close_duration=2,background_color="red")  

        if ok:
            current_time = t.time() - star_time

            window["-Timer-"].update(
                f"{round(current_time // 60):02d}:{round(current_time % 60):02d}"
            )

            if current_time >= tiempo:
                print("Termino el tiempo.")
                sg.popup("Se termino el tiempo !")
                datosJugada["Tiempo"] = int(t.time())
                datosJugada["Evento"] = "Fin"
                datosJugada["Estado"] = "timeout"
                registroJugadas.registrar_jugada(datosJugada.values())
                break




    window.close()