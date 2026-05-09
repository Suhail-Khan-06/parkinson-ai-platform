from fastapi import APIRouter, HTTPException, UploadFile, File
import pandas as pd

from backend.schemas.voice_schema import VoiceRequest, VoiceResponse
from backend.services.voice_service import VoiceService

router = APIRouter()

# ==========================================================
# Lazy-loaded Voice Service
# ==========================================================

service = None


def get_service():
    global service

    if service is None:
        service = VoiceService()

    return service


# ==========================================================
# JSON Prediction Endpoint
# ==========================================================

@router.post("/predict/voice", response_model=VoiceResponse)
def predict_voice(request: VoiceRequest):
    service = get_service()

    try:
        return service.predict(request.features)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# ==========================================================
# CSV Upload Prediction Endpoint
# ==========================================================

@router.post("/predict/voice/csv")
async def predict_voice_csv(file: UploadFile = File(...)):
    service = get_service()

    try:
        df = pd.read_csv(file.file)

        # Remove optional columns if present
        if "name" in df.columns:
            df = df.drop(columns=["name"])

        if "status" in df.columns:
            df = df.drop(columns=["status"])

        results = service.predict_batch(df)

        return {
            "num_samples": len(results),
            "results": results
        }

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Invalid CSV: {str(e)}"
        )