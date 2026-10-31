import os
import sys
import nltk
from nltk.tokenize import word_tokenize
from dotenv import load_dotenv
from google import genai

# --- CONFIGURATION ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def setup_nltk():
    """Download required NLTK data if not present."""
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        print("Downloading NLTK data...")
        nltk.download('punkt', quiet=True)
        print("NLTK setup complete.")

def initialize_ai():
    """Initialize Gemini client."""
    if not API_KEY:
        print("❌ API Key not found.")
        print("Add GEMINI_API_KEY in your .env file")
        sys.exit(1)

    return genai.Client(api_key=API_KEY)

def process_input_with_nltk(text):
    """Basic NLP preprocessing using NLTK."""
    tokens = word_tokenize(text)
    clean_tokens = [t for t in tokens if len(t) > 1 or t.isalnum()]
    return " ".join(clean_tokens)

def main():
    print("--- Initializing Chatbot ---")

    # Setup NLTK
    setup_nltk()

    # Setup AI
    try:
        client = initialize_ai()
        conversation = "You are a friendly, funny, and helpful chatbot.\n"
    except Exception as e:
        print("Error initializing AI:", e)
        return

    print("\n" + "="*50)
    print("🤖 AI CHATBOT (FINAL VERSION)")
    print("Type 'exit' or 'quit' to stop.")
    print("="*50 + "\n")

    # Chat loop
    while True:
        try:
            user_input = input("You: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Bot: Goodbye! 👋")
                break

            if not user_input.strip():
                continue

            # NLP preprocessing
            processed_text = process_input_with_nltk(user_input)

            # Build conversation
            conversation += f"User: {processed_text}\nBot: "

            # Generate response
            response = client.models.generate_content(
                model="gemini-2.0-flash",   # ✅ FIXED MODEL
                contents=conversation      # ✅ CORRECT FORMAT
            )

            reply = response.text

            # Save response in memory
            conversation += f"{reply}\n"

            print(f"Bot: {reply}")
            print("-" * 30)

        except KeyboardInterrupt:
            print("\nBot: Exiting...")
            break

        except Exception as e:
            print("Bot: Oops, something went wrong.")
            print("DEBUG:", e)

if __name__ == "__main__":
    main()