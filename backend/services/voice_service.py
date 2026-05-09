import joblib
import pandas as pd
import logging
from backend.config.settings import settings

MODEL_PATH = "models/voice_model/xgb_model.pkl"
SCALER_PATH = "data/processed/scaler.pkl"
FEATURE_NAMES_PATH = "data/processed/feature_names.pkl"

# Logging setup
logging.basicConfig(
    filename=settings.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class VoiceService:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)
        self.feature_names = joblib.load(FEATURE_NAMES_PATH)

        logging.info("Voice model loaded successfully")

    # Single prediction
    def predict(self, feature_dict):
        missing = [f for f in self.feature_names if f not in feature_dict]
        if missing:
            raise ValueError(f"Missing features: {missing}")

        ordered = [feature_dict[f] for f in self.feature_names]
        df = pd.DataFrame([ordered], columns=self.feature_names)

        scaled = self.scaler.transform(df)

        pred = self.model.predict(scaled)[0]
        prob = self.model.predict_proba(scaled)[0][1]

        return {
            "prediction": int(pred),
            "parkinsons_probability": float(prob)
        }

    # Batch prediction
    def predict_batch(self, df: pd.DataFrame):
        missing = [f for f in self.feature_names if f not in df.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")

        df = df[self.feature_names]
        scaled = self.scaler.transform(df)

        preds = self.model.predict(scaled)
        probs = self.model.predict_proba(scaled)[:, 1]

        results = [
            {
                "prediction": int(p),
                "parkinsons_probability": float(pr)
            }
            for p, pr in zip(preds, probs)
        ]

        return results