import logging
import os
import sys
from pathlib import Path

from control_loop import run_loop
from hardware.Button import Button
from hardware.Light import Light
from message.Message import Message
from message.fetch_message import fetch_message
from morse.MorseLights import MorseLights

DEFAULT_DATA_PATH = "data"
DEFAULT_LOG_PATH = "log"


def configure_logging(run_mode):
    log_dir = Path(log_path)
    log_file = log_dir / f'{run_mode}.log'
    if not log_dir.exists() or not log_dir.is_dir():
        log_dir.mkdir()
    if not log_file.exists():
        log_file.touch()

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] (%(threadName)-10s) '
                               '[%(filename)s:%(lineno)d] %(message)s',
                        filename=log_file.absolute())
    return log_file


def start_lights(data_location):
    message = Message(Path(data_location))
    morse_lights = MorseLights(
        dot_light=Light(6),
        dash_light=Light(13),
        new_letter=Light(27),
        new_word=Light(22)
    )
    run_loop(Button(), morse_lights, message)


def fetch(data_location, message_url):
    message = Message(Path(data_location))
    try:
        fetch_message(message, message_url)
    except RuntimeError as e:
        logger.error(f"Failed to fetch message! {e}")
        raise e


if __name__ == '__main__':
    mode = sys.argv[1]

    data_path = os.getenv("MSG_BOT_DATA_PATH") or DEFAULT_DATA_PATH
    log_path = os.getenv("MSG_BOT_LOG_PATH") or DEFAULT_LOG_PATH

    log_file = configure_logging(mode)
    logger = logging.getLogger()
    logger.info(f"Starting up with data path: {data_path}, log file: {log_file.name}")

    if mode == 'lights':
        start_lights(data_path)
    elif mode == 'fetch':
        msg_url = os.getenv("MSG_BOT_MSG_URL")
        if msg_url is None:
            raise RuntimeError("Missing required env var MSG_BOT_MSG_URL")
        fetch(data_path, msg_url)
