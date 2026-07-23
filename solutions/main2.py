import ollama
import re


def generate_obj(prompt):
    system = """
You are a professional 3D OBJ mesh generator.

Return ONLY valid Wavefront OBJ content.

Rules:
- Every vertex must use: v X Y Z
- Every face must reference existing vertices only
- Count vertices before creating faces
- Use triangular faces only
- Create a closed low-poly mesh
- No markdown
- No explanations
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
                "content": f"Create a low poly 3D model of: {prompt}"
            }
        ],
        options={
            "temperature": 0.2
        }
    )

    return response["message"]["content"]


def clean_obj(obj_data):

    lines = []

    vertices = 0

    # remove markdown
    obj_data = obj_data.replace("```obj", "")
    obj_data = obj_data.replace("```", "")

    for line in obj_data.splitlines():

        line = line.strip()

        if line.startswith("v "):
            parts = line.split()

            if len(parts) == 4:
                vertices += 1
                lines.append(line)

        elif line.startswith("f "):

            parts = line.split()[1:]

            valid = True

            for p in parts:
                try:
                    index = int(p)
                    if index > vertices:
                        valid = False
                except:
                    valid = False

            if valid:
                lines.append(line)

    return "\n".join(lines)


def save_obj(filename, obj_data):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(obj_data)


if __name__ == "__main__":

    object_name = input("What should I create? ")

    obj = generate_obj(object_name)

    obj = clean_obj(obj)

    save_obj("generated_model.obj", obj)

    print("Created generated_model.obj")