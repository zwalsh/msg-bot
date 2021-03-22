import logging

logger = logging.getLogger()


class Light:

    def __init__(self):
        self._on = False

    def turn_on(self):
        self._on = True
        logger.info("On!")

    def turn_off(self):
        self._on = False
        logger.info("Off!")
