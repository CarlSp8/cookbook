
import os
from google import genai
from google.genai import types
from PIL import Image

class GeminiFramework:
    def __init__(self, api_key: str = None, model_id: str = "gemini-2.0-flash"):
        """
        Initialize the GeminiFramework.

        Args:
            api_key (str): The Google Gemini API key. If None, looks for GEMINI_API_KEY env var.
            model_id (str): The model ID to use (default: gemini-2.0-flash).
        """
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            print("Warning: No API key provided and GEMINI_API_KEY not found in environment.")
            # We don't raise an error immediately to allow for mock usage or later setup,
            # but client init will likely fail if attempted.

        self.model_id = model_id
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        else:
            self.client = None

        self.chat_session = None

    def generate_text(self, prompt: str, system_instruction: str = None) -> str:
        """
        Generate text from a prompt.

        Args:
            prompt (str): The prompt text.
            system_instruction (str, optional): System instructions for the model.

        Returns:
            str: The generated text response.
        """
        if not self.client:
            raise ValueError("Client not initialized. Please provide a valid API key.")

        config = types.GenerateContentConfig(
            system_instruction=system_instruction
        ) if system_instruction else None

        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt,
            config=config
        )
        return response.text

    def generate_with_image(self, prompt: str, image_path: str) -> str:
        """
        Generate content from a prompt and a local image.

        Args:
            prompt (str): The text prompt.
            image_path (str): Path to the image file.

        Returns:
            str: The generated response.
        """
        if not self.client:
            raise ValueError("Client not initialized.")

        try:
            image = Image.open(image_path)
            # Resize if necessary or handle limitations, simplified here
        except Exception as e:
            raise ValueError(f"Could not open image at {image_path}: {e}")

        response = self.client.models.generate_content(
            model=self.model_id,
            contents=[image, prompt]
        )
        return response.text

    def start_chat(self, history: list = None):
        """
        Start a new chat session.

        Args:
            history (list, optional): Initial history.
        """
        if not self.client:
            raise ValueError("Client not initialized.")

        self.chat_session = self.client.chats.create(
            model=self.model_id,
            history=history
        )

    def send_chat_message(self, message: str) -> str:
        """
        Send a message to the active chat session.

        Args:
            message (str): The message text.

        Returns:
            str: The response from the model.
        """
        if not self.chat_session:
            self.start_chat()

        response = self.chat_session.send_message(message)
        return response.text

    def upload_file(self, file_path: str) -> types.File:
        """
        Upload a file for use with the API.

        Args:
            file_path (str): Path to the file.

        Returns:
            types.File: The uploaded file object.
        """
        if not self.client:
            raise ValueError("Client not initialized.")

        return self.client.files.upload(file=file_path)

    def generate_from_file(self, prompt: str, file_obj: types.File) -> str:
        """
        Generate content using an uploaded file.

        Args:
            prompt (str): The prompt.
            file_obj (types.File): The file object returned from upload_file.

        Returns:
            str: Response text.
        """
        if not self.client:
            raise ValueError("Client not initialized.")

        response = self.client.models.generate_content(
            model=self.model_id,
            contents=[file_obj, prompt]
        )
        return response.text

    def count_tokens(self, prompt: str) -> int:
        """
        Count tokens for a given prompt.

        Args:
             prompt (str): The prompt text.

        Returns:
            int: The token count.
        """
        if not self.client:
             raise ValueError("Client not initialized.")

        response = self.client.models.count_tokens(
            model=self.model_id,
            contents=prompt,
        )
        return response.total_tokens
