from fastapi import FastAPI
from pydantic import BaseModel

from llm_service import LLMService

app = FastAPI()
openApiClient = LLMService()


class PromptRequest(BaseModel):
    prompt: str


@app.post("/prompt")
async def prompt(request: PromptRequest):
    return openApiClient.process(request.prompt)