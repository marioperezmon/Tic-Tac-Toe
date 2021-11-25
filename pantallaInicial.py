#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from Boton import boton
from time import sleep

def reset():
    import os
    import sys
    os.execl(sys.executable, sys.executable, *sys.argv)

# elegir el modo de juego
def menuInicial():

    pygame.init()

    # Fondo y colores de la pantalla
    bg          = (240, 240, 240)
    rojo        = (212, 30, 30)
    rojoClaro   = (255, 64, 64)
    azul        = (21, 188, 235)
    negro       = (0, 0, 0)
    blanco      = (255, 255, 255)
    dorado      = (168, 151, 50)
    doradoClaro = (224, 206, 99)

    txtTitulo = "Tres en Raya"
    txtModos = "Modos de Juego:"
    txtModo1 = "1 vs 1"
    txtModo2 = "1 vs PC"

    pygame.display.set_caption(txtTitulo)
    size = width, height = 500, 400
    screen = pygame.display.set_mode(size)

    screen.fill(blanco)

    btModo1 = boton(rojo  , 210, (height // 2) - 40, 70, 40, txtModo1)
    btModo2 = boton(rojo  , 210, (height // 2) + 15, 70, 40, txtModo2)
    btSalir = boton(dorado, 210, (height // 2) + 100, 70, 40, 'SALIR')

    modo = {}
    modo[0] = "1 VS 1"
    modo[1] = "1 VS PC"
    modoSeleccionado = False

    while not modoSeleccionado:

        screen.fill(blanco)

        # Render de los botones
        btSalir.draw(screen)
        btModo1.draw(screen)
        btModo2.draw(screen)

        font = pygame.font.Font('freesansbold.ttf', 25)

        # Mostrar TITULO
        text = font.render(txtTitulo, True, rojo, bg)
        textRect = text.get_rect()
        textRect.center = (width // 2, (height // 6))
        screen.blit(text, textRect)

        # Mostrar MODOS
        text = font.render(txtModos, True, rojo, bg)
        textRect = text.get_rect()
        textRect.center = (width // 2, (height // 6) + 40)
        screen.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Si se clica en "SALIR"
                if btSalir.mouseIsOver(mousePos):
                    sleep(1)
                    quit()

                # Si se clica en "1 VS 1"
                if btModo1.mouseIsOver(mousePos):
                    modo_jugar_int = 0
                    # print("Modo " + modo[modo_jugar_int] + " seleccionado")
                    return modo[modo_jugar_int]

                # Si se clica en "1 VS PC"
                elif btModo2.mouseIsOver(mousePos):
                    modo_jugar_int = 1
                    # print("Modo " + modo[modo_jugar_int] + " seleccionado")
                    return modo[modo_jugar_int]

            if btModo1.mouseIsOver(mousePos):
                btModo1.color = rojoClaro
            else:
                btModo1.color = rojo

            if btModo2.mouseIsOver(mousePos):
                btModo2.color = rojoClaro
            else:
                btModo2.color = rojo

            if btSalir.mouseIsOver(mousePos):
                btSalir.color = doradoClaro
            else:
                btSalir.color = dorado

        pygame.display.update()

