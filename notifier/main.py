"""
mountaincometome:notifier:main
"""

from radiality import Ring

from core import Notifier


if __name__ == '__main__':
    Notifier().sensor('0.0.0.0', 50006).attract(
        Ring().cohere('0.0.0.0', 50000)
    ).arise()
