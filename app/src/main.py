import pygame
import renderer
import ctypes
from GameLogic import game

ctypes.windll.user32.SetProcessDPIAware()

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

gameState = game.Game()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Wordle Clone')

    running = True
    while running:
        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                running = False

        game.update(gameState, events)

        renderer.render(screen, gameState)


    pygame.quit()

if __name__ == '__main__':
    main()