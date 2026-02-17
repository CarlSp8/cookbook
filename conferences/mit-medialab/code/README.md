# Code Examples

This directory contains code examples and demos from MIT Media Lab presentations.

## Organization

Each subdirectory represents a different presentation or workshop:

```
code/
├── example-1/
│   ├── README.md
│   ├── requirements.txt
│   └── main.py
└── example-2/
    ├── README.md
    └── notebook.ipynb
```

## Adding New Examples

When adding a new code example:

1. Create a new subdirectory with a descriptive name
2. Include a README.md with:
   - Description of the example
   - Prerequisites
   - Setup instructions
   - Usage instructions
3. Include all necessary code files
4. If using Python, include a `requirements.txt` or `pyproject.toml`
5. Test that the example works before submitting

## Common Setup

Most examples will require:
- Python 3.8 or higher
- A Gemini API key (get one at [Google AI Studio](https://aistudio.google.com/app/apikey))
- The Google Generative AI Python library: `pip install google-generativeai`

For more information, see the [Gemini API Quickstart](https://github.com/google-gemini/cookbook/tree/main/quickstarts).
