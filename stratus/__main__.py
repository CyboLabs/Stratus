import asyncio

from .engine import Stratus

loop = asyncio.new_event_loop()
stratus = Stratus(loop)
try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.close()
