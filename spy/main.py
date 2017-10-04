"""
mountaincometome:spy:main
"""

from radiality import Ring

from core import Spy


if __name__ == '__main__':
    Spy().sensor('0.0.0.0', 50004).attract(
        Ring().cohere('0.0.0.0', 50000)
    ).arise()
