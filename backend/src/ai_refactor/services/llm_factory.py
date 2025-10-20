from ai_refactor.services.open_ai_service import OpenAIClient
from ai_refactor.services.local_llm_service import LocalLLMClient
from ai_refactor.services.deepseek_client import DeepSeekClient

def get_llm_client(model_name: str = "openai"):
    """
    Returns an instance of the appropriate LLM client.
    Supports:
        - OpenAI (GPT-3.5, GPT-4)
        - Local LLaMA models
        - DeepSeek-R1 via Hugging Face OpenAI-compatible API
    """
    model_name = model_name.lower().strip()

    # OpenAI models
    if model_name in ["openai", "gpt", "gpt-3.5-turbo", "gpt-4"]:
        return OpenAIClient(model=model_name)

    # Local LLaMA models
    elif model_name in ["llama", "llama2", "local"]:
        return LocalLLMClient()

    # DeepSeek-R1 model
    elif model_name in ["deepseek", "deepseek-r1"]:
        # Use the exact Hugging Face repo ID
        return DeepSeekClient(model="deepseek-ai/DeepSeek-R1")

    else:
        raise ValueError(f"Unsupported model: {model_name}")
