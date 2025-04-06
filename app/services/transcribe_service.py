import whisper

model = whisper.load_model("tiny")

def transcribeText(filePath,language='English'):
    # Transcribe the audio
    result = model.transcribe(filePath, language=language.lower())
    
    return result['text']