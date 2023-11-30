import pygame
import renderer
from src.GameLogic import game

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

gameState = game.Game()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Würdle')

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