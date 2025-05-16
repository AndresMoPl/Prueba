#Tronco
import time as T
import HOJA 
import RandomB as R
import turtle



print(" --------------------",'\n',"--------CLUE--------",'\n',"--------------------")

T.sleep(2)

while True:
    Start=int(input("Bienvenido a Clue! Escriba (1) para comenzar: "))
    if Start==1:
        Usuario=input("Ingresa tu nombre: ")
        print('\n',"En la mansion Sánchez, ocurrio un misterioso asesinato, el inspector de",'\n',"policía necesita tu ayuda para resolver el caso. Luego de estar en",'\n',"una reunión con diferentes personajes de la farándula San-",'\n',"Bonaventuriana, en la mansión apareció asesinado el amo de llaves",'\n')
        print("Tu misión es encontrar al asesino, el arma que utilizó y el lugar",'\n',"exacto en donde se cometió el acto, para así, culminar con éxito la",'\n',"búsqueda y ganarte una condecoración por parte del inspector de policía.",'\n')
        print("(6 PERSONAJES     7 ARMAS     9 LUGARES)",'\n')
        print("1)JUGAR CONTRA EL PC     2)JUGAR CON OTRO JUGADOR",'\n')
        Gmode=int(input("Seleccion el modo de juego que quiera jugar: "))
        if Gmode==1:
            print('\n',"Estas son tus cartas!",'\n')
            print(R.CartasJugador(),'\n')
            while True:
                print("1) Acusacion \n 2)Suposicion \n 3)Hoja \n 4)Mis cartas")
                print(Usuario, "Es tu turno!", end='')
                Select=int(input(" Elije la opcion que desees: "))
                if Select==1:
                    print("Estas seguro que quieres acusar ? (SI TE EQUIVOCAS PERDERAS EL JUEGO!)")
                    Desicion=int(input("1)SI    2)NO       : "))
                    if Desicion==1:
                        R.prueba()
                        arma=input("Ingresa el nombre del arma(primera letra mayuscula): ")
                        asesino=input("Ingresa el nombre del asesino(primera letra mayuscula): ")
                        lugar=input("Ingresa el nombre del lugar(primera letra mayuscula): ")
                        R.sobre(arma, asesino, lugar)
                elif Select==2:
                    print("En la suposicion puedes adivinar que cartas tiene tu contrincante, escribe y se de dira si por lo menos acertaste una carta")
                    arma=input("Ingresa el nombre del arma(primera letra mayuscula): ")
                    asesino=input("Ingresa el nombre del asesino(primera letra mayuscula): ")
                    lugar=input("Ingresa el nombre del lugar(primera letra mayuscula): ")
                    
                elif Select==3:
                    HOJA.HOJA()
                elif Select==4:
                    R.CartasJugador()
                else:
                    print("La opcion no se encuentra disponible, intentalo de nuevo! ")
                    pass

        if Gmode==2:
            R.sobre()











    else:
        pass

    



    