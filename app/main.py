# Updated
from fastapi import FastAPI
from app.api import transcribe, ai_chat, speech

app = FastAPI()
app.include_router(transcribe.router)
app.include_router(ai_chat.router)
app.include_router(ai_chat.router)
app.include_router(ai_chat.speech)
