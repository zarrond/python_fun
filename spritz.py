import sys
import fileinput
from math import ceil
from time import sleep
from termcolor import colored

def get_orp(word_length):
    percent = 0.35
    orp = int(ceil(word_length * percent))
    return orp if orp <= 5 else 5


def get_longest(text):
    return len(sorted(text, key=len, reverse=True)[0])


def get_spaces(word, max_length):
    max_orp = get_orp(max_length)
    if len(word) < 3:
        orp = len(word)
    else:
        orp = get_orp(len(word))
    prefix_space = (max_orp - orp)
    postfix_space = (max_length - len(word) - prefix_space)
    return (orp, prefix_space, postfix_space)


def color_orp_char(word, orp):
    RED = '\x1b[91m'
    NORMAL = '\x1b[0m'
    chars = list(word)
    #print(chars)
    #chars[orp] = colored(chars[orp], 'red')
    #print(chars)
    chars.insert(orp, RED)
    chars.insert((orp + 2), NORMAL)
    return "".join(chars)


def print_word(word, orp_config):
    orp, prefix_space, postfix_space = orp_config
    orp = orp - 1
    #print_string = (" " * prefix_space) + color_orp_char(word, orp) + (" " * postfix_space)
    print_string = color_orp_char(word, orp)
    print("{}  {}".format(print_string, len(print_string)), end='\r')


def clean_articles(text):
    remove = (',', '.', '!', '?', '-', ';')
    for char in remove:
        text = text.replace(char, " <PAUSE> ")
    text = text.strip()
    # text = text.replace("\n", " <PAUSE> <PAUSE> ")
    return text.split()


def spritz(wpm, text):
    sleep_interval = (60.0 / wpm)
    text = clean_articles(text)
    max_length = get_longest(text)

    for word in text:
        if word == "<PAUSE>":
            sleep(sleep_interval * 3)
            continue
        word_sleep_interval = 0.01 * len(word)
        sleep(sleep_interval + word_sleep_interval)
        orp_config = get_spaces(word, max_length)
        print_word(word, orp_config)


def otherMain():
    wpm = 200
    text = ""
    for line in fileinput.input('text.txt'):
        text += line

    spritz(wpm, text)


def main():
    wpm = int(sys.argv[1])
    text = ""
    for line in fileinput.input(sys.argv[2:]):
        text += line

    spritz(wpm, text)


if __name__ == "__main__":
    otherMain()
    # main()


