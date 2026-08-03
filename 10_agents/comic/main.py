import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

PROMPT = """
You are a professional comic book writer.

Generate a 6-panel comic.

Return only JSON using the following format:

{
  "title": "...",
  "characters": [
    {
      "name": "...",
      "description": "..."
    }
  ],
  "panels": [
    {
      "panel": 1,
      "scene": "...",
      "dialogue": "...",
      "image_prompt": "..."
    }
  ]
}

Theme:
A robot discovers an abandoned city.
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": MODEL,
        "prompt": PROMPT,
        "stream": False
    }
)

result = response.json()

text = result["response"]

print(text)

try:
    comic = json.loads(text)

    with open("comic.json", "w", encoding="utf8") as f:
        json.dump(comic, f, indent=4, ensure_ascii=False)

    print("Comic saved to comic.json")

except Exception:
    print("The response was not valid JSON.")