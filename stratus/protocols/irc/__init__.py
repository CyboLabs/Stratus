import asyncio
import types

from ..base import BaseStreamingProtocol

from .message import IrcMessage


__all__ = ['IrcProtocol', 'IrcMessage']


class IrcProtocol(BaseStreamingProtocol):

    def parse_message(self, data: bytes) -> IrcMessage:
        return IrcMessage(data)

    def on_message(self, msg: IrcMessage) -> None:
        print(msg)

    def write(self, data: bytes) -> None:
        self.transport.write(data)

    @classmethod
    def create_connection(cls, loop: asyncio.BaseEventLoop, **kwargs) -> types.coroutine:
        host = kwargs['host']
        port = kwargs['port']
        return loop.create_connection(lambda: cls(loop), host=host, port=port)
