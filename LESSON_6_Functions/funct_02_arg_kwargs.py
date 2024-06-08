#
#
##  -------
# 🟠 ARGS
# ----------
# args will work like in javascript
# ** The *args parameter allows you to write a function that can accept a varying number of individual positional arguments in each call

def multiple_items(*args):
    # as you can see i am not adding names like in the num1 & num2, instead i grab the various values within the multiple_items("Dave"...
        print(args)
        print(type(args))

multiple_items("Dave", "John", "Noaln")
#result
#('Dave', 'John', 'Noaln')
# <class 'tuple'>
#
#
#
# EXAMPLE 2

def myFun(arg1, *argv):
    print('First argument :', arg1)
    for arg in argv:
        print('Next argument through *argv :', arg)

myFun('Hello', 'Welcome', 'to', 'Paradisse')
# RESULT:
# First argument : Hello
# Next argument through *argv : Welcome
# Next argument through *argv : to
# Next argument through *argv : Paradisse

#
#
#

#---------
# 🟠  KWARGS
# ----------

def myFune(**kwargs):
    for key, value in kwargs.items():
    #String with placeholders and format specifiers
        format_string = "%s == %s"
        #Using % operator to provide values that replace the placeholders
        print(format_string % (key, value))
#The % operator takes a tuple (key, value) and substitutes each %s with the respective elements of the tuple.




myFune(first="my", mid="beautiful", last="life")


# OUTPUT:
#first == my
# mid == beautiful
# last == life

#

#
#
#------------
## **  Real scenario (SPOTFY)
# -----------
#

def update_playlist(playlist_id, **kwargs):
    """
    Update a Spotify-like playlist with provided details.

    :param playlist_id: ID of the playlist to update.
    :param kwargs: Dictionary of playlist details to update.
    """
    print(f"Updating playlist with ID: {playlist_id}")
    for key, value in kwargs.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")

    # Simulate sending updated data to a Spotify-like service
    # For example, sending a request to an API endpoint
    # response = requests.post(f"https://api.spotify.com/playlists/{playlist_id}", json=kwargs)
    # print(f"Response: {response.status_code}")

# Driver code
update_playlist(
    playlist_id="12345",
    name="My Favorite Songs",
    description="A collection of my favorite songs from various genres.",
    tracks=["Track1", "Track2", "Track3"],
    public=True
)



# - `update_playlist(playlist_id, **kwargs)`: The function takes a playlist_id and any number of additional keyword arguments (\*\*kwargs).

# - The playlist_id is a required argument, while `**kwargs` allows passing optional details like **name, description, tracks, and public**.

## * result

# Updating playlist with ID: 12345
# Name: My Favorite Songs
# Description: A collection of my favorite songs from various genres.
# Tracks: ['Track1', 'Track2', 'Track3']
# Public: True
