"""
mountaincometome:monitor:effectors
"""

from radiality import effect
from radiality import Effector


class Configurator(Effector):

    @effect
    async def database_configured(self, host, port, db_name, table_name):
        print(
            'The [{db}] database of the [{host}:{port}] server has the '
            '[{table}] table'.format(
                host=host, port=port, db=db_name, table=table_name
            )
        )


class Watcher(Effector):

    @effect
    async def catching(self, i):
        print('The [{0}] watcher try to catch something...'.format(i))

    @effect
    async def catched(self, i):
        print('The [{0}] watcher catched something'.format(i))
