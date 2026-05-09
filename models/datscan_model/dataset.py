import os

from torchvision import datasets, transforms
from torch.utils.data import DataLoader


def get_dataloaders(
    data_dir="data/raw/datscan_png",
    batch_size=8
):

    # -----------------------------
    # TRAIN TRANSFORMS
    # -----------------------------

    train_transform = transforms.Compose([

        transforms.Grayscale(num_output_channels=3),

        transforms.Resize((224, 224)),

        transforms.RandomHorizontalFlip(p=0.5),

        transforms.RandomRotation(10),

        transforms.RandomAffine(
            degrees=0,
            translate=(0.05, 0.05),
            scale=(0.95, 1.05)
        ),

        transforms.ToTensor(),

        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    # -----------------------------
    # TEST TRANSFORMS
    # -----------------------------

    test_transform = transforms.Compose([

        transforms.Grayscale(num_output_channels=3),

        transforms.Resize((224, 224)),

        transforms.ToTensor(),

        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    # -----------------------------
    # DATASETS
    # -----------------------------

    train_dataset = datasets.ImageFolder(
        os.path.join(data_dir, "train"),
        transform=train_transform
    )

    test_dataset = datasets.ImageFolder(
        os.path.join(data_dir, "test"),
        transform=test_transform
    )

    # -----------------------------
    # DATALOADERS
    # -----------------------------

    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=batch_size,
        shuffle=False
    )

    return train_loader, test_loader