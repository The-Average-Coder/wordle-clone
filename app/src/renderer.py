import pygame
from UI import colours
from UI import game_window
from GameLogic.game import Game

def render(screen: pygame.Surface, gameState: Game):
    screen.fill(colours.WHITE)

    game_window.render(screen, gameState)

    pygame.display.flip()