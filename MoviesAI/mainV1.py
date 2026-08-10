import ollama
import json


def create_movie(prompt):
    system_prompt = """
You are an AI film director.

The user will give you an idea for a short movie.

Transform the idea into a cinematic movie plan.

Return ONLY valid JSON with this structure:

{
    "title": "Movie title",
    "genre": "genre",
    "style": "visual style",
    "scenes": [
        {
            "scene_number": 1,
            "duration_seconds": 5,
            "description": "What happens",
            "camera": "Camera movement and shot",
            "lighting": "Lighting description",
            "characters": ["character names"],
            "dialogue": "Dialogue or empty string",
            "video_prompt": "Detailed prompt for a video generation model"
        }
    ]
}

Create 5 scenes.
Each scene should be approximately 5 seconds.
The scenes must form one continuous story.
Maintain character consistency.
"""

    response = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


prompt = input("Describe your movie: ")

movie = create_movie(prompt)

print("\n===== MOVIE =====\n")
print(movie)

# Save the result
with open("movie.json", "w", encoding="utf-8") as file:
    file.write(movie)

print("\nMovie plan saved to movie.json")