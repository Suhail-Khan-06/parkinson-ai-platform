import torch.nn as nn

from torchvision import models
from torchvision.models import EfficientNet_B0_Weights


def get_model():

    model = models.efficientnet_b0(
        weights=EfficientNet_B0_Weights.DEFAULT
    )

    # Freeze all layers first
    for param in model.parameters():
        param.requires_grad = False

    # Unfreeze last feature block
    for param in model.features[-1].parameters():
        param.requires_grad = True

    # Replace classifier
    model.classifier = nn.Sequential(
        nn.Dropout(0.3),
        nn.Linear(
            model.classifier[1].in_features,
            2
        )
    )

    return model