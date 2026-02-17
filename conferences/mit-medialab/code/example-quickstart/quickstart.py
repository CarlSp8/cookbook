"""
Example: Gemini API Quickstart

A simple example demonstrating basic text generation with the Gemini API.
This can be used as a template for MIT Media Lab presentation code examples.
"""

import os
import google.generativeai as genai

def main():
    # Configure the API key
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY environment variable not set. "
            "Get your API key at https://aistudio.google.com/app/apikey"
        )
    
    genai.configure(api_key=api_key)
    
    # Initialize the model
    model = genai.GenerativeModel("gemini-3-flash-preview")
    
    # Generate content
    prompt = "Explain the Gemini API in one sentence."
    print(f"Prompt: {prompt}\n")
    
    response = model.generate_content(prompt)
    print(f"Response: {response.text}")

if __name__ == "__main__":
    main()
