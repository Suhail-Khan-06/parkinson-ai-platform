import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os
import joblib

DATA_PATH = "data/raw/parkinsons.csv"
OUTPUT_DIR = "data/processed"


def load_data():
    df = pd.read_csv(DATA_PATH)
    return df


def preprocess(df):
    # Drop non-feature column
    df = df.drop(columns=["name"])

    # Features and target
    X = df.drop("status", axis=1)
    y = df["status"]

    # Save feature names (IMPORTANT)
    feature_names = X.columns.tolist()

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test, scaler, feature_names


def save_data(X_train, X_test, y_train, y_test, scaler, feature_names):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    joblib.dump(X_train, f"{OUTPUT_DIR}/X_train.pkl")
    joblib.dump(X_test, f"{OUTPUT_DIR}/X_test.pkl")
    joblib.dump(y_train, f"{OUTPUT_DIR}/y_train.pkl")
    joblib.dump(y_test, f"{OUTPUT_DIR}/y_test.pkl")
    joblib.dump(scaler, f"{OUTPUT_DIR}/scaler.pkl")
    joblib.dump(feature_names, f"{OUTPUT_DIR}/feature_names.pkl")


if __name__ == "__main__":
    df = load_data()

    X_train, X_test, y_train, y_test, scaler, feature_names = preprocess(df)

    save_data(X_train, X_test, y_train, y_test, scaler, feature_names)

    print("✅ Data preprocessing complete")