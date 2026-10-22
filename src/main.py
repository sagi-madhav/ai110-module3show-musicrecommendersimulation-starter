"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.
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
    """Main execution point for running recommendations."""
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    print_recommendations("Default Pop/Happy", user_prefs, recommendations)


if __name__ == "__main__":
    main()
