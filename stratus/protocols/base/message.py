class BaseMessage:
    def __init__(self, data: bytes):
        self.data = data

    @property
    def target(self):
        raise NotImplementedError

    @property
    def sender(self):
        raise NotImplementedError

    @property
    def message(self):
        raise NotImplementedError
