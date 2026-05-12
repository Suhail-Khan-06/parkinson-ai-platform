# 🧠 Parkinson AI Platform

> AI-powered multimodal Parkinson's disease detection using voice biomarkers, spiral handwriting analysis, and DATScan medical imaging.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-black)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

Parkinson AI Platform is a full-stack, multimodal artificial intelligence system for early Parkinson's disease detection.

The platform combines three complementary diagnostic modalities:

1. 🎤 **Voice Biomarker Analysis** – Detects vocal impairments associated with Parkinson's disease.
2. ✍️ **Spiral Handwriting Analysis** – Identifies motor control abnormalities from spiral drawings.
3. 🧠 **DATScan Medical Imaging Analysis** – Analyzes dopaminergic degeneration patterns from SPECT brain scans.

These independent predictions are fused using a custom multimodal decision engine to generate:

- Final Parkinson risk prediction
- Confidence score
- Clinical interpretation
- Downloadable PDF diagnostic report

---

## 🚀 Live Demo

### 🌐 Frontend

https://parkinson-ai-platform.vercel.app

### ⚙️ Backend API

https://parkinson-ai-backend.onrender.com

### 📚 API Documentation

https://parkinson-ai-backend.onrender.com/docs

> **Note:** Free-tier hosting may temporarily sleep after inactivity.

---

## ✨ Features

### 🎤 Voice Biomarker Analysis
- Uses XGBoost classifier
- Based on acoustic biomarkers (jitter, shimmer, NHR, HNR, etc.)
- Outputs Parkinson probability

### ✍️ Spiral Handwriting Detection
- EfficientNet-B0 CNN
- Detects tremor and motor-control irregularities
- Accepts uploaded spiral drawings

### 🧠 DATScan Imaging Analysis
- Deep learning model trained on PPMI-derived DATScan images
- Processes medical SPECT scans
- Predicts healthy vs Parkinson patterns

### 🧠 Multimodal Fusion Engine
- Combines predictions from all modalities
- Generates final diagnosis and confidence score

### 📄 AI Diagnostic Report
- Professional PDF report generation
- Includes modality-level results and clinical interpretation

### 🌐 Full-Stack Web Application
- Next.js frontend
- FastAPI backend
- Responsive dashboard

---

## 🏗️ System Architecture

```text
                   ┌────────────────────┐
                   │    User Inputs     │
                   │────────────────────│
                   │ Voice Features     │
                   │ Spiral Image       │
                   │ DATScan Image      │
                   └─────────┬──────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
 ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
 │ Voice Model    │ │ Spiral CNN     │ │ DATScan CNN    │
 │ (XGBoost)      │ │ EfficientNet   │ │ PyTorch Model  │
 └───────┬────────┘ └───────┬────────┘ └───────┬────────┘
         │                  │                  │
         └──────────────────┼──────────────────┘
                            ▼
                 ┌────────────────────┐
                 │  Fusion Engine     │
                 │ Weighted Decision  │
                 └─────────┬──────────┘
                           ▼
                 ┌────────────────────┐
                 │ Final Prediction   │
                 │ Confidence Score   │
                 │ PDF Report         │
                 └────────────────────┘
```

---

## 🛠️ Technology Stack

### Backend
- Python
- FastAPI
- PyTorch
- XGBoost
- Scikit-learn
- ReportLab

### Frontend
- Next.js 15
- React
- TypeScript
- Tailwind CSS
- ShadCN UI
- Recharts

### Deployment
- Vercel (Frontend)
- Render (Backend)

### Data Sources
- UCI Parkinson's Dataset
- Spiral Drawing Dataset
- PPMI DATScan Dataset

---

## 📂 Project Structure

```text
parkinson-ai-platform/
│
├── backend/
│   ├── api/
│   │   ├── main.py
│   │   └── v1/
│   │       ├── routes_voice.py
│   │       ├── routes_spiral.py
│   │       ├── routes_datscan.py
│   │       └── routes_fusion.py
│   │
│   ├── services/
│   │   ├── voice_service.py
│   │   ├── spiral_service.py
│   │   ├── datscan_service.py
│   │   └── fusion_service.py
│   │
│   ├── schemas/
│   ├── config/
│   └── utils/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── public/
│
├── models/
│   ├── voice_model/
│   ├── spiral_model/
│   ├── datscan_model/
│   └── fusion_engine/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── scripts/
├── tests/
├── docker/
├── requirements.txt
└── README.md
```

---

## 🧪 Model Details

