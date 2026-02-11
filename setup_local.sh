#!/bin/bash

# Gemini API Cookbook - Local Setup Script
# This script sets up the local environment for running the cookbook examples

set -e

echo "=========================================="
echo "Gemini API Cookbook - Local Setup"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "Found Python version: $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists. Skipping creation."
else
    python3 -m venv venv
    echo "Virtual environment created successfully."
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "Virtual environment activated."
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "pip upgraded successfully."
echo ""

# Install core dependencies
echo "Installing core dependencies..."
pip install -q jupyter notebook ipykernel google-generativeai google-api-python-client python-dotenv
echo "Core dependencies installed."
echo ""

# Install additional dependencies for examples
echo "Installing additional dependencies for examples..."
pip install -q gradio gradio-webrtc websockets numpy 2>/dev/null || echo "Optional dependencies skipped (gradio)"
echo "Additional dependencies installed."
echo ""

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cat > .env << 'EOF'
# Gemini API Configuration
# Get your API key from: https://aistudio.google.com/app/apikey
GOOGLE_API_KEY=your_api_key_here
EOF
    echo ".env file created. Please add your GOOGLE_API_KEY to the .env file."
else
    echo ".env file already exists."
fi
echo ""

# Check if API key is set
if grep -q "your_api_key_here" .env 2>/dev/null; then
    echo "⚠️  WARNING: Please update the GOOGLE_API_KEY in the .env file with your actual API key."
    echo "   Get your API key from: https://aistudio.google.com/app/apikey"
    echo ""
fi

echo "=========================================="
echo "Setup completed successfully!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Add your API key to the .env file: nano .env"
echo "2. Activate the virtual environment: source venv/bin/activate"
echo "3. Start the local web server: python3 serve_local.py"
echo "4. Or run Jupyter notebooks: jupyter notebook"
echo ""
echo "To run specific examples:"
echo "  - Gradio audio example: python3 examples/gradio_audio.py"
echo "  - LiveAPI example: python3 quickstarts/Get_started_LiveAPI.py"
echo ""
