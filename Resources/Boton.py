#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Define la clase Boton usando pygame
'''

import Resources.Colours as col
import pygame

class c_boton():

    def __init__(self, color, x, y, widht, height, text='', accion=None, fontSize=30):
        self.color = color
        # Posicion del boton en la pantalla
        self.x = x
        self.y = y
        # Dimensiones
        self.widht = widht
        self.height = height
        self.text = text
        self.accion = accion
        self.fontSize = fontSize

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.widht, self.height), 0)

        # Si hay un texto para mostrar en el boton
        if self.text != '':
            font = pygame.font.Font('OwnFreeSansBold.ttf', self.fontSize)
            text = font.render(self.text, True, col.negro)
            screen.blit(text, (self.x + (self.widht/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    # Comprueba si el raton esta sobre el boton
    def mouseIsOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.widht:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

