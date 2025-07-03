import whisper
import re

# Load Whisper model (use 'base' for speed — later we can try 'medium' or 'large')
model = whisper.load_model("base")

def transcribe_and_anonymize(audio_path: str) -> dict:
    # Transcribe audio
    result = model.transcribe(audio_path)

    # Raw transcription text
    original_text = result.get("text", "")

    # Run anonymization
    scrubbed_text = scrub_text(original_text)

    return {
        "transcription": original_text,
        "anonymized_transcription": scrubbed_text
    }

def scrub_text(text: str) -> str:
    # Very basic PII scrubber for demo purposes
    # We’ll expand later with better NER (Named Entity Recognition)

    scrubbed = text

    # Remove phone numbers
    scrubbed = re.sub(r"\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b", "[PHONE]", scrubbed)

    # Remove emails
    scrubbed = re.sub(r"\S+@\S+\.\S+", "[EMAIL]", scrubbed)

    # Remove names (placeholder: remove any capitalized word pairs)
    scrubbed = re.sub(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", "[NAME]", scrubbed)

    return scrubbed
