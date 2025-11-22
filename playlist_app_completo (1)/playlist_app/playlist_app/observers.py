from .models import PlaylistObserver
from typing import Any

class LoggerObserver:
    def update(self, event: str, data: Any) -> None:
        if event == 'track_added':
            print(f"[Logger] Track added: {data}")
        elif event == 'track_removed':
            print(f"[Logger] Track removed: {data}")
        else:
            print(f"[Logger] Event {event} -> {data}")
