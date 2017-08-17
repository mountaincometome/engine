"""
mountaincometome:watcher:main
"""

from radiality import Ring

from core import Watcher


if __name__ == '__main__':
    Watcher().sensor('0.0.0.0', 50004).attract(
        Ring().cohere('0.0.0.0', 50000)
    ).arise()
