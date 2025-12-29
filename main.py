from fastapi import FastAPI
from retriever import retrieve
from llm import generate_answer

app = FastAPI()

@app.get("/ask")
def ask(query: str, top_k: int = 5):
    context = retrieve(query, top_k=top_k)
    answer = generate_answer(context, query)

    return {
        "top_k_used": top_k,
        "context": context,
        "answer": answer
    }
