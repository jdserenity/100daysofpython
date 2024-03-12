import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato = pandas.read_csv('./nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (i, row) in nato.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def input_word():
    while True:
        word = input('Input your word: ').lower()
        alphabet = [key.lower() for key in nato_dict.keys()]
        successful = True

        for letter in word:
            if letter not in alphabet:
                print('Sorry! Only letters in the alphabet please.')
                successful = False
                break

        if successful:
            return word


word = input_word()

word_list = [nato_dict[letter.upper()] for letter in word if letter.upper() in nato_dict]

print(word_list)

# word_phonetic = [nato_dict[letter] for letter in word]

# print(word_phonetic)
