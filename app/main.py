# Updated
from fastapi import FastAPI
from app.api import transcribe, ai_chat, speech

app = FastAPI()
app.include_router(transcribe.router)
app.include_router(ai_chat.router)
app.include_router(speech.router)

@app.get("/")
def not_found():
    return f"Welcome to page"
    
@app.on_event("startup")
async def show_routes():
    print("Available Routes:")
    for route in app.routes:
        print(f"{route.path} → {route.name}")