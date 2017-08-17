"""
mountaincometome:configurator:main
"""

from radiality import Ring

from core import Configurator


if __name__ == '__main__':
    Configurator().sensor('0.0.0.0', 50002).attract(
        Ring().cohere('0.0.0.0', 50000)
    ).arise()
