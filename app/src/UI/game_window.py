import pygame
from UI import colours
from UI.Fonts import fonts
from GameLogic.game import Game

DEFAULT_LETTER_OFFSET = (19, 18)
LETTER_OFFSETS = {'I': (24, 18), 'J': (22, 18), 'M': (15, 18), 'W': (14, 18)}

class LetterElement:
    def __init__(self, position: tuple, value: str, colour: tuple):
        self.position = position
        self.value = value
        self.colour = colour

    def render(self, screen: pygame.Surface):
        letter_offset = DEFAULT_LETTER_OFFSET if self.value not in LETTER_OFFSETS else LETTER_OFFSETS[self.value]
        if self.value == '':
            pygame.draw.rect(screen, self.colour, pygame.Rect(self.position, (60, 60)), 2)
        elif self.colour == colours.LIGHT_GREY:
            pygame.draw.rect(screen, colours.DARK_GREY, pygame.Rect(self.position, (60, 60)), 2)
            screen.blit(fonts.guess_font.render(self.value, True, colours.BLACK), (self.position[0] + letter_offset[0], self.position[1] + letter_offset[1]))
        else:
            pygame.draw.rect(screen, self.colour, pygame.Rect(self.position, (60, 60)))
            screen.blit(fonts.guess_font.render(self.value, True, colours.WHITE), (self.position[0] + letter_offset[0], self.position[1] + letter_offset[1]))

game_window_offset = (640, 140)
letter_element_positions = [(0, 0), (65, 0), (130, 0), (195, 0), (260, 0),
                      (0, 65), (65, 65), (130, 65), (195, 65), (260, 65),
                      (0, 130), (65, 130), (130, 130), (195, 130), (260, 130),
                      (0, 195), (65, 195), (130, 195), (195, 195), (260, 195),
                      (0, 260), (65, 260), (130, 260), (195, 260), (260, 260),
                      (0, 325), (65, 325), (130, 325), (195, 325), (260, 325)]
letter_elements = [LetterElement((game_window_offset[0] + i[0], game_window_offset[1] + i[1]), '', colours.LIGHT_GREY) for i in letter_element_positions]

def set_word(index: int, word: str, colours: list = [colours.LIGHT_GREY] * 5):
    if len(word) != 5:
        return
    for letter_index, letter in enumerate(word):
        set_letter(index, letter_index, letter, colours[letter_index])

def set_letter(word_index: int, letter_index: int, letter: str, colour: tuple = colours.LIGHT_GREY):
    letter_elements[word_index * 5 + letter_index].value = letter
    letter_elements[word_index * 5 + letter_index].colour = colour

def clear_word(index: int):
    for i in range(5):
        set_letter(index, i, '')

def render(screen: pygame.Surface, game_state: Game):
    for i,j in enumerate(game_state.words):
        set_word(i, j.word.upper(), j.colours)
    clear_word(len(game_state.words))
    for i,j in enumerate(game_state.current_word):
        set_letter(len(game_state.words), i, j.upper())
    for i in letter_elements:
        i.render(screen)