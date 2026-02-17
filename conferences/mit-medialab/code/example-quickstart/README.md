# Example: Gemini API Quickstart

This is an example of how to structure code examples for MIT Media Lab presentations.

## Description

A simple example demonstrating basic text generation with the Gemini API. This example can be used as a template for adding your own code examples.

## Prerequisites

- Python 3.8 or higher
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your API key as an environment variable:
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   ```

   Or on Windows:
   ```cmd
   set GOOGLE_API_KEY=your-api-key-here
   ```

## Usage

Run the example:
```bash
python quickstart.py
```

The script will:
1. Initialize the Gemini API client
2. Generate a response to a simple prompt
3. Print the result

## Code Structure

- `quickstart.py` - Main example script
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Related Resources

- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Python SDK Documentation](https://ai.google.dev/gemini-api/docs/quickstart?lang=python)
- [More Examples](https://github.com/google-gemini/cookbook/tree/main/quickstarts)

## License

This example follows the license of the cookbook repository. See [LICENSE](../../../LICENSE).
