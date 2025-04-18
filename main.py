alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
morse_code = ['▄ ▄▄▄', '▄▄▄ ▄ ▄ ▄', '▄▄▄ ▄ ▄▄▄ ▄', '▄▄▄ ▄ ▄', '▄', '▄ ▄ ▄▄▄ ▄', '▄▄▄ ▄▄▄ ▄', '▄ ▄ ▄ ▄', '▄ ▄',
              '▄ ▄▄▄ ▄▄▄ ▄▄▄', '▄▄▄ ▄ ▄▄▄', '▄ ▄▄▄ ▄ ▄', '▄▄▄ ▄▄▄', '▄▄▄ ▄', '▄▄▄ ▄▄▄ ▄▄▄', '▄ ▄▄▄ ▄▄▄ ▄',
              '▄▄▄ ▄▄▄ ▄ ▄▄▄', '▄ ▄▄▄ ▄', '▄ ▄ ▄', '▄▄▄', '▄ ▄ ▄▄▄', '▄ ▄ ▄ ▄▄▄', '▄ ▄▄▄ ▄▄▄', '▄▄▄ ▄ ▄ ▄▄▄', '▄▄▄ ▄ ▄▄▄ ▄▄▄',
              '▄▄▄ ▄▄▄ ▄ ▄', '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄', '▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄', '▄ ▄ ▄ ▄▄▄ ▄▄▄', '▄ ▄ ▄ ▄ ▄▄▄', '▄ ▄ ▄ ▄ ▄',
              '▄▄▄ ▄ ▄ ▄ ▄', '▄▄▄ ▄▄▄ ▄ ▄ ▄', '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄', '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄', '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄']

active = True

while active:
    to_be_translated = input(
        'Welcome to the Morse translator! Please enter what you would like translated into Morse code: ').lower()

    morse_word = ''

    for letter in to_be_translated:
        if letter in alphabet:
            alphabet_index = alphabet.index(letter)
            morse_word += " " + morse_code[alphabet_index] + " "
        elif letter == ' ':
            morse_word += "       "

    print(f"{to_be_translated} translates to: {morse_word}")

    response = input("Would you like to translate another word or phrase? Y/N?").lower()
    if response == 'n':
        active = False
        print('Goodbye!')



