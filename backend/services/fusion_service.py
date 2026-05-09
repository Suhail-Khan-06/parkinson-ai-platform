from backend.services.voice_service import VoiceService
from backend.services.spiral_service import SpiralService
from backend.services.datscan_service import DATScanService

from models.fusion_engine.fusion import fuse_predictions
from models.fusion_engine.explainer import generate_explanation


class FusionService:

    def __init__(self):

        self.voice_service = VoiceService()

        self.spiral_service = SpiralService()

        self.datscan_service = DATScanService()

    def predict(
        self,
        voice_features,
        spiral_image,
        datscan_image
    ):

        # -----------------------------
        # Voice
        # -----------------------------

        voice_result = self.voice_service.predict(
            voice_features
        )

        voice_prob = voice_result[
            "parkinsons_probability"
        ]

        voice_conf = voice_prob

        # -----------------------------
        # Spiral
        # -----------------------------

        spiral_result = self.spiral_service.predict(
            spiral_image
        )

        spiral_prob = spiral_result[
            "parkinsons_probability"
        ]

        spiral_conf = spiral_result[
            "confidence"
        ]

        # -----------------------------
        # DATScan
        # -----------------------------

        datscan_result = self.datscan_service.predict(
            datscan_image
        )

        datscan_prob = datscan_result[
            "parkinsons_probability"
        ]

        datscan_conf = datscan_result[
            "confidence"
        ]

        # -----------------------------
        # Fusion
        # -----------------------------

        fusion_result = fuse_predictions(

            voice_prob,
            voice_conf,

            spiral_prob,
            spiral_conf,

            datscan_prob,
            datscan_conf
        )

        # -----------------------------
        # Explanation
        # -----------------------------

        explanation = generate_explanation(

            fusion_result,

            voice_result,
            spiral_result,
            datscan_result
        )

        return {

            "fusion_result": fusion_result,

            "explanation": explanation,

            "voice_result": voice_result,

            "spiral_result": spiral_result,

            "datscan_result": datscan_result
        }