from termcolor import colored
import time
import math
import re
from colorama import Fore, Back, Style, init
import sys
## define
SPRITZ_coeff = 0.35
INITIAL_BLANK = 10
init()

def blankspace(num):
    print(' '*(num+INITIAL_BLANK), end='')


def get_orp(word_length):
    percent = 0.35
    orp = int(math.ceil(word_length * percent))
    return orp if orp <= 5 else 5


def spritz_print(word, orp):
    s = word
    if len(word) > 2:
        s = s[:orp] + colored(word[orp], 'red') + s[orp + 1:]
    elif len(word) == 2:
        s = s[0] + colored(word[1], 'red')
    else:
        s = colored(word[0], 'red')


    print(s, end=" "*max_len+"\r")
    time.sleep(sleep_duration+0.01*len(word))
    print("", end='\r')

print()
with open("text.txt", 'r') as f:
    words = re.sub(r'([^\w0-9_ ])+', '', f.read()).split(" ")
max_len = len(max(words, key=len))
red_pos = math.ceil(max_len*SPRITZ_coeff)
red_pos = red_pos if red_pos < 5 else 5
wpm = int(sys.argv[1])
sleep_duration = 60.0/wpm
for word in words:
    #word = words[i]
    lenght = len(word)
    orp = get_orp(lenght)
    #print(word)
    blankspace(red_pos-(orp-1))
    spritz_print(word, orp)

"""
for i in range(5):
    print(colored("hello "+str(i), "red"), end='')
    time.sleep(0.1)
    print(end='\r')
"""

##sucCession
##  dPi