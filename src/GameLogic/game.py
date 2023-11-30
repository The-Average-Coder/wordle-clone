import string
import pygame
from src.GameLogic import word

class Game:
    def __init__(self, answer: str = '', words: list = None, currentWord: str = ''):
        self.answer = answer if answer != '' else self.generateAnswer()
        self.words = words if words != None else list()
        self.currentWord = currentWord

    def generateAnswer(self) -> str:
        return 'hello'

    def clearCurrentWord(self):
        self.currentWord = ''

    def backspaceCurrentWord(self):
        if len(self.currentWord) > 0:
            self.currentWord = self.currentWord[0:-1]

    def typeLetter(self, letter: str):
        if len(letter) != 1:
            return
        if len(self.currentWord) >= 5:
            return
        self.currentWord += letter

    def submitWord(self):
        if len(self.currentWord) == 5:
            self.words.append(word.generateWord(self.currentWord, ''))
        self.clearCurrentWord()

def update(gameState: Game, events: list):
    for i in events:
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_BACKSPACE:
                gameState.backspaceCurrentWord()
            elif i.key == pygame.K_RETURN:
                gameState.submitWord()
            elif pygame.key.name(i.key).lower() in string.ascii_lowercase:
                gameState.typeLetter(pygame.key.name(i.key).lower())