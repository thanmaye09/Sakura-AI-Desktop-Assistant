"""Search links and optional OpenAI API response generation."""
import os
from urllib.parse import quote_plus


def google_search_url(query: str) -> str:
    if not query.strip():
        raise ValueError("Enter a search query")
    return "https://www.google.com/search?q=" + quote_plus(query.strip())


def ask_openai(prompt: str) -> str:
    if not prompt.strip():
        raise ValueError("Enter a question first")
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY in your .env file to enable API answers")
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("Install optional AI dependencies: pip install -r requirements-ai.txt") from exc

    client = OpenAI()
    result = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.5"),
        input=prompt.strip(),
        store=False,
    )
    return result.output_text or "No text was returned."

