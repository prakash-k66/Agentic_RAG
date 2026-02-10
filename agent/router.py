import ollama

MODEL_NAME = "gemma:2b"


def agent_decision(query):

    decision_prompt = f"""
    You are an AI routing agent.

    Decide whether the user's question requires searching
    in uploaded documents.

    Rules:
    - Greetings or casual conversation → DIRECT
    - General knowledge questions → DIRECT
    - Questions about documents, PDFs, reports, or uploaded data → SEARCH

    Respond with ONLY one word:
    DIRECT or SEARCH

    Question: {query}
    """

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": decision_prompt}]
    )

    decision = response["message"]["content"].strip().upper()

    if "SEARCH" in decision:
        return "search"

    return "direct"
