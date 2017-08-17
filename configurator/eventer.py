"""
mountaincometome:configurator:eventer
"""

from radiality import event
from radiality import Eventer


class Configurator(Eventer):

    @event
    async def database_configured(self, host, port, db_name, table_name):
        pass
