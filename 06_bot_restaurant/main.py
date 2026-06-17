from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    file_name: str


def load_txt(file_name):
    with open(f"knowledge/{file_name}.txt", "r", encoding="utf-8") as f:
        return f.read()


def build_knowledge(text):
    data = {}

    for line in text.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip().lower()] = value.strip()

    return data
    
def find_answer(question, knowledge):
    question = question.lower()

    for key, value in knowledge.items():
        if key in question:
            return value
        
    return None

@app.post("/chat")
def chat(req: ChatRequest):

    text = load_txt(req.file_name)
    knowledge = build_knowledge(text)

    answer = find_answer(req.message, knowledge)

    if answer:
        return {"answer": answer}
    
    return {
        "answer": "I don't Know thet yet.",
        "available_data": knowledge
    }
    