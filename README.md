# Parkinson AI Platform

AI-powered multimodal system for Parkinson’s disease detection.

## 🚀 Features

- 🎤 Voice Analysis (XGBoost)
- ✏️ Spiral Drawing Classification (EfficientNet CNN)
- 🧠 DATScan Brain Imaging (ResNet50 CNN)
- 🔗 Multimodal Fusion Engine
- 📊 Risk Scoring + Assistance System

---

## 🧱 Tech Stack

- Python, PyTorch
- FastAPI (Backend)
- React (Frontend)
- PostgreSQL (Database)
- Docker (Deployment)

---

## 📁 Project Structure

parkinson-ai-platform/
│
├── data/
│ ├── raw/ # Original datasets (ignored in git)
│ ├── processed/ # Cleaned datasets
│
├── models/
│ ├── voice_model/
│ ├── spiral_model/
│ ├── datscan_model/
│ ├── fusion_engine/
│
├── backend/
│ ├── api/
│ ├── services/
│
├── frontend/
├── notebooks/
├── scripts/
├── tests/
├── docker/
│
├── requirements.txt
├── README.md
├── .gitignore

---

## ⚙️ Setup

```bash
git clone https://github.com/YOUR_USERNAME/parkinson-ai-platform.git
cd parkinson-ai-platform

# Create virtual environment
python -m venv venv
Activate virtual environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate
Install dependencies
pip install -r requirements.txt
📥 Dataset

Download the UCI Parkinson’s dataset and place it here:

data/raw/parkinsons.csv
🧠 Development Phases
Voice Model (XGBoost)
Spiral CNN
DATScan CNN
Fusion Engine
Backend API
Frontend
Deployment
⚠️ Notes
Raw datasets are not included due to size/privacy
Models will be saved as .pkl / .pt files
📌 Status

🚧 Currently building: Voice Detection Model


---
```
