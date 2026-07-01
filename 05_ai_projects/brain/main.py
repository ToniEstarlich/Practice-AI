from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user = data["message"]

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": user,
            "stream": True
        },
        stream=True
    )

    output = ""

    for line in response.iter_lines():
        if line:
            decoded = line.decode("utf-8")

            try:
                json_data = json.loads(decoded)
                output += json_data.get("response", "")
            except:
                pass

    return jsonify({"reply": output})

if __name__ == "__main__":
    app.run(debug=True)