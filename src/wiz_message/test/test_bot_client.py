from unittest import TestCase

from wiz_message.bot_client import BotClient, BotClientHolder
from wiz_message.message import Message


class A(BotClient):
    @classmethod
    def filter(cls, webhook: str):
        if webhook == "A":
            return True

    def send_message(self, message: Message):
        pass

    def convert_message(self, message: Message):
        pass


class B(BotClient):
    @classmethod
    def filter(cls, webhook: str):
        if webhook == "B":
            return True

    def send_message(self, message: Message):
        pass

    def convert_message(self, message: Message):
        pass


class TestBotClientHolder(TestCase):
    def test_gen_client(self):
        h = BotClientHolder([A, B])
        h.gen_client("A", "AA")
        h.gen_client("A", "AB")
        h.gen_client("B", "AA")
        self.assertEqual(len(h.clients), 3)
        self.assertEqual(h.clients[0].webhook, "A")
        self.assertEqual(h.clients[0].secret_key, "AA")

        self.assertEqual(h.clients[1].webhook, "A")
        self.assertEqual(h.clients[1].secret_key, "AB")

        self.assertEqual(h.clients[2].webhook, "B")
        self.assertEqual(h.clients[2].secret_key, "AA")
