from fastapi import APIRouter, UploadFile, File

from backend.services.datscan_service import DATScanService

router = APIRouter()

service = DATScanService()


@router.post("/predict/datscan")
async def predict_datscan(
    file: UploadFile = File(...)
):

    result = service.predict(file.file)

    return result