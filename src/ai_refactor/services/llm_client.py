from abc import ABC, abstractmethod

class BaseLLMClient(ABC):
    """Abstract base class for any LLM client."""

    @abstractmethod
    def get_refactor(self, code: str) -> str:
        """Generate a refactor suggestion for the given code."""
        pass
