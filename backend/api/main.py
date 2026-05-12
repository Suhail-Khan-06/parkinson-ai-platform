from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.v1.routes_voice import router as voice_router
from backend.api.v1.routes_spiral import router as spiral_router
from backend.api.v1.routes_datscan import router as datscan_router
from backend.api.v1.routes_fusion import router as fusion_router

app = FastAPI(
    title="Parkinson AI API",
    version="1.0.0"
)

# Allow frontend domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://parkinson-ai-platform.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(voice_router, prefix="/api/v1")
app.include_router(spiral_router, prefix="/api/v1")
app.include_router(datscan_router, prefix="/api/v1")
app.include_router(fusion_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Parkinson AI API is running"}