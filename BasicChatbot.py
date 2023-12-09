import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import random

nltk.download('punkt')
nltk.download('stopwords')

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Hey!"],
            "how are you": ["I'm doing well, thank you!", "Not bad, thanks for asking."],
            "bye": ["Goodbye!", "See you later!", "Bye!"],
            "default": ["I'm not sure how to respond to that.", "Can you ask me something else?", "Sorry, I don't understand."]
        }

        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    def preprocess_text(self, text):
        words = word_tokenize(text)
        words = [self.stemmer.stem(word.lower()) for word in words if word.isalnum() and word.lower() not in self.stop_words]
        return words

    def respond(self, user_input):
        words = self.preprocess_text(user_input)

        for key in self.responses:
            if any(word in self.responses[key] for word in words):
                return random.choice(self.responses[key])

        return random.choice(self.responses["default"])

if __name__ == "__main__":
    chatbot = SimpleChatbot()

    print("Simple Chatbot: Hello! How can I help you today? (Type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Simple Chatbot: Goodbye!")
            break

        response = chatbot.respond(user_input)
        print(f"Simple Chatbot: {response}")