### 🎤 Voice Model
| Item | Details |
|------|---------|
| Algorithm | XGBoost Classifier |
| Dataset | UCI Parkinson's Dataset |
| Input | 22 acoustic biomarkers |
| Output | Parkinson probability |

### ✍️ Spiral Model
| Item | Details |
|------|---------|
| Architecture | EfficientNet-B0 |
| Framework | PyTorch |
| Input Size | 224 × 224 RGB |
| Output | Healthy / Parkinson |

### 🧠 DATScan Model
| Item | Details |
|------|---------|
| Architecture | CNN-based classifier |
| Dataset | PPMI DATScan images |
| Input Size | 224 × 224 |
| Output | Healthy / Parkinson |

### 🧠 Fusion Model
| Item | Details |
|------|---------|
| Method | Weighted multimodal decision fusion |
| Inputs | Voice + Spiral + DATScan |
| Output | Final diagnosis and confidence |

---

## 📊 Current Dataset Summary

### Voice Dataset
- UCI Parkinson's Disease dataset
- Acoustic features from sustained phonation recordings

### Spiral Dataset
- Healthy and Parkinson spiral drawings

### DATScan Dataset
- PPMI-derived DATScan SPECT images
- Current working subset used for prototype development

---

## 📄 Example Output

```json
{
  "final_prediction": "Healthy",
  "confidence": 0.82,
  "risk_score": 18.6,
  "voice_result": {
    "parkinsons_probability": 0.19
  },
  "spiral_result": {
    "prediction": "healthy",
    "confidence": 0.69
  },
  "datscan_result": {
    "prediction": "healthy",
    "confidence": 0.50
  },
  "clinical_interpretation": "DATScan imaging strongly influenced the final prediction."
}
```

---

## 📄 Sample PDF Report

The platform automatically generates a professional diagnostic report containing:

- Timestamp
- Final prediction
- Confidence score
- Modality-wise results
- AI-generated clinical interpretation

---

## 🖥️ Screenshots

### Landing Page

_Add screenshot here_

### Dashboard

_Add screenshot here_

### Prediction Results

_Add screenshot here_

### PDF Diagnostic Report

_Add screenshot here_

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/Suhail-Khan-06/parkinson-ai-platform.git
cd parkinson-ai-platform
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

#### Windows
```bash
venv\Scripts\activate
```

#### macOS/Linux
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

### Backend (`.env`)

```env
LOG_FILE=logs/app.log
SCALER_PATH=data/processed/scaler.pkl
```

### Frontend (`frontend/.env.local`)

```env
NEXT_PUBLIC_API_URL=https://parkinson-ai-backend.onrender.com
```

---

## ▶️ Running the Backend

```bash
uvicorn backend.api.main:app --reload
```

Backend will be available at:

```text
http://127.0.0.1:8000
```

API docs:

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Running the Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at:

```text
http://localhost:3000
```

---

## 🚀 Deployment

### Frontend (Vercel)

```bash
vercel --prod
```

### Backend (Render)

Start command:

```bash
uvicorn backend.api.main:app --host 0.0.0.0 --port $PORT
```

---

## 📡 API Endpoints

### Voice Prediction
```http
POST /api/v1/predict/voice
```

### Spiral Prediction
```http
POST /api/v1/predict/spiral
```

### DATScan Prediction
```http
POST /api/v1/predict/datscan
```

### Fusion Prediction
```http
POST /api/v1/predict/fusion
```

### PDF Report Generation
```http
POST /api/v1/fusion/report
```

---

## 🧪 Testing

```bash
pytest
```

---

## 📈 Future Improvements

- Larger DATScan training dataset
- Advanced ensemble methods (FRLF)
- Explainability (Grad-CAM)
- User authentication
- Longitudinal patient tracking
- Clinical trial support
- Mobile application

---

## 🏆 Resume Highlights

- Developed a multimodal AI platform for Parkinson's disease detection.
- Combined XGBoost and deep learning models for medical diagnosis.
- Built scalable REST APIs using FastAPI.
- Developed a production-grade Next.js frontend.
- Automated clinical PDF report generation.
- Deployed full-stack application using Vercel and Render.

---

## 📚 References

1. UCI Machine Learning Repository – Parkinson's Dataset
2. Parkinson's Progression Markers Initiative (PPMI)
3. PyTorch Documentation
4. FastAPI Documentation
5. Next.js Documentation

---

## 👨‍💻 Author

**Suhail Ahmed Khan**

- GitHub: https://github.com/Suhail-Khan-06
- LinkedIn: _Add your LinkedIn URL here_

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, please consider giving it a star on GitHub.

