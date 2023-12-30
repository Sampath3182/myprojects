import re
import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK resources (only need to run this once)
#nltk.download("punkt")
#nltk.download("stopwords")

# Sample responses for the chatbot
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! How can I help you?", "Hey! What can I do for you?"],
    "balance": "Bank balance in the account is Rs. Xxxxx.xx",
    "transfer": "To transfer money to other bank accounts, follow these steps:\n1. Log in to your account.\n2. Go to the 'Transfer' section.\n3. Add the recipient's bank account details.\n4. Enter the amount and confirm the transfer.",
    "help": "I can assist you with checking your bank balance and providing instructions on transferring money to other bank accounts.",
    "cards":"follow below steps \n1.log in to your account \n2.go to cards section \n3. select your card type\n4.provide required details and documents\n5.complete your application",
    "fallback": "I'm sorry, I didn't quite understand that. Could you please rephrase?"
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r"(hello|hi)", user_input):
        return random.choice(responses["greeting"])
    elif re.search(r"bank balance|balance|my balance|balance enquiry", user_input):
        return responses["balance"]
    elif re.search("How should I transfer the amount to other bank accounts ?|transfer|money transfer|transfer money other accounts", user_input):
        return responses["transfer"]
    elif re.search(r"apply for credit|how to apply credit card|apply for debit card", user_input):
        return responses["cards"]
    elif re.search(r"help", user_input):
        return responses["help"]
    else:
        return responses["fallback"]

# Main chat loop
print("Welcome to Internet Banking Chatbot!")
print("Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a nice day.")
        break
    else:
        response = chatbot_response(user_input)
        print("Chatbot:", response)
