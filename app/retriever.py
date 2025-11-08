import json
import numpy as np
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
from .utils import detect_intents   # ✅ NEW


# ===============================
# ✅ Load Data Files
# ===============================

DATA_DIR = "data/"

with open(DATA_DIR + "catalog.json", "r") as f:
    CATALOG = json.load(f)

EMBEDDINGS = np.load(DATA_DIR + "embeddings.npy")

with open(DATA_DIR + "bm25.json", "r") as f:
    bm25_data = json.load(f)

tokenized_corpus = bm25_data["tokenized_corpus"]
BM25 = BM25Okapi(tokenized_corpus)

MODEL = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")


# ===============================
# ✅ Test Type Mapping
# ===============================

TEST_TYPE_MAP = {
    "K": "Knowledge & Skills",
    "P": "Personality & Behaviour"
}


def infer_test_type(name: str):
    name_lower = name.lower()

    # ✅ Technical → K
    technical_keywords = [
        "python", "java", "sql", "server", "developer",
        "analysis", "analyst", "data", "numerical",
        "digital", "automata", "technical", "advertising"
    ]

    for kw in technical_keywords:
        if kw in name_lower:
            return [TEST_TYPE_MAP["K"]]

    # ✅ Behavioural → P
    behavioral_keywords = [
        "leadership", "team", "opq", "behaviour",
        "sales", "interpersonal", "communication", "collaboration"
    ]

    for kw in behavioral_keywords:
        if kw in name_lower:
            return [TEST_TYPE_MAP["P"]]

    return [TEST_TYPE_MAP["K"]]   # default



# ===============================
# ✅ Hybrid Retrieval Function
# ===============================

def retrieve_assessments(query: str, top_k=10):
    if not query.strip():
        return []

    # --------------------------------------------
    # ✅ 1. BM25 Scores
    # --------------------------------------------
    query_tokens = query.lower().split()
    bm25_scores = np.array(BM25.get_scores(query_tokens))

    if bm25_scores.max() > 0:
        bm25_scores = bm25_scores / bm25_scores.max()

    # --------------------------------------------
    # ✅ 2. Embedding Scores
    # --------------------------------------------
    query_emb = MODEL.encode([query])[0]
    query_emb = query_emb / np.linalg.norm(query_emb)

    doc_emb = EMBEDDINGS / np.linalg.norm(EMBEDDINGS, axis=1, keepdims=True)
    emb_scores = np.dot(doc_emb, query_emb)

    emb_scores = (emb_scores - emb_scores.min()) / (emb_scores.max() - emb_scores.min() + 1e-9)

    # --------------------------------------------
    # ✅ 3. Base Hybrid Score
    # --------------------------------------------
    final_scores = 0.5 * bm25_scores + 0.5 * emb_scores

    # --------------------------------------------
    # ✅ 4. Intent Detection (K/P balancing)
    # --------------------------------------------
    needs_tech, needs_beh = detect_intents(query)

    if needs_tech:
        for i, item in enumerate(CATALOG):
            if "Knowledge & Skills" in infer_test_type(item["name"]):
                final_scores[i] += 0.15   # small boost

    if needs_beh:
        for i, item in enumerate(CATALOG):
            if "Personality & Behaviour" in infer_test_type(item["name"]):
                final_scores[i] += 0.15

    # --------------------------------------------
    # ✅ 5. Sort Top K
    # --------------------------------------------
    top_indices = final_scores.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        item = CATALOG[idx]

        results.append({
            "name": item["name"],
            "url": item["url"],
            "description": item.get("description", ""),
            "duration": item.get("duration", 0),
            "adaptive_support": item.get("adaptive_support", "No"),
            "remote_support": item.get("remote_support", "No"),
            "test_type": infer_test_type(item["name"])
        })

    return results
