import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

DATA_DIR = "data/processed"
MODEL_PATH = "models/voice_model/xgb_model.pkl"

def load():
    X_test = joblib.load(f"{DATA_DIR}/X_test.pkl")
    y_test = joblib.load(f"{DATA_DIR}/y_test.pkl")
    model = joblib.load(MODEL_PATH)
    return X_test, y_test, model

def evaluate():
    X_test, y_test, model = load()

    y_pred = model.predict(X_test)

    print("\n📊 Accuracy:", accuracy_score(y_test, y_pred))
    print("\n📄 Classification Report:\n", classification_report(y_test, y_pred))
    print("\n🔢 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    evaluate()