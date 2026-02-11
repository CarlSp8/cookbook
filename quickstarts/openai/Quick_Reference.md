# OpenAI SDK with Gemini: Quick Reference

This is a quick reference guide for using the **OpenAI SDK** with **Gemini API**. Perfect for developers who want to get started quickly!

## 🚀 Setup (2 lines!)

**Python:**
```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",  # Get from ai.google.dev
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
```

**JavaScript:**
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
    apiKey: process.env.GOOGLE_API_KEY,
    baseURL: 'https://generativelanguage.googleapis.com/v1beta/openai/'
});
```

---

## 💬 Text Generation

```python
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

---

## 🎯 Common Patterns

### System Instructions
```python
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "How do I reverse a string in Python?"}
    ]
)
```

### Multi-turn Conversation
```python
messages = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language."},
    {"role": "user", "content": "What's it used for?"}
]

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=messages
)
```

### Streaming
```python
stream = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end='')
```

### Temperature Control
```python
# More creative (0-2)
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[...],
    temperature=1.5  # Higher = more creative
)

# More focused (0-2)
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[...],
    temperature=0.2  # Lower = more deterministic
)
```

---

## 🖼️ Images

### Image from URL
```python
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"}
                }
            ]
        }
    ]
)
```

### Base64 Image
```python
import base64

with open("image.jpg", "rb") as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}
                }
            ]
        }
    ]
)
```

### Multiple Images
```python
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Compare these images"},
                {"type": "image_url", "image_url": {"url": "url1"}},
                {"type": "image_url", "image_url": {"url": "url2"}}
            ]
        }
    ]
)
```

---

## 🔧 Function Calling

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=tools,
    tool_choice="auto"
)

# Check if function was called
if response.choices[0].message.tool_calls:
    function_call = response.choices[0].message.tool_calls[0]
    print(f"Function: {function_call.function.name}")
    print(f"Arguments: {function_call.function.arguments}")
```

---

## 📋 JSON Mode

```python
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "List 3 colors in JSON format"}
    ],
    response_format={"type": "json_object"}
)

import json
data = json.loads(response.choices[0].message.content)
```

---

## 🔢 Embeddings

```python
# Single text
response = client.embeddings.create(
    model="text-embedding-004",
    input="Hello world"
)
embedding = response.data[0].embedding

# Multiple texts
response = client.embeddings.create(
    model="text-embedding-004",
    input=["Text 1", "Text 2", "Text 3"]
)
embeddings = [item.embedding for item in response.data]

# Similarity
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similarity = cosine_similarity(embeddings[0], embeddings[1])
```

---

## 📝 Model Selection

| Model | Best For | Speed | Cost |
|-------|----------|-------|------|
| `gemini-2.5-flash` | Everyday tasks | ⚡⚡⚡ Fast | $ |
| `gemini-2.5-flash-lite` | Simple, ultra-fast tasks | ⚡⚡⚡ Fastest | $ |
| `gemini-2.5-pro` | Complex reasoning | ⚡ Slower | $$$ |
| `gemini-3-flash-preview` | Latest fast model (preview) | ⚡⚡⚡ Fast | $ |
| `gemini-3-pro-preview` | Latest reasoning (preview) | ⚡ Slower | $$$ |
| `text-embedding-004` | Embeddings | ⚡⚡ Fast | $ |

---

## 🎛️ Common Parameters

```python
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[...],
    
    # Generation control
    temperature=0.7,        # 0-2, creativity level
    max_tokens=500,         # Max response length
    top_p=0.9,             # Nucleus sampling
    
    # Response format
    response_format={"type": "json_object"},  # JSON mode
    
    # Tools
    tools=[...],           # Function calling
    tool_choice="auto",    # auto, none, or specific
    
    # Streaming
    stream=True            # Real-time responses
)
```

---

## ⚡ Environment Variables

**Set once, use everywhere:**

```bash
export GOOGLE_API_KEY="your-gemini-api-key"
```

Then in code:
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GOOGLE_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
```

**Or use OpenAI env vars:**
```bash
export OPENAI_API_KEY="your-gemini-api-key"
export OPENAI_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai/"
```

Then:
```python
client = OpenAI()  # Auto-detects env vars
```

---

## 🚨 Error Handling

```python
try:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[...]
    )
except Exception as e:
    print(f"Error: {e}")
    
# Check response
if response.choices[0].finish_reason == "stop":
    print("Success!")
elif response.choices[0].finish_reason == "length":
    print("Response truncated, increase max_tokens")
```

---

## 💡 Tips & Tricks

### 1. List Available Models
```python
models = client.models.list()
for model in models:
    print(model.id)
```

### 2. Count Tokens Before Sending
Use approximate formula: ~1 token per 4 characters for English text.

### 3. Reuse Client
```python
# Good: Reuse client
client = OpenAI(api_key=..., base_url=...)
response1 = client.chat.completions.create(...)
response2 = client.chat.completions.create(...)

# Avoid: Creating new client each time
```

### 4. Batch for Efficiency
```python
# Generate embeddings for multiple texts at once
response = client.embeddings.create(
    model="text-embedding-004",
    input=["Text 1", "Text 2", "Text 3", ...]  # Up to 100+ texts
)
```

### 5. Use System Instructions
```python
# Better: Use system message for consistent behavior
messages = [
    {"role": "system", "content": "You are a helpful assistant that..."},
    {"role": "user", "content": "..."}
]

# vs just user messages
```

---

## ⚠️ What Doesn't Work

These require the **Gemini SDK**:

- ❌ **Video input** - Use [Gemini SDK](../Video_understanding.ipynb)
- ❌ **Large files (>20MB)** - Use [Gemini File API](../File_API.ipynb)
- ❌ **Live API** - Use [Gemini Live API](../Get_started_LiveAPI.ipynb)
- ❌ **Grounding (Search/Maps)** - Use [Gemini SDK](../Grounding.ipynb)
- ❌ **Context Caching** - Use [Gemini SDK](../Caching.ipynb)

**Solution:** Use both SDKs in the same project! See [Feature Comparison](./Feature_Comparison.md).

---

## 📚 Full Examples

- [Basic Chat](./Basic_Chat.ipynb) - Complete chat examples
- [Images](./Working_with_Images.ipynb) - Multimodal prompts
- [Embeddings](./Embeddings.ipynb) - Semantic search
- [Migration Guide](./Migration_Guide.md) - Switch from OpenAI
- [Limitations](./Limitations.md) - Known issues & workarounds

---

## 🔗 Links

- **Get API Key:** [ai.google.dev/aistudio](https://aistudio.google.com/app/apikey)
- **Documentation:** [ai.google.dev/gemini-api/docs/openai](https://ai.google.dev/gemini-api/docs/openai)
- **Pricing:** [ai.google.dev/pricing](https://ai.google.dev/pricing)
- **Support:** [discuss.ai.google.dev](https://discuss.ai.google.dev/)

---

## 🎯 Quick Start Checklist

- [ ] Get API key from [ai.google.dev](https://aistudio.google.com/app/apikey)
- [ ] Install OpenAI SDK: `pip install openai`
- [ ] Set base URL: `base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`
- [ ] Use Gemini model names: `gemini-2.5-flash`, `gemini-2.5-pro`
- [ ] Test with simple prompt
- [ ] ✅ You're ready to go!

---

**Happy coding with Gemini! 🚀**
