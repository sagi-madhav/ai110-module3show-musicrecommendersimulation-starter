"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender with diverse profiles.
"""

try:
    from src.recommender import load_songs, recommend_songs
except ModuleNotFoundError:
    from recommender import load_songs, recommend_songs


def print_recommendations(profile_name: str, user_prefs: dict, recommendations: list) -> None:
    """Prints formatted recommendations with scores and match reasons."""
    print(f"Profile: {profile_name}")
    print(f"Preferences: genre={user_prefs.get('genre')}, mood={user_prefs.get('mood')}, energy={user_prefs.get('energy')}")
    print("Recommendations:")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"  {rank}. {song['title']} by {song['artist']} ({song['genre']})")
        print(f"     Score: {score:.2f}")
        print(f"     Reasons: {explanation}")
    print("-" * 50)


def main() -> None:
    """Runs recommendation tests across diverse listener profiles."""
    songs = load_songs("data/songs.csv")

    profiles = [
        (
            "High-Energy Pop",
            {"genre": "pop", "mood": "happy", "energy": 0.85},
        ),
        (
            "Chill Lofi",
            {"genre": "lofi", "mood": "chill", "energy": 0.35},
        ),
        (
            "Deep Intense Rock",
            {"genre": "rock", "mood": "intense", "energy": 0.90},
        ),
        (
            "Adversarial Conflicted Profile",
            {"genre": "metal", "mood": "chill", "energy": 0.95},
        ),
    ]

    print("\nRunning Recommender Evaluation:\n")
    for name, prefs in profiles:
        recommendations = recommend_songs(prefs, songs, k=5)
        print_recommendations(name, prefs, recommendations)


if __name__ == "__main__":
    main()
