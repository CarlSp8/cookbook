# Real-World Examples: OpenAI SDK with Gemini

This document shows practical, real-world examples of using the OpenAI SDK with Gemini API.

## 📝 Example 1: AI-Powered Documentation Q&A

Build a documentation Q&A system using embeddings and chat:

```python
from openai import OpenAI
import numpy as np

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Your documentation sections
docs = [
    "Installation: Run 'pip install mypackage' to install the package.",
    "Authentication: Set the API_KEY environment variable with your key.",
    "Basic Usage: Import the library with 'import mypackage' and call mypackage.run().",
    "Error Handling: All errors inherit from MyPackageError class.",
    "Configuration: Create a config.yaml file in your project root."
]

# Generate embeddings for documentation
doc_response = client.embeddings.create(
    model="text-embedding-004",
    input=docs
)
doc_embeddings = [item.embedding for item in doc_response.data]

def answer_question(question):
    # Find most relevant documentation
    q_response = client.embeddings.create(
        model="text-embedding-004",
        input=question
    )
    q_embedding = q_response.data[0].embedding
    
    # Calculate similarities
    similarities = [
        np.dot(q_embedding, doc_emb) / 
        (np.linalg.norm(q_embedding) * np.linalg.norm(doc_emb))
        for doc_emb in doc_embeddings
    ]
    
    # Get top 2 most relevant sections
    top_indices = np.argsort(similarities)[-2:][::-1]
    context = "\n\n".join([docs[i] for i in top_indices])
    
    # Generate answer using chat
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful documentation assistant. Answer questions based on the provided context."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ]
    )
    
    return response.choices[0].message.content

# Use it
print(answer_question("How do I install the package?"))
print(answer_question("Where do I put my API key?"))
```

---

## 🖼️ Example 2: Image Analysis API

Create a REST API endpoint for image analysis:

```python
from fastapi import FastAPI, File, UploadFile
from openai import OpenAI
import base64

app = FastAPI()

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@app.post("/analyze-image")
async def analyze_image(
    file: UploadFile = File(...),
    prompt: str = "Describe this image in detail"
):
    # Read and encode image
    image_bytes = await file.read()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    
    # Analyze with Gemini
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )
    
    return {
        "description": response.choices[0].message.content,
        "model": response.model,
        "usage": {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens
        }
    }

# Run with: uvicorn main:app --reload
```

---

## 💬 Example 3: Chatbot with Memory

Build a chatbot that remembers conversation context:

```python
from openai import OpenAI

class Chatbot:
    def __init__(self, api_key, system_instruction="You are a helpful assistant."):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self.messages = [
            {"role": "system", "content": system_instruction}
        ]
        self.model = "gemini-2.5-flash"
    
    def chat(self, user_message):
        # Add user message
        self.messages.append({
            "role": "user",
            "content": user_message
        })
        
        # Get response
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        
        # Add assistant response to history
        assistant_message = response.choices[0].message.content
        self.messages.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def reset(self):
        """Clear conversation history"""
        self.messages = [self.messages[0]]  # Keep system message

# Usage
bot = Chatbot(api_key="YOUR_API_KEY", 
              system_instruction="You are a Python programming tutor.")

print(bot.chat("What is a list in Python?"))
print(bot.chat("How do I add items to it?"))  # Remembers context
print(bot.chat("Show me an example"))  # Continues conversation
```

---

## 🔧 Example 4: Function Calling Weather Bot

Create a weather bot with function calling:

```python
from openai import OpenAI
import json

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define available functions
def get_weather(location, unit="celsius"):
    """Simulated weather API call"""
    # In real app, call actual weather API
    return {
        "location": location,
        "temperature": 22 if unit == "celsius" else 72,
        "unit": unit,
        "condition": "sunny"
    }

def get_forecast(location, days=3):
    """Simulated forecast API call"""
    return {
        "location": location,
        "forecast": [
            {"day": 1, "temp": 22, "condition": "sunny"},
            {"day": 2, "temp": 20, "condition": "cloudy"},
            {"day": 3, "temp": 18, "condition": "rainy"}
        ]
    }

# Function definitions for the model
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_forecast",
            "description": "Get weather forecast for multiple days",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "days": {"type": "integer", "minimum": 1, "maximum": 7}
                },
                "required": ["location"]
            }
        }
    }
]

# Map function names to actual functions
available_functions = {
    "get_weather": get_weather,
    "get_forecast": get_forecast
}

def chat_with_functions(user_message):
    messages = [{"role": "user", "content": user_message}]
    
    # First call to model
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    
    response_message = response.choices[0].message
    
    # Check if model wants to call a function
    if response_message.tool_calls:
        # Execute function calls
        messages.append(response_message)
        
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            # Call the actual function
            function_response = available_functions[function_name](**function_args)
            
            # Add function response to messages
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(function_response)
            })
        
        # Get final response from model
        final_response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=messages
        )
        
        return final_response.choices[0].message.content
    else:
        return response_message.content

# Usage
print(chat_with_functions("What's the weather in Paris?"))
print(chat_with_functions("Give me a 5-day forecast for Tokyo"))
```

---

## 📊 Example 5: Content Moderation System

Build a content moderation system:

