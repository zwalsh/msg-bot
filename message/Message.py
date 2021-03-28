import logging
from pathlib import Path

_MSG_FILE_NAME = 'message.txt'
_UNREAD_FILE_NAME = 'unread.txt'

logger = logging.getLogger()


class Message:

    def __init__(self, root_path: Path):
        if not (root_path.exists() and root_path.is_dir()):
            root_path.mkdir()
        self._msg_file = root_path / _MSG_FILE_NAME
        if not self._msg_file.exists():
            self._msg_file.touch()
        self._unread_file = root_path / _UNREAD_FILE_NAME
        if not self._unread_file.exists():
            self._unread_file.touch()
        self._last_unread = False

    def is_unread(self):
        unread = self._unread_file.read_text().strip() == 'True'
        if unread and not self._last_unread:
            logger.info('Detected new message!')
            logger.info(f'New message: {self._msg_file.read_text()}')
            self._last_unread = True
        return unread

    def _set_unread(self, unread):
        self._last_unread = unread
        self._unread_file.write_text(str(unread))

    def get_message(self):
        self._set_unread(False)
        return self._msg_file.read_text()

    def set_message(self, msg):
        logger.info(f'Setting new message: {msg}')
        self._msg_file.write_text(msg)
        self._set_unread(True)
