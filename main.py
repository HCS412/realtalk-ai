from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload

app = FastAPI(
    title="RealTalk AI",
    description="Train AI on real conversations from the real world — not just Reddit or Silicon Valley.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS so you can later connect from a mobile or web frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only. Lock this down in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register route modules
app.include_router(upload.router, prefix="/api/upload", tags=["Upload"])

@app.get("/")
def root():
    return {"message": "Welcome to RealTalk AI"}
