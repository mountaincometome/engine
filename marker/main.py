"""
mountaincometome:marker:main
"""

from radiality import Ring

from core import Marker


if __name__ == '__main__':
    Marker().sensor('0.0.0.0', 50005).attract(
        Ring().cohere('0.0.0.0', 50000)
    ).arise()
