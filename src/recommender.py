import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Song:
    """Represents a song and its audio and metadata attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represents a user's musical preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """Provides object-oriented song scoring and ranking based on user profiles."""
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Ranks songs by score against a user profile and returns the top k songs."""
        def calculate_score(song: Song) -> float:
            score = 0.0
            if song.genre.lower() == user.favorite_genre.lower():
                score += 2.0
            if song.mood.lower() == user.favorite_mood.lower():
                score += 1.0
            energy_diff = abs(song.energy - user.target_energy)
            score += max(0.0, 1.0 - energy_diff)
            return score

        return sorted(self.songs, key=calculate_score, reverse=True)[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a readable explanation string detailing why a song was recommended."""
        reasons = []
        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("genre match (+2.0)")
        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("mood match (+1.0)")
        energy_diff = abs(song.energy - user.target_energy)
        energy_score = max(0.0, 1.0 - energy_diff)
        reasons.append(f"energy similarity (+{energy_score:.2f})")
        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Loads song records from a CSV file into a list of parsed dictionaries."""
    songs: List[Dict] = []
    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"].strip(),
                "artist": row["artist"].strip(),
                "genre": row["genre"].strip().lower(),
                "mood": row["mood"].strip().lower(),
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)
    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculates a numerical compatibility score and explanation reasons for a song."""
    score = 0.0
    reasons: List[str] = []

    preferred_genre = user_prefs.get("genre") or user_prefs.get("favorite_genre")
    if preferred_genre and song["genre"].lower() == preferred_genre.lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    preferred_mood = user_prefs.get("mood") or user_prefs.get("favorite_mood")
    if preferred_mood and song["mood"].lower() == preferred_mood.lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    target_energy = user_prefs.get("energy") if "energy" in user_prefs else user_prefs.get("target_energy")
    if target_energy is not None:
        energy_diff = abs(song["energy"] - float(target_energy))
        energy_sim = max(0.0, 1.0 - energy_diff)
        score += energy_sim
        reasons.append(f"energy similarity (+{energy_sim:.2f})")

    return round(score, 2), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores all songs, sorts them in descending order, and returns the top k recommendations."""
    scored_candidates = []
    for song in songs:
        song_score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "no specific matches"
        scored_candidates.append((song, song_score, explanation))

    sorted_recommendations = sorted(scored_candidates, key=lambda item: item[1], reverse=True)
    return sorted_recommendations[:k]
