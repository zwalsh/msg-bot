import requests

from message import logger
from message.Message import Message


def fetch_message(msg: Message, message_url):
    logger.info(f"Checking if a new message exists at {message_url}")
    response = requests.get(message_url)
    if response.status_code != 200:
        logger.error(f"Received non-200 response: {response.text}")
        raise RuntimeError(f"Fetching message failed with reason: {response.reason}")
    remote_msg = response.text.strip()
    logger.info(f"Remote message is currently {remote_msg}")
    msg.set_message(remote_msg)
