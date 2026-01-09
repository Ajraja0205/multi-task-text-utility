import chromadb
from chromadb.config import Settings

# Initialize ChromaDB client (persistent)
chroma_client = chromadb.Client(
    Settings(
        persist_directory="chroma_db",
        anonymized_telemetry=False
    )
)

# Create or get collection
collection = chroma_client.get_or_create_collection(
    name="chat_memory"
)

def store_chat(question: str, answer: str):
    collection.add(
        documents=[answer],
        metadatas=[{"question": question}],
        ids=[str(hash(question))]
    )


def retrieve_similar(query: str, threshold: float = 0.15):
    results = collection.query(
        query_texts=[query],
        n_results=1
    )

    # ✅ Defensive checks
    if (
        not results
        or "documents" not in results
        or "distances" not in results
        or not results["documents"]
        or not results["documents"][0]
        or not results["distances"]
        or not results["distances"][0]
    ):
        return None

    distance = results["distances"][0][0]

    # Lower distance = more similar
    if distance < threshold:
        return results["documents"][0][0]

    return None


