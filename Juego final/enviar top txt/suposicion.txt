from time import sleep as t
import random as r
import cartas 
import hoja as h

#Funcion para suponer a partir de las cartas disponibles
def suposicion():
    sup = [] #lista de suposición
    while True: #iteración de personajes
        for i, p in enumerate(cartas.personajes, 1):
            print(f"({i}) {p}")
            t(0.2)
        op = input("Seleccione el personaje: ")
        if op.isdigit() and 1 <= int(op) <= len(cartas.personajes): # elección de opción
            personaje = cartas.personajes[int(op) - 1]
            print("Información guardada, sigamos...\n")
            sup.append(personaje)
            break
        else:
            print("No seleccionaste nada. ")
    while True: #iteración de armas
        for i, a in enumerate(cartas.armas, 1):
            print(f"({i}) {a}")
            t(0.2)
        op = input("Seleccione el arma: ")
        if op.isdigit() and 1 <= int(op) <= len(cartas.armas): # elección de opción
            arma = cartas.armas[int(op) - 1]
            print("Información guardada, sigamos...")
            sup.append(arma)
            break
        else:
            print("No seleccionaste nada. ")
    while True: #iteración de lugares
        for i, l in enumerate(cartas.lugares, 1):
            print(f"({i}) {l}")
            t(0.2)
        op = input("Seleccione el lugar: ")
        if op.isdigit() and 1 <= int(op) <= len(cartas.lugares): # elección de opción
            lugar = cartas.lugares[int(op) - 1]
            print("Información guardada, sigamos...\n")
            sup.append(lugar)
            break
        else:
            print("No seleccionaste nada. ")
    return sup

#funcion para generar match entre suposicion y cartas distribuidas en jugador 1
def comparativajg1(jugador_2, sup):
    acierto = []
    for carta in sup: # itera las cartas con la suposicion del jugador
        if carta in jugador_2 :
            acierto.append(carta) #si cupmple lo guarda en una lista
    if acierto: #si acertamos dos cartas nos retorna una de las dos opciones
        carta_acertada = r.choice(acierto)
        print("Acertaste con al menos una carta")
        print(f"Te mostraré una al azar: {carta_acertada}")
    else:
        print("Mala suerte, no tienes ninguna carta en tu suposición")
    return acierto

#función que nos arroja un sub_menu que muestra la hoja para agregar información
def sub_menu1(sup, jugador_2, hoja):
    aciertos = comparativajg1(jugador_2, sup)
    if aciertos: # interactua con el menú de hoja para poder anexar información desde la suposición y gurdar.
        op = input("¿Desea marcar esta información en su hoja? \n 1) Sí \n 2) No: ")
        if op == "1":
            h.HOJA1(hoja)
        else:
            print("Saliendo al menú de juego...")
    else:
        print("No hubo aciertos, por tanto no se mostrará la hoja.")

'''Aquí funciona de la misma manera para jugador 1, pero esta parte esta enfocada en el jugador 2 para el modo de dos jugadores'''
#funcion para generar match entre suposicion y cartas distribuidas en jugador 2
def comparativajg2(jugador_1, sup):
    acierto = []
    for carta in sup:
        if carta in jugador_1 :
            acierto.append(carta)
    if acierto:
        carta_acertada = r.choice(acierto)
        print("Acertaste con al menos una carta")
        print(f"Te mostraré una al azar: {carta_acertada}")
    else:
        print("Mala suerte, no tienes ninguna carta en tu suposición")
    return acierto

#función que nos arroja un sub_menu que muestra la hoja para agregar información
def sub_menu2(sup, jugador_1, hoja):
    aciertos = comparativajg2(jugador_1, sup)
    
    if aciertos:
        op = input("¿Desea marcar esta información en su hoja? \n 1) Sí \n 2) No: ")
        if op == "1":
            h.HOJA2(hoja)
        else:
            print("Saliendo al menú de juego...")
    else:
        print("No hubo aciertos, por tanto no se mostrará la hoja.")