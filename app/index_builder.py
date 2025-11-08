import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict

INDEX_DIR = "data/"

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


# -------------------------------
# Load Embedding Model
# -------------------------------
def load_embedding_model():
    """
    Load sentence transformer model.
    """
    return SentenceTransformer(MODEL_NAME)


# -------------------------------
# Prepare text for BM25 + embeddings
# -------------------------------
def prepare_text(assessment: Dict) -> str:
    """
    Combine important fields into a single text string.
    Used for BM25 and embedding encoding.
    """
    parts = [
        assessment.get("name", ""),
        assessment.get("description", ""),
        " ".join(assessment.get("test_type", []))
    ]
    return " ".join(parts).strip()


# -------------------------------
# Build Index (BM25, Embeddings, FAISS)
# -------------------------------
def build_index(assessments: List[Dict]):
    """
    Build BM25 + Embedding + FAISS index.
    Full logic to be added later.
    """
    print("Building index... (placeholder)")

    # Prepare text corpus
    texts = [prepare_text(a) for a in assessments]

    # TODO: BM25 creation
    # TODO: Embedding encoding
    # TODO: FAISS index creation

    index_data = {
        "texts": texts,
        "assessments": assessments,
        "bm25": None,
        "embeddings": None,
        "faiss_index": None
    }

    return index_data


# -------------------------------
# Save Index Files
# -------------------------------
def save_index(index_data):
    """
    Save index files into /data folder.
    """
    print("Saving index... (placeholder)")
    os.makedirs(INDEX_DIR, exist_ok=True)

    # Save basic info
    with open(os.path.join(INDEX_DIR, "index.json"), "w", encoding="utf-8") as f:
        json.dump({"count": len(index_data.get("assessments", []))}, f)


# -------------------------------
# Load Index Files
# -------------------------------
def load_index():
    """
    Load index files from /data folder.
    Currently returns None until implementation begins.
    """
    print("Loading index... (placeholder)")
    return None
