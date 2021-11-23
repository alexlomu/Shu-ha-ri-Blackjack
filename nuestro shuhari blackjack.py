from random import choice, sample
#Creamos una diccionario asignandole a cada carta su valor
cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}
#Creamos la función del juego
def play():
    #Mostramos las cartas y las puntuaciones de cada una
    print("Cartas: {}".format(" ".join(cartas.keys())))
    print("Valor: {}".format(list(cartas.values())))

    print("Diseño de las cartas con sus valores")
    for carta, valor in cartas.items():
        print("La carta {} vale {}".format(carta, valor))

    #Creamos una lista con el diccionario de cartas
    lista_cartas = list(cartas)

    #Sacamos las dos primeras cartas del jugador, sumamos sus valores y le decimos su puntuacíon actual
    print("La banca le da dos cartas.")
    print("Sus cartas son:", end=" ")
    carta = choice(lista_cartas)
    puntuacion = cartas[carta]
    print(carta, end=" ")
    carta = choice(lista_cartas)
    puntuacion += cartas[carta]
    print(carta, end=" ")
    print(" >>> Su puntuacion es de", puntuacion)

    #En el caso de que el jugador quiera pedir más cartas sólo podrá ser mientras su puntuacíon sea inferior a 21
    plantarse = False
    while puntuacion < 21 and plantarse == False:
        pedir_carta = input("¿Desea pedir una carta? Responda si o no: ")
        pedir_carta = pedir_carta.lower()
        if pedir_carta == "si":
            carta = choice(lista_cartas)
            puntuacion += cartas[carta]
            print("Su nueva carta es:")
            print(carta, end=" ")
            print(" >>> Su nueva puntuación es de", puntuacion)
        elif pedir_carta == "no":
            print("Se ha plantado.")
            plantarse = True
        else:
            print("Introduzca una respuesta válida.")
    #Le damos dos cartas a la banca y mostramos su puntuación
    main_banca = sample(lista_cartas, 2)
    puntuacion_banca = sum(cartas[carta] for carta in main_banca)
    print("La banca muestra sus cartas.")
    print("La banca tiene: {} {} >> La puntuacion de la banca es {}".format(main_banca[0],
                                                            main_banca[1],
                                                            puntuacion_banca))
    #Los diferentes resultados de la partida dependiendo de la puntuacion
    if puntuacion > 21:
        print("Se ha pasado, gana la banca.")
    if puntuacion == puntuacion_banca:
        print("La banca y usted han empatado")
    if puntuacion < 21 and puntuacion < puntuacion_banca:
        print("Ha ganado la banca.")
    if puntuacion < 21 and puntuacion > puntuacion_banca:
        print("Ha ganado!!")
    if puntuacion == 21 and puntuacion_banca != 21:
        print("Felicidades ha hecho BLACKJACK!! Ha ganado!!")
    #Preguntamos si quiere volver a jugar
    volver_jugar = input("¿Quiere volver a jugar? Responda si o no: ")
    volver_jugar = volver_jugar.lower()
    if volver_jugar == "si":
        play()
    if volver_jugar == "no":
        print("Hasta la próxima!")
#Llamamos a la función para empezar a jugar
play()
