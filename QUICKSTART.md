# Quick Start Guide - Gemini API Cookbook

Get started with the Gemini API Cookbook in just a few minutes!

## 🎯 One-Command Setup

```bash
# Run this single command to set everything up
./setup_local.sh && source venv/bin/activate
```

## 🔑 Add Your API Key

1. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Add it to `.env`:
   ```bash
   echo "GOOGLE_API_KEY='your-key-here'" > .env
   ```

## 🌐 Start Browsing

Launch the web interface:

```bash
python3 serve_local.py
```

Your browser will open to `http://localhost:8000` with a searchable index of all tutorials!

## 📓 Or Use Jupyter

Prefer notebooks? Start Jupyter:

```bash
jupyter notebook
```

## 🚀 Run Examples

Try the interactive Gradio audio example:

```bash
python3 examples/gradio_audio.py
```

## 📚 What's Available?

- **46 Quickstarts**: Learn specific API features
- **36 Examples**: See practical applications
- **Web Interface**: Browse everything in one place

## ❓ Need Help?

- 📖 Full guide: [DEPLOYMENT.md](./DEPLOYMENT.md)
- 🌐 Documentation: [ai.google.dev](https://ai.google.dev/gemini-api/docs)
- 💬 Forum: [discuss.ai.google.dev](https://discuss.ai.google.dev/)

## ⚡ Quick Examples

### Text Generation
```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Explain quantum computing')
print(response.text)
```

### Image Analysis
```python
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(['Describe this image', image])
print(response.text)
```

---

**Happy coding! 🌟**
