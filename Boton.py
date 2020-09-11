import pygame

# Fondo y colores de la pantalla
negro = (0, 0, 0)

# Clase BOTON
class boton():
    def __init__(self, color, x, y, widht, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.widht, self.height), 0)

        # Si hay un texto para mostrar en el boton
        if self.text != '':
            font = pygame.font.Font('freesansbold.ttf', 15)
            text = font.render(self.text, True, negro)
            screen.blit(text, (self.x + (self.widht/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    # Funcion para controlar si el raton esta sobre el boton
    def mouseIsOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.widht:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False