import joblib
import os
from xgboost import XGBClassifier

DATA_DIR = "data/processed"
MODEL_DIR = "models/voice_model"

def load_data():
    X_train = joblib.load(f"{DATA_DIR}/X_train.pkl")
    y_train = joblib.load(f"{DATA_DIR}/y_train.pkl")
    return X_train, y_train

def train():
    model = XGBClassifier(
        n_estimators=200,
        max_depth=4,
        learning_rate=0.05,
        random_state=42,
        use_label_encoder=False,
        eval_metric="logloss"
    )

    X_train, y_train = load_data()
    model.fit(X_train, y_train)

    return model

def save_model(model):
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, f"{MODEL_DIR}/xgb_model.pkl")

if __name__ == "__main__":
    model = train()
    save_model(model)

    print("✅ Model training complete")