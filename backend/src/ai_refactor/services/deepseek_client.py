import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from ai_refactor.services.llm_client import BaseLLMClient

class DeepSeekClient(BaseLLMClient):
    def __init__(self, api_key: str = None, model: str = "deepseek-ai/DeepSeek-R1"):
        load_dotenv()
        self.token = api_key or os.getenv("HUGGINGFACE_API_KEY")
        if not self.token:
            raise ValueError("HUGGINGFACE_API_KEY not found in .env file!")

        self.client = InferenceClient(token=self.token)
        self.model_name = model

    def get_refactor(self, code: str) -> str:
        prompt = f"""
Analyze the following code (language unknown) and:
1. Detect the programming language.
2. Suggest improvements, refactors, or security/performance fixes.
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
            max_tokens=500  # correct parameter for your version
        )

        # DEBUG: inspect raw response
        print("Raw Hugging Face response:", response)

        # Safely extract the content
        if hasattr(response, "choices") and response.choices:
            msg = response.choices[0].message
            if msg and "content" in msg:
                return msg["content"]

        return "No output from model"
