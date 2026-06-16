from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    file_name: str


def load_txt(file_name):
    with open(f"knowledge/{file_name}.txt", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/chat")
def chat(req: ChatRequest):

    context = load_txt(req.file_name)

    question = req.message.lower()

    if "opening hours" in question:
        return {
            "answer": "We are open from 12:00 to 22:00"
        }

    if "menu" in question:
        return {
            "answer": "We have pizza, pasta and lasagna"
        }

    if "phone" in question:
        return {
            "answer": "Our phone number is 123456789"
        }

    if "address" in question:
        return {
            "answer": "We are at Calle Mayor 12"
        }

    if "reservation" in question:
        return {
            "answer": "Reservations are only by phone"
        }

    return {
        "answer": f"I don't understand the question.\n\nAvailable information:\n{context}"
    }