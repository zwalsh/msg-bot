import logging
import time

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

    def blink(self, times=5):
        for i in range(0, times):
            self.turn_on()
            time.sleep(0.1)
            self.turn_off()
