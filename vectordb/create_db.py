import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_PATH = "data/pdfs"
DB_PATH = "vectordb/chroma_db"


def load_documents():
    docs = []
    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            docs.extend(loader.load())
    return docs


def create_vector_db():

    docs = load_documents()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80
    )

    chunks = text_splitter.split_documents(docs)

    embedding = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )

    db.add_documents(chunks)

    print("✅ Vector DB Created Successfully")


if __name__ == "__main__":
    create_vector_db()
