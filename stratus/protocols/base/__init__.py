import asyncio
import types

from .message import BaseMessage


class BaseProtocol:

    def __init__(self, loop: asyncio.BaseEventLoop):
        super().__init__()
        self.loop = loop
        self.transport = asyncio.transports.BaseTransport

    @classmethod
    def create_connection(cls, loop, **kwargs) -> types.coroutine:
        raise NotImplementedError

    def write(self, data: bytes) -> None:
        raise NotImplementedError

    def parse_message(self, data: bytes) -> BaseMessage:
        raise NotImplementedError

    def on_message(self, msg: BaseMessage) -> None:
        raise NotImplementedError


class BaseStreamingProtocol(BaseProtocol, asyncio.Protocol):

    def data_received(self, data: bytes) -> None:
        msg = self.parse_message(data)
        self.loop.call_soon(self.on_message, msg)

    def connection_made(self, transport: asyncio.transports.Transport) -> None:
        self.transport = transport
