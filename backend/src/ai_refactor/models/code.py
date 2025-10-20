from pydantic import BaseModel

# Input JSON model
class CodeRequest(BaseModel):
    code: str                  # The code snippet to analyze
    model: str = "llama"  # Optional, default model

# Output JSON model
class CodeResponse(BaseModel):
    suggestion: str            # The suggested refactored or improved code
