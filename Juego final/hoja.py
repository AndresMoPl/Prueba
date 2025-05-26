from cartas import personajes, armas, lugares

# funcion para crea una hoja por medio de las cartas
def generar_hoja():
    hoja = []
    hoja.append(["QUIEN?","//////////","//////////","//////////","//////////"]) #formatos de la hoja
    for p in personajes:
        hoja.append([p,"_","_","_","_"])
    hoja.append(["ARMAS?","//////////","//////////","//////////","//////////"])
    for a in armas:
        hoja.append([a,"_","_","_","_"])
    hoja.append(["LUGARES?","//////////","//////////","//////////","//////////"])
    for l in lugares:
        hoja.append([l,"_","_","_","_"])
    return hoja

# formatamos la hoja para que se pueda visualizar de la mejor manera
def mostrar_hoja(hoja):
    print(f"| {' ':<5} | {' ':<30} | {'C':<5} | {'L':<5} | {'U':<5} | {'E':<5}|")
    print("-"*73)
    print(f"| {' ':<5} | {'COLUMNA':<30} | {'1.':<5} | {'2.':<5} | {'3.':<5} | {'4.':<5}|")
    print("-"*73)
    for i, fila in enumerate(hoja): #itera todas las opciones de generado de hoja
        columna = "FILA" if i == '0' else f"{i})"
        print(f"| {columna:<5} | {fila[0]:<30} | {fila[1]:<5} | {fila[2]:<5} | {fila[3]:<5} | {fila[4]:<5}|")
        print("-"*73)

# Función para mostrar y modificar la hoja de jugador 1
def HOJA1(hoja):
    mostrar_hoja(hoja)
    
    while True:
        print("\n1) Marcar con X  2) Borrar marca  3) Salir")
        opcion = input("Selecciona tu movimiento: ")
        if opcion == '1' or opcion == '2':
            while True: #while para acceso de hoja y marcar en la hoja
                f = input("Fila (1-{}): ".format(len(hoja)-1))
                c = input("Columna (1-4): ")
                if f in ['0', len(personajes)+1, len(personajes)+len(armas)+2] or c < '1' or c > '4':
                    print("No puedes modificar títulos o fuera de rango.")
                else:
                    if opcion == '1':
                        hoja[int(f)][int(c)] = "X"
                    elif opcion == '2':
                        if hoja[int(f)][int(c)] == "X":
                            hoja[int(f)][int(c)] = "_"
                        else:
                            print("No hay una X para borrar.")
                    mostrar_hoja(hoja)
                    break
        elif opcion == '3':
            break
        else:
            print("Opción inválida.")

'''FUNCIONA EXACTAMENTE IGUAL A LA HOJA 1 PERO DEDICADA PARA EL JUGADOR 2'''
# Función para mostrar y modificar la hoja de jugador 2
def HOJA2(hoja):
    mostrar_hoja(hoja)

    while True:
        print("\n1) Marcar con X  2) Borrar marca  3) Salir")
        opcion = input("Selecciona tu movimiento: ")
        if opcion == '1' or opcion == '2':
            while True:#while para acceso de hoja y marcar en la hoja
                f = input("Fila (1-{}): ".format(len(hoja)-1))
                c = input("Columna (1-4): ")
                if f in ['0', len(personajes)+1, len(personajes)+len(armas)+2] or c < '1' or c > '4':
                    print("No puedes modificar títulos o fuera de rango.")
                else:
                    if opcion == '1':
                        hoja[int(f)][int(c)] = "X"
                    elif opcion == '2':
                        if hoja[int(f)][int(c)] == "X":
                            hoja[int(f)][int(c)] = "_"
                        else:
                            print("No hay una X para borrar.")
                    mostrar_hoja(hoja)
                    break
        elif opcion == '3':
            break
        else:
            print("Opción inválida.")
