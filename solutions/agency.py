from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI(title="AI Real Estate Lead Manager")


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:8b"


class LeadRequest(BaseModel):
    message: str


SYSTEM_PROMPT = """
You are an AI assistant working for a real estate agency.

Your job is to analyse incoming customer enquiries.

Extract:

- Intent (buy, rent, sell)
- Budget
- Bedrooms
- Preferred location
- Urgency
- Priority (Low, Medium, High)
- One sentence summary

Then generate a professional email reply.

Return everything in clean Markdown.
"""


@app.post("/analyse")
def analyse_lead(request: LeadRequest):

    prompt = f"""
{SYSTEM_PROMPT}

Customer message:

{request.message}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return {
        "analysis": data["response"]
    }


@app.get("/")
def home():
    return {
        "message": "AI Real Estate Lead Manager is running."
    }