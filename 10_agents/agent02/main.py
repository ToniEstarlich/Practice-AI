import requests

# -----------------------------
# 🧠 OLLAMA (BRAIN)
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
# ⚙️ TOOL: SAVE FILE
# -----------------------------

def save_html(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


# -----------------------------
# 🤖 AGENT
# -----------------------------

class LandingPageAgent:

    def generate_landing_page(self, idea):

        prompt = f"""
You are a senior front-end developer.

Create a FULL landing page using:
- HTML
- CSS (inside <style>)
- jQuery animations (use CDN)
- Modern design
- Responsive layout

The landing page is for:
{idea}

Requirements:
- Include hero section
- Call to action button
- Features section
- Testimonials section
- Footer
- Use placeholder images from Pexels (use https://images.pexels.com URLs)
- Add simple jQuery animations (fadeIn, slideDown)

Return ONLY the full HTML file.
"""

        return call_ollama(prompt)


    def run(self, idea):

        print("\n🚀 LANDING PAGE AGENT STARTED\n")

        print("🧠 Generating HTML...\n")
        html = self.generate_landing_page(idea)

        print("💾 Saving file...\n")
        save_html("landing.html", html)

        print("\n✅ DONE -> landing.html created")


# -----------------------------
# ▶️ RUN
# -----------------------------

if __name__ == "__main__":

    agent = LandingPageAgent()

    idea = input("Enter landing page idea:\n> ")

    agent.run(idea)