"""
mountaincometome:spy:core
"""

import asyncio
from random import random
from uuid import uuid4

import eventer
import effectors


class Spy(eventer.Spy, effectors.Configurator, effectors.Pulsar):
    """
    The `Spy` core
    """
    MAX_SLEEP_TIME = 5  # 5 sec

    _id = None

    def __init__(self):
        """
        self: Spy
        """
        super().__init__()

        self._id = str(uuid4())

    def attract(self, ring):
        """
        self: Spy
        ring: radiality.Ring

        return: Spy
        """
        ring.focus(self)

        return self

    def arise(self):
        """
        self: Spy
        """
        loop = asyncio.get_event_loop()

        try:
            self._intro()
            # Runs the infinite event loop only
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self._outro()
            # Exit
            loop.close()

    def _intro(self):
        print('The `{0}` core running...'.format(self.__class__.__name__))
        channel_uri = self.channel_uri()
        if channel_uri:
            print('and it is available at [{0}]...'.format(channel_uri))

    def _outro(self):
        print('\nThe `{0}` core is stopped'.format(self.__class__.__name__))

    async def _catch(self):
        # Causes the `catching` event
        await self.catching(i=self._id)
        # Simulates i/o operation using sleep
        await asyncio.sleep(self.MAX_SLEEP_TIME * random())
        # Causes the `catched` event
        await self.catched(i=self._id)
