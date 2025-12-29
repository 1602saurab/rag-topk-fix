import numpy as np
from embeddings import embed
from data import DOCUMENTS

DOC_EMBEDDINGS = embed(DOCUMENTS)  ### (number of docs, embedding_dimension)

def retrieve(query, top_k=5, threshold=0.5):
    query_vec = embed([query])[0]

    scores = np.dot(DOC_EMBEDDINGS, query_vec)

    ranked = list(zip(DOCUMENTS, scores))
    ranked.sort(key=lambda x: x[1], reverse=True)

    # 🔥 PRODUCTION FIX: similarity filtering
    filtered = [doc for doc, score in ranked if score >= threshold]

    return filtered[:top_k]

