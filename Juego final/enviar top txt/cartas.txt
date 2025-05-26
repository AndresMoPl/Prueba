import random

#Listas de cartas
personajes = ["Sanchez", "Timoty", "Violet", "Miss jade", "Ágata", "Madame Marfil"]
armas =["Candelabro","Daga antigua","Estatua de Mármol","Cuerda de terciopelo","Veneno en copa","Bastón con empuñadura de oro", "Pistola de bolsillo"]
lugares = ["Biblioteca secreta","Sala de música","Invernadero","Comedor principal","Galería de arte","Cocina del servicio","Sala de armas","Despacho privado","Salón de baile"]

#funcion para crear la distribucion
def distribucion_sobre():
        asesino = random.choice(personajes)#definimos el asesino
        arma = random.choice(armas)#el arma
        lugar = random.choice(lugares)#El lugar
        sobre = (asesino,arma,lugar)#guardamos todas las 3 cartas del asesino

        cartas = [p for p in personajes if p != asesino] + \
                [a for a in armas if a != arma] + \
                [l for l in lugares if l != lugar]#creamos una lista combinada con todas las cartas omitiendo lo que hay en el sobre
        random.shuffle(cartas)#toma la secuencia y retorna la secuencia en desorden

        jugador_1 =cartas[:7] #primeras 7 cartas para el jugador 1
        jugador_2 =cartas[7:14] #de la septima a la 14 para el 2
        cartas_no_jugadas = cartas[14:] #no se tienen en cuenta, se reparten
        
        return {
                "sobre": sobre,
                "jugador1": jugador_1,
                "jugador2": jugador_2,
                "cartas_fuera": cartas_no_jugadas,
                "hojas": {"jugador1": [], "jugador2": []}
        }#generamos un diccionario con la clave de los terminos y valores con las funciones ya definidas

