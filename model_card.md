# Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Goal / Task

The goal of VibeFinder 1.0 is to suggest music tracks from a song catalog based on a listener's taste preferences. The model predicts which songs a user will enjoy by comparing the user's favorite genre, desired mood, and target energy against the attributes of each song.

---

## 3. Data Used

- Catalog Size: 18 songs loaded from `data/songs.csv` (expanded from 10 starter tracks with 8 diverse tracks).
- Features per Song: id, title, artist, genre, mood, energy (0.0 to 1.0), tempo_bpm, valence, danceability, and acousticness.
- Genres Represented: pop, lofi, rock, ambient, jazz, synthwave, indie pop, classical, hip-hop, r&b, metal, folk, electronic, blues, and reggae.
- Moods Represented: happy, chill, intense, relaxed, moody, focused, calm, confident, soulful, aggressive, reflective, energetic, melancholic, and uplifting.
- Dataset Limitations: The catalog is small, contains no audio waveforms or lyrics, and has only 1 to 2 tracks for several genres.

---

## 4. Algorithm Summary

The model uses a simple rule-based scoring system to evaluate songs:
1. Genre Match (+2.0 points): If the song genre matches the user favorite genre, add 2.0 points.
2. Mood Match (+1.0 point): If the song mood matches the user preferred mood, add 1.0 point.
3. Energy Similarity (up to +1.0 point): Calculated as `1.0 - abs(song_energy - target_energy)`. Songs with energy levels close to the target receive nearly a full point.

The highest possible score is 4.0 points. The system scores every song in the catalog, sorts them from highest score to lowest score, and returns the top k recommendations with a written explanation of awarded points.

---

## 5. Observed Behavior / Biases

- Genre Dominance: Because matching a genre awards 2.0 points, genre strongly outweighs mood and energy. For example, when testing a "Happy Pop" profile, the workout song "Gym Hero" scored second because of its pop tag, even though its mood was "intense" rather than "happy."
- Small Catalog Fallback: When a user selects a genre with only one track in the catalog, that track gets the top spot and all remaining recommendations are pulled from other genres based only on energy similarity.
- Conflicting Preferences: When given conflicting requirements (such as metal genre with chill mood), the system splits recommendations between loud metal tracks and soft lofi tracks, creating an inconsistent playlist.

---

## 6. Evaluation Process

We evaluated the recommender by running diverse listener profiles, performing logic experiments, and comparing pairwise outputs:
- Profiles Tested: High-Energy Pop, Chill Lofi, Deep Intense Rock, and an adversarial Conflicted Profile (Metal with Chill mood).
- Sensitivity Experiments: Shifting weights (halving genre to 1.0 and doubling energy similarity to 2.0) allowed cross-genre songs that matched the mood and energy to beat mismatched songs within the same genre. Removing the mood check completely flattened recommendations into simple energy filters.

### Evaluation Terminal Output

```text
Profile: High-Energy Pop
Preferences: genre=pop, mood=happy, energy=0.85
Recommendations:
  1. Sunrise City by Neon Echo (pop)
     Score: 3.97
     Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.97)
  2. Gym Hero by Max Pulse (pop)
     Score: 2.92
     Reasons: genre match (+2.0), energy similarity (+0.92)
  3. Rooftop Lights by Indigo Parade (indie pop)
     Score: 1.91
     Reasons: mood match (+1.0), energy similarity (+0.91)
  4. Street Cipher by Mic Masters (hip-hop)
     Score: 1.00
     Reasons: energy similarity (+1.00)
  5. Electric Horizon by Pulse Grid (electronic)
     Score: 0.97
     Reasons: energy similarity (+0.97)
--------------------------------------------------
Profile: Chill Lofi
Preferences: genre=lofi, mood=chill, energy=0.35
Recommendations:
  1. Library Rain by Paper Lanterns (lofi)
     Score: 4.00
     Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+1.00)
  2. Midnight Coding by LoRoom (lofi)
     Score: 3.93
     Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.93)
  3. Focus Flow by LoRoom (lofi)
     Score: 2.95
     Reasons: genre match (+2.0), energy similarity (+0.95)
  4. Spacewalk Thoughts by Orbit Bloom (ambient)
     Score: 1.93
     Reasons: mood match (+1.0), energy similarity (+0.93)
  5. Coffee Shop Stories by Slow Stereo (jazz)
     Score: 0.98
     Reasons: energy similarity (+0.98)
--------------------------------------------------
Profile: Deep Intense Rock
Preferences: genre=rock, mood=intense, energy=0.9
Recommendations:
  1. Storm Runner by Voltline (rock)
     Score: 3.99
     Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.99)
  2. Gym Hero by Max Pulse (pop)
     Score: 1.97
     Reasons: mood match (+1.0), energy similarity (+0.97)
  3. Electric Horizon by Pulse Grid (electronic)
     Score: 0.98
     Reasons: energy similarity (+0.98)
  4. Street Cipher by Mic Masters (hip-hop)
     Score: 0.95
     Reasons: energy similarity (+0.95)
  5. Iron Foundry by Rust & Iron (metal)
     Score: 0.94
     Reasons: energy similarity (+0.94)
--------------------------------------------------
Profile: Adversarial Conflicted Profile
Preferences: genre=metal, mood=chill, energy=0.95
Recommendations:
  1. Iron Foundry by Rust & Iron (metal)
     Score: 2.99
     Reasons: genre match (+2.0), energy similarity (+0.99)
  2. Midnight Coding by LoRoom (lofi)
     Score: 1.47
     Reasons: mood match (+1.0), energy similarity (+0.47)
  3. Library Rain by Paper Lanterns (lofi)
     Score: 1.40
     Reasons: mood match (+1.0), energy similarity (+0.40)
  4. Spacewalk Thoughts by Orbit Bloom (ambient)
     Score: 1.33
     Reasons: mood match (+1.0), energy similarity (+0.33)
  5. Gym Hero by Max Pulse (pop)
     Score: 0.98
     Reasons: energy similarity (+0.98)
--------------------------------------------------
```

