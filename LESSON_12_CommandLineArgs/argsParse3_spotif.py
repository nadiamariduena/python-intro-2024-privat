def recommend_song(mood, genre):
    recommendations ={
        "happy": {
            "pop": "Happy by Pharrell Williams",
            "rock": "Don't Stop Believin' by Journey",
            "hip hop": "Can't Stop the Feeling! by Justin    Timberlake"
        },
        "chill": {
            "pop": "Sunflower by Post Malone & Swae Lee",
            "electronic": "Strobe by Deadmau5",
            "indie": "Holocene by Bon Iver"
        }
    }

    if mood in recommendations and genre in recommendations[mood]:
        song = recommendations[mood][genre]
        print(f"If you're feeling {mood}, I recommend \"{song}\".")