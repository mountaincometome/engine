"""
mountaincometome:configurator:core
"""

import asyncio

import eventer


class Configurator(eventer.Configurator):
    """
    The `Configurator` core
    """

    def attract(self, ring):
        """
        self: Configurator
        ring: radiality.Ring

        return: Configurator
        """
        ring.focus(self)

        return self

    def arise(self):
        """
        self: Configurator
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
