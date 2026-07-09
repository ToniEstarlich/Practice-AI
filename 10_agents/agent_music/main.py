import ollama
import torch
import scipy
from transformers import AutoProcessor, MusicgenForConditionalGeneration

# Load MusicGen model (only the first time takes a while)
processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

# User idea
idea = input("Enter music idea:\n> ")

print("\n🎵 MUSIC AGENT STARTED\n")

# Ask Ollama to improve the prompt
response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": f"""
Create a professional prompt for an AI music generator.

Music idea:
{idea}

Return only the prompt.
"""
        }
    ]
)

prompt = response["message"]["content"]

print("🧠 Prompt created:\n")
print(prompt)

print("\n🎼 Generating music...")

# Generate music
inputs = processor(
    text=[prompt],
    return_tensors="pt",
)

audio = model.generate(**inputs)

sampling_rate = model.config.audio_encoder.sampling_rate

scipy.io.wavfile.write(
    "music.wav",
    rate=sampling_rate,
    data=audio[0, 0].cpu().numpy(),
)

print("\n✅ Music saved as music.wav")