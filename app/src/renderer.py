import pygame
from UI import colours, navbar, game_window, keyboard
from GameLogic.game import Game

def render(screen: pygame.Surface, game_state: Game):
    screen.fill(colours.WHITE)

    navbar.render(screen)
    game_window.render(screen, game_state)
    keyboard.render(screen, game_state)

    pygame.display.flip()