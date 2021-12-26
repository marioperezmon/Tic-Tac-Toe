#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Define funciones para jugar una partida
    El metodo principal es empezarPartida, que es llamado por el script main
'''

# POSIBLES MEJORAS:
#     Rehacer la forma en que comprueba el ganador
#     Rehacer la forma en que el PC calcula su jugada (p. ej. comprobar si el jug1 tiene la victoria a 1 movimiento)
#     En el modo VS PC, comprobar si jug1 ha ganado para que PC ya no haga su movimiento

from somelib import *

import Resources.Colours as col
from Resources.Boton import c_boton as boton

from main import reset

import pygame


# comprueba el ganador
def checkWinner(jugadasJ1, jugadasJ2):

    ganador = ""
    fin = False
    empate = False

    # Comprobacion de forma simple
    movimientosJ1 = jugadasJ1.split(" ")
    movimientosJ2 = jugadasJ2.split(" ")

    # print ("j1 = ", movimientosJ1)
    # print ("j2 = ", movimientosJ2)

    # Comprobacion VERTICAL
    if "00" in movimientosJ1 and "01" in movimientosJ1 and "02" in movimientosJ1:
        ganador = "J1"
        fin = True
    elif "10" in movimientosJ1 and "11" in movimientosJ1 and "12" in movimientosJ1:
        ganador = "J1"
        fin = True
    elif "20" in movimientosJ1 and "21" in movimientosJ1 and "22" in movimientosJ1:
        ganador = "J1"
        fin = True
    elif "00" in movimientosJ2 and "01" in movimientosJ2 and "02" in movimientosJ2:
        ganador = "J2"
        fin = True
    elif "10" in movimientosJ2 and "11" in movimientosJ2 and "12" in movimientosJ2:
        ganador = "J2"
        fin = True
    elif "20" in movimientosJ2 and "21" in movimientosJ2 and "22" in movimientosJ2:
        ganador = "J2"
        fin = True
    else:

        # Comprobacion HORIZONTAL
        if "00" in movimientosJ1 and "10" in movimientosJ1 and "20" in movimientosJ1:
            ganador = "J1"
            fin = True
        elif "01" in movimientosJ1 and "11" in movimientosJ1 and "21" in movimientosJ1:
            ganador = "J1"
            fin = True
        elif "02" in movimientosJ1 and "12" in movimientosJ1 and "22" in movimientosJ1:
            ganador = "J1"
            fin = True
        elif "00" in movimientosJ2 and "10" in movimientosJ2 and "20" in movimientosJ2:
            ganador = "J2"
            fin = True
        elif "01" in movimientosJ2 and "11" in movimientosJ2 and "21" in movimientosJ2:
            ganador = "J2"
            fin = True
        elif "02" in movimientosJ2 and "12" in movimientosJ2 and "22" in movimientosJ2:
            ganador = "J2"
            fin = True
        else:

            # Comprobacion DIAGONAL
            if "00" in movimientosJ1 and "11" in movimientosJ1 and "22" in movimientosJ1:
                ganador = "J1"
                fin = True
            elif "20" in movimientosJ1 and "11" in movimientosJ1 and "02" in movimientosJ1:
                ganador = "J1"
                fin = True
            elif "00" in movimientosJ2 and "11" in movimientosJ2 and "22" in movimientosJ2:
                ganador = "J2"
                fin = True
            elif "20" in movimientosJ2 and "11" in movimientosJ2 and "02" in movimientosJ2:
                ganador = "J2"
                fin = True
            else:

                # Comprobacion EMPATE
                # Se resta un espacio en blanco al final
                numJugadasJ1 = len(movimientosJ1) - 1
                # Se resta un espacio en blanco al final
                numJugadasJ2 = len(movimientosJ2) - 1

                # Si no hay ganador y se realizaron 9 jugadas, hay empate
                if numJugadasJ1 + numJugadasJ2 == 9:
                    ganador = "EMPATE"
                    fin = True
                    empate = True

    return fin, ganador, empate

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

# Funcion que inicia una partida de 1 VS 1
def iniciaPartida1vs1():

    # Turnos jugadores (empieza el jugador 1)
    turnoJ1 = True

    # Jugadas de cada jugador
    jugadasJ1 = ""
    jugadasJ2 = ""

    # Estado (valores) inicial de la partida
    estado = np.zeros((nXc, nYc))  # configuracion vacia

    # Variable para controlar si la partida esta activa / terminada
    partidaActiva = True

    # Inicialmente, se pone fin a false
    fin = False

    # Se muestra un boton "INICIAR"
    # PENDIENTE

    return turnoJ1, jugadasJ1, jugadasJ2, estado, partidaActiva, fin

# Metodo principal (comienza una nueva partida en el modo indicado por parametro)
def empezarPartida(modo):
    
    print("comenzando una partida desde el script tresEnRaya.py. Modo = " + modo)

    pygame.init()

    pygame.display.set_caption('Tres en Raya - ' + modo)

    size = width, height
    screen = pygame.display.set_mode(size)

    bg = (240, 240, 240)
    screen.fill(bg)
    
    # Numero de celdas (3x3) y dimensiones
    nXc = 3
    nYc = 3

    dimCH = height / nXc
    dimCW = width  / nYc


    btReiniciar = boton(col.dorado, 170, 305, 80, 40, 'Reiniciar')
    btSalir     = boton(col.rojo, 250, 305, 40, 40, 'X')

    # Turnos jugadores
    turnoJ1, jugadasJ1, jugadasJ2, estado, partidaActiva, fin = iniciaPartida1vs1()

    while 1:

        # Copia el estado de la partida
        copiaEstado = np.copy(estado)

        # Rellenar la pantalla
        screen.fill(bg)

        # Muestra los botones de reiniciar y salir
        btReiniciar.draw(screen)
        btSalir.draw(screen)

        # Comprueba si la partida termino y si hay ganador
        fin, ganador, empate = checkWinner(jugadasJ1, jugadasJ2)

        # Si hubo empate, se muestra en el titulo
        if empate:
            txtEmpate = 'EMPATE'

            # Mostrar empate (TITULO)
            pygame.display.set_caption(txtEmpate)

            # Mostrar empate (PANTALLA)
            text = font.render(txtEmpate, True, col.dorado, bg)
            textRect = text.get_rect()
            textRect.center = (width // 3.7, 325)
            screen.blit(text, textRect)

        # Si no hubo empate, se muestran los turnos o el ganador
        else:
            font = pygame.font.Font('freesansbold.ttf', 18)

            if fin: # Si la partida llego al fin, se muestra el ganador

                # print("La partida llego al fin")

                if ganador == "J1":
                    txtGanador = "GANA JUG 1!!"
                    colorGanador = col.rojo

                elif ganador == "J2":
                    # Si se juega 1 VS PC
                    if modo == "1 VS PC":
                        txtGanador = "GANA PC!!"

                    else: # Si gana el J2 (PC)
                        txtGanador = "GANA JUG 2!!"

                    colorGanador = col.azul

                # Mostrar ganador (TITULO)
                pygame.display.set_caption(txtGanador)

                # Mostrar ganador (PANTALLA)
                text = font.render(txtGanador, True, colorGanador, bg)
                textRect = text.get_rect()
                textRect.center = (width // 3.7, 325)
                screen.blit(text, textRect)

                # PENDIENTE: Cambiar boton "REINICIAR" por "JUGAR DE NUEVO"

            else: # Si no llego al fin, se muestra el turno

                if turnoJ1:
                    txtTurno = "Turno: Jugador 1"
                    colorTurno = col.rojo

                else:
                    # Si se juega 1 VS PC
                    if modo == "1 VS PC":
                        txtTurno = "Turno: PC"

                    # Si se juega 1 VS 1
                    else:
                        txtTurno = "Turno: Jugador 2"

                    colorTurno = col.azul

                # Mostrar turno (PANTALLA - "Turno: Jugador 1/2/PC")
                text = font.render(txtTurno, True, colorTurno, bg)
                textRect = text.get_rect()
                textRect.center = (width // 3.7, 325)
                screen.blit(text, textRect)

        # Capturar eventos
        ev = pygame.event.get()

        # Si se juega 1 VS 1, el juego va por clicks de ambos jugadores
        if modo == "1 VS 1":

            # sin un for de control de eventos, falla al abrir pygame window
            for event in ev:
                if event.type == pygame.QUIT:
                    quit()

                mousePos = pygame.mouse.get_pos()

                # Si se pulsa la tecla 'r', se reincia la partida
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()

                    if key == 'r':
                        reset()

                # Si se clica el boton 'Reiniciar', se reincia la partida
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

                # Si se pulso el raton y la partida sigue activa
                if sum(mouseclick) > 0 and not fin and not empate:

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
                            # print("Se actualizo la casilla ", celX, celY, " con valor = ", copiaEstado[celX, celY])

                            # Apunta la jugada y pasa turno
                            if turnoJ1:
                                jugadasJ1 = jugadasJ1 + str(celX) + str(celY) + " "
                                turnoJ1 = False
                            else:
                                jugadasJ2 = jugadasJ2 + str(celX) + str(celY) + " "
                                turnoJ1 = True

        # Si se juega 1 VS PC
        else:

            # Si le toca al J1, se recogen los clicks
            if turnoJ1:

                # sin un for de control de eventos, falla al abrir pygame window
                for event in ev:
                    if event.type == pygame.QUIT:
                        quit()

                    mousePos = pygame.mouse.get_pos()

                    # Si se pulsa la tecla 'r', se reincia la partida
                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()

                        if key == 'r':
                            reset()

                    # Si se clica el boton 'Reiniciar', se reincia la partida
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

                    # Si se pulso el raton y la partida sigue activa
                    if sum(mouseclick) > 0 and not fin and not empate:

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
                                # print("Se actualizo la casilla ", celX, celY, " con valor = ", copiaEstado[celX, celY])

                                # Apunta la jugada de J1 y pasa turno
                                jugadasJ1 = jugadasJ1 + str(celX) + str(celY) + " "
                                turnoJ1 = False

            # Si le toca al PC, se calcula su jugada
            else:

                # PC calcula su jugada y juega
                celX, celY = pc_calculaJugada(copiaEstado)

                # actualizar estado de la celda
                copiaEstado[celX, celY] = 1

                # Apunta la jugada de J1 y pasa turno
                jugadasJ2 = jugadasJ2 + str(celX) + str(celY) + " "
                turnoJ1 = True

   
            #RENDER DEL TABLERO
 
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

