import ollama


# Company configuration
# This information will later be replaced by data uploaded by each company
COMPANY = {
    "name": "My Company",
    "whatsapp_number": "",
    "information": """
    We are a service company.
    Business hours: Monday to Friday from 9:00 AM to 6:00 PM.
    We provide personalised customer support.
    """
}


def setup_company():
    # Configure the company WhatsApp number
    print("=== CONFIGURE WHATSAPP AI AGENT ===")

    phone_number = input("Enter the company WhatsApp number: ")

    COMPANY["whatsapp_number"] = phone_number

    print("\nAI Agent configured for:")
    print(COMPANY["whatsapp_number"])



def ask_ollama(customer_message):

    # Create the AI agent prompt using company information
    prompt = f"""
    You are an AI customer support agent.

    Company:
    {COMPANY['name']}

    Company information:
    {COMPANY['information']}

    Customer message:
    {customer_message}

    Answer professionally, clearly and briefly.
    """


    # Send the request to the local Ollama model
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    return response["message"]["content"]



def main():

    # Start company configuration
    setup_company()

    print("\nAI Agent is active.")
    print("Type customer messages to test the agent.")
    print("Type 'exit' to close.\n")


    while True:

        customer_message = input("Customer: ")

        if customer_message.lower() == "exit":
            break


        # Generate AI response
        answer = ask_ollama(customer_message)


        print("\nAI Agent:")
        print(answer)
        print("-" * 40)



if __name__ == "__main__":
    main()