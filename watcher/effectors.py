"""
mountaincometome:watcher:effectors
"""

from radiality import effect
from radiality import Effector


class Configurator(Effector):

    @effect
    async def database_configured(self, host, port, db_name, table_name):
        pass


class Pulsar(Effector):

    @effect
    async def pulse(self):
        await self._catch()
