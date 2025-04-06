from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import FileResponse
from app.utils.file_ops import save_upload_file
from app.services.speech_service import text2Speech
router = APIRouter()

@router.post("/speak")
async def speech(request: Request):
    try:
        body = await request.json()
        speech_txt = body.get("speech_txt")
        speechResponse = text2Speech(speech_txt)
        return FileResponse(
            path=speechResponse["path"],
            media_type=speechResponse["media_type"],
            filename=speechResponse["filename"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))