import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# -----------------------------
# OLLAMA FUNCTION
# -----------------------------

def call_ollama(prompt, model="llama3"):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    return response.json()["response"]


# -----------------------------
# PDF TOOL (your first real tool)
# -----------------------------

def create_pdf(filename, content):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    y = height - 50

    lines = content.split("\n")

    for line in lines:
        c.drawString(50, y, line[:100])  # simple safe limit
        y -= 20

        if y < 50:
            c.showPage()
            y = height - 50

    c.save()


# -----------------------------
# AGENT
# -----------------------------

class PDFAgent:
    def __init__(self):
        pass

    def generate_content(self, topic):
        prompt = f"""
You are a professional content writer.

Create a structured report about:
{topic}

Include:
- Title
- Introduction
- 3 main sections
- Conclusion

Format it clearly for a PDF document.
"""

        return call_ollama(prompt)

    def run(self, topic):
        print("\nAGENT STARTED\n")

        print("Generating content...\n")
        content = self.generate_content(topic)

        print("Creating PDF...\n")
        filename = "output.pdf"
        create_pdf(filename, content)

        print(f"\nDONE -> {filename}")


# -----------------------------
# EXECUTION
# -----------------------------

if __name__ == "__main__":
    agent = PDFAgent()

    topic = input("Enter PDF topic:\n> ")

    agent.run(topic)