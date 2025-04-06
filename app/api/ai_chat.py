from fastapi import APIRouter, Request, HTTPException
from app.services.ai_service import aiprompt_handle

router = APIRouter()

@router.post("/ask_ai")
async def ai_response(request: Request):
    try:
        body = await request.json()
        prompt = body.get("prompt")
        if not prompt:
            raise HTTPException(status_code=422, detail="Missing 'prompt'")
        result = aiprompt_handle(prompt)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
