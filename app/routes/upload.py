from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Optional
import uuid
import os

router = APIRouter()

# Ensure a temp folder exists for saving files locally (for now)
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

@router.post("/audio")
async def upload_audio(
    audio_file: UploadFile = File(...),
    location_type: Optional[str] = Form(None),
    tags: Optional[str] = Form(None)
):
    try:
        # Create a unique filename
        file_id = str(uuid.uuid4())
        original_filename = audio_file.filename
        saved_filename = f"{file_id}_{original_filename}"
        file_path = os.path.join(TEMP_DIR, saved_filename)

        # Save the uploaded audio file temporarily
        with open(file_path, "wb") as f:
            f.write(await audio_file.read())

        return JSONResponse({
            "status": "success",
            "message": "Audio uploaded successfully",
            "file_id": file_id,
            "filename": saved_filename,
            "location_type": location_type,
            "tags": tags
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={
            "status": "error",
            "message": str(e)
        })
