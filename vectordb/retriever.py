from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DB_PATH = "vectordb/chroma_db"

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embedding
)

# Increased k for better context retrieval
retriever = db.as_retriever(search_kwargs={"k": 5})
