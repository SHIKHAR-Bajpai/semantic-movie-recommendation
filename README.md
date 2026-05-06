# 🎬 Semantic Movie Recommendation System

A semantic movie recommendation/search system built using:

- Sentence Transformers
- Cosine Similarity
- Local embeddings (no API limits)
- Semantic search instead of keyword matching

This project recommends movies based on the **meaning** of the user query rather than exact keywords.

---

# 🚀 Features

✅ Semantic movie search  
✅ Local embedding generation  
✅ No API quota/rate limits  
✅ Fast cosine similarity retrieval  
✅ Persistent embeddings using pickle  
✅ Uses transformer-based embedding models  

---

# 🧠 How It Works

```text
Movie Dataset
    ↓
Generate Embeddings
    ↓
Store Embeddings
    ↓
User Query
    ↓
Query Embedding
    ↓
Cosine Similarity
    ↓
Top Matching Movies
```

---

# 📦 Tech Stack

- Python
- Pandas
- NumPy
- Sentence Transformers
- BAAI/bge-base-en-v1.5

---

# 📂 Project Structure

```bash
semantic_movie_recommendation/
│
├── main.py
├── embeddings.pkl
├── IMDB-movies-dataset.csv
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your_repo_url>
cd semantic_movie_recommendation
```

---

## 2️⃣ Create Virtual Environment

### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
python main.py
```

---

# 💡 Example Query

```text
Enter your types and mood for a movie:
An intense spy thriller involving undercover missions
```

---

# 📌 Example Output

```text
Here are the top 10 movies recommended for you:

4.6/5 -----> Pathaan
4.5/5 -----> Spy
4.4/5 -----> Tehran
```

---

# 🧠 Core Concepts Used

## 🔹 Embeddings

Movie descriptions are converted into vector representations using:

```text
BAAI/bge-base-en-v1.5
```

This allows semantic understanding of movie meaning.

---

## 🔹 Cosine Similarity

Similarity between:
- user query embedding
- movie embeddings

is calculated using cosine similarity.

Higher score = better semantic match.

---

# 📁 Embedding Persistence

Embeddings are stored locally using:

```python
df.to_pickle("embeddings.pkl")
```

This avoids regenerating embeddings every run.

---

# ⚠️ Important Notes

## If You Change:
- embedding model
- dataset
- combined_text structure

Delete old embeddings:

```bash
rm embeddings.pkl
```

Then rerun project.

---

# 🔥 Future Improvements

- Add FastAPI backend
- Add React frontend
- Add genre filtering
- Add hybrid search
- Add RAG explanation layer
- Store embeddings in pgvector
- Add chatbot interface

---

# 📚 Learning Outcomes

This project teaches:

- Semantic Search
- Embeddings
- Vector Similarity
- Retrieval Systems
- AI Recommendation Systems
- Foundations of RAG

---

# 🚀 Future Goal

Convert this into a full:

```text
Retrieval-Augmented Generation (RAG) System
```

where:
- movies are retrieved
- LLM explains recommendations naturally

---

# 👨‍💻 Author

Built as part of an AI Engineering learning journey.
