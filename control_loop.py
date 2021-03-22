import time

from read_message import read_message


def run_loop(button, light, message):
    while True:
        if message.is_unread():
            light.turn_on()
        if button.pressed():
            light.blink()
            time.sleep(5)
            read_message(message.get_message(), light)
