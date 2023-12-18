import string
import pygame
import random
from GameLogic import word

with open('GameLogic/words.txt') as file:
    legalWords = {i.strip() for i in file.readlines()}

with open('GameLogic/answers.txt') as file:
    answers = [i.strip() for i in file.readlines()]

class Game:
    def __init__(self, answer: str = '', words: list = None, current_word: str = ''):
        self.answer = answer if answer != '' else self.generate_answer()
        self.words = words if words != None else list()
        self.current_word = current_word
        self.complete = False if len(self.words) == 0 else (self.words[-1].word == self.answer)

    def generate_answer(self) -> str:
        return random.choice(answers)

    def clear_current_word(self):
        self.current_word = ''

    def backspace_current_word(self):
        if len(self.current_word) > 0:
            self.current_word = self.current_word[0:-1]

    def type_letter(self, letter: str):
        if len(letter) != 1:
            return
        if len(self.current_word) >= 5:
            return
        self.current_word += letter

    def submit_word(self):
        if self.current_word in legalWords:
            self.words.append(word.generate_word_object(self.current_word, self.answer))
            self.complete = (self.words[-1].word == self.answer)
        self.clear_current_word()

def update(game_state: Game, events: list):
    if game_state.complete:
        return
    
    for i in events:
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_BACKSPACE:
                game_state.backspace_current_word()
            elif i.key == pygame.K_RETURN:
                game_state.submit_word()
            elif pygame.key.name(i.key).lower() in string.ascii_lowercase:
                game_state.type_letter(pygame.key.name(i.key).lower())