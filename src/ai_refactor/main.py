from fastapi import FastAPI
from ai_refactor.routers import refactor

app = FastAPI(
    title="AI-Powered Code Refactor API",
    description="Analyze any code snippet; LLM detects language and suggests refactors",
    version="1.0.0"
)

# Include router
app.include_router(refactor.router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to AI Code Refactor API"}
