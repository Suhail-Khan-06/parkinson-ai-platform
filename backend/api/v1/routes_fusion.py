import json
import tempfile
import os

from io import BytesIO

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form
from fastapi.responses import FileResponse
from PIL import Image

import pydicom
import numpy as np

from backend.utils.report_generator import generate_report
from backend.services.fusion_service import FusionService

router = APIRouter()

service = FusionService()


# =========================================
# Helper Function
# =========================================

def load_datscan_image(upload_file: UploadFile):

    filename = upload_file.filename.lower()

    # -----------------------------------
    # NORMAL IMAGE
    # -----------------------------------

    if filename.endswith((".png", ".jpg", ".jpeg")):

        image = Image.open(
            BytesIO(upload_file.file.read())
        ).convert("RGB")

        return image

    # -----------------------------------
    # DICOM
    # -----------------------------------

    elif filename.endswith(".dcm"):

        dicom = pydicom.dcmread(upload_file.file)

        pixel_array = dicom.pixel_array.astype(np.float32)

        # normalize
        pixel_array -= pixel_array.min()

        pixel_array /= pixel_array.max()

        pixel_array *= 255.0

        pixel_array = pixel_array.astype(np.uint8)

        image = Image.fromarray(pixel_array)

        image = image.convert("RGB")

        return image

    # -----------------------------------
    # UNSUPPORTED
    # -----------------------------------

    else:

        raise ValueError(
            "Unsupported DATSCAN format. Use PNG/JPG/DICOM."
        )


# =========================================
# PREDICTION ENDPOINT
# =========================================

@router.post("/predict/fusion")
async def predict_fusion(

    voice_data: str = Form(...),

    spiral_file: UploadFile = File(...),

    datscan_file: UploadFile = File(...)
):

    try:

        # -----------------------------------
        # PARSE VOICE JSON
        # -----------------------------------

        voice_features = json.loads(voice_data)

        # -----------------------------------
        # LOAD SPIRAL IMAGE
        # -----------------------------------

        spiral_image = Image.open(
            BytesIO(await spiral_file.read())
        ).convert("RGB")

        # -----------------------------------
        # LOAD DATSCAN
        # -----------------------------------

        datscan_image = load_datscan_image(
            datscan_file
        )

        # -----------------------------------
        # RUN FUSION MODEL
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


# =========================================
# PDF REPORT ENDPOINT
# =========================================

@router.post("/fusion/report")
async def generate_fusion_report(

    voice_data: str = Form(...),

    spiral_file: UploadFile = File(...),

    datscan_file: UploadFile = File(...)
):

    try:

        # -----------------------------------
        # PARSE VOICE JSON
        # -----------------------------------

        voice_features = json.loads(voice_data)

        # -----------------------------------
        # LOAD SPIRAL IMAGE
        # -----------------------------------

        spiral_image = Image.open(
            BytesIO(await spiral_file.read())
        ).convert("RGB")

        # -----------------------------------
        # LOAD DATSCAN
        # -----------------------------------

        datscan_image = load_datscan_image(
            datscan_file
        )

        # -----------------------------------
        # RUN PREDICTION
        # -----------------------------------

        result = service.predict(

            voice_features,

            spiral_image,

            datscan_image
        )

        # -----------------------------------
        # GENERATE PDF
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
        # RETURN PDF
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