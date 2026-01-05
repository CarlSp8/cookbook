
import os
from gemini_framework import GeminiFramework

def main():
    # Example usage of the GeminiFramework

    # Ensure you have set the GEMINI_API_KEY environment variable
    # or pass it directly to the constructor: GeminiFramework(api_key="YOUR_KEY")
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("Please set the GEMINI_API_KEY environment variable to run this example.")
        # For demonstration purposes, we'll initialize without a key to show the structure,
        # but API calls will fail if we try to execute them.
        framework = GeminiFramework(api_key="dummy_key_for_demo")
        print("Framework initialized with dummy key.")
    else:
        framework = GeminiFramework()
        print("Framework initialized.")

    print("\n--- 1. Simple Text Generation ---")
    prompt = "Explain how the internet works to a 5 year old."
    print(f"Prompt: {prompt}")
    try:
        response = framework.generate_text(prompt)
        print(f"Response:\n{response}")
    except Exception as e:
        print(f"Error generating text: {e}")

    print("\n--- 2. System Instructions ---")
    sys_instruction = "You are a pirate."
    prompt = "Hello, how are you?"
    print(f"System Instruction: {sys_instruction}")
    print(f"Prompt: {prompt}")
    try:
        response = framework.generate_text(prompt, system_instruction=sys_instruction)
        print(f"Response:\n{response}")
    except Exception as e:
        print(f"Error generating text with system instruction: {e}")

    print("\n--- 3. Chat Session ---")
    try:
        framework.start_chat()
        msg1 = "My name is Jules."
        print(f"User: {msg1}")
        resp1 = framework.send_chat_message(msg1)
        print(f"Gemini: {resp1}")

        msg2 = "What is my name?"
        print(f"User: {msg2}")
        resp2 = framework.send_chat_message(msg2)
        print(f"Gemini: {resp2}")
    except Exception as e:
        print(f"Error in chat session: {e}")

    print("\n--- 4. Token Counting ---")
    prompt = "The quick brown fox jumps over the lazy dog."
    try:
        count = framework.count_tokens(prompt)
        print(f"Prompt: '{prompt}'")
        print(f"Token count: {count}")
    except Exception as e:
        print(f"Error counting tokens: {e}")

if __name__ == "__main__":
    main()
