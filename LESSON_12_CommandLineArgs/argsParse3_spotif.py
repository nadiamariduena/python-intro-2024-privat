def spotify_greeting(username, lang):
    music_preferences = {
        "pop": {
            "English": "Hey there, pop lover",
            "Spanish": "!Hola amante del pop",
            "German": "Hallo, Pop-Liebhaber"
            },
        "rock": {
            "English": "Rock on, {}",
            "Spanish": "!Rockea, {}",
            "German": "Rocke weiter, {}"

            },
        "jazz": {
            "English": "Smooth vibes coming your way, {}",
            "Spanish": "!Vibra suave, {}",
            "German": "Sanfte Vibes für dich, {}"
        }
    }

    # Simulating fetching user's music preferences from Spotify API
    # Let's assume we have a function called fetch_music_preferences(username) that returns user's music preferences