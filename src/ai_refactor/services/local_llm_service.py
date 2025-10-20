from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from ai_refactor.services.llm_client import BaseLLMClient

class LocalLLMClient(BaseLLMClient):
    def __init__(self):
        """
        Initializes a Hugging Face InferenceClient for Meta-LLaMA-3.
        Requires HUGGINGFACE_API_KEY in your .env file.
        """
        load_dotenv()
        hf_token = os.getenv("HUGGINGFACE_API_KEY")
        if not hf_token:
            raise ValueError("HUGGINGFACE_API_KEY not found in .env file!")

        self.client = InferenceClient(token=hf_token)
        self.model_name = "meta-llama/Meta-Llama-3-8B-Instruct"

    def get_refactor(self, code: str) -> str:
        """
        Sends a chat-style prompt to the remote LLaMA model.
        Returns the assistant’s response as a string.
        """
        prompt = f"""
Analyze the following code (language unknown) and:
1. Detect the programming language.
2. Suggest improvements, refactors, or performance/security fixes.
3. Provide the improved code.

Code:
{code}
"""
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]

        response = self.client.chat_completion(
            model=self.model_name,
            messages=messages,
            max_tokens=500
        )

        return response.choices[0].message["content"]