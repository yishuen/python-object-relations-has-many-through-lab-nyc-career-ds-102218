from artist import Artist
lady_gaga = Artist("Lady Gaga")
lcd_soundsystem = Artist("LCD Soundsystem")
vulfpeck = Artist("Vulfpeck")

from genre import Genre
pop = Genre("Pop")
rock = Genre("Rock")
alt = Genre("Alternative")
indie = Genre("Indie")
folk = Genre("Folk")
country = Genre("Country")
funk = Genre("Funk")
jam = Genre("Jam")

from song import Song
back_pocket = Song("Back Pocket", vulfpeck, funk)
animal_spirits = Song("Animal Spirits", vulfpeck, funk)
dance_yrself_clean = Song("Dance Yrself Clean", lcd_soundsystem, alt)
all_my_friends = Song("All My Friends", lcd_soundsystem, alt)
shallow = Song("Shallow", lady_gaga, country)
the_cure = Song("The Cure", lady_gaga, pop)
someone_great = Song("Someone Great", lcd_soundsystem, indie)
dean_town = Song("Dean Town", vulfpeck, indie)

print(lady_gaga.songs())
print(lcd_soundsystem.genres())
print(pop.songs())
print(indie.artists())
