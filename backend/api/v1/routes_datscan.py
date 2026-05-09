from fastapi import APIRouter, UploadFile, File

from backend.services.datscan_service import DATScanService

router = APIRouter()
service = None

def get_service():
    global service
    if service is None:
        service = DATScanService()
    return service


@router.post("/predict/datscan")
async def predict_datscan(
    file: UploadFile = File(...)
):

    result = service.predict(file.file)

    return result