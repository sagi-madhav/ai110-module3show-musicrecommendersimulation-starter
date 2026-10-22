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

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
