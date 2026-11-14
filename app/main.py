from app.schemas import HeartDiseaseInput
from fastapi import FastAPI
import joblib
from pathlib import Path
import pandas as pd
# Create FastAPI application
app = FastAPI(
    title="Heart Disease Prediction API",
    description="An ML API for educational heart disease prediction",
    version="1.0.0"
)
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "heart_model.joblib"

model = joblib.load(MODEL_PATH)
# First endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Heart Disease Prediction API"
    }
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
@app.get("/info")
def model_info():
    return {
        "model_name": "Logistic Regression",
        "features": [
            "age",
            "sex",
            "cp",
            "trestbps",
            "chol",
            "fbs",
            "restecg",
            "thalach",
            "exang",
            "oldpeak",
            "slope",
            "ca",
            "thal"
        ],
        "number_of_features": 13
    }
@app.post("/predict")
def predict_heart_disease(data: HeartDiseaseInput):

    input_data = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_data)

    result = bool(prediction[0])

    return {
        "heart_disease": result
    }