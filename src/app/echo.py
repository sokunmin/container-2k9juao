from fastapi import FastAPI
from fastapi_poe.types import ProtocolMessage
from fastapi_poe.client import get_bot_response
import asyncio

app = FastAPI()

async def get_responses(api_key, message_content):
    message = ProtocolMessage(role="user", content=message_content)
    responses = []
    async for partial in get_bot_response(messages=[message], bot_name="GPT-3.5-Turbo", api_key=api_key):
        responses.append(partial)
    return responses


@app.post("/api/respond")
async def respond(message_content: str):
    api_key = "ZUxAdhHe0TWI7RxnpIDo4KQakLm79WRr"  # Replace with your actual API key
    responses = await get_responses(api_key, message_content)
    return {"responses": responses}
