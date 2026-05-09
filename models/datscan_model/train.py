import torch
import torch.nn as nn
import torch.optim as optim

from dataset import get_dataloaders
from model import get_model

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

MODEL_PATH = "models/datscan_model/resnet_datscan.pth"


def evaluate(model, loader):

    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():

        for images, labels in loader:

            images = images.to(DEVICE)
            labels = labels.to(DEVICE)

            outputs = model(images)

            _, preds = torch.max(outputs, 1)

            total += labels.size(0)

            correct += (preds == labels).sum().item()

    return correct / total


def train(model, train_loader, test_loader, epochs=30):

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(
        filter(lambda p: p.requires_grad, model.parameters()),
        lr=0.0001
    )

    best_acc = 0.0

    patience = 5
    counter = 0

    for epoch in range(epochs):

        model.train()

        running_loss = 0.0

        for images, labels in train_loader:

            images = images.to(DEVICE)
            labels = labels.to(DEVICE)

            optimizer.zero_grad()

            outputs = model(images)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

            running_loss += loss.item()

        val_acc = evaluate(model, test_loader)

        print(
            f"Epoch {epoch+1}, "
            f"Loss: {running_loss:.4f}, "
            f"Val Acc: {val_acc:.4f}"
        )

        # Save best model
        if val_acc > best_acc:

            best_acc = val_acc
            counter = 0

            torch.save(
                model.state_dict(),
                MODEL_PATH
            )

        else:
            counter += 1

        # Early stopping
        if counter >= patience:

            print("\n🛑 Early stopping triggered")
            break

    print(f"\n✅ Best Accuracy: {best_acc:.4f}")


def main():

    train_loader, test_loader = get_dataloaders()

    model = get_model().to(DEVICE)

    train(
        model,
        train_loader,
        test_loader
    )


if __name__ == "__main__":
    main()