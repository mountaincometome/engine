"""
mountaincometome:pulsar:core
"""

import asyncio

import eventer
import effectors


class Pulsar(eventer.Pulsar, effectors.Configurator):
    """
    The `Pulsar` core
    """
    PERIOD = 60  # 60 sec

    _task = None  # type: asyncio.Task

    def attract(self, ring):
        """
        self: Pulsar
        ring: radiality.Ring

        return: Pulsar
        """
        ring.focus(self)

        return self

    def arise(self):
        """
        self: Pulsar
        """
        loop = asyncio.get_event_loop()

        try:
            self._task = asyncio.ensure_future(self._pulsation())

            self._intro()
            # Running
            loop.run_until_complete(self._task)
        except KeyboardInterrupt:
            # Causes the `terminated` event
            loop.run_until_complete(self.terminated())
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

    async def _pulsation(self):
        while True:
            # Causes the `pulse` event
            await self.pulse()
            # Pauses
            await asyncio.sleep(self.PERIOD)
        # Causes the `completed` event
        await self.completed()
        # Stops all tasks
        self._stop()

    def _stop(self):
        for task in asyncio.Task.all_tasks():
            if task != self._task:
                task.cancel()
