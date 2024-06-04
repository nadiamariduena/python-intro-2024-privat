# notice what is happening here
def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

# result
#17
# 27
def playlistBuilder(songs):
    #
    #
    return lambda playlist_name: f"Adding songs to {playlist_name} playlist: {', '.join(songs)}"

# List of songs for the "Chill Vibes" playlist
chill_vibes_songs = ["Song 1", "Song 2", "Song 3"]
# List of songs for the "Summer Hits" playlist
summer_hits_songs = ["Song A", "Song B", "Song C"]


# Here you are assigning the value of chill_vibes_songs to addChillVibesSongs, then the addChillVibesSongs will be appending a new song "Song 4"
# Look ath the scope of the playlistBuilder
addChillVibesSongs = playlistBuilder(chill_vibes_songs)
addSummerHitsSongs = playlistBuilder(summer_hits_songs)

# Add a new song to the "Chill Vibes" playlist
chill_vibes_songs.append("Song 4")

print(addChillVibesSongs("Chill Vibessss"))
print(addSummerHitsSongs("Summer Hits"))

