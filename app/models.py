from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

# This model is used for returning metadata about uploaded files
class UploadResponse(BaseModel):
    file_id: str = Field(..., example=str(uuid.uuid4()))
    filename: str
    location_type: Optional[str] = Field(None, example="barbershop")
    tags: Optional[str] = Field(None, example="basketball,black culture")
    upload_time: datetime = Field(default_factory=datetime.utcnow)
    status: str = "success"
    message: str = "Audio uploaded successfully"
