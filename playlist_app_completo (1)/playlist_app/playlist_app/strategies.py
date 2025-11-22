from typing import List
from .models import Track
import random

class PlaybackStrategy:
    def order(self, tracks: List[Track]) -> List[Track]:
        raise NotImplementedError

class NormalStrategy(PlaybackStrategy):
    def order(self, tracks):
        return list(tracks)

class ShuffleStrategy(PlaybackStrategy):
    def order(self, tracks):
        shuffled = list(tracks)
        random.shuffle(shuffled)
        return shuffled

class RepeatOneStrategy(PlaybackStrategy):
    def order(self, tracks):
        # For repeat-one, we return the list but player will repeat current
        return list(tracks)

class ReverseStrategy(PlaybackStrategy):
    def order(self, tracks):
        return list(reversed(tracks))
