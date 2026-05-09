from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)


# ✅ Test: API is alive
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Parkinson AI API is running"


# ✅ Test: Health check
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


# ✅ Test: Valid prediction
def test_valid_prediction():
    payload = {
        "features": [
            119.992,157.302,74.997,0.00784,0.00007,0.00370,0.00554,0.01109,
            0.04374,0.426,0.02182,0.03130,0.02971,0.06545,0.02211,21.033,
            0.414783,0.815285,-4.813031,0.266482,2.301442,0.284654
        ]
    }

    response = client.post("/api/v1/predict/voice", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "prediction" in data
    assert "parkinsons_probability" in data


# ❌ Test: Invalid input (wrong feature length)
def test_invalid_feature_length():
    payload = {
        "features": [1, 2, 3]
    }

    response = client.post("/api/v1/predict/voice", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Expected 22 features"