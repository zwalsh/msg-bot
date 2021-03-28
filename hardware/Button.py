import logging

from gpiozero import Button as GPIOButton

_GPIO_PIN = 5

logger = logging.getLogger()


class Button:

    def __init__(self, pin=_GPIO_PIN):
        self.button = GPIOButton(pin=pin, hold_time=0.5, pull_up=False)

    def pressed(self):
        held = self.button.is_held
        if held:
            logger.info('Button pressed!')
        return held
