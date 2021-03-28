import logging
import os
from pathlib import Path

from control_loop import run_loop
from hardware.Button import Button
from hardware.Light import Light
from message.Message import Message
from morse.MorseLights import MorseLights

DEFAULT_DATA_PATH = "data"
DEFAULT_LOG_PATH = "log"

if __name__ == '__main__':
    data_path = os.getenv("MSG_BOT_DATA_PATH") or DEFAULT_DATA_PATH
    log_path = os.getenv("MSG_BOT_LOG_PATH") or DEFAULT_LOG_PATH

    log_dir = Path(log_path)
    log_file = log_dir / 'msg-bot.log'
    if not log_dir.exists() or not log_dir.is_dir():
        log_dir.mkdir()
    if not log_file.exists():
        log_file.touch()

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s',
                        filename=log_file.absolute())

    logger = logging.getLogger()

    logger.info(f"Starting up with data path: {data_path}, log file: {log_file.name}")
    message = Message(Path(data_path))
    morse_lights = MorseLights(
        dot_light=Light(6),
        dash_light=Light(13),
        new_letter=Light(27),
        new_word=Light(22)
    )
    run_loop(Button(), morse_lights, message)
