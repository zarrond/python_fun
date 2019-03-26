CODE = {'a': '.-',     'b': '-...',   'c': '-.-.',
        'd': '-..',    'e': '.',      'f': '..-.',
        'g': '--.',    'h': '....',   'i': '..',
        'j': '.---',   'k': '-.-',    'l': '.-..',
        'm': '--',     'n': '-.',     'o': '---',
        'p': '.--.',   'q': '--.-',   'r': '.-.',
        's': '...',    't': '-',      'u': '..-',
        'v': '...-',   'w': '.--',    'x': '-..-',
        'y': '-.--',   'z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',

        'а': '.-', 'б': '-...', 'в': '.--',
        'г': '--.', 'д': '-..', 'е': '.',
        'ж': '...-', 'з': '--..', 'и': '..',
        'й': '.---', 'к': '-.-', 'л': '.-..',
        'м': '--', 'н': '-.', 'о': '---',
        'п': '.--.', 'р': '.-.', 'с': '...',
        'т': '-', 'у': '..-', 'ф': '..-.',
        'х': '....', 'ц': '-.-.', 'ч': '---.',
        'ш': '----', 'щ': '--.-', 'ъ': '.--.-.',
        'ы': '-.--', 'ь': '-..-', 'э': '..-..',
        'ю': '..--', 'я': '.-.-'
        }


def morse_encode(input_string):
    """
    :param input_string:
    :return: morse_string, error, error_string
    """
    morse_string = ""
    error_string = ""
    error = False

    console_print = True if __file__ == "morse.py" else False

    for letter in input_string:
        try:
            morse_letter = CODE[letter.lower()]
        except KeyError:
            error = True
            error_string = error_string + letter
            if console_print:
                print("Letter {} not found in morse dictionary".format(letter))
        else:
            if console_print:
                print("{}: {}".format(letter, morse_letter))
            morse_string = morse_string + morse_letter
    if len(morse_string) > 0:
        if console_print:
            print("Morse string: {}".format(morse_string))
        else:
            return morse_string, error, error_string


def main():
    try:
        while True:
            word = input()
            morse_encode(word)
    except KeyboardInterrupt:
        print("Bye", end="")
        exit(0)


if __name__ == '__main__':
    main()
