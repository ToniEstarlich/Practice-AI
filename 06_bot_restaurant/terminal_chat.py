import requests

URL = "http://127.0.0.1:8000/chat"

print("🤖 Restaurant Bot (type 'exit' to quit)\n")

while True:
    message = input("You: ")

    if message.lower() == "exit":
        print("Bot: Goodbye 👋")
        break

    response = requests.post(URL, json={
        "message": message,
        "file_name": "restaurant"
    })

    data = response.json()

    print("Bot:", data["answer"])