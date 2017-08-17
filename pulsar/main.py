"""
mountaincometome:pulsar:main
"""

from radiality import Ring

from core import Pulsar


if __name__ == '__main__':
    Pulsar().sensor('0.0.0.0', 50003).attract(
        Ring().cohere('0.0.0.0', 50000)
    ).arise()
