import logging
import os
from pathlib import Path

from control_loop import run_loop
from hardware.Button import Button
from hardware.Light import Light
from message.Message import Message
from morse.MorseLights import MorseLights

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s', )

logger = logging.getLogger()

DEFAULT_DATA_PATH = "data"

if __name__ == '__main__':
    data_path = os.getenv("MSG_BOT_DATA_PATH") or DEFAULT_DATA_PATH
    logger.info(f"Starting up with data path {data_path}")
    message = Message(Path(data_path))
    morse_lights = MorseLights(
        dot_light=Light(6),
        dash_light=Light(13),
        new_letter=Light(27),
        new_word=Light(22)
    )
    run_loop(Button(), morse_lights, message)
