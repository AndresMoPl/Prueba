from time import sleep as t
import cartas

'''El sistema de acusación funciona igual que suposicion de acuerdo al guardado de cartas'''
#Función para realizar la acusación
def acusacion():
    acus = [] # lista de acusación
    while True:
        for i, p in enumerate(cartas.personajes, 1):
            print(f"({i}) {p}")
            t(0.2)
        op = input("Seleccione el personaje: ")
        if op.isdigit() and 1 <= int(op) <= len(cartas.personajes): #elección de personajes
            personaje = cartas.personajes[int(op) - 1]
            print("Información guardada, sigamos...")
            acus.append(personaje)
            break
        else:
            print("No seleccionaste nada. ")
    while True:
        for i, a in enumerate(cartas.armas, 1):
            print(f"({i}) {a}")
            t(0.2)
        op = input("Seleccione el arma: ")
        if op.isdigit() and 1 <= int(op) <= len(cartas.armas):#elección de armas
            arma = cartas.armas[int(op) - 1]
            print("Información guardada, sigamos...")
            acus.append(arma)
            break
        else:
            print("No seleccionaste nada. ")
    while True:
        for i, l in enumerate(cartas.lugares, 1):
            print(f"({i}) {l}")
            t(0.2)
        op = input("Seleccione el lugar: ")
        if op.isdigit() and 1 <= int(op) <= len(cartas.lugares):#elección de lugares
            lugar = cartas.lugares[int(op) - 1]
            print("Información guardada, sigamos...")
            acus.append(lugar)
            break
        else:
            print("No seleccionaste nada. ")
    return acus


#funcion para comparar sobre con la acusacion
def gana_pierde(sobre):
    acus = acusacion() # arreglo para integrar la funcion acusacion()
    if acus == sobre: #si el jugador acierta el sobre ganara, de lo contrario pierde y se acaba el modo de juego
        return f"¡Felicidades, has ganando el sobre contenia {sobre} !"
    else:
        return f"Lo siento, has perdido tu acusación esta errada el sobre contenia {sobre}"

#con este arreglo evitamos que corra la funcion acusacion, a menos de que se llame
if __name__ == "__main__":
    juego = cartas.distribucion_sobre()
    gana_pierde(juego["sobre"])