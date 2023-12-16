import string
import pygame
import random
from GameLogic import word

with open('GameLogic/words.txt') as file:
    legalWords = {i.strip() for i in file.readlines()}

with open('GameLogic/answers.txt') as file:
    answers = [i.strip() for i in file.readlines()]

class Game:
    def __init__(self, answer: str = '', words: list = None, currentWord: str = ''):
        self.answer = answer if answer != '' else self.generateAnswer()
        self.words = words if words != None else list()
        self.currentWord = currentWord
        self.complete = False if len(self.words) == 0 else (self.words[-1].word == self.answer)

    def generateAnswer(self) -> str:
        return random.choice(answers)

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
        if self.currentWord in legalWords:
            self.words.append(word.generateWord(self.currentWord, self.answer))
            self.complete = (self.words[-1].word == self.answer)
        self.clearCurrentWord()

def update(gameState: Game, events: list):
    if gameState.complete:
        return
    
    for i in events:
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_BACKSPACE:
                gameState.backspaceCurrentWord()
            elif i.key == pygame.K_RETURN:
                gameState.submitWord()
            elif pygame.key.name(i.key).lower() in string.ascii_lowercase:
                gameState.typeLetter(pygame.key.name(i.key).lower())