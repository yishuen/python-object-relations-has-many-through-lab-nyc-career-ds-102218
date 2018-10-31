# remeber to import the Song class here
from song import Song

class Artist:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def songs(self):
        matches = list(filter(lambda s: s._artist == self, Song._all))
        return matches

    def genres(self):
        matches = list(filter(lambda s: s._artist == self, Song._all))
        genre_objs = list(map(lambda s: s._genre, matches))
        return genre_objs


# from genre import Genre
# pop = Genre("Pop")
# country = Genre("Country")
#
# lady_gaga = Artist("Lady Gaga")
# shallow = Song("Shallow", lady_gaga, country)
# the_cure = Song("The Cure", lady_gaga, pop)
