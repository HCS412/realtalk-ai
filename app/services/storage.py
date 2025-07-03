import os
import shutil
from datetime import datetime

# Temporary directory for storing files
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

def save_audio_locally(uploaded_file, filename: str) -> str:
    """
    Saves uploaded audio to the temp directory
    """
    file_path = os.path.join(TEMP_DIR, filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    return file_path

def cleanup_temp_file(file_path: str):
    """
    Optionally delete file after processing
    """
    if os.path.exists(file_path):
        os.remove(file_path)

def get_upload_metadata(file_id: str, filename: str, location_type: str = None, tags: str = None) -> dict:
    """
    Generate consistent metadata dictionary for audio uploads
    """
    return {
        "file_id": file_id,
        "filename": filename,
        "location_type": location_type,
        "tags": tags,
        "upload_time": datetime.utcnow().isoformat()
    }
