import logging
import time

logger = logging.getLogger()

# length of time in seconds for a morse Dot
# dot = 1 unit
# dash = 3 units
# between letters = 3 units
# between words = 7 units
MORSE_TIME_UNIT_S = 1.0 / 3.0
DOT = MORSE_TIME_UNIT_S
DASH = MORSE_TIME_UNIT_S * 3
SYMBOL_PAUSE = MORSE_TIME_UNIT_S
LETTER_PAUSE = MORSE_TIME_UNIT_S * 3
WORD_PAUSE = MORSE_TIME_UNIT_S * 7

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


def read_message(msg, light):
    logger.info(f"Reading {msg} out on light")
    words = msg.upper().split()
    for word in words:
        _read_word(word, light)
        time.sleep(WORD_PAUSE)


def _read_word(word, light):
    logger.info(f"Reading {word} out on light")
    letters = [letter for letter in word if letter in MORSE_CODE_DICT.keys()]
    for i, letter in enumerate(letters):
        _read_letter(letter, light)
        if i != len(letters) - 1:
            time.sleep(LETTER_PAUSE)


def _read_letter(letter, light):
    pattern = MORSE_CODE_DICT[letter]
    logger.info(f"Reading {letter} out as {pattern}")
    for i, symbol in enumerate(pattern):
        pause = DOT if symbol == '.' else DASH
        light.turn_on()
        time.sleep(pause)
        light.turn_off()
        # pause between each symbol, but not after the last one
        if i != len(pattern) - 1:
            time.sleep(SYMBOL_PAUSE)
