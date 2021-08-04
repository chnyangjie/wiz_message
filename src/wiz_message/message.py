import abc


class Message(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def to_json(self):
        pass


class TextMessage(Message, metaclass=abc.ABCMeta):
    def __init__(self):
        self._title = ""
        self._content = ""
        self._at_all = False


class MarkdownMessage(Message, metaclass=abc.ABCMeta):

    def __init__(self):
        self._title = ""
        self._content = ""
        self._template = "red"
        self._at_all = False
