"""
mountaincometome:notifier:core
"""

import asyncio

import eventer
import effectors


class Notifier(eventer.Notifier, effectors.Configurator):
    """
    The `Notifier` core
    """

    def attract(self, ring):
        """
        self: Notifier
        ring: radiality.Ring

        return: Notifier
        """
        ring.focus(self)

        return self

    def arise(self):
        """
        self: Notifier
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
