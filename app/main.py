from fastapi import FastAPI
from app.api.routes import router
from app.services.vector_store_service import VectorStore
from app.workflows.agent_graph import build_graph
import os

app = FastAPI()

# Existing components (UNCHANGED)
app.include_router(router, prefix="/api")
graph = build_graph()
vector_store = VectorStore()


# -------------------------------
# CHUNKING FUNCTION
# -------------------------------
def chunk_text(text, chunk_size=120):
    words = text.split()
    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]


# -------------------------------
# STARTUP: LOAD + CHUNK DOCUMENTS
# -------------------------------
@app.on_event("startup")
def load_documents():

    docs = []
    metadatas = []

    folder_path = "data/market_docs"

    for file in os.listdir(folder_path):

        if not file.endswith(".txt"):
            continue

        with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
            text = f.read()

        #  NEW: Chunking
        chunks = chunk_text(text)

        for chunk in chunks:
            docs.append(chunk)
            metadatas.append({
                "source": file,
                "text": chunk
            })

    #  IMPORTANT: pass metadata also
    vector_store.add_documents(docs, metadatas)

    print(f" Loaded {len(docs)} chunks into vector store")