"""
mountaincometome:pulsar:eventer
"""

from radiality import event
from radiality import Eventer


class Pulsar(Eventer):

    @event
    async def pulse(self):
        pass

    @event
    async def completed(self):
        pass

    @event
    async def terminated(self):
        pass
