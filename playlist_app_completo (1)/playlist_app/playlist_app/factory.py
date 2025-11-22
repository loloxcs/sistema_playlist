from .models import Track

class TrackFactory:
    """Factory Method: creates Track objects from different input shapes."""

    @staticmethod
    def create_from_dict(data: dict) -> Track:
        title = data.get('title') or data.get('name') or 'Unknown'
        artist = data.get('artist') or data.get('band') or 'Unknown Artist'
        duration = int(data.get('duration', 0))
        return Track(title, artist, duration)

    @staticmethod
    def create_from_csv_line(line: str, sep=',') -> Track:
        # simple CSV: title,artist,duration
        parts = [p.strip() for p in line.split(sep)]
        title = parts[0] if len(parts) > 0 else 'Unknown'
        artist = parts[1] if len(parts) > 1 else 'Unknown Artist'
        try:
            duration = int(parts[2]) if len(parts) > 2 else 0
        except ValueError:
            duration = 0
        return Track(title, artist, duration)
