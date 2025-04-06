from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.transcribe_service import transcribeText
from app.utils.file_ops import save_upload_file

router = APIRouter()

@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        file_path = await save_upload_file(file)
        text = transcribeText(file_path)
        return {"transcription": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
