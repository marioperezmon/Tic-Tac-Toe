#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Define una serie de variables y funciones para jugar una partida
    El metodo principal es jugarPartida, que es llamado por el script main
'''

# TODO
#     Rehacer la forma de comprobar el ganador
#     Rehacer la forma en la que el PC calcula su jugada (p. ej. comprobar si alguien tiene la victoria a 1 movimiento)

from somelib import *

import Resources.Colours as col
from Resources.Boton import c_boton as boton

from main import reset

import pygame

# Funcion que muestra las jugadas de ambos jugadores en el tablero
def renderTablero():

    global screen

    # Recorrer cada celda
    for x in range(0, nXc):
        for y in range(0, nYc):

            # Crear el poligono a mostrar (uno por cada casilla)
            poly = [((x)   * dimCH, (y)   * dimCW),
                    ((x+1) * dimCH, (y)   * dimCW),
                    ((x+1) * dimCH, (y+1) * dimCW),
                    ((x)   * dimCH, (y+1) * dimCW)]

            casilla = str(x) + str(y)

            # comprobar si la casilla fue jugada por algun jugador
            if casilla in jugadasJ1:

                # pygame.draw.polygon(screen, (232, 35, 35), poly, int(abs(1 - estado[x, y])))
                pygame.draw.circle(screen,
                                    col.rojo,
                                    (int((x + 0.5) * dimCH),
                                    int ((y + 0.5) * dimCW)),
                                    int(dimCH/2.2),
                                    int(abs(1 - estado[x, y])))

                pygame.draw.polygon(screen, col.negro, poly, 1)

            elif casilla in jugadasJ2:

                # pygame.draw.polygon(screen, (21, 188, 235), poly, int(abs(1 - estado[x, y])))
                pygame.draw.line(screen,
                                    col.azul,
                                    (int((x)     * dimCH), int((y)     * dimCW)),
                                    (int((x + 1) * dimCH), int((y + 1) * dimCW)),
                                    5)

                pygame.draw.line(screen,
                                    col.azul,
                                    (int((x) * dimCH), int((y + 1) * dimCW)),
                                    (int((x + 1) * dimCH), int((y) * dimCW)),
                                    5)

                pygame.draw.polygon(screen, col.negro, poly, 1)

            # Si la casilla no la jugo nadie, se muestra vacia
            else: 
                pygame.draw.polygon(screen, col.negro, poly, int(abs(1 - estado[x, y])))

# Funcion que calcula la siguiente jugada del PC
def pcCalculaJugada(copiaEstado):

    # Elige una celda al azar
    x = np.random.randint(0, 3)
    y = np.random.randint(0, 3)
    # print("Busca celda: [" + str(x) + ", " + str(y) + "] = " + str(copiaEstado[x, y]))

    # Mientras no elija una celda vacia
    while copiaEstado[x, y] == 1:
        # print("Busca celda: [" + str(x) + ", " + str(y) + "] = " + str(copiaEstado[x, y]))

        # Sigue buscando
        x = np.random.randint(0, 3)
        y = np.random.randint(0, 3)

    # print("Celda selecionada = [" + str(x) + ", " + str(y) + "]")
    return x, y

# Recibe las jugadas de ambos jugadores y comprueba si hay un ganador
def checkWinner(jugadasJ1, jugadasJ2):

    ganador = ""

    # si el J1 jugo menos de 3 veces, no hay ganador aun (el J1 juega primero)
    if len(jugadasJ1) < 9:
        return ganador

    movimientosJ1 = jugadasJ1.split(" ")
    movimientosJ2 = jugadasJ2.split(" ")

    #print("cWinner - j1 =", movimientosJ1, "| len =", len(jugadasJ1))
    #print("cWinner - j2 =", movimientosJ2, "| len =", len(jugadasJ2))

    # Comprobacion VERTICAL
    if "00" in movimientosJ1 and "01" in movimientosJ1 and "02" in movimientosJ1:
        ganador = "J1"
    elif "10" in movimientosJ1 and "11" in movimientosJ1 and "12" in movimientosJ1:
        ganador = "J1"
    elif "20" in movimientosJ1 and "21" in movimientosJ1 and "22" in movimientosJ1:
        ganador = "J1"
    elif "00" in movimientosJ2 and "01" in movimientosJ2 and "02" in movimientosJ2:
        ganador = "J2"
    elif "10" in movimientosJ2 and "11" in movimientosJ2 and "12" in movimientosJ2:
        ganador = "J2"
    elif "20" in movimientosJ2 and "21" in movimientosJ2 and "22" in movimientosJ2:
        ganador = "J2"
    else:

        # Comprobacion HORIZONTAL
        if "00" in movimientosJ1 and "10" in movimientosJ1 and "20" in movimientosJ1:
            ganador = "J1"
        elif "01" in movimientosJ1 and "11" in movimientosJ1 and "21" in movimientosJ1:
            ganador = "J1"
        elif "02" in movimientosJ1 and "12" in movimientosJ1 and "22" in movimientosJ1:
            ganador = "J1"
        elif "00" in movimientosJ2 and "10" in movimientosJ2 and "20" in movimientosJ2:
            ganador = "J2"
        elif "01" in movimientosJ2 and "11" in movimientosJ2 and "21" in movimientosJ2:
            ganador = "J2"
        elif "02" in movimientosJ2 and "12" in movimientosJ2 and "22" in movimientosJ2:
            ganador = "J2"
        else:

            # Comprobacion DIAGONAL
            if "00" in movimientosJ1 and "11" in movimientosJ1 and "22" in movimientosJ1:
                ganador = "J1"
            elif "20" in movimientosJ1 and "11" in movimientosJ1 and "02" in movimientosJ1:
                ganador = "J1"
            elif "00" in movimientosJ2 and "11" in movimientosJ2 and "22" in movimientosJ2:
                ganador = "J2"
            elif "20" in movimientosJ2 and "11" in movimientosJ2 and "02" in movimientosJ2:
                ganador = "J2"
            else:

                # Comprobacion EMPATE
                
                # Se resta un espacio en blanco al final de las jugadas de ambos
                numJugadasJ1 = len(movimientosJ1) - 1
                numJugadasJ2 = len(movimientosJ2) - 1

                # Si no hay ganador y se realizaron 9 jugadas, hay empate
                if numJugadasJ1 + numJugadasJ2 == 9:
                    ganador = "EMPATE"
                    
    return ganador

# Funcion que muestra si hay un ganador o a quien le toca el turno
def mostrarInfoTurno(modo):

    # Comprueba si hay un ganador/empate
    ganador = checkWinner(jugadasJ1, jugadasJ2)
    
    global fin
    fin = ganador != ""

    # Si termino la partida
    if fin:
            
        # con empate
        if ganador == "EMPATE":
            colorMostrado = col.dorado
            txtMostrado = ganador

        # sin empate, un ganador
        else:

            if ganador == "J1":
                colorMostrado = col.rojo
            else:
                colorMostrado = col.azul

                # si jugo vs pc, gano el pc, si no, gano el j2
                if modo == "1 VS PC":
                    ganador = "PC"
                
            txtMostrado = "GANA " + ganador + "!"
    
    # Si no termino la partida
    else:

        if turnoJ1:
            txtMostrado = "Turno - Jugador 1"
            colorMostrado = col.rojo

        else:

            if modo == "1 VS PC":
                txtMostrado = "Turno - PC"
            else:
                txtMostrado = "Turno - Jugador 2"

            colorMostrado = col.azul
    
    # Muestra la info en el titulo y en la pantalla
    pygame.display.set_caption(txtMostrado)

    text = font.render(txtMostrado, True, colorMostrado, bg)
    textRect = text.get_rect()
    textRect.center = (width // 3.7, 325)
    screen.blit(text, textRect)

# Metodo principal (comienza una nueva partida en el modo indicado)
def jugarPartida(modo):

    pygame.init()

    pygame.display.set_caption('Tres en Raya - ' + modo)

    screen.fill(bg)

    btReiniciar = boton(col.dorado, 170, 305, 80, 40, 'Reiniciar', fontSize=15)
    btSalir     = boton(col.rojo, 250, 305, 40, 40, 'X', fontSize=15)

    # estas variables se inicializan al importar el script, fuera de cualquier funcion
    global turnoJ1, jugadasJ1, jugadasJ2, estado

    while True:

        # Guarda una copia del estado de la partida
        copiaEstado = np.copy(estado)

        screen.fill(bg)

        # Muestra los botones
        btReiniciar.draw(screen)
        btSalir.draw(screen)

        '''
            SE MUESTRA SI TERMINO O NO LA PARTIDA Y SI HUBO UN EMPATE/GANADOR
        '''

        mostrarInfoTurno(modo)

        '''
            CONTROL DE EVENTOS (CLICKS O TECLAS) + ACTUALIZA LA COPIA DEL ESTADO CON LA NUEVA JUGADA HECHA
        '''

        # Capturar eventos
        ev = pygame.event.get()

        for event in ev:

            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                    quit()

            # Si se pulsa una tecla
            if event.type == pygame.KEYDOWN:

                key = pygame.key.get_pressed()

                if key == 'r': # TODO -> revisar pq no funciona esto...
                    reset()

            # Si hay un click
            if event.type == pygame.MOUSEBUTTONDOWN:

                if btReiniciar.mouseIsOver(mousePos):
                    reset()

                elif btSalir.mouseIsOver(mousePos):
                    quit()

            if btReiniciar.mouseIsOver(mousePos):
                btReiniciar.color = col.doradoClaro
            else:
                btReiniciar.color = col.dorado

            if btSalir.mouseIsOver(mousePos):
                btSalir.color = col.rojoClaro
            else:
                btSalir.color = col.rojo

            mouseclick = pygame.mouse.get_pressed()

            # si termino la partida, el bucle continua pq podria darle a "Reiniciar" o a "X"
            
            # si no termino la partida
            if not fin:

                # si se pulso el raton en 1 VS 1
                if modo == "1 VS 1" and sum(mouseclick) > 0:

                    # posicion del raton (en pixeles)
                    posX, posY = pygame.mouse.get_pos()

                    # calculo de celda
                    celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))

                    # Si clicka dentro de el espacio de juego
                    if posX < width and posY < 300:

                        # Si la celda no estaba ya "jugada" (elegida)
                        if copiaEstado[celX, celY] == 0:

                            # actualiza estado de la celda
                            copiaEstado[celX, celY] = 1
                            #print("Se actualizo la casilla ", celX, celY, " con valor = ", copiaEstado[celX, celY])

                            # Apunta la jugada y cambia el turno
                            if turnoJ1:
                                jugadasJ1 += str(celX) + str(celY) + " "
                                
                            else:
                                jugadasJ2 += str(celX) + str(celY) + " "
                            
                            turnoJ1 = not turnoJ1
                
                elif modo == "1 VS PC":

                    # Si le toca al J1 y se pulso el raton
                    if turnoJ1 and sum(mouseclick) > 0:

                            # J1 clicka una casilla y juega

                            # posicion del raton (en pixeles)
                            posX, posY = pygame.mouse.get_pos()

                            # calculo de celda
                            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))

                            # Si clicka dentro de el espacio de juego
                            if posX < width and posY < 300:

                                # Si la celda no estaba ya ocupada
                                if copiaEstado[celX, celY] == 0:
                                    # actualizar estado de la celda

                                    copiaEstado[celX, celY] = 1
                                    #print("Se actualizo la casilla ", celX, celY, " con valor = ", copiaEstado[celX, celY])

                                    # Apunta la jugada y devuelve el turno al PC
                                    jugadasJ1 += str(celX) + str(celY) + " "
                                    turnoJ1 = False

                    # Si le toca al PC
                    elif not turnoJ1:

                        # PC calcula su jugada y juega
                        celX, celY = pcCalculaJugada(copiaEstado)

                        # actualizar estado de la celda
                        copiaEstado[celX, celY] = 1

                        # Apunta la jugada y devuelve el turno al J1
                        jugadasJ2 += str(celX) + str(celY) + " "
                        turnoJ1 = True

        '''
            RENDER DEL TABLERO
        '''

        renderTablero()

        # Carga el nuevo estado de la partida
        estado = copiaEstado

        pygame.display.flip()

#########################

# Variables necesarias para iniciar y jugar una partida

width = 300
height_turno = 50
height = width + height_turno
size = width, height

screen = pygame.display.set_mode(size)
font = pygame.font.Font('OwnFreeSansBold.ttf', 18)

bg = (240, 240, 240)

# Numero de celdas (3x3) y dimensiones
nXc = nYc = 3
dimCH = dimCW = 300 / nXc

# Estado inicial de la partida (valor de cada celda: 0 -> no hay ficha , 1 -> hay ficha)
estado = np.zeros((nXc, nYc))

# Variable para controlar si le toca al jug1 o no (inicialmente si)
turnoJ1 = True

# String para guardar las jugadas de cada jugador
jugadasJ1 = ""
jugadasJ2 = ""

# Declaracion de la variable fin (Inicialmente a false)
#   FIN se define en cada iteracion en la funcion mostrarInfoTurno despues de comprobar si hay ganador
#   y se consulta en el bucle principal para ver si termino la partida y no permitir mas jugadas
fin = False

