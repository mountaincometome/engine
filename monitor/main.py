"""
mountaincometome:monitor:main
"""

from radiality import Ring

from core import Monitor


if __name__ == '__main__':
    Monitor().sensor('0.0.0.0', 50001).attract(
        Ring().cohere('0.0.0.0', 50000)
    ).arise()
