import pygame
from GameLogic.game import Game

import colours
from UI import game_window

def render(screen: pygame.Surface, gameState: Game):
    screen.fill(colours.WHITE)

    game_window.render(screen, gameState)

    pygame.display.flip()