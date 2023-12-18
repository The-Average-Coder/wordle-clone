from UI import colours

class Word:
    def __init__(self, word: str, colours: list):
        self.word = word
        self.colours = colours

# Takes the submitted word + answer and returns a word object with all the letter colours
def generate_word_object(word: str, answer: str):
    guess_letters = [i for i in word]
    answer_letters = [i for i in answer]
    colour_list = [colours.DARK_GREY] * 5

    for i, (letter, answerLetter) in enumerate(zip(guess_letters, answer_letters)):
        if letter == answerLetter:
            guess_letters[i] = ''
            answer_letters[i] = ''
            colour_list[i] = colours.GREEN
    for i, letter in enumerate(guess_letters):
        if letter == '':
            continue
        if letter in answer_letters:
            answer_letters.remove(letter)
            colour_list[i] = colours.YELLOW

    return Word(word, colour_list)