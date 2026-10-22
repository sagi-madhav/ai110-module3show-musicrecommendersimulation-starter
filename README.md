# Music Recommender Simulation

## Project Summary

This project is a Python-based music recommender simulation. It loads song data from a CSV file, accepts a user profile with preferred music characteristics, calculates a similarity score for every song using transparent scoring rules, and ranks the catalog to return top song recommendations with clear explanations.

---

## How The System Works

Real-world music streaming platforms like Spotify and YouTube use two main approaches to recommend songs: collaborative filtering and content-based filtering. Collaborative filtering uses collective user behavior, analyzing listening histories, playlist additions, likes, and skips to find users with similar habits and recommend what peers enjoyed. Content-based filtering analyzes the attributes of the music itself, such as genre, mood, tempo, energy, and acoustic qualities. Real systems blend both methods at scale. Our simulation focuses on content-based filtering, matching song attributes directly against a user taste profile.

### Features Used in the Simulation

Specific features used by each `Song`:
- `id`: Unique integer identifier for the song
- `title`: Name of the song track
- `artist`: Recording artist or band
- `genre`: Musical style (for example: pop, lofi, rock, jazz, synthwave)
- `mood`: Emotional vibe (for example: happy, chill, intense, relaxed, moody)
- `energy`: Numerical intensity value between 0.0 (very calm) and 1.0 (very energetic)
- `tempo_bpm`: Song speed measured in beats per minute
- `valence`: Positiveness of the musical sound between 0.0 and 1.0
- `danceability`: How suitable the track is for dancing between 0.0 and 1.0
- `acousticness`: Confidence score between 0.0 and 1.0 that the track is acoustic

Specific features used by `UserProfile`:
- `favorite_genre`: The genre the user wants to listen to
- `favorite_mood`: The mood or feeling the user wants
- `target_energy`: The preferred energy level on a 0.0 to 1.0 scale
- `likes_acoustic`: Boolean indicator for whether the user prefers acoustic sounds

### Algorithm Recipe

The recommender uses a transparent point-based scoring rule:
1. Genre Match (+2.0 points): Awarded when the song genre matches the user favorite genre exactly.
2. Mood Match (+1.0 point): Awarded when the song mood matches the user favorite mood exactly.
3. Energy Similarity (up to +1.0 point): Computed as `1.0 - abs(song_energy - target_energy)`. Songs with energy levels close to the target receive nearly a full point, while distant songs receive fewer points.

The maximum possible score for a song is 4.0 points.

### Recommendation Pipeline

The recommendation process runs as follows:
1. Input: A user profile dictionary containing target preferences (favorite genre, favorite mood, target energy).
2. Process: The program loops over every song in the catalog, evaluates it against the user profile using the scoring recipe, and records both the numerical score and the match reasons.
3. Output: The program sorts all evaluated songs from highest score to lowest score and returns the top k ranked songs.

### Expected Biases

- Genre Dominance: Because matching a genre provides 2.0 points out of a total possible 4.0 points, the system heavily favors genre over mood or vibe. Great songs that share the user target mood and energy might be overlooked if they belong to another genre.
- Linear Energy Gap: The energy scoring treats distance linearly across the whole scale, which may treat small energy variations in quiet acoustic music the same as large shifts in high energy music.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```text
Loaded songs: 18

Top recommendations:

Profile: Default Pop/Happy
Preferences: genre=pop, mood=happy, energy=0.8
Recommendations:
  1. Sunrise City by Neon Echo (pop)
     Score: 3.98
     Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)
  2. Gym Hero by Max Pulse (pop)
     Score: 2.87
     Reasons: genre match (+2.0), energy similarity (+0.87)
  3. Rooftop Lights by Indigo Parade (indie pop)
     Score: 1.96
     Reasons: mood match (+1.0), energy similarity (+0.96)
  4. Night Drive Loop by Neon Echo (synthwave)
     Score: 0.95
     Reasons: energy similarity (+0.95)
  5. Street Cipher by Mic Masters (hip-hop)
     Score: 0.95
     Reasons: energy similarity (+0.95)
--------------------------------------------------
```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



