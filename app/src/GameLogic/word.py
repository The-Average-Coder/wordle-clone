from UI import colours

class Word:
    def __init__(self, word: str, colours: list):
        self.word = word
        self.colours = colours

# Takes the submitted word + answer and returns a word object with all the letter colours
def generateWord(word: str, answer: str):
    letterList = [i for i in word]
    answerLetterList = [i for i in answer]
    colourList = [colours.DARK_GREY] * 5

    for i, (letter, answerLetter) in enumerate(zip(letterList, answerLetterList)):
        if letter == answerLetter:
            letterList[i] = ''
            answerLetterList[i] = ''
            colourList[i] = colours.GREEN
    for i, letter in enumerate(letterList):
        if letter == '':
            continue
        if letter in answerLetterList:
            answerLetterList.remove(letter)
            colourList[i] = colours.YELLOW

    return Word(word, colourList)