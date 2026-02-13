from agent.router import agent_decision
from vectordb.retriever import retriever
import ollama

MODEL_NAME = "llama3:8b"


def direct_answer(query):
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": query}]
    )
    return response["message"]["content"]


def rag_answer(query):

    action = agent_decision(query)
    print(f"Agent Decision: {action}")

    # DIRECT PATH
    if action == "direct":
        return direct_answer(query)

    # SEARCH PATH
    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Debug (temporary)
    print("\nRetrieved Context Preview:\n", context[:500])

    prompt = f"""
    You are an AI assistant.

    Use the context below to answer the question.
    If the user asks for a summary, summarize the context clearly.

    Context:
    {context}

    Question:
    {query}
    """

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

