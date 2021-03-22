import logging
import os
from pathlib import Path

from control_loop import run_loop
from hardware.Button import Button
from hardware.Light import Light
from message.Message import Message
from read_message import read_message

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s', )

logger = logging.getLogger()

if __name__ == '__main__':
    data_path = os.getenv("MSG_BOT_DATA_PATH")
    logger.info(f"Starting up with data path {data_path}")
    message = Message(Path(data_path or "data"))
    run_loop(Button(), Light(), message)
