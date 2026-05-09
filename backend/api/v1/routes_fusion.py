import json
from io import BytesIO

from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from PIL import Image

import pydicom
import numpy as np

from backend.utils.report_generator import generate_report
from backend.services.fusion_service import FusionService

router = APIRouter()

# ==========================================================
# Lazy-loaded Fusion Service
# Prevents Render free-tier memory crash on startup
# ==========================================================

service = None


def get_service():
    global service

    if service is None:
        service = FusionService()

    return service


# ==========================================================
# Helper Function: Load DATScan (PNG/JPG/DICOM)
# ==========================================================

def load_datscan_image(upload_file: UploadFile):
    filename = upload_file.filename.lower()

    # -----------------------------------
    # Standard image formats
    # -----------------------------------
    if filename.endswith((".png", ".jpg", ".jpeg")):
        image = Image.open(
            BytesIO(upload_file.file.read())
        ).convert("RGB")
        return image

    # -----------------------------------
    # DICOM format
    # -----------------------------------
    elif filename.endswith(".dcm"):
        dicom = pydicom.dcmread(upload_file.file)

        pixel_array = dicom.pixel_array.astype(np.float32)

        # Normalize to 0–255
        pixel_array -= pixel_array.min()

        if pixel_array.max() > 0:
            pixel_array /= pixel_array.max()

        pixel_array *= 255.0
        pixel_array = pixel_array.astype(np.uint8)

        image = Image.fromarray(pixel_array).convert("RGB")

        return image

    # -----------------------------------
    # Unsupported format
    # -----------------------------------
    else:
        raise ValueError(
            "Unsupported DATScan format. Use PNG, JPG, JPEG, or DICOM."
        )


# ==========================================================
# Multimodal Prediction Endpoint
# ==========================================================

@router.post("/predict/fusion")
async def predict_fusion(
    voice_data: str = Form(...),
    spiral_file: UploadFile = File(...),
    datscan_file: UploadFile = File(...)
):
    # Lazy-load model only when endpoint is called
    service = get_service()

    try:
        # -----------------------------------
        # Parse voice JSON
        # -----------------------------------
        voice_features = json.loads(voice_data)

        # -----------------------------------
        # Load spiral image
        # -----------------------------------
        spiral_image = Image.open(
            BytesIO(await spiral_file.read())
        ).convert("RGB")

        # -----------------------------------
        # Load DATScan
        # -----------------------------------
        datscan_image = load_datscan_image(datscan_file)

        # -----------------------------------
        # Run multimodal fusion
        # -----------------------------------
        result = service.predict(
            voice_features,
            spiral_image,
            datscan_image
        )

        return result

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


# ==========================================================
# PDF Report Endpoint
# ==========================================================

@router.post("/fusion/report")
async def generate_fusion_report(
    voice_data: str = Form(...),
    spiral_file: UploadFile = File(...),
    datscan_file: UploadFile = File(...)
):
    # Lazy-load model only when endpoint is called
    service = get_service()

    try:
        # -----------------------------------
        # Parse voice JSON
        # -----------------------------------
        voice_features = json.loads(voice_data)

        # -----------------------------------
        # Load spiral image
        # -----------------------------------
        spiral_image = Image.open(
            BytesIO(await spiral_file.read())
        ).convert("RGB")

        # -----------------------------------
        # Load DATScan
        # -----------------------------------
        datscan_image = load_datscan_image(datscan_file)

        # -----------------------------------
        # Run prediction
        # -----------------------------------
        result = service.predict(
            voice_features,
            spiral_image,
            datscan_image
        )

        # -----------------------------------
        # Generate PDF report
        # -----------------------------------
        pdf_path = generate_report(
            fusion_result=result["fusion_result"],
            voice_result=result["voice_result"],
            spiral_result=result["spiral_result"],
            datscan_result=result["datscan_result"],
            explanation=result["explanation"],
            output_path="parkinson_report.pdf"
        )

        # -----------------------------------
        # Return PDF file
        # -----------------------------------
        return FileResponse(
            pdf_path,
            media_type="application/pdf",
            filename="parkinson_report.pdf"
        )

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }