import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "base")  # Whisper model
    TMP_DIR = os.getenv("TMP_DIR", "/tmp")

settings = Settings()
