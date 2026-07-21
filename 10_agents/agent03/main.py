import requests
import os


# -----------------------------
# OLLAMA FUNCTION
# -----------------------------

def call_ollama(prompt, model="llama3"):

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0
        }
    }

    response = requests.post(url, json=payload)

    return response.json()["response"]
# -----------------------------
# README TOOL
# -----------------------------

def create_readme(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)



# -----------------------------
# README AGENT
# -----------------------------

class READMEAgent:

    def __init__(self):
        pass


    def generate_content(self, project_info):

        prompt = f"""
You are a Markdown formatter.

Your ONLY task is to convert the provided text into a clean README.md file.

STRICT RULES:

- Do NOT write new content.
- Do NOT add explanations.
- Do NOT add missing sections.
- Do NOT guess information.
- Do NOT improve or expand the text.
- Do NOT create examples.
- Do NOT add technologies, features, commands, or descriptions.
- Do NOT change the meaning.

You can ONLY:
- Add Markdown formatting.
- Fix indentation.
- Add missing Markdown symbols (#, ##, -, ```).
- Organize the existing text into readable sections.

The output must contain ONLY information that already exists in the input.

Input text:

{project_info}


Return ONLY the final README.md content.
"""


        return call_ollama(prompt)



    def run(self, project_info):

        print("\nREADME AGENT STARTED\n")


        print("Generating README content...\n")

        content = self.generate_content(project_info)


        print("Creating README.md...\n")

        filename = "README.md"

        create_readme(filename, content)


        print(f"DONE -> {filename}")



# -----------------------------
# EXECUTION
# -----------------------------

if __name__ == "__main__":

    agent = READMEAgent()


    # Read project description from file
    with open("project_input.txt", "r", encoding="utf-8") as file:
        project = file.read()


    agent.run(project)