# Migrating from OpenAI API to Gemini API

This guide helps you migrate your existing **OpenAI API code** to use **Gemini models** with minimal changes. Gemini API offers OpenAI SDK compatibility, making migration straightforward for most use cases.

## 🚀 Quick Migration (2 Steps!)

For most OpenAI code, migration requires only **2 changes**:

### Step 1: Change the API Key and Base URL

**Before (OpenAI):**
```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")  # OpenAI API key
```

**After (Gemini with OpenAI SDK):**
```python
from openai import OpenAI

client = OpenAI(
    api_key="AIza...",  # Gemini API key from ai.google.dev
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
```

### Step 2: Update Model Names

**Before (OpenAI):**
```python
response = client.chat.completions.create(
    model="gpt-4o",  # or gpt-4, gpt-3.5-turbo, etc.
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**After (Gemini):**
```python
response = client.chat.completions.create(
    model="gemini-2.5-pro",  # or gemini-2.5-flash, gemini-3-flash-preview
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**That's it!** Most of your code will work without further changes.

---

## 📋 Model Mapping Guide

Here's how OpenAI models map to Gemini models:

| OpenAI Model | Gemini Equivalent | Use Case |
|--------------|-------------------|----------|
| **gpt-4o** | `gemini-2.5-pro` | Complex reasoning, long context |
| **gpt-4o-mini** | `gemini-2.5-flash` | Fast, everyday tasks |
| **gpt-4-turbo** | `gemini-2.5-pro` | Advanced capabilities |
| **gpt-4** | `gemini-2.5-pro` | Deep reasoning |
| **gpt-3.5-turbo** | `gemini-2.5-flash-lite` | Simple, fast tasks |
| **text-embedding-3-large** | `text-embedding-004` | Text embeddings |
| **text-embedding-3-small** | `text-embedding-004` | Text embeddings |
| **text-embedding-ada-002** | `text-embedding-004` | Text embeddings |
| **o1** (reasoning) | `gemini-2.5-pro` with thinking | Complex problem solving |
| **o1-mini** | `gemini-2.5-flash` with thinking | Fast reasoning |

### Latest Gemini Models (Preview)
- `gemini-3-flash-preview` - Next-gen fast model
- `gemini-3-pro-preview` - Next-gen reasoning model

---

## 🔧 Common Migration Scenarios

### 1. Basic Chat Completion

**OpenAI:**
```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is AI?"}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)
```

**Gemini (OpenAI SDK):**
```python
from openai import OpenAI

client = OpenAI(
    api_key="AIza...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",  # ← Only change
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is AI?"}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)
```

**Changes:** ✅ Just API key, base URL, and model name!

---

### 2. Streaming Responses

**OpenAI:**
```python
stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

**Gemini (OpenAI SDK):**
```python
stream = client.chat.completions.create(
    model="gemini-2.5-flash",  # ← Only change
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

**Changes:** ✅ Just model name!

---

### 3. Vision / Image Input

**OpenAI:**
```python
response = client.chat.completions.create(
    model="gpt-4o",
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

**Gemini (OpenAI SDK):**
```python
response = client.chat.completions.create(
    model="gemini-2.5-flash",  # ← Only change
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

**Changes:** ✅ Just model name!

---

### 4. Function Calling

**OpenAI:**
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=tools,
    tool_choice="auto"
)
```

**Gemini (OpenAI SDK):**
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gemini-2.5-flash",  # ← Only change
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=tools,
    tool_choice="auto"
)
```

**Changes:** ✅ Just model name!

---

### 5. JSON Mode / Structured Outputs

**OpenAI:**
```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "List 3 colors in JSON"}],
    response_format={"type": "json_object"}
)
```

**Gemini (OpenAI SDK):**
```python
response = client.chat.completions.create(
    model="gemini-2.5-flash",  # ← Only change
    messages=[{"role": "user", "content": "List 3 colors in JSON"}],
    response_format={"type": "json_object"}
)
```

**Changes:** ✅ Just model name!

---

### 6. Embeddings

**OpenAI:**
```python
response = client.embeddings.create(
    model="text-embedding-3-large",
    input="Hello world"
)
embedding = response.data[0].embedding
```

**Gemini (OpenAI SDK):**
```python
response = client.embeddings.create(
    model="text-embedding-004",  # ← Gemini embedding model
    input="Hello world"
)
embedding = response.data[0].embedding
```

**Changes:** ✅ Just model name!

---

### 7. Batch API

**OpenAI:**
```python
batch = client.batches.create(
    input_file_id="file-abc123",
    endpoint="/v1/chat/completions",
    completion_window="24h"
)
```

**Gemini (OpenAI SDK):**
```python
batch = client.batches.create(
    input_file_id="file-abc123",
    endpoint="/v1/chat/completions",
    completion_window="24h"
)
```

**Changes:** ✅ None! Works as-is (just update model names in batch file).

---

## ⚠️ Known Differences & Limitations

While most features work identically, here are some differences to be aware of:

### 1. Video Understanding
**Status:** ❌ Not available via OpenAI SDK

**Workaround:** Use native Gemini SDK
```python
import google.generativeai as genai

genai.configure(api_key="AIza...")
model = genai.GenerativeModel('gemini-2.5-flash')
video_file = genai.upload_file('video.mp4')
response = model.generate_content([video_file, "Describe this video"])
```

### 2. Large Audio/Video Files
**Status:** ⚠️ Limited in OpenAI SDK (20MB max request size)

**Workaround:** Use Gemini File API
```python
import google.generativeai as genai

genai.configure(api_key="AIza...")
audio_file = genai.upload_file('large_audio.mp3')
model = genai.GenerativeModel('gemini-2.5-flash')
response = model.generate_content([audio_file, "Transcribe this"])
```

### 3. Grounding with Google Search
**Status:** ❌ Not available via OpenAI SDK

**Workaround:** Use native Gemini SDK
```python
from google.generativeai.types import Tool, GoogleSearch

model = genai.GenerativeModel(
    'gemini-2.5-flash',
    tools=[Tool(google_search=GoogleSearch())]
)
response = model.generate_content("Latest AI news?")
```

### 4. Context Caching
**Status:** ❌ Not available via OpenAI SDK

**Workaround:** Use Gemini Caching API
```python
cached_content = genai.caching.CachedContent.create(
    model='gemini-2.5-flash',
    contents=[large_document],
    ttl='3600s'
)
model = genai.GenerativeModel.from_cached_content(cached_content)
```

### 5. Live API (Real-time)
**Status:** ❌ Not available via OpenAI SDK

**Workaround:** Use Gemini Live API with native SDK

---

## 🛠️ Environment Variables

### OpenAI Standard
```bash
export OPENAI_API_KEY="sk-..."
```

### Gemini with OpenAI SDK
**Option 1: Use GOOGLE_API_KEY**
```bash
export GOOGLE_API_KEY="AIza..."
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

**Option 2: Reuse OPENAI_API_KEY**
```bash
export OPENAI_API_KEY="AIza..."
export OPENAI_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai/"
```

Then in code:
```python
from openai import OpenAI

client = OpenAI()  # Reads OPENAI_API_KEY and OPENAI_BASE_URL automatically
```

---

## 📊 Cost Comparison

Gemini models are often more cost-effective than OpenAI:

| Task | OpenAI (gpt-4o) | Gemini (2.5-pro) | Savings |
|------|-----------------|------------------|---------|
| Input (per 1M tokens) | $2.50 | $1.25 | **50%** |
| Output (per 1M tokens) | $10.00 | $5.00 | **50%** |
| Embeddings (per 1M tokens) | $0.13 | $0.025 | **81%** |

*Prices as of 2025. Check latest pricing on [ai.google.dev](https://ai.google.dev/pricing)*

---

## ✅ Migration Checklist

- [ ] Get Gemini API key from [ai.google.dev](https://aistudio.google.com/app/apikey)
- [ ] Update `api_key` to Gemini API key
- [ ] Add `base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`
- [ ] Update model names (see mapping table above)
- [ ] Test text generation
- [ ] Test streaming (if used)
- [ ] Test vision/images (if used)
- [ ] Test function calling (if used)
- [ ] Test embeddings (if used)
- [ ] Test batch API (if used)
- [ ] Identify features requiring native Gemini SDK (video, grounding, caching)
- [ ] Add native Gemini SDK for advanced features (if needed)
- [ ] Update error handling (error formats may differ slightly)
- [ ] Test thoroughly in staging environment
- [ ] Monitor token usage and costs
- [ ] Deploy to production!

---

## 🆘 Troubleshooting

### Error: "Invalid API key"
- ✅ Ensure you're using a **Gemini API key** from [ai.google.dev](https://aistudio.google.com/app/apikey)
- ✅ OpenAI API keys (`sk-...`) won't work with Gemini

### Error: "Model not found"
- ✅ Check model name is correct (e.g., `gemini-2.5-flash`, not `gpt-4o`)
- ✅ Use `client.models.list()` to see available models

### Responses seem different
- ✅ Gemini models have different behaviors than GPT models
- ✅ Adjust `temperature`, system instructions, or prompts as needed
- ✅ Gemini models may be more or less creative depending on the task

### Video input not working
- ✅ Video is not supported via OpenAI SDK
- ✅ Use native Gemini SDK with File API

### Large files failing
- ✅ OpenAI SDK has 20MB request limit
- ✅ Use Gemini File API for large files

---

## 📚 Next Steps

- [Feature Comparison](./Feature_Comparison.md) - Detailed comparison of capabilities
- [Limitations & Workarounds](./Limitations.md) - Known issues and solutions
- [Basic Chat Example](./Basic_Chat.ipynb) - Start with simple examples
- [Comprehensive Guide](../Get_started_OpenAI_Compatibility.ipynb) - Full walkthrough

---

## 🎯 Summary

**Migration is easy:** For most use cases, you only need to change:
1. API key
2. Base URL
3. Model names

**The rest of your code stays the same!**

For advanced Gemini features (video, grounding, caching), you'll need the native Gemini SDK, but you can use both SDKs together in the same project.

Happy migrating! 🚀
