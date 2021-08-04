import abc

from wiz_message.message import Message


class BotClient(metaclass=abc.ABCMeta):
    def __init__(self, webhook, secret_key):
        self._webhook = webhook
        self._secret_key = secret_key

    @abc.abstractmethod
    def send_message(self, message: Message):
        pass
