import torch.nn as nn
from torchvision import models
from torchvision.models import EfficientNet_B0_Weights


def get_model():
    model = models.efficientnet_b0(
        weights=EfficientNet_B0_Weights.DEFAULT
    )

    # Freeze all
    for param in model.features.parameters():
        param.requires_grad = False

    # 🔥 Unfreeze last TWO blocks
    for param in model.features[-2:].parameters():
        param.requires_grad = True

    model.classifier[1] = nn.Linear(
        model.classifier[1].in_features, 2
    )

    return model