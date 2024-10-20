import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources (first-time run only)
nltk.download('punkt')

# Predefined responses for the chatbot
responses = [
    "Hello! How can I help you?",
    "I'm here to assist you.",
    "You can ask me anything about AI.",
    "I'm just a simple chatbot, but I do my best!",
    "Thank you for chatting with me!",
]

# Tokenize input sentences
def tokenize(text):
    return nltk.word_tokenize(text.lower())

# Vectorize text input using TF-IDF
def vectorize(text, vectorizer):
    return vectorizer.transform([text])

def chatbot():
    print("AI Chatbot: Hello! Type 'quit' to exit the chat.")

    # Train the TF-IDF vectorizer with predefined responses
    vectorizer = TfidfVectorizer(tokenizer=tokenize)
    vectorizer.fit(responses)

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            print("AI Chatbot: Goodbye!")
            break

        # Find the most relevant response using cosine similarity
        input_vec = vectorize(user_input, vectorizer)
        similarities = cosine_similarity(input_vec, vectorizer.transform(responses))
        best_match_index = similarities.argmax()
        best_response = responses[best_match_index]

        print(f"AI Chatbot: {best_response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()