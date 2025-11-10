# TASK 4: Basic Chatbot
def chatbot_response(user_input):
    user_input = user_input.lower()  

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! 👋"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "fine" in user_input or "good" in user_input:
        return "That's nice to hear! 😊"
    elif "name" in user_input:
        return "I'm ChatBot 1.0 — your friendly rule-based assistant!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day! 👋"
    else:
        return "Sorry, I didn’t understand that. Could you rephrase?"

print("🤖 ChatBot 1.0: Hello! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("ChatBot:", response)
    
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break
