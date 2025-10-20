from fastapi import APIRouter, HTTPException
from ai_refactor.models.code import CodeRequest, CodeResponse
from ai_refactor.services.llm_factory import get_llm_client  # unified LLM factory

router = APIRouter(prefix="/refactor", tags=["Refactor"])

@router.post("/", response_model=CodeResponse)
async def refactor_code(request: CodeRequest):
    """
    Accepts code and optional model name, returns a suggested refactor.
    Supports OpenAI, Local LLaMA, and DeepSeek-R1 models.
    """
    try:
        # Get the appropriate LLM client based on request.model
        client = get_llm_client(request.model)

        # Call the client's get_refactor method
        suggestion = client.get_refactor(request.code)

        # Ensure the suggestion is never empty
        if not suggestion or suggestion.strip() == "":
            suggestion = "No suggestion could be generated."

        return CodeResponse(suggestion=suggestion)

    except Exception as e:
        # Provide detailed error for debugging
        raise HTTPException(status_code=500, detail=f"LLM error: {str(e)}")

