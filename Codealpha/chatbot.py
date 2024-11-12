import nltk
import random
import string
from nltk.corpus import wordnet

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Responses for basic conversations
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you?"]

# Sample responses based on keywords
responses = {
    "name": ["I am a chatbot without a name. You can call me Bot!", "I go by many names, but 'Bot' is fine!"],
    "age": ["I am as old as the internet!", "Age is just a number. I am timeless."],
    "language": ["I am programmed in Python!", "I speak the language of code."],
    "creator": ["I was created by a Python enthusiast!", "Someone who loves Python coded me!"],
}

# Tokenize and normalize text
def normalize_text(text):
    return text.lower()

# Basic greeting response
def check_for_greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    return None

# Simple keyword matching for responses
def generate_response(user_input):
    user_input = normalize_text(user_input)
    
    # Check for greetings first
    greeting = check_for_greeting(user_input)
    if greeting:
        return greeting
    
    # Check if keywords are in user input
    for keyword, response_list in responses.items():
        if keyword in user_input:
            return random.choice(response_list)
    
    # Default response if no keyword matches
    return "I'm sorry, I didn't understand that. Can you tell me more?"

# Main chat function
def chat():
    print("Chatbot: Hello! I’m here to chat. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
chat()
