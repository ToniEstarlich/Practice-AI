import requests
from diffusers import StableDiffusionPipeline
import torch


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
# 🎨 IMAGE GENERATOR TOOL
# -----------------------------

class ImageGenerator:

    def __init__(self):

        print("Loading image model...")

        device = "cuda" if torch.cuda.is_available() else "cpu"

        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if device=="cuda" else torch.float32,
            ignore_mismatched_sizes=True
        )

        self.pipe.to(device)

        self.device = device

        print("Model loaded on:", device)


    def generate(self, prompt, filename):

        image = self.pipe(
            prompt,
            num_inference_steps=25
        ).images[0]

        image.save(
            filename,
            "JPEG"
        )


# -----------------------------
# 🤖 IMAGE AGENT
# -----------------------------

class ImageAgent:


    def create_image_prompt(self, idea):

        prompt = f"""

Create a professional image generation prompt.

User wants:

{idea}

Include:
- subject
- environment
- lighting
- camera angle
- style
- colors
- realistic details

Return only the prompt.

"""

        return call_ollama(prompt)



    def run(self, idea):

        print("\n🎨 IMAGE AGENT STARTED\n")


        print("🧠 Creating prompt...")

        image_prompt = self.create_image_prompt(idea)


        print("\nPrompt generated:")
        print(image_prompt)



        print("\n🖼 Generating JPEG image...")


        generator = ImageGenerator()


        generator.generate(
            image_prompt,
            "generated_image.jpeg"
        )


        print("\n✅ DONE")
        print("Created:")
        print("- generated_image.jpeg")



# -----------------------------
# ▶️ RUN
# -----------------------------

if __name__ == "__main__":


    agent = ImageAgent()


    idea = input(
        "Enter image idea:\n> "
    )


    agent.run(idea)