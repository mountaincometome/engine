"""
mountaincometome:watcher:eventer
"""

from radiality import event
from radiality import Eventer


class Watcher(Eventer):

    @event
    async def catching(self, i):
        pass

    @event
    async def catched(self, i):
        pass
