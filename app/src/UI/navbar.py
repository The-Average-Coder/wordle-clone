import pygame
from UI import colours

NAVBAR_HEIGHT = 65

def render(screen: pygame.Surface):
    wordle_logo = pygame.image.load('UI/Images/WordleLogo.jpg')
    screen.blit(wordle_logo, ((screen.get_width() - wordle_logo.get_width()) / 2, 4))
    pygame.draw.line(screen, colours.LIGHT_GREY, (0,NAVBAR_HEIGHT), (screen.get_width(), NAVBAR_HEIGHT))