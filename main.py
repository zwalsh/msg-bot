import logging

from control_loop import run_loop
from hardware.Button import Button
from hardware.Light import Light
from message.Message import Message
from read_message import read_message

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s', )

if __name__ == '__main__':
    read_message("Hi Jaclyn", Light())
    # run_loop(Button(), Light(), Message())
