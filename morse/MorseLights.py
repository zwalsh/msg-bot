import time

from hardware.Light import Light
from morse.MORSE_CONSTANTS import DOT, DASH, LETTER_PAUSE, WORD_PAUSE


class MorseLights:

    def __init__(self, dot_light: Light, dash_light: Light, new_letter: Light, new_word: Light):
        self._dot_light = dot_light
        self._dash_light = dash_light
        self._new_letter = new_letter
        self._new_word = new_word

    def dot(self):
        self._dot_light.turn_on()
        time.sleep(DOT)
        self._dot_light.turn_off()

    def dash(self):
        self._dash_light.turn_on()
        time.sleep(DASH)
        self._dash_light.turn_off()

    def new_letter(self):
        self._new_letter.turn_on()
        time.sleep(LETTER_PAUSE)
        self._new_letter.turn_off()

    def new_word(self):
        self._new_word.turn_on()
        time.sleep(WORD_PAUSE)
        self._new_word.turn_off()

    def turn_on(self):
        for light in self.all_lights():
            light.turn_on()

    def blink(self, times=5):
        for i in range(0, times):
            for light in self.all_lights():
                light.turn_on()
            time.sleep(0.1)
            for light in self.all_lights():
                light.turn_off()
            time.sleep(0.1)

    def all_lights(self):
        return [self._dot_light, self._dash_light, self._new_letter, self._new_word]
