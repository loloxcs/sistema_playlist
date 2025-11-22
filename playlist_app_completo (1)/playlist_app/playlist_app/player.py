from __future__ import annotations
from typing import Optional, List
from .models import Playlist, Track
from .strategies import PlaybackStrategy, NormalStrategy
import threading

class _PlayerSingletonMeta(type):
    _instance = None
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Player(metaclass=_PlayerSingletonMeta):
    """Singleton: single player instance throughout the app."""

    def __init__(self):
        self.current_playlist: Optional[Playlist] = None
        self.strategy: PlaybackStrategy = NormalStrategy()
        self._queue: List[Track] = []
        self._index = 0
        self.is_playing = False

    def load_playlist(self, playlist: Playlist):
        self.current_playlist = playlist
        self._queue = self.strategy.order(playlist.list_tracks())
        self._index = 0

    def set_strategy(self, strategy: PlaybackStrategy):
        self.strategy = strategy
        if self.current_playlist:
            self._queue = self.strategy.order(self.current_playlist.list_tracks())

    def play(self):
        if not self._queue:
            print("[Player] Queue is empty.")
            return
        self.is_playing = True
        track = self._queue[self._index]
        print(f"[Player] Playing: {track}")

    def next(self):
        if not self._queue:
            return
        self._index = (self._index + 1) % len(self._queue)
        self.play()

    def prev(self):
        if not self._queue:
            return
        self._index = (self._index - 1) % len(self._queue)
        self.play()

    def stop(self):
        self.is_playing = False
        print("[Player] Stopped.")

