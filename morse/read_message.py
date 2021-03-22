import logging
import time

from morse.MORSE_CONSTANTS import SYMBOL_PAUSE, LETTER_PAUSE, WORD_PAUSE
from morse.MorseLights import MorseLights

logger = logging.getLogger()

MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ', ': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '!': '-.-.--',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-'
}


def read_message(msg, lights: MorseLights):
    logger.info(f"Reading {msg} out on light")
    words = msg.upper().split()
    for word in words:
        _read_word(word, lights)
        time.sleep(WORD_PAUSE)


def _read_word(word, lights):
    logger.info(f"Reading {word} out on light")
    letters = [letter for letter in word if letter in MORSE_CODE_DICT.keys()]
    for i, letter in enumerate(letters):
        _read_letter(letter, lights)
        if i != len(letters) - 1:
            lights.new_letter()


def _read_letter(letter, lights):
    pattern = MORSE_CODE_DICT[letter]
    logger.info(f"Reading {letter} out as {pattern}")
    for i, symbol in enumerate(pattern):
        if symbol == '.':
            lights.dot()
        if symbol == '-':
            lights.dash()
        # pause between each symbol, but not after the last one
        if i != len(pattern) - 1:
            lights.new_word()
