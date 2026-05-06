import pandas as pd
import numpy as np
import os
from google import genai
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# use this for using local model for embedding
model = SentenceTransformer(
    "BAAI/bge-base-en-v1.5"
)
def get_embeddings(text):
    return model.encode(text)

# use this for using gemini-cloud model for embedding 
# def get_embeddings_cloud(text):
#     response = client.models.embed_content(
#         model="gemini-embedding-2",
#         contents=text
#     )

#     return response.embeddings[0].values

def cosine_sim(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

def normalize_score(score):
    normalized = ((score + 1) / 2) * 5
    return round(normalized, 1)

def search(query):
    query_emd = get_embeddings(query)
    top_k = 10
    scores = []

    for text,data in zip(df["movie_name"], df["embedding"]):
        score = cosine_sim(query_emd , data)
        scores.append((text, score))

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    return scores[:top_k]
    
if os.path.exists("embeddings.pkl"):
    df = pd.read_pickle("embeddings.pkl")
else:
    df = pd.read_csv('IMDB-movies-dataset.csv')
    df["combined_text"] = (df["genre"] + " " + df["overview"])
    
    df["embedding"] = df["combined_text"].apply(get_embeddings)
    df.to_pickle("embeddings.pkl")


def recommend():

    query = input("\nEnter your genre or mood for a movie: ")
    results = search(query)
    results = sorted(results, key=lambda x: x[1], reverse=True)

    print("\nHere are the top 10 movies recommended for you:\n")
    i = 1 
    for text, score in results:
        matched_recommendation = normalize_score(score)
        print(f"{i})  {matched_recommendation:.1f} --> {text}")
        i += 1


recommend()

