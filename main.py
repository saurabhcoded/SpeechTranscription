from fastapi import FastAPI, Query, File, UploadFile
from fastapi.responses import FileResponse
from speech import text2Speech,speech2Text

app = FastAPI()


@app.get("/speak/")
def speak(text: str = Query(..., min_length=1)):
    try:
        speechResponse = text2Speech(text)
        return FileResponse(
            path=speechResponse["path"],
            media_type=speechResponse["media_type"],
            filename=speechResponse["filename"]
        )
    except Exception as e:
        raise RuntimeError(f"Voice conversion failed: {e}")
    
@app.post("/transcribe/")
async def speak(file: UploadFile = File(...)):
    try:
        file_location = f"/tmp/{file.filename}"
        
        # Save uploaded file
        with open(file_location, "wb") as f:
            f.write(await file.read())

        # Transcribe
        text = speech2Text(file_location)
        return {"transcription": text}
    except Exception as e:
        raise RuntimeError(f"Transcription failed: {e}")
