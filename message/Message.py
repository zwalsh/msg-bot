
class Message:

    def __init__(self):
        self._message = "msg"
        self._unread = False

    def is_unread(self):
        return self._unread

    def get_message(self):
        self._unread = False
        return self._message

    def set_message(self, msg):
        self._message = msg
        self._unread = True
