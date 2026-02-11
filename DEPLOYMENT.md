# Gemini API Cookbook - Local Deployment Guide

This guide explains how to set up and run the Gemini API Cookbook locally on your machine.

## Table of Contents

- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Cookbook](#running-the-cookbook)
- [Using Jupyter Notebooks](#using-jupyter-notebooks)
- [Running Python Examples](#running-python-examples)
- [Troubleshooting](#troubleshooting)
- [Advanced Configuration](#advanced-configuration)

## Quick Start

The fastest way to get started:

```bash
# 1. Clone the repository (if not already done)
git clone https://github.com/google-gemini/cookbook.git
cd cookbook

# 2. Run the setup script
chmod +x setup_local.sh
./setup_local.sh

# 3. Add your API key to .env file
nano .env  # or use your preferred editor

# 4. Activate the virtual environment
source venv/bin/activate

# 5. Start the local web server
python3 serve_local.py
```

Your browser should automatically open to `http://localhost:8000` where you can browse all available tutorials and examples.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**: Check with `python3 --version`
- **pip**: Usually comes with Python
- **Git**: For cloning the repository
- **A Gemini API Key**: Get one from [Google AI Studio](https://aistudio.google.com/app/apikey)

### Optional Dependencies

For specific examples, you may need:
- **ffmpeg@6**: Required for the Gradio audio examples (Mac: `brew install ffmpeg@6`)
- **Node.js**: Required for JavaScript examples (if using quickstarts-js)

## Installation

### Step 1: Setup the Environment

Run the setup script to create a virtual environment and install dependencies:

```bash
./setup_local.sh
```

This script will:
- ✅ Create a Python virtual environment
- ✅ Install core dependencies (Jupyter, google-generativeai, etc.)
- ✅ Install additional dependencies for examples (gradio, websockets, etc.)
- ✅ Create a `.env` file for your API key

### Step 2: Configure Your API Key

1. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Open the `.env` file:
   ```bash
   nano .env
   ```
3. Replace `your_api_key_here` with your actual API key:
   ```
   GOOGLE_API_KEY=AIza...your_key_here
   ```
4. Save and close the file

### Step 3: Activate the Virtual Environment

```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

## Running the Cookbook

### Option 1: Web Browser Interface (Recommended)

Start the local web server to browse all tutorials:

```bash
python3 serve_local.py
```

This will:
- Generate an index page listing all quickstarts and examples
- Start a web server on `http://localhost:8000`
- Automatically open your browser

Features:
- 🔍 Search functionality to find specific tutorials
- 📊 Statistics showing available resources
- 🎨 Clean, modern interface
- 📱 Mobile-responsive design

### Option 2: Jupyter Notebook Interface

For an interactive notebook experience:

```bash
jupyter notebook
```

This will:
- Start Jupyter Notebook server
- Open the Jupyter interface in your browser
- Allow you to navigate to any `.ipynb` file and run it

### Option 3: JupyterLab (Advanced)

For a more feature-rich IDE experience:

```bash
# Install JupyterLab (if not already installed)
pip install jupyterlab

# Start JupyterLab
jupyter lab
```

## Using Jupyter Notebooks

### Running a Notebook

1. Navigate to the notebook you want to run (via web interface or Jupyter)
2. Open the `.ipynb` file
3. Run cells individually with `Shift+Enter` or run all cells from the menu

### Common Notebook Commands

- `Shift + Enter`: Run current cell and move to next
- `Ctrl + Enter`: Run current cell and stay on it
- `Alt + Enter`: Run current cell and insert new cell below
- `DD` (press D twice): Delete current cell
- `A`: Insert cell above
- `B`: Insert cell below

### API Key in Notebooks

Most notebooks expect your API key to be available. The setup ensures it's loaded from `.env`:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('GOOGLE_API_KEY')
```

Or you can set it directly in the notebook:

```python
import os
os.environ['GOOGLE_API_KEY'] = 'your-api-key-here'
```

## Running Python Examples

### Interactive Examples

Some examples like `gradio_audio.py` provide interactive web interfaces:

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Run the Gradio audio example
python3 examples/gradio_audio.py
```

This will start a Gradio interface at `http://127.0.0.1:7860/`

### LiveAPI Examples

To run LiveAPI examples:

```bash
python3 quickstarts/Get_started_LiveAPI.py
```

### Script Examples

For standalone scripts:

```bash
python3 quickstarts/file-api/sample.py
```

## Troubleshooting

### API Key Issues

**Problem**: "API key not found" or authentication errors

**Solution**:
1. Verify your API key is correctly set in `.env`
2. Make sure you're using the correct key from [Google AI Studio](https://aistudio.google.com/app/apikey)
3. Check that `.env` is in the repository root
4. Ensure the virtual environment is activated

### Import Errors

**Problem**: `ModuleNotFoundError` when running examples

**Solution**:
```bash
# Activate virtual environment
source venv/bin/activate

# Install missing package
pip install <package-name>

# Or reinstall all dependencies
pip install -r quickstarts/file-api/requirements.txt
```

### Port Already in Use

**Problem**: Port 8000 is already in use

**Solution**:
```bash
# Find and kill the process using port 8000
lsof -ti:8000 | xargs kill -9

# Or use a different port
python3 serve_local.py --port 8080
```

### Jupyter Kernel Issues

**Problem**: Kernel not found or crashes

**Solution**:
```bash
# Ensure ipykernel is installed
pip install ipykernel

# Register the kernel
python3 -m ipykernel install --user --name=venv
```

### FFmpeg Issues (Gradio Examples)

**Problem**: Gradio audio examples fail

**Solution** (macOS):
```bash
brew uninstall ffmpeg
brew install ffmpeg@6
brew link ffmpeg@6
```

**Solution** (Linux):
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

## Advanced Configuration

### Custom Port for Web Server

Edit `serve_local.py` and change the `PORT` variable:

```python
PORT = 8080  # or any other port
```

### Installing Additional Dependencies

For specific examples that require extra packages:

```bash
source venv/bin/activate
pip install <package-name>
```

### Using with Docker (Optional)

If you prefer containerized deployment, you can create a Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir jupyter google-generativeai google-api-python-client python-dotenv

EXPOSE 8000

CMD ["python3", "serve_local.py"]
```

Build and run:
```bash
docker build -t gemini-cookbook .
docker run -p 8000:8000 -v $(pwd)/.env:/app/.env gemini-cookbook
```

### Environment Variables

You can set additional environment variables in `.env`:

```bash
GOOGLE_API_KEY=your_key_here
JUPYTER_PORT=8888
SERVER_PORT=8000
```

### Updating the Cookbook

To update to the latest version:

```bash
git pull origin main
./setup_local.sh  # Reinstall dependencies if needed
python3 generate_index.py  # Regenerate index
```

## Available Resources

After setup, you'll have access to:

- **125+ Jupyter Notebooks**: Interactive tutorials covering all Gemini API features
- **Python Scripts**: Standalone examples for specific use cases
- **Web Interface**: Browse all resources with search functionality
- **Documentation**: Comprehensive guides and API references

## Getting Help

If you encounter issues:

1. Check this troubleshooting guide
2. Review the [main README](README.md)
3. Visit the [Google AI Developer Forum](https://discuss.ai.google.dev/)
4. Check the [official documentation](https://ai.google.dev/gemini-api/docs)

## Next Steps

After setup:

1. 📚 Start with [Get Started](quickstarts/Get_started.ipynb) notebook
2. 🔐 Review [Authentication](quickstarts/Authentication.ipynb) guide
3. 🎯 Explore specific features in quickstarts
4. 💡 Try practical examples for real-world applications
5. 🚀 Build your own applications using the Gemini API

---

**Happy coding with Gemini API! 🌟**
