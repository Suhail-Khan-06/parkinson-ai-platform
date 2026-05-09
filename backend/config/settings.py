import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    MODEL_PATH = os.getenv("MODEL_PATH")
    SCALER_PATH = os.getenv("SCALER_PATH")
    LOG_FILE = os.getenv("LOG_FILE")


settings = Settings()