### Explaining "Gym Hero" in Plain Language

To a non-programmer, it might seem confusing why an intense workout song like "Gym Hero" appears for someone who asked for "Happy Pop." This happens because of our scoring weights. A genre match gives 2.0 points, while a mood match only gives 1.0 point. Since "Gym Hero" is labeled as pop, it gets 2.0 points right away. Its energy is 0.93, which is very close to the target of 0.85, so it gets another 0.92 points. That gives it a total score of 2.92. Even though it is not a happy song, its genre points are high enough to push it into second place over happy songs from other genres.

### Pairwise Profile Comparisons

- High-Energy Pop vs. Chill Lofi: High-Energy Pop recommends loud, upbeat tracks like "Sunrise City" and "Gym Hero", while Chill Lofi shifts completely to quiet study tracks like "Library Rain" and "Midnight Coding". This makes sense because the energy target dropped from 0.85 to 0.35 and the preferred mood changed from happy to chill.
- Chill Lofi vs. Deep Intense Rock: Chill Lofi selects quiet beats with high acousticness, whereas Deep Intense Rock selects heavy guitar tracks like "Storm Runner" and "Iron Foundry". This confirms the system responds correctly to opposite ends of the energy spectrum.
- Deep Intense Rock vs. High-Energy Pop: Both profiles want high energy (0.85 to 0.90), but the rock profile places "Storm Runner" at the top while the pop profile places "Sunrise City" at the top. This proves the 2.0 point genre weight prevents high-energy songs from bleeding across genres.
- Deep Intense Rock vs. Adversarial Conflicted Profile: While the rock profile produces a coherent list, the conflicted profile (metal genre with chill mood) causes the system to compromise awkwardly. It shows one metal song at the top and then fills the rest of the list with quiet lofi songs, creating a mixed result.

---

## 7. Intended Use and Non-Intended Use

- Intended Use: Educational simulation, classroom learning, and exploring basic concepts of content-based recommendation systems in Python.
- Non-Intended Use: Real-world commercial streaming, production recommendation engines, audio playback platforms, or safety-critical personalization.

---

## 8. Ideas for Improvement

1. Tunable Feature Weights: Allow users to adjust sliders for how much they care about genre versus mood or energy.
2. Additional Audio Features: Incorporate valence (musical happiness) and acousticness into the scoring formula to capture finer nuances.
3. Catalog Diversity and Deduplication: Add a reranking step that prevents multiple songs by the same artist or subgenre from dominating all recommendation slots.

---

## 9. Personal Reflection

- Biggest Learning Moment: My biggest learning moment was discovering how strongly developer choices shape recommendations. Deciding that genre is worth 2.0 points while mood is worth 1.0 point directly dictated what songs appeared at the top, showing that algorithms always reflect their designers' assumptions.
- Using AI Tools and Verification: AI tools helped quickly create diverse song data, draft scoring functions, and brainstorm edge cases. However, I needed to double-check import paths between module mode and script mode, and verify that the mathematical formulas remained bounded between 0.0 and 1.0.
- Surprise About Simple Algorithms: I was surprised by how much simple arithmetic feels like genuine recommendation intelligence. Even a short formula calculating absolute differences can create a list of songs that feels cohesive and personalized.
- Next Steps for the Project: If I extended this project, I would build an interactive web interface with Streamlit, add user skip and like tracking to simulate collaborative filtering, and test the algorithm on a catalog of thousands of tracks.
