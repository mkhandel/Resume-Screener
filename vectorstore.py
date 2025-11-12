import os
import faiss
import numpy as np
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


#text-embedding-3-small does semantic matching, meaning it matches meanings rather than just keywords
def get_embedding(text, model="text-embedding-3-small"):
    #openai's model converts text (in this case, a resume or job description) into a vector
    resp = client.embeddings.create(model=model, input=text)
    return np.array(resp.data[0].embedding, dtype=np.float32)

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def build_faiss_index(embeddings):
    if not embeddings:
        raise ValueError("No embeddings provided")
    #create an empty FAISS index that is configured to store vectors of length dim
    dim = len(embeddings[0]["embedding"])
    index = faiss.IndexFlatL2(dim)
    #why does FAISS rely on NumPy arrays? NumPy stores array elements at contiguous bloks of memory, making it super fast. It also supports vectorized operations, which, when asked 2*[1,3], would give [2, 6] instead of [1,3,1,3] like a regular array would give
    vectors = np.array([r["embedding"] for r in embeddings])
    index.add(vectors)
    return index

def search_faiss(index, query, resumes, top_k=5):
    #this function searches the faiss index and returns the top 5 resumes
    #matching the job description

    #remember, the index is information on all the resumes as vectors
    #the query is the job description
    query_embedding = get_embedding(query)
    D, I = index.search(np.array([query_embedding]), top_k)
    results = []
    for idx, score in zip(I[0], D[0]):
        if idx < len(resumes):
            results.append({
                "filename": resumes[idx]["filename"],
                "content": resumes[idx]["content"],
                "score": float(score)
            })
    return results
