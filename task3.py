def reflex_chatbot(user_input):
    """
    Simple Reflex Chatbot based on keyword matching.
    Operates strictly without memory or conversation history.
    """
    text = user_input.lower()
    rules = [
        # Base Rules (from lab instructions)
        (["hello", "hi", "hey"], "Hello! How can I help you today?"),
        (["bye", "goodbye"], "Goodbye! Have a great day."),
        (["name"], "I am a simple reflex chatbot built for the AI lab."),
        (["help"], "You can ask me to say hello, tell you my name, ask about python, time, or say bye."),
        
        # 4 Extended Rules
        (["python"], "Python is a popular programming language widely used in AI and machine learning."),
        (["time", "clock"], "I don't have access to a real-time clock, but check your system tray for the current time!"),
        (["weather"], "As a simple reflex agent, I don't have live weather sensors, but room temperature is usually fine!"),
        (["course", "lab", "agent"], "This is Lab #3 covering AI Agents, PEAS Framework, and Simple Reflex Agents.")
    ]
    
    # Check rules sequentially based on keyword matching
    for keywords, reply in rules:
        if any(k in text for k in keywords):
            return reply
            
    return "Sorry, I did not understand that. Type 'help' for options."

def main():
    print("=== SIMPLE REFLEX CHATBOT (Type 'bye' or 'exit' to quit) ===")
    while True:
        user_input = input("You: ")
        
        # Check termination condition
        if user_input.lower().strip() in ("bye", "goodbye", "exit"):
            print("Bot:", reflex_chatbot(user_input))
            break
            
        response = reflex_chatbot(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()