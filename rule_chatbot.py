# Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hello! I am your assistant. Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day 😊")
            break

        # Greetings
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you today?")

        # Asking about chatbot
        elif "who are you" in user_input:
            print("Chatbot: I am a simple rule-based chatbot created in Python.")

        # Asking about time (static response for now)
        elif "time" in user_input:
            print("Chatbot: Sorry, I cannot tell the time yet. But I will learn soon!")

        # Asking about weather
        elif "weather" in user_input:
            print("Chatbot: It's always sunny inside my program ☀️")

        # Default response
        else:
            print("Chatbot: I'm not sure about that. Can you ask something else?")

# Run the chatbot
chatbot()
