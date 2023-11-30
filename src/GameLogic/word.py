import sys
sys.path.append('..')

import colours

class Word:
    def __init__(self, word: str, colours: list):
        self.word = word
        self.colours = colours

# Takes the submitted word + answer and returns a word object with all the letter colours
def generateWord(word: str, answer: str):
    return Word(word, [colours.YELLOW] * 5)