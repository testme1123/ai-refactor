from openai import OpenAI
import os
from ai_refactor.services.llm_client import BaseLLMClient

class OpenAIClient(BaseLLMClient):
    def __init__(self, api_key: str = None, model: str = "gpt-3.5-turbo"):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model

    def get_refactor(self, code: str) -> str:
        prompt = f"""
        Analyze the following code (language unknown) and:
        1. Detect the programming language.
        2. Suggest improvements, refactors, or security/performance fixes.
        3. Provide the improved code.

        Code:
        ```
        {code}
        ```
        Please output the detected language first, then your suggested improvements.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content
