import json
import os
import PySimpleGUI as sg
from manejadoresTablero import nivel1a3,nivel4y5
from play import menuTablero
from setting import pedirDatos, criterios,funcionesImagenes


def loop(user):
    """ 
    
    Manda el nivel del jugador actual y muestra el tablero de juego.

    :Parametro user: es un String.
    """

    lvl = pedirDatos.pedirLvl(user)
    lista_criterios = criterios.listaCriterios()   


    if lvl.endswith("1"):
        nivel1a3.play(user,lista_criterios[:4]) 
    elif lvl.endswith("2") :        
        nivel1a3.play(user,lista_criterios[:6])     
    elif lvl.endswith("3"):
        nivel1a3.play(user,lista_criterios[:8])
    elif lvl.endswith("4"):
        lista_criterios_img1 = funcionesImagenes.ropa_mujer()
        nivel4y5.play(user,lista_criterios_img1[:6])        
    else:
        lista_criterios_img2 = funcionesImagenes.pokemons()
        nivel4y5.play(user,lista_criterios_img2[:8])

