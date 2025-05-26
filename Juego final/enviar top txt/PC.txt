import cartas as card
import time as t
import random as r

prueba = card.distribucion_sobre()
P1cards = prueba["jugador1"] 
Pccard = prueba["jugador2"]
OutCard = prueba["cartas_fuera"]
Win = prueba["sobre"]
moneda=[1,2] #probabilidades del 50%, para que la maquina acierte una suposición
suerte =[1,2,3] #pobabilidades de 66.6%, para que la maquina acierte en su acusación
findeljuego=False

#Funcion para que inicie la maquina(turno maquina)
def turnopc(var):
    findeljuego=False
    suerte =[1,2,3]
    print("Es el turno de tu contrincante!")      
    for i in "pensar":
        print('.',end='')
        t.sleep(1)

    if var==15: #la maquina hara suposición, hasta el turno numero 15, ya que para este turno entrara la acusación
        acusar = r.choice(suerte)
        print("\n Tu oponente decidio acusar! \n")
        if acusar in [1,2]:
            print("Tu contrincante a decidido acusar a ", Win)
            print("La respuesta es....")
            t.sleep(1)
            print("CORRECTA \n Haz perdido")
            findeljuego=True #el juego acabara una vez la acusación sea verdadera o incorrecta
        elif acusar==3:           
            print("Tu contrincante a decicido acusar a ",Pccard[0:3] )
            print("La respuesta es....")
            t.sleep(1)
            print("INCORRECTA \n HAS GANADO!")
            findeljuego=True #el juego acabara una vez la acusación sea verdadera o incorrecta  

    else:
        print("\n Tu oponente decidio suponer! \n")
        suerte = r.choice(moneda)
        if suerte==1:
            print("El contrincante encontro de tus cartas la carta:", r.choice(P1cards)) #La maquina podra suponer una de tus cartas
        else:
            print("El contrincante pregunto por la carta: ",r.choice(OutCard or Win),"la cual no se encuentra en tus cartas ni en las de el contrincante") #la maquina supone una carta de las que no se encuentran en ninguna de las barajas

def final():
    return findeljuego

