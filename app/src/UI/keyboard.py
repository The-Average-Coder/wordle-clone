import pygame
from UI import colours
from UI.Fonts import fonts
from GameLogic.game import Game
from GameLogic.word import Word

KEYBOARD_ELEMENT_HEIGHT = 60
KEYBOARD_ELEMENT_WIDTH = 45
KEYBOARD_SPECIAL_ELEMENT_WIDTH = 70
DEFAULT_LETTER_OFFSET = (16, 19)
LETTER_OFFSETS = {'I': (19, 19), 'J': (22, 18), 'M': (15, 18), 'W': (14, 19), 'ENTER': (16, 23), 'BACK': (18, 23)}

class KeyboardElement:
    def __init__(self, letter: str, colour: tuple, position: tuple, specialElement: bool = False):
        self.letter = letter
        self.colour = colour
        self.position = position
        self.specialElement = specialElement
    
    def render(self, screen: pygame.Surface):
        letter_offset = DEFAULT_LETTER_OFFSET if self.letter not in LETTER_OFFSETS else LETTER_OFFSETS[self.letter]
        if self.specialElement:
            pygame.draw.rect(screen, self.colour, pygame.Rect(self.position, (KEYBOARD_SPECIAL_ELEMENT_WIDTH, KEYBOARD_ELEMENT_HEIGHT)), border_radius=4)
            screen.blit(fonts.special_keyboard_font.render(self.letter, True, colours.BLACK),
                        (self.position[0] + letter_offset[0], self.position[1] + letter_offset[1]))
        else:
            pygame.draw.rect(screen, self.colour, pygame.Rect(self.position, (KEYBOARD_ELEMENT_WIDTH, KEYBOARD_ELEMENT_HEIGHT)), border_radius=4)
            screen.blit(fonts.keyboard_font.render(self.letter, True, colours.BLACK if self.colour == colours.LIGHT_GREY else colours.WHITE),
                        (self.position[0] + letter_offset[0], self.position[1] + letter_offset[1]))


QWERTY_LETTERS = 'qwertyuiopasdfghjklzxcvbnm'.upper()

keyboard_offset = (555, 600)
keyboard_element_positions = [(0, 0), (50, 0), (100, 0), (150, 0), (200, 0), (250, 0), (300, 0), (350, 0), (400, 0), (450, 0),
                              (25, 70), (75, 70), (125, 70), (175, 70), (225, 70), (275, 70), (325, 70), (375, 70), (425, 70),
                              (75, 140), (125, 140), (175, 140), (225, 140), (275, 140), (325, 140), (375, 140)]
keyboard_elements = [KeyboardElement(QWERTY_LETTERS[i], colours.LIGHT_GREY, (keyboard_offset[0] + position[0], keyboard_offset[1] + position[1]))
                     for i,position in enumerate(keyboard_element_positions)]
keyboard_elements.append(KeyboardElement('ENTER', colours.LIGHT_GREY, (keyboard_offset[0], keyboard_offset[1] + 140), True))
keyboard_elements.append(KeyboardElement('BACK', colours.LIGHT_GREY, (keyboard_offset[0] + 425, keyboard_offset[1] + 140), True))

def render(screen: pygame.Surface, game_state: Game):
    colour_priority = [colours.DARK_GREY, colours.YELLOW, colours.GREEN]
    letter_colours = {}
    
    for word in game_state.words:
        word_colours = word.colours
        for i, letter in enumerate(word.word):
            if letter in letter_colours:
                letter_colours[letter.upper()] = max(colour_priority.index(word_colours[i]), letter_colours[letter])
            else:
                letter_colours[letter.upper()] = colour_priority.index(word_colours[i])

    for i in keyboard_elements:
        if i.letter in letter_colours:
            i.colour = colour_priority[letter_colours[i.letter]]
        i.render(screen)
