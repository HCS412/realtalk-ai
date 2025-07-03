from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Optional
import uuid

from app.services.storage import save_audio_locally, get_upload_metadata
from app.services.anonymizer import transcribe_and_anonymize
from app.models import UploadResponse

router = APIRouter()

@router.post("/audio", response_model=UploadResponse)
async def upload_audio(
    audio_file: UploadFile = File(...),
    location_type: Optional[str] = Form(None),
    tags: Optional[str] = Form(None)
):
    try:
        # Generate unique filename
        file_id = str(uuid.uuid4())
        filename = f"{file_id}_{audio_file.filename}"

        # Save audio to temp folder
        file_path = save_audio_locally(audio_file, filename)

        # Transcribe and anonymize
        transcript_data = transcribe_and_anonymize(file_path)

        # Prepare metadata
        metadata = get_upload_metadata(
            file_id=file_id,
            filename=filename,
            location_type=location_type,
            tags=tags
        )

        # Build full response
        response = {
            **metadata,
            "status": "success",
            "message": "Audio uploaded and processed successfully",
            "transcription": transcript_data["transcription"],
            "anonymized_transcription": transcript_data["anonymized_transcription"]
        }

        return JSONResponse(content=response)

    except Exception as e:
        return JSONResponse(status_code=500, content={
            "status": "error",
            "message": str(e)
        })
