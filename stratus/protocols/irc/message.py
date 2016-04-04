from ..base.message import BaseMessage


class IrcMessage(BaseMessage):

    @property
    def message(self):
        return ''

    @property
    def target(self):
        return ''

    @property
    def sender(self):
        return ''

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return self.data.decode()