```python
from openai import OpenAI
import json

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def moderate_content(text):
    """Check if content is appropriate"""
    
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "user",
                "content": f"""Analyze this text for inappropriate content.
Return JSON with:
- is_safe: boolean
- categories: list of any issues found (hate_speech, violence, sexual, spam, etc.)
- confidence: 0-1
- explanation: brief reason

Text: {text}"""
            }
        ],
        response_format={"type": "json_object"}
    )
    
    result = json.loads(response.choices[0].message.content)
    return result

# Usage
result = moderate_content("This is a normal comment about cooking.")
print(f"Safe: {result['is_safe']}")
print(f"Categories: {result.get('categories', [])}")
```

---

## 🔍 Example 6: Smart Search with Reranking

Implement semantic search with reranking:

```python
from openai import OpenAI
import numpy as np

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class SmartSearch:
    def __init__(self, documents):
        self.documents = documents
        
        # Generate embeddings for all documents
        response = client.embeddings.create(
            model="text-embedding-004",
            input=documents
        )
        self.embeddings = [item.embedding for item in response.data]
    
    def search(self, query, top_k=5):
        # Get query embedding
        q_response = client.embeddings.create(
            model="text-embedding-004",
            input=query
        )
        q_embedding = q_response.data[0].embedding
        
        # Calculate similarities
        similarities = []
        for doc_emb in self.embeddings:
            sim = np.dot(q_embedding, doc_emb) / (
                np.linalg.norm(q_embedding) * np.linalg.norm(doc_emb)
            )
            similarities.append(sim)
        
        # Get top-k
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Rerank using LLM
        candidates = [self.documents[i] for i in top_indices]
        reranked = self.rerank(query, candidates)
        
        return reranked
    
    def rerank(self, query, candidates):
        """Use LLM to rerank candidates for better relevance"""
        
        prompt = f"""Query: {query}

Rank these documents by relevance to the query.
Return JSON with an array of documents in order of relevance.

Documents:
{json.dumps(candidates, indent=2)}"""
        
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        return result.get('documents', candidates)

# Usage
docs = [
    "Python is a programming language",
    "Machine learning uses algorithms",
    "The weather is nice today",
    "Neural networks are powerful",
    "JavaScript runs in browsers"
]

search = SmartSearch(docs)
results = search.search("What is ML?", top_k=3)
print("Search results:", results)
```

---

## 🎨 Example 7: Creative Writing Assistant

Build a writing assistant with style transfer:

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class WritingAssistant:
    def __init__(self):
        self.model = "gemini-2.5-flash"
    
    def rewrite(self, text, style):
        """Rewrite text in a different style"""
        
        styles = {
            "professional": "formal, business-appropriate language",
            "casual": "friendly, conversational tone",
            "academic": "scholarly, well-researched style",
            "creative": "imaginative, descriptive language",
            "simple": "clear, easy-to-understand language"
        }
        
        style_desc = styles.get(style, style)
        
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"""Rewrite this text using {style_desc}:

{text}

Provide only the rewritten text."""
                }
            ]
        )
        
        return response.choices[0].message.content
    
    def expand(self, text, target_length=200):
        """Expand short text to longer version"""
        
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"""Expand this text to approximately {target_length} words while maintaining its core message:

{text}"""
                }
            ]
        )
        
        return response.choices[0].message.content
    
    def summarize(self, text, max_sentences=3):
        """Summarize text"""
        
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"""Summarize this text in {max_sentences} sentences:

{text}"""
                }
            ]
        )
        
        return response.choices[0].message.content

# Usage
assistant = WritingAssistant()

text = "The project was completed successfully and met all requirements."

print("Professional:", assistant.rewrite(text, "professional"))
print("Casual:", assistant.rewrite(text, "casual"))
print("Expanded:", assistant.expand(text, target_length=100))
```

---

## 🌐 Example 8: Multi-Language Support

Build a translation and localization system:

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def translate(text, target_language, context=None):
    """Translate text with optional context"""
    
    prompt = f"Translate this to {target_language}: {text}"
    
    if context:
        prompt += f"\n\nContext: {context}"
    
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

def localize(text, target_region, preserve_variables=True):
    """Localize text for a specific region"""
    
    prompt = f"""Localize this text for {target_region}, adapting:
- Cultural references
- Idioms
- Date/time formats
- Currency
"""
    
    if preserve_variables:
        prompt += "\nPreserve any variables in {{curly braces}}."
    
    prompt += f"\n\nText: {text}"
    
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

# Usage
print(translate("Hello, how are you?", "Spanish"))
print(translate("The meeting is at 3 PM", "French", 
               context="Business email"))
print(localize("The sale ends on 12/25 at midnight!", "UK English"))
```

---

## 📚 More Examples

For more detailed examples, check out:

- [Basic Chat](./Basic_Chat.ipynb) - Core chat functionality
- [Working with Images](./Working_with_Images.ipynb) - Image analysis
- [Embeddings](./Embeddings.ipynb) - Semantic search
- [Full Guide](../Get_started_OpenAI_Compatibility.ipynb) - Comprehensive tutorial

---

## 💡 Pro Tips

1. **Cache Embeddings**: Store embeddings in a database to avoid regenerating
2. **Batch Requests**: Process multiple items together for efficiency
3. **Error Handling**: Always wrap API calls in try-except blocks
4. **Rate Limiting**: Implement exponential backoff for retries
5. **Token Management**: Monitor usage to optimize costs
6. **Streaming**: Use streaming for long responses to improve UX

---

**Happy building! 🚀**
