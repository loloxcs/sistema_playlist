from playlist_app.models import Playlist
from playlist_app.factory import TrackFactory
from playlist_app.player import Player
from playlist_app.strategies import ShuffleStrategy, NormalStrategy, ReverseStrategy
from playlist_app.observers import LoggerObserver
import time

def demo():
    # Create playlist
    pl = Playlist('My Favorites')

    # Attach an observer (Observer pattern)
    logger = LoggerObserver()
    pl.attach(logger)

    # Create tracks via factory (Factory Method)
    t1 = TrackFactory.create_from_dict({'title':'Song A','artist':'Artist 1','duration':210})
    t2 = TrackFactory.create_from_csv_line('Song B,Artist 2,180')
    t3 = TrackFactory.create_from_dict({'name':'Song C','band':'Artist 3','duration':200})

    pl.add_track(t1)
    pl.add_track(t2)
    pl.add_track(t3)

    print('\nPlaylist tracks:')
    for i, t in enumerate(pl.list_tracks()):
        print(i+1, t)

    # Player is a singleton
    player = Player()
    player.load_playlist(pl)

    # Play normally
    player.play()
    time.sleep(0.5)
    player.next()

    # Switch strategy to shuffle (Strategy pattern)
    player.set_strategy(ShuffleStrategy())
    print('\n[Demo] After switching to ShuffleStrategy:')
    player.play()

    # Reverse
    player.set_strategy(ReverseStrategy())
    print('\n[Demo] After switching to ReverseStrategy:')
    player.play()

    # Stop
    player.stop()

if __name__ == '__main__':
    demo()
