def chatbot():
    print("Hello! I am ChatBot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ['hi', 'hello', 'hey']:
            print("Bot: Hello! How can I help you today?")
        elif 'your name' in user_input:
            print("Bot: I am a simple rule-based chatbot.")
        elif 'how are you' in user_input:
            print("Bot: I'm just a bunch of code, but I'm doing great!")
        elif 'help' in user_input:
            print("Bot: I can answer simple questions. Try asking about my name or say hello!")
        elif user_input in ['bye', 'exit', 'quit']:
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Can you rephrase?")

if __name__ == "__main__":
    chatbot()
