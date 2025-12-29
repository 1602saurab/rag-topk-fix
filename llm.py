def generate_answer(context, query):
    if not context:
        return "No relevant context found."

    return f"""
Answer based on trusted context:

Context:
{context}

Question:
{query}
"""
