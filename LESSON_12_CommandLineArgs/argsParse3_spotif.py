def recommend_song(mood, genre):
    recommendations = {
        "happy": {
            "pop": "Happy by Pharrell Williams",
            "rock": "Don't Stop Believin' by Journey",
            "hip hop": "Can't Stop the Feeling! by Justin Timberlake"
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
    else:
        print("Sorry, we don't have a recommendation for that combination.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Get a song recommendation based on mood and genre."
    )

    parser.add_argument(
        "-m", "--mood", metavar="mood",
        required=True, choices=["happy", "chill"],
        help="The mood you're in."
    )

    parser.add_argument(
        "-g", "--genre", metavar="genre",
        required=True, choices=["pop", "rock", "hip hop", "electronic", "indie"],
        help="The genre you prefer."
    )

    args = parser.parse_args()

    recommend_song(args.mood, args.genre)
# python3 argsParse3_spotif.py -m "happy" -g "pop"

#
# result:
#If you're feeling happy, I recommend "Happy by Pharrell Williams".