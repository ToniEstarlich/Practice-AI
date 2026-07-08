import requests

# -----------------------------
# OLLAMA CLIENT FUNCTION
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
# AGENT CORE
# -----------------------------

class MarketingAgent:
    def __init__(self):
        self.memory = {}

    def generate_strategy(self, goal):
        prompt = f"""
You are an expert marketing strategist.

User goal:
{goal}

Create a simple 3-step social media strategy.
"""

        return call_ollama(prompt)

    def generate_posts(self, goal):
        prompt = f"""
You are a social media content creator.

User goal:
{goal}

Generate 3 daily posts for LinkedIn and X.
Each post must:
- Be engaging
- Include hashtags
- Be different in tone and style
"""

        return call_ollama(prompt)

    def run(self, goal):
        print("\nAGENT STARTED\n")

        print("Generating strategy...\n")
        strategy = self.generate_strategy(goal)
        print(strategy)

        print("\nGenerating posts...\n")
        posts = self.generate_posts(goal)
        print(posts)

        print("\nDONE")


# -----------------------------
# EXECUTION
# -----------------------------

if __name__ == "__main__":
    agent = MarketingAgent()

    goal = input("Enter your goal (e.g. get clients as freelancer):\n> ")

    agent.run(goal)