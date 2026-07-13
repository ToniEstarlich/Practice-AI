import requests
import os


class SchemeAgent:

    def __init__(self, model="llama3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"


    def ask_brain(self, prompt):

        print("🔗 Connecting to Ollama...")

        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            print("🧠 Generating response...")

            response = requests.post(
                self.url,
                json=data,
                timeout=300
            )

            print("📩 Response received")
            print("Status:", response.status_code)

            result = response.json()

            return result["response"]

        except requests.exceptions.ConnectionError:

            print("❌ Cannot connect to Ollama.")
            print("Run: ollama serve")

            return ""

        except requests.exceptions.Timeout:

            print("⏳ Ollama took too long.")

            return ""


    def create_website(self, idea):

        prompt = f"""
You are a professional frontend developer.

Create a complete single file index.html.

Requirements:

- Use HTML5.
- Include CSS inside <style>.
- Include JavaScript inside <script>.
- Responsive design.
- Modern UI.
- No external frameworks.

The website idea is:

{idea}

Return ONLY the HTML code.
Do not use markdown.
Do not explain.
"""


        html = self.ask_brain(prompt)


        if not html:
            print("❌ No HTML generated.")
            return


        # Remove markdown if the AI adds it
        html = html.replace("```html", "")
        html = html.replace("```", "")


        os.makedirs(
            "output",
            exist_ok=True
        )


        file_path = "output/index.html"


        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)


        print(f"✅ Website created: {file_path}")



if __name__ == "__main__":

    agent = SchemeAgent()


    idea = input(
        "Describe the website: "
    )


    agent.create_website(
        idea
    )