from time import sleep as t
import gameplay as g


#Saludo
usuario = input("Hola, bienvenido.\n Para comenzar dime tu nombre: ")
t(1)
print(f"un gusto {usuario}, comencemos...")

# Funcion principal que define el modo de juego
def menu_inicial():
    t(3)
    #Texto de bienvenida e introducción del juego
    print(f"\n ===BIENVENIDO A CLUE THE GAME {usuario.upper()}====")
    print("")
    print("En un misterioso asesinato en la mansión Sánchez, el inspector de policía necesita tu ayuda para resolver el caso. \nLuego de estar en una reunión con diferentes personajes de la farándula San Bonaventuriana, \nen la mansión apareció asesinado el amo de  llaves. \nEn la reunión estaban presentes 6 invitad@s que incluyen al dueño de la mansión, el señor Sánchez. \nHay tres aspectos clave que debes determinar: quién cometió el asesinato, con qué arma y en qué lugar de la mansión. ")
    print("La mansión cuenta con un total de 9 lugares (cuartos, cocinas, baños, bibliotecas, e.t.c.) y en el momento del asesinato \nse han encontrado 7 posibles armas.")
    print("")
    print(f"Tu misión es encontrar al asesino, el arma que utilizó y el lugar exacto en donde se cometió el acto, para así, \nculminar con éxito la búsqueda y ganarte una condecoración por parte del inspector de policía.".upper())
    while True:
        #menú principal de modos de juegos
        print("Menú principal.")
        op = input("\n 1)Dos jugadores.\n 2)Jugar contra el PC.\n 3)Salir ")
        if op =="1":
            g.gameplayjugador() #modo dos jugadores
        elif op == "2":
            g.gameplaypc() #modo contra el pc
        elif op == "3":
            t(1)
            print(" ")
            print("Saliendo...")
            break
        else:
            t(1)
            print("Parece que no has elegido bien. Intentemos nuevamente...")
    t(1)
    print(f"Gracias por jugar {usuario}.")

#ejecucion del menú y gameplay en general
menu_inicial()



