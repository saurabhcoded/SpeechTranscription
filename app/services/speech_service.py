from TTS.api import TTS
from pathlib import Path
import uuid

TEMP_DIR = Path("/tmp")
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def text2Speech(text):
    file_id = f"{uuid.uuid4()}.wav"
    output_path = TEMP_DIR / file_id

    tts.tts_to_file(text=text, file_path=str(output_path))

    return {
        "path": output_path,
        "media_type": "audio/wav",
        "filename": "tts.wav"
    }