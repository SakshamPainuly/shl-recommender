import requests
from bs4 import BeautifulSoup
import re


def clean_text(text: str) -> str:
    """Clean extracted text."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_text_from_url(url: str) -> str:
    """
    Extracts readable text from a job description URL.
    Works for LinkedIn, Indeed, Naukri, etc.
    """
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/118.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "lxml")

        # Remove scripts, styles, navbars, footers
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.extract()

        # Extract main text
        texts = soup.get_text(separator=" ")

        return clean_text(texts)

    except Exception as e:
        print("URL extract error:", e)
        return ""
def detect_intents(query: str):
    """Very simple intent detection based on keywords."""

    q = query.lower()

    technical_keywords = [
        "python", "java", "sql", "javascript", "developer",
        "engineer", "coding", "programming", "data", "analysis",
        "react", "node", "frontend", "backend"
    ]

    behavioral_keywords = [
        "communication", "team", "collaboration", "leadership",
        "behaviour", "personality", "attitude", "culture fit",
        "soft skills", "stakeholder", "adaptability"
    ]

    needs_technical = any(k in q for k in technical_keywords)
    needs_behavioral = any(k in q for k in behavioral_keywords)

    return needs_technical, needs_behavioral
