import time

from hardware.Light import Light
from morse.MORSE_CONSTANTS import DOT, DASH


class MorseLights:

    def __init__(self, dot_light: Light, dash_light: Light):
        self._dot_light = dot_light
        self._dash_light = dash_light

    def dot(self):
        self._dot_light.turn_on()
        time.sleep(DOT)
        self._dot_light.turn_off()

    def dash(self):
        self._dash_light.turn_on()
        time.sleep(DASH)
        self._dash_light.turn_off()

    def turn_on(self):
        self._dot_light.turn_on()
        self._dash_light.turn_on()

    def blink(self):
        self._dot_light.blink()
        self._dash_light.blink()
