# app/utils/file_ops.py
import os
import shutil
import uuid
from fastapi import UploadFile
from app.core.config import settings

async def save_upload_file(upload_file: UploadFile, destination: str = None) -> str:
    ext = os.path.splitext(upload_file.filename)[-1]
    tmp_filename = f"{uuid.uuid4()}{ext}"
    tmp_dir = settings.TMP_DIR if not destination else destination
    os.makedirs(tmp_dir, exist_ok=True)
    file_path = os.path.join(tmp_dir, tmp_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return file_path

def delete_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)
