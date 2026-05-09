import torch
import torch.nn.functional as F

from PIL import Image

from torchvision import transforms
from torchvision import models
from torchvision.models import EfficientNet_B0_Weights

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

MODEL_PATH = "models/datscan_model/resnet_datscan.pth"


class DATScanService:

    def __init__(self):

        # -----------------------------
        # Load EfficientNet
        # -----------------------------

        self.model = models.efficientnet_b0(
            weights=EfficientNet_B0_Weights.DEFAULT
        )

        self.model.classifier = torch.nn.Sequential(
            torch.nn.Dropout(0.3),
            torch.nn.Linear(
                self.model.classifier[1].in_features,
                2
            )
        )

        self.model.load_state_dict(
            torch.load(
                MODEL_PATH,
                map_location=DEVICE
            )
        )

        self.model.to(DEVICE)

        self.model.eval()

        # -----------------------------
        # Image preprocessing
        # -----------------------------

        self.transform = transforms.Compose([

            transforms.Grayscale(
                num_output_channels=3
            ),

            transforms.Resize((224, 224)),

            transforms.ToTensor(),

            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

        self.classes = [
            "healthy",
            "parkinson"
        ]

    def predict(self, image):

        image = image.convert("L")

        image = self.transform(image)

        image = image.unsqueeze(0)

        image = image.to(DEVICE)

        with torch.no_grad():

            outputs = self.model(image)

            probs = F.softmax(outputs, dim=1)

            confidence, pred = torch.max(probs, 1)

        prediction = self.classes[pred.item()]

        parkinson_probability = probs[0][1].item()

        return {

            "prediction": prediction,

            "confidence": confidence.item(),

            "parkinsons_probability": parkinson_probability
        }