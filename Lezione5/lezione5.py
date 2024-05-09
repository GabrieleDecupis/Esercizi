#1. Create a Playlist:
#
#Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
#The function should return a dictionary with the playlist name and a set of songs. 
#Call the function with different numbers of songs to demonstrate flexibility.
#
#Example: create_playlist("Road Trip", {"Song 1", "Song 2"})
#
#Write a function called add_like() that accepts a dictionary, the name of a playlist, 
#and a boolean value indicating whether it is liked (True or False). 
#This function should return an updated dictionary.
#
#Example: add_like(dictionary, “Road Trip”, liked=True)

def create_playlist(name_playlist: str, *song: str) -> dict:
    playlist: dict = {}
    songs: set = set(song)
    playlist[name_playlist] = songs
    return playlist

def add_like(playlist: dict, name_playlist: str, like: bool) -> dict:
    playlist = {playlist, name_playlist, like}
    return playlist

print(add_like(create_playlist("Road trip", 'Song1' 'Song2' 'Song 3')),True)