import string

import pygame
from src import colours
from src.Fonts import fonts
from src.GameLogic.game import Game
from src.GameLogic.word import Word

LETTER_OFFSETS = {'I': (24, 18), 'J': (22, 18), 'M': (15, 18), 'W': (14, 18)}

class LetterBox:
    def __init__(self, position: tuple, value: str, colour: tuple):
        self.position = position
        self.value = value
        self.colour = colour

    def render(self, screen: pygame.Surface):
        letterOffset = (19, 18) if self.value not in LETTER_OFFSETS else LETTER_OFFSETS[self.value]
        if self.value == '':
            pygame.draw.rect(screen, self.colour, pygame.Rect(self.position, (60, 60)), 2)
        elif self.colour == colours.LIGHT_GREY:
            pygame.draw.rect(screen, colours.DARK_GREY, pygame.Rect(self.position, (60, 60)), 2)
            screen.blit(fonts.letterBoxFont.render(self.value, True, colours.BLACK), (self.position[0] + letterOffset[0], self.position[1] + letterOffset[1]))
        else:
            pygame.draw.rect(screen, self.colour, pygame.Rect(self.position, (60, 60)))
            screen.blit(fonts.letterBoxFont.render(self.value, True, colours.WHITE), (self.position[0] + letterOffset[0], self.position[1] + letterOffset[1]))

gameWindowOffset = (640, 100)
letterBoxPositions = [(0, 0), (65, 0), (130, 0), (195, 0), (260, 0),
                      (0, 65), (65, 65), (130, 65), (195, 65), (260, 65),
                      (0, 130), (65, 130), (130, 130), (195, 130), (260, 130),
                      (0, 195), (65, 195), (130, 195), (195, 195), (260, 195),
                      (0, 260), (65, 260), (130, 260), (195, 260), (260, 260),
                      (0, 325), (65, 325), (130, 325), (195, 325), (260, 325)]
letterBoxes = [LetterBox((gameWindowOffset[0] + i[0], gameWindowOffset[1] + i[1]), '', colours.LIGHT_GREY) for i in letterBoxPositions]

def setWord(index: int, word: str, colours: list = [colours.LIGHT_GREY] * 5):
    if len(word) != 5:
        return
    for letterIndex,letter in enumerate(word):
        setLetter(index, letterIndex, letter, colours[letterIndex])

def setLetter(wordIndex: int, letterIndex: int, letter: str, colour: tuple = colours.LIGHT_GREY):
    letterBoxes[wordIndex * 5 + letterIndex].value = letter
    letterBoxes[wordIndex * 5 + letterIndex].colour = colour

def clearWord(index: int):
    for i in range(5):
        setLetter(index, i, '')

def render(screen: pygame.Surface, gameState: Game):
    for i,j in enumerate(gameState.words):
        setWord(i, j.word.upper(), j.colours)
    clearWord(len(gameState.words))
    for i,j in enumerate(gameState.currentWord):
        setLetter(len(gameState.words), i, j.upper())
    for i in letterBoxes:
        i.render(screen)