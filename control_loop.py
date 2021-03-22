from read_message import read_message


def run_loop(button, light, message):
    while True:
        if message.is_unread():
            light.turn_on()
        if button.pressed():
            read_message(message.get_message(), light)
