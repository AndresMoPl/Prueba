#Random

import random as R


asesinos=["Andres","Camilo","Tomas","David","Juan","Sofia"]
Armas=["Escopeta", "Espada", "Pistola", "Arco", "Cuchillo","Lanza","Granada"]
Lugares=["Lobby", "Sala", "Comedor", "Biblioteca", "Cocina","Juegos","Dormitorio","Jardin","Sotano",]

cartas=[]

ArmaA = R.choice(Armas)
Armas.remove(ArmaA)
AsesinoA = R.choice(asesinos)
asesinos.remove(AsesinoA)
LugaresA = R.choice(Lugares)
Lugares.remove(LugaresA)

cartas.append(asesinos)
cartas.append(Armas)
cartas.append(Lugares)

def prueba():
    Sobre=(ArmaA, AsesinoA, LugaresA)
    print(Sobre) 




def sobre(arma, asesino, lugares):
    Sobre=(ArmaA, AsesinoA, LugaresA)
    print(Sobre) 

    if ArmaA==arma and AsesinoA==asesino and LugaresA==lugares:
        print("!GANASTE!")
    else:
        print("PERDISTE")    


    return Sobre


shuffledC=[]
for x in cartas:
    for i in x:
        shuffledC.append(i)

R.shuffle(shuffledC)#Cartas revueltas


def CartasJugador():
    
    CartasJ=[]
    Card7=shuffledC[:7]
    CartasJ.append(Card7)

    print(CartasJ)#Cartas del jugador
    return CartasJ

def CartasPC():

    CartasPC=[]
    Card7=shuffledC[-7:]
    CartasPC.append(Card7)

    print(CartasPC)#Cartas del pc o jugador 2
    return CartasPC


def TurnoPC():
    print("Es el turno del rival !")
    print("Tu contrincante ha hecho una suposicion")











