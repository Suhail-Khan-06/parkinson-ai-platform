import torch
import torch.nn as nn
from torchvision import transforms, models
from torchvision.models import EfficientNet_B0_Weights
from PIL import Image
import logging

MODEL_PATH = "models/spiral_model/efficientnet_spiral.pth"

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

logging.basicConfig(level=logging.INFO)


class SpiralService:
    def __init__(self):
        self.model = self._load_model()
        self.transform = self._get_transform()
        self.classes = ["healthy", "parkinson"]  # must match ImageFolder order

        logging.info("Spiral model loaded")

    def _load_model(self):
        model = models.efficientnet_b0(
            weights=EfficientNet_B0_Weights.DEFAULT
        )
        model.classifier[1] = nn.Linear(
            model.classifier[1].in_features, 2
        )

        model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
        model.to(DEVICE)
        model.eval()

        return model

    def _get_transform(self):
        return transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

    def predict(self, image):

        image = image.convert("RGB")
        img = self.transform(image).unsqueeze(0).to(DEVICE)

        with torch.no_grad():

            outputs = self.model(img)

            probs = torch.softmax(outputs, dim=1)

            parkinson_prob = probs[0][1].item()

            pred_class = torch.argmax(probs, dim=1).item()

        return {
            "prediction": self.classes[pred_class],

            "confidence": float(probs[0][pred_class]),

            "parkinsons_probability": float(parkinson_prob)
    }