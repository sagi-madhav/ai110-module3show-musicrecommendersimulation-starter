# Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch 1.0

---

## 2. Intended Use  

This model is a prototype content-based music recommender designed for educational simulation and exploration. It matches user preferences against a catalog of songs to produce top song recommendations with plain language explanations. It assumes the user can identify their preferred genre, mood, and energy level. It is built for learning and demonstration rather than large-scale commercial streaming.

---

## 3. How the Model Works  

The model uses a simple rule-based scoring system to judge how well each song fits what the listener wants. It looks at three main qualities:
1. Genre Match: If the song belongs to the user's favorite genre, it earns 2.0 points.
2. Mood Match: If the song matches the user's preferred mood, it earns 1.0 point.
3. Energy Similarity: The model checks how close the song's energy level is to the user's target energy. Songs that are very close in energy earn up to 1.0 point.

Each song receives a total score between 0.0 and 4.0 points, alongside a list of specific reasons explaining why points were awarded. The model sorts all songs from highest to lowest score and presents the top recommendations to the user.

---

## 4. Data  

The simulation runs on a curated catalog in `data/songs.csv`:
- Catalog Size: 18 songs (expanded from the initial 10 starter tracks with 8 new diverse entries).
- Genres Represented: pop, lofi, rock, ambient, jazz, synthwave, indie pop, classical, hip-hop, r&b, metal, folk, electronic, blues, and reggae.
- Moods Represented: happy, chill, intense, relaxed, moody, focused, calm, confident, soulful, aggressive, reflective, energetic, melancholic, and uplifting.
- Audio Features: Each song includes energy (0.0 to 1.0), tempo in beats per minute, valence (happiness), danceability, and acousticness.
- Missing Data: The catalog does not include lyrics, language metadata, artist popularity, release era, or dynamic audio waveforms.

---

## 5. Strengths  

- Predictable and Explainable: Every single recommendation comes with a direct mathematical explanation detailing exactly which points were awarded.
- Strong Alignment for Standard Profiles: When a user provides straightforward preferences (like lofi and chill), the top tracks match human intuition closely.
- Smooth Proximity Scoring: The energy formula rewards songs that are near the user's preference along a gradient rather than treating energy as a binary match.

---

## 6. Limitations and Bias 

During our experiments, we discovered that the system heavily over-prioritizes genre over mood and vibe because a genre match awards 2.0 points out of a maximum of 4.0. For example, when testing the High-Energy Pop profile, "Gym Hero" ranked second because it matched the pop genre, even though its mood was "intense" rather than "happy," beating out an indie pop track that actually matched the "happy" mood. Furthermore, because several genres in the catalog have only a single song, once that song is recommended, all remaining slots are filled with tracks from unrelated genres based solely on energy proximity. Users with cross-genre or non-traditional music tastes risk receiving poor recommendations because the system cannot recognize stylistic overlap outside exact text labels.

---

## 7. Evaluation  

We evaluated the recommender using four distinct user profiles to test its accuracy, consistency, and vulnerability to conflicting preferences:
1. High-Energy Pop: genre=pop, mood=happy, energy=0.85
2. Chill Lofi: genre=lofi, mood=chill, energy=0.35
3. Deep Intense Rock: genre=rock, mood=intense, energy=0.90
4. Adversarial Conflicted Profile: genre=metal, mood=chill, energy=0.95

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

To a non-programmer, it might seem confusing why an intense workout anthem like "Gym Hero" keeps showing up for a listener who asked for "Happy Pop." This happens because of how points are weighted in the algorithm recipe. The system awards 2.0 points for a genre match, but only 1.0 point for a mood match. Since "Gym Hero" is labeled as pop, it immediately receives 2.0 points. Because its energy is 0.93 (very close to the target of 0.85), it receives another 0.92 points, giving it a total of 2.92. Even though it is not "happy," its genre points outweigh happier songs from other genres, so it earns the second spot on the list.

### Pairwise Profile Comparisons

- High-Energy Pop vs. Chill Lofi: High-Energy Pop populates the list with loud, upbeat tracks like "Sunrise City" and "Gym Hero", while Chill Lofi completely transitions to quiet study music like "Library Rain" and "Midnight Coding". This makes sense because the energy target dropped from 0.85 down to 0.35 and the preferred mood changed from happy to chill.
- Chill Lofi vs. Deep Intense Rock: Chill Lofi selects mellow beats with high acousticness, whereas Deep Intense Rock selects heavy distorted tracks like "Storm Runner" and "Iron Foundry". This confirms the model effectively handles opposite ends of the intensity spectrum.
- Deep Intense Rock vs. High-Energy Pop: Both profiles seek high energy (0.85 to 0.90), but the rock profile ranks "Storm Runner" at the top while the pop profile ranks "Sunrise City" at the top. This demonstrates that the 2.0 point genre weight successfully prevents high-energy songs from bleeding indiscriminately across genres.
- Deep Intense Rock vs. Adversarial Conflicted Profile: While Deep Intense Rock yields cohesive suggestions, the conflicted profile (metal with chill mood at 0.95 energy) exposes how the system breaks down. It recommends "Iron Foundry" for the metal genre points, but then fills slots 2 through 4 with quiet lofi songs to satisfy the chill mood, creating a disjointed listening queue.

---

## 8. Future Work  

- Tunable Weights: Allow users to specify whether they care more about genre or emotional mood.
- Multi-Attribute Scoring: Incorporate valence (musical positivity) and acousticness into the proximity score to better distinguish cheerful acoustic music from electronic dance tracks.
- Diversity and Deduplication Filters: Prevent a single artist or genre from dominating all secondary recommendation slots.
- Hybrid Collaborative Filtering: Combine content attributes with actual user behavior data, such as skip counts and playlist additions.

---

## 9. Personal Reflection  

Building this simulation demystified how streaming platforms turn subjective musical taste into objective mathematical rankings. By translating songs into numerical features and applying weighted scoring rules, we can automate recommendations that often feel intuitive. However, the simulation also showed how easily algorithmic assumptions create blind spots. When genre is weighted heavily, the system can trap users in rigid categories and ignore great tracks with the exact mood they want. Designing fair AI systems requires constantly testing edge cases and questioning our default weights.  
