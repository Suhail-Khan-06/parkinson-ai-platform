from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image
import io

from backend.services.spiral_service import SpiralService

router = APIRouter()
service = None

def get_service():
    global service
    if service is None:
        service = SpiralService()
    return service

@router.post("/predict/spiral")
async def predict_spiral(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        result = spiral_service.predict(image)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))