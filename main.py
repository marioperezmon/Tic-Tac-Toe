#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Autor : Mario Perez Montenegro
    Lanza el menu principal del Tres en raya, que permite iniciar una partida
'''

def interrupcion(sig, frame):
    salir = input("\n\n[?] CTRL+C detectado... ¿Quieres salir? (S/N)\n").lower()
    
    if salir == "s":
        print("\n[!] Saliendo...\n")
        sys.exit(1)
    else:
        print("\n[!] Continuando...\n")

def reset():
    os.execl(sys.executable, sys.executable, *sys.argv)

# Muestra el menu principal y devuelve el modo seleccionado
def mainMenu():

    pygame.init()

    txtTitulo = "Tres en Raya - Modo"
    pygame.display.set_caption(txtTitulo)

    size = width, height = 1280, 800
    screen = pygame.display.set_mode(size)

    screen.fill(col.blanco)

    font = pygame.font.Font('OwnFreeSansBold.ttf', 40)
    text = font.render(txtTitulo, True, col.rojo, col.blanco)
    textRect = text.get_rect()
    textRect.center = (width // 2, (height // 4))

    modos = {}
    modos[0] = "1 VS 1"
    modos[1] = "1 VS PC"

    width_bt = 170
    # posicion a lo ancho donde empiezan los botones
    pos_width_bt = width//2 - width_bt/2

    # tamanho y separacion a lo alto de cada boton
    height_bt = separacion_height = 50
    # posicion a lo alto donde empiezan los botones
    pos_height_bt = height/2 - (3*height_bt + 2*separacion_height) /2

    bt_modo1 = boton(col.rojo  , pos_width_bt, pos_height_bt+separacion_height*0, width_bt, height_bt, modos[0])
    bt_modo2 = boton(col.rojo  , pos_width_bt, pos_height_bt+separacion_height*2, width_bt, height_bt, modos[1])
    bt_salir = boton(col.dorado, pos_width_bt, pos_height_bt+separacion_height*4, width_bt, height_bt, 'SALIR')

    while True:

        screen.fill(col.blanco)

        # Muestra el titulo y los botones
        screen.blit(text, textRect)

        bt_modo1.draw(screen)
        bt_modo2.draw(screen)
        bt_salir.draw(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()

            mousePos = pygame.mouse.get_pos()

            # cuando haya un clic
            if event.type == pygame.MOUSEBUTTONDOWN:

                if bt_salir.mouseIsOver(mousePos):
                    sys.exit(0)

                # Modo "1 VS 1"
                if bt_modo1.mouseIsOver(mousePos):
                    return bt_modo1.text

                # Modo "1 VS PC"
                elif bt_modo2.mouseIsOver(mousePos):
                    return bt_modo2.text

            if bt_modo1.mouseIsOver(mousePos):
                bt_modo1.color = col.rojoClaro
            else:
                bt_modo1.color = col.rojo

            if bt_modo2.mouseIsOver(mousePos):
                bt_modo2.color = col.rojoClaro
            else:
                bt_modo2.color = col.rojo

            if bt_salir.mouseIsOver(mousePos):
                bt_salir.color = col.doradoClaro
            else:
                bt_salir.color = col.dorado

        pygame.display.update()

import os, sys, signal

if __name__ == "__main__":

    import Resources.Colours as col
    from Resources.Boton import c_boton as boton
    
    import pygame

    # Ctrl + C
    signal.signal(signal.SIGINT, interrupcion)

    # Funcion principal (muestra el menu y devuelve el modo seleccionado)
    modo = mainMenu()

    from partida import jugarPartida
    jugarPartida(modo)

