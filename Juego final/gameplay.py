from time import sleep as t
import suposicion as s
import acusacion as a
import hoja as h
import cartas
from PC import turnopc as pc 
import PC



#Funcion para jugar en 2 jugadores
def gameplayjugador():
    t(2)
    hoja_j1 = h.generar_hoja() #genera una nueva hoja durante el juego para cada jugador
    hoja_j2 = h.generar_hoja()
    
    print("Entrando...")
    
    juego = cartas.distribucion_sobre() 
    jugador_1 = juego["jugador1"] #generamos las cartas para cada jugador
    jugador_2 = juego["jugador2"]

    turno = 1 #turno de jugador, modo dos jugadores
    
    while True:
        print(f"\n Turno del jugador {turno}") #turno en juego
        
        if turno == 1: #aquí por cada jugador se mostraran las cartas de su mazo por turno
            print(f"Tienes las siguientes cartas en tu mazo:\n{jugador_1}")
        else:
            print(f"Tienes las siguientes cartas en tu mazo:\n{jugador_2}")
        
        op = input("\n 1)Hacer suposición.\n 2)Hacer acusación.\n 3)Ver hoja. \n 4)Finalizar Turno \n 5)Salir al menú principal: ") #opciones
        
        pass
        if op == "1": #itera todo el modulo de suposición por turno de jugador
            sup = s.suposicion()
            if turno == 1:
                s.sub_menu1(sup, jugador_2, hoja_j1)
            else:
                s.sub_menu2(sup, jugador_1, hoja_j2)
        elif op =="2": #itera todo el modulo de acusación por turno de jugador
            resultado = a.gana_pierde(juego["sobre"])
            print(resultado)
            break
        elif op =="3": #itera todo el modulo de hoja para cada jugador por turno
            if turno == 1:
                h.HOJA1(hoja_j1)
            else:
                h.HOJA2(hoja_j2)
        elif op == "4": #cambio de turno
            t(1)
            print("Estamos cambiando de turno")
            turno = 2 if turno ==1 else 1
        elif op =="5":
            t(0.5)
            print("Saliendo al menú principal..")
            break
        else:
            t(2)
            print("Parece que no has elegido bien. Intentemos nuevamente...")


'''ESTA FUNCIONA ITERA EL MODULO PC Y SOLO SE UTILIZA AL JUGADOR 1 PARA JUGAR'''
def gameplaypc():
    t(2)

    print("Entrando...")

    hoja_j1 = h.generar_hoja()
    
    juego = cartas.distribucion_sobre()
    jugador_1 = juego["jugador1"]
    jugador_2 = juego["jugador2"]
    var=1 #Número de turnos jugados

    print(f"Tienes las siguientes cartas en tu mazo:\n{jugador_1}")

    while True:
        op = input("\n 1)Hacer suposición.\n 2)Hacer acusación.\n 3)Ver hoja. \n 4)Finalizar Turno \n 5)Salir al menú principal: ")
        if op == "1":
            sup = s.suposicion()
            s.sub_menu1(sup, jugador_2, hoja_j1)
        elif op =="2":
            resultado = a.gana_pierde(juego["sobre"])
            print(resultado)
            break
        elif op =="3":
            h.HOJA1(hoja_j1)
        elif op == "4":            
            PC.turnopc(var)
            if  PC.final() == True:
                break
            else:
                var+=1 #suma de turnos
                pass
        elif op =="5":
            t(0.5)
            print("Saliendo al menú principal..")
            break
        else:
            t(2)
            print("Parece que no has elegido bien. Intentemos nuevamente...")