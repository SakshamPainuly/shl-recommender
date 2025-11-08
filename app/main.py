from fastapi import FastAPI
from pydantic import BaseModel
from .retriever import retrieve_assessments
from .utils import extract_text_from_url

app = FastAPI()


class RecommendRequest(BaseModel):
    query: str | None = None
    url: str | None = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/recommend")
def recommend(request: RecommendRequest):

    # ✅ Determine input source (URL or text)
    if request.url and not request.query:
        query_text = extract_text_from_url(request.url)
    else:
        query_text = request.query or ""

    # ✅ Call hybrid retriever
    results = retrieve_assessments(query_text)

    # ✅ Return response in SHL format
    return {
        "recommended_assessments": results
    }
