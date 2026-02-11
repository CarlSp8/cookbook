# OpenAI SDK Compatibility with Gemini API

This directory contains guides and examples for using the **OpenAI SDK** with the **Gemini API**. Gemini API offers OpenAI SDK compatibility, allowing you to use familiar OpenAI client libraries to interact with Gemini models.

## 🚀 Quick Start

To use Gemini with the OpenAI SDK, simply point the base URL to Gemini's OpenAI-compatible endpoint:

**Python:**
```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

**JavaScript/TypeScript:**
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
    apiKey: process.env.GEMINI_API_KEY,
    baseURL: 'https://generativelanguage.googleapis.com/v1beta/openai/'
});

const response = await client.chat.completions.create({
    model: 'gemini-2.5-flash',
    messages: [{ role: 'user', content: 'Hello!' }]
});
console.log(response.choices[0].message.content);
```

## 📚 Available Guides

### Core Guides
| Guide | Description | Language |
|-------|-------------|----------|
| [Getting Started](../Get_started_OpenAI_Compatibility.ipynb) | Comprehensive introduction to using OpenAI SDK with Gemini | Python |
| [Basic Chat](./Basic_Chat.ipynb) | Simple text generation and chat completions | Python |
| [Basic Chat (JS)](./Basic_Chat.js) | Simple text generation and chat completions | JavaScript |
| [Working with Images](./Working_with_Images.ipynb) | Multimodal prompts with images | Python |
| [Structured Outputs](./Structured_Outputs.ipynb) | Extract structured data and JSON | Python |
| [Embeddings](./Embeddings.ipynb) | Generate text embeddings | Python |

### Advanced Guides
| Guide | Description | Language |
|-------|-------------|----------|
| [Batch Processing](./Batch_Processing.ipynb) | Process multiple requests efficiently | Python |
| [Function Calling](./Function_Calling.ipynb) | Use tools and function calling | Python |
| [Streaming Responses](./Streaming.ipynb) | Stream responses in real-time | Python |

### Migration & Comparison
| Guide | Description |
|-------|-------------|
| [OpenAI to Gemini Migration](./Migration_Guide.md) | Step-by-step migration guide |
| [Feature Comparison](./Feature_Comparison.md) | What works, what doesn't |
| [Limitations & Workarounds](./Limitations.md) | Known limitations and solutions |

## ✅ What Works with OpenAI SDK

The following features are **fully supported** using the OpenAI SDK:

- ✅ **Text Generation** - Chat completions with Gemini models
- ✅ **Multimodal Input** - Images in prompts
- ✅ **Structured Outputs** - JSON mode and response schemas
- ✅ **Function Calling** - Tool use and function execution
- ✅ **Embeddings** - Text embeddings generation
- ✅ **Batch API** - Batch request processing
- ✅ **Streaming** - Real-time response streaming
- ✅ **Model Listing** - Enumerate available models
- ✅ **Thinking Models** - Access to Gemini thinking models

## ⚠️ Limitations & Native SDK Required

Some features require the **native Gemini SDK**:

| Feature | OpenAI SDK | Workaround |
|---------|-----------|------------|
| **Video Input** | ❌ Not supported | Use [Gemini SDK](../Video_understanding.ipynb) |
| **File Upload API** | ⚠️ Limited | Use [Gemini File API](../File_API.ipynb) |
| **Audio Input** | ⚠️ Limited | Use [Gemini SDK for audio](../Audio.ipynb) |
| **Live API** | ❌ Not supported | Use [Gemini Live API](../Get_started_LiveAPI.ipynb) |
| **Grounding** | ❌ Not supported | Use [Gemini SDK](../Grounding.ipynb) |
| **Caching** | ❌ Not supported | Use [Gemini SDK](../Caching.ipynb) |

## 🔑 API Key Setup

Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Environment Variables

**Option 1: GOOGLE_API_KEY (Recommended)**
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

**Option 2: OPENAI_API_KEY**
```bash
export OPENAI_API_KEY="your-gemini-api-key-here"
export OPENAI_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai/"
```

### In Code

**Python:**
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("GOOGLE_API_KEY"),
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

## 🎯 Model Names

Use these model IDs with the OpenAI SDK:

| Model | ID | Best For |
|-------|-----|----------|
| Gemini 3.0 Flash Preview | `gemini-3-flash-preview` | Fast, multimodal tasks (preview) |
| Gemini 3.0 Pro Preview | `gemini-3-pro-preview` | Complex reasoning (preview) |
| Gemini 2.5 Flash | `gemini-2.5-flash` | Fast, everyday tasks |
| Gemini 2.5 Flash Lite | `gemini-2.5-flash-lite` | Ultra-fast, simple tasks |
| Gemini 2.5 Pro | `gemini-2.5-pro` | Complex, multi-step reasoning |

Full model list: [Gemini Models Documentation](https://ai.google.dev/gemini-api/docs/models/gemini)

## 🆚 OpenAI SDK vs Gemini SDK

### When to Use OpenAI SDK
- ✅ Migrating existing OpenAI code
- ✅ Using familiar OpenAI patterns
- ✅ Multi-provider compatibility
- ✅ Standard chat, embeddings, function calling

### When to Use Gemini SDK
- ✅ Video understanding
- ✅ Advanced audio capabilities
- ✅ Live API (real-time multimodal)
- ✅ Grounding with Google Search
- ✅ Context caching
- ✅ Latest Gemini-specific features

**Pro Tip:** You can use **both SDKs** in the same project for different features!

## 📖 Additional Resources

- [Official Gemini OpenAI Compatibility Docs](https://ai.google.dev/gemini-api/docs/openai)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [OpenAI Node.js SDK](https://github.com/openai/openai-node)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Gemini API Cookbook](https://github.com/google-gemini/cookbook)

## 🤝 Contributing

Found an issue or want to add more examples? Contributions welcome! See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

## 📜 License

Apache License 2.0 - See [LICENSE](../../LICENSE) for details.
