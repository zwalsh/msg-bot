import time

from morse.MorseLights import MorseLights
from morse.read_message import read_message


def run_loop(button, lights: MorseLights, message):
    while True:
        if message.is_unread():
            lights.turn_on()
        if button.pressed():
            lights.blink()
            time.sleep(5)
            read_message(message.get_message(), lights)
