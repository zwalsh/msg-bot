from pathlib import Path

_MSG_FILE_NAME = 'message.txt'
_UNREAD_FILE_NAME = 'unread.txt'


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

    def is_unread(self):
        return self._unread_file.read_text().strip() == 'True'

    def get_message(self):
        self._unread_file.write_text('False')
        return self._msg_file.read_text()

    def set_message(self, msg):
        self._msg_file.write_text(msg)
        self._unread_file.write_text('True')
