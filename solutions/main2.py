import ollama


def generate_obj(prompt):
    system = """
You are a 3D model generator.

Return ONLY valid Wavefront OBJ file content.

Rules:
- Start with vertex lines using "v"
- Use face lines using "f"
- Do not add explanations
- Create a simple closed mesh
"""

    response = ollama.chat(
        model="llama3:latest", 
        messages=[
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": f"Create a 3D OBJ model of: {prompt}"
            }
        ]
    )

    return response["message"]["content"]


def save_obj(filename, obj_data):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(obj_data)


if __name__ == "__main__":

    object_name = input("What should I create? ")

    obj = generate_obj(object_name)

    # remove markdown if Ollama adds it
    obj = obj.replace("```obj", "")
    obj = obj.replace("```", "")

    save_obj("generated_model.obj", obj)

    print("Created generated_model.obj")