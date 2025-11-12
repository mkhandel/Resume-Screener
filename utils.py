import os
from vectorstore import get_embedding, cosine_similarity

def load_resumes(folder_path):
    resumes = []
    #for each file name in the directory
    for i, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                resumes.append({
                    "id": i,                  # assign a numeric ID
                    "filename": filename,
                    "content": f.read()
                })
    return resumes

def embed_resumes(resumes):
    embeddings = []
    for r in resumes:
        emb = get_embedding(r["content"])
        embeddings.append({
            "id": r["id"],
            "filename": r["filename"],
            "content": r["content"],
            "embedding": emb
        })
    return embeddings

#code below was phased out
"""
def search_resumes(query, resumes, resume_embeddings, top_k=5):
    query_embedding = get_embedding(query)
    scores = [cosine_similarity(query_embedding, emb["embedding"]) for emb in resume_embeddings]
    ranked = sorted(zip(scores, resumes), key=lambda x: x[0], reverse=True)
    results = [{"filename": r["filename"], "score": float(s)} for s, r in ranked[:top_k]]
    return results
"""
