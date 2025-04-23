from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.llama_chat import ask_mistral

router = APIRouter()

class Prompt(BaseModel):
    prompt: str

@router.post("/chat")
async def chat(prompt_data: Prompt):
    response = ask_mistral(prompt_data.prompt)
    return {"response": response}
