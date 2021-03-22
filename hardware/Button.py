import logging
from gpiozero import Button as GPIOButton

logger = logging.getLogger()

_GPIO_PIN = 5


class Button:

    def __init__(self, pin=_GPIO_PIN):
        self.button = GPIOButton(pin, hold_time=0.5)

    def pressed(self):
        return self.button.is_held
