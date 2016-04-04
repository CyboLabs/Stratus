import asyncio

import stratus.protocols.irc

config = {
    'protocols': [
        {
            'name': 'irc',
            'protocol': stratus.protocols.irc.IrcProtocol,
            'connect': {
                'host': 'chat.freenode.net',
                'port': 6667
            }
        }
    ]
}


class Stratus:
    """
    The core of the bot. Processes Events
    """
    def __init__(self, loop):
        self.loop = loop
        self.protocols = {}
        asyncio.ensure_future(self.load_protocol('irc'), loop=self.loop)

    async def load_protocol(self, name):
        if name in self.protocols:
            raise ValueError('%s already loaded' % name)
        protocol_dict = next((p for p in config['protocols'] if p['name'] == name), None)
        if protocol_dict is None:
            raise KeyError('%s is not a defined protocol' % name)
        _, self.protocols[name] = await asyncio.ensure_future(
            protocol_dict['protocol'].create_connection(
                self.loop, **protocol_dict.get('connect', {})),
            loop=self.loop
        )
