#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Define una serie de variables y funciones para jugar una partida
    El metodo principal es empezarPartida, que es llamado por el script main
'''

# POSIBLES MEJORAS:
#     Rehacer la forma en de compruebar el ganador
#     Rehacer la forma en la que el PC calcula su jugada (p. ej. comprobar si alguien tiene la victoria a 1 movimiento)
#     En el modo VS PC, comprobar si jug1 ha ganado para que PC ya no haga su movimiento
# PENDIENTE: Cambiar boton "REINICIAR" por "JUGAR DE NUEVO" ?
# TODO -> distribuir mejor en funciones diferenciadas la funcion empezarPartida()

from somelib import *

import Resources.Colours as col
from Resources.Boton import c_boton as boton

from main import reset

import pygame

# Funcion que calcula la jugada que hara el PC
def pc_calculaJugada(copiaEstado):
    # print("PC calculando jugada...")

    # Busca una celda vacia
    x = np.random.randint(0, 3)
    y = np.random.randint(0, 3)
    # print("Busca celda: [" + str(x) + ", " + str(y) + "] = " + str(copiaEstado[x, y]))

    # Mientras no encuentre una celda vacia
    while copiaEstado[x, y] == 1:
        # print("Busca celda: [" + str(x) + ", " + str(y) + "] = " + str(copiaEstado[x, y]))

        # Sigue buscando
        x = np.random.randint(0, 3)
        y = np.random.randint(0, 3)

    # print("Celda random selecionada = [" + str(x) + ", " + str(y) + "]")
    return x, y

# Recibe las jugadas de ambos jugadores y comprueba si hay un ganador
def checkWinner(jugadasJ1, jugadasJ2):

    ganador = ""

    movimientosJ1 = jugadasJ1.split(" ")
    movimientosJ2 = jugadasJ2.split(" ")

    #print("cWinner - j1 = ", movimientosJ1)
    #print("cWinner - j2 = ", movimientosJ2)

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

# Metodo principal (comienza una nueva partida en el modo indicado por parametro)
def empezarPartida(modo):
    
    print("comenzando una partida desde el script tresEnRaya.py. Modo = " + modo)

    pygame.init()

    pygame.display.set_caption('Tres en Raya - ' + modo)

    screen = pygame.display.set_mode(size)

    font = pygame.font.Font('freesansbold.ttf', 18)

    screen.fill(bg)

    btReiniciar = boton(col.dorado, 170, 305, 80, 40, 'Reiniciar', fontSize=15)
    btSalir     = boton(col.rojo, 250, 305, 40, 40, 'X', fontSize=15)

    # Estado inicial de la partida (valor de cada celda: 0 -> no hay ficha , 1 -> hay ficha)
    estado = np.zeros((nXc, nYc))

    global turnoJ1, jugadasJ1, jugadasJ2

    # Se muestra un boton "INICIAR"
    # PENDIENTE ??

    while True:

        # Guarda una copia del estado de la partida
        copiaEstado = np.copy(estado)

        screen.fill(bg)

        # Muestra los botones
        btReiniciar.draw(screen)
        btSalir.draw(screen)

        # Comprueba si hay ganador/empate
        ganador = checkWinner(jugadasJ1, jugadasJ2)

        '''
            SE COMPRUEBA SI TERMINO O NO LA PARTIDA Y SI HUBO UN EMPATE/GANADOR
        '''

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

            # Si hay un clic
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

            # si termino la partida, el bucle continua pq podria darle a "X" o a "Reiniciar"
            
            # si no termino la partida
            if not fin:

                # si se pulso el raton en 1 VS 1
                if modo == "1 VS 1" and sum(mouseclick) > 0:

                    # posicion del raton (en pixeles)
                    posX, posY = pygame.mouse.get_pos()

                    # calculo de celda
                    celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))

                    # Si clica dentro de el espacio de juego
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

                            # J1 clica una casilla y juega

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
                        celX, celY = pc_calculaJugada(copiaEstado)

                        # actualizar estado de la celda
                        copiaEstado[celX, celY] = 1

                        # Apunta la jugada y devuelve el turno al J1
                        jugadasJ2 += str(celX) + str(celY) + " "
                        turnoJ1 = True
        '''
            RENDER DEL TABLERO
        '''
 
        # Recorrer cada celda
        for x in range(0, nXc):
            for y in range(0, nYc):

                # Crear el poligono a mostrar
                poly = [((x)   * dimCH, (y)   * dimCW),
                        ((x+1) * dimCH, (y)   * dimCW),
                        ((x+1) * dimCH, (y+1) * dimCW),
                        ((x)   * dimCH, (y+1) * dimCW)]

                casilla = str(x) + str(y)

                if casilla in jugadasJ1:
                    # pygame.draw.polygon(screen, (232, 35, 35), poly, int(abs(1 - estado[x, y])))
                    # print(casilla, "la jugo j1")
                    pygame.draw.circle(screen,
                                    col.rojo,
                                    (int((x + 0.5) * dimCH),
                                        int((y + 0.5) * dimCW)),
                                        int(dimCH/2.2),
                                        int(abs(1 - estado[x, y])))

                    pygame.draw.polygon(screen, col.negro, poly, 1)

                elif casilla in jugadasJ2:
                    # pygame.draw.polygon(screen, (21, 188, 235), poly, int(abs(1 - estado[x, y])))
                    # print(casilla, "la jugo j2")
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

                else: # Si la casilla aun no la pulso nadie, se muestra vacia
                    pygame.draw.polygon(screen, col.negro, poly, int(abs(1 - estado[x, y])))

        # Cargar nuevo estado de la partida
        estado = copiaEstado

        pygame.display.flip()

#########################

# Variables necesarias para iniciar y jugar una partida

size = width, height = 300, 350
bg = (240, 240, 240)

# Numero de celdas (3x3) y dimensiones
nXc = 3
nYc = 3

dimCH = height / nXc
dimCW = width / nYc

# Variable para controlar si le toca al jug1 o no (inicialmente si)
turnoJ1 = True

# String para guardar las jugadas de cada jugador
jugadasJ1 = ""
jugadasJ2 = ""

# Inicialmente, se pone fin a false
fin = False

print("OJO!! Se han definido las variables basicas para iniciar una partida")

