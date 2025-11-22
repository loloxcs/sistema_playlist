from typing import List, Protocol, Any

class Track:
    def __init__(self, title: str, artist: str, duration: int):
        self.title = title
        self.artist = artist
        self.duration = duration  # seconds

    def __repr__(self):
        m, s = divmod(self.duration, 60)
        return f"{self.title} - {self.artist} ({m}:{s:02d})"

# Observer infrastructure (Subject / Observer)
class PlaylistObserver(Protocol):
    def update(self, event: str, data: Any) -> None:
        ...

class Playlist:
    def __init__(self, name: str):
        self.name = name
        self._tracks: List[Track] = []
        self._observers: List[PlaylistObserver] = []

    # Observer methods
    def attach(self, observer: PlaylistObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: PlaylistObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify(self, event: str, data: Any = None) -> None:
        for o in list(self._observers):
            try:
                o.update(event, data)
            except Exception:
                pass

    # Playlist operations
    def add_track(self, track: Track) -> None:
        self._tracks.append(track)
        self._notify('track_added', track)

    def remove_track(self, index: int) -> None:
        if 0 <= index < len(self._tracks):
            t = self._tracks.pop(index)
            self._notify('track_removed', t)

    def list_tracks(self) -> List[Track]:
        return list(self._tracks)

