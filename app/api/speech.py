from fastapi import APIRouter, FileResponse, Request, HTTPException
from app.utils.file_ops import save_upload_file

router = APIRouter()

@router.get("/speak/")
def speech(request: Request):
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