
## SHL Assessment Recommender (RAG)

A lightweight Retrieval-Augmented tool that recommends SHL assessments from a catalog using a hybrid ranker (BM25 + Sentence Embeddings) with a simple Gradio web UI.

## 🚀 Live Demo

## ✅ Web App (Gradio UI)

🔗 [https://sakshampainuly-shl-recommender.hf.space/](https://sakshampainuly-shl-recommender.hf.space/)

## ✅ Programmatic Access (Gradio Inference API)

## Endpoint (POST):

[https://sakshampainuly-shl-recommender.hf.space/run/search](https://sakshampainuly-shl-recommender.hf.space/run/search)

## Example:

## curl -X POST \

## -H "Content-Type: application/json" \

  -d '{"data":["Hiring a Python developer with SQL"]}' \

  [https://sakshampainuly-shl-recommender.hf.space/run/search](https://sakshampainuly-shl-recommender.hf.space/run/search)

✅ Returns a Markdown string of top recommendations

✅ (This Space is Gradio-only — no custom FastAPI routes)

## ✨ Features

🔎 Hybrid retrieval: BM25 (keyword) + all-mpnet-base-v2 (semantic)

🧭 Rule-based test-type inference (Knowledge & Skills / Personality & Behaviour)

## 🖥️ Gradio UI for manual exploration

📦 Precomputed indices for fast inference and low compute usage

## 🧠 How It Works

## Catalog prepared → catalog.json

## BM25 tokens → bm25.json

Embeddings (768-dim mpnet vectors) → embeddings.npy

## Query-time ranking:

## Compute BM25 score

Compute cosine similarity using sentence embeddings

## Combine:

Final Score = 0.5 × BM25  +  0.5 × Embedding Score

Return Top-K assessments with test-type tags.

## 🗂️ Repo Structure

## shl-recommender/

## ├── app/

│   ├── main.py            # (if using FastAPI locally; optional)

│   ├── retriever.py       # hybrid retrieval logic (optional)

## │   ├── utils.py

## │   ├── data_loader.py

## │   └── index_builder.py

## ├── data/

│   ├── catalog.json       # SHL items (name, url, …)

## │   ├── bm25.json          # BM25 tokens

## │   └── embeddings.npy     # 768-d vectors

## ├── README.md

## ├── requirements.txt

└── (optional) Dockerfile, evaluation notebook, submission CSV

## ✅ Minimal runtime needs only:

## app.py

## requirements.txt

data/ files (catalog.json, bm25.json, embeddings.npy)

## 🔧 Local Run

## Install

## pip install -r requirements.txt

## Start the app

## python app.py

## Open UI

[http://localhost:7860](http://localhost:7860)

## 🧪 Quick Usage (UI)

## Try a JD like:

“Hiring a Python developer with SQL and good communication.”

You’ll receive 5–10 recommended assessments with URLs and a test-type:

## ✅ Knowledge & Skills

## ✅ Personality & Behaviour

## 📡 Programmatic Usage (Gradio Inference API)

## Endpoint (POST):

## .../run/search

## Body:

## { "data": ["<your query here>"] }

## Response:

Markdown with top recommendations.

## 📦 Requirements

## gradio

## sentence-transformers

## rank-bm25

## numpy

## pandas

✅ Models download automatically on first run.

## 📝 Notes

## ✅ No scraping needed

## ✅ Test-type inference is rule-based

✅ Designed to be fast, simple & aligned with assignment requirements

## 👤 Author

## Saksham Painuly

Feel free to reach out or open an issue.
=======
# shl-recommender
Web-based SHL assessment recommender using hybrid RAG (BM25 + Embeddings)
>>>>>>> 451f0dfd3c8851cec81ebb670120501b0013f224
