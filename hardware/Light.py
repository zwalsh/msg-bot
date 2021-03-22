import logging
from gpiozero import LED

logger = logging.getLogger()

_GPIO_PIN = 6


class Light:

    def __init__(self, pin=_GPIO_PIN):
        self.led = LED(pin)

    def turn_on(self):
        self.led.on()
        logger.info("On!")

    def turn_off(self):
        self.led.off()
        logger.info("Off!")
