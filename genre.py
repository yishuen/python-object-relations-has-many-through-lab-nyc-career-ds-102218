# remeber to import the Song class here
from song import Song

class Genre:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def songs(self):
        matches = list(filter(lambda s: s._genre == self, Song._all))
        return matches

    def artists(self):
        matches = list(filter(lambda s: s._genre == self, Song._all))
        artist_objs = list(map(lambda s: s._artist, matches))
        return artist_objs
