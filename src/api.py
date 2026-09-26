"""
FastAPI service for the machine failure prediction model.

Run with: uvicorn src.api:app --reload
Needs model.joblib and scaler.joblib, which come from notebooks/03_train_model.ipynb.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI(title="Predictive Maintenance API")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")
SCALER_PATH = os.path.join(os.path.dirname(__file__), "scaler.joblib")

model = None
scaler = None


def load_model():
    global model, scaler
    if model is None:
        if not os.path.exists(MODEL_PATH):
            raise HTTPException(
                status_code=503,
                detail="Model not found. Run notebooks/03_train_model.ipynb first.",
            )
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
    return model, scaler


class SensorReading(BaseModel):
    air_temperature_k: float
    process_temperature_k: float
    rotational_speed_rpm: float
    torque_nm: float
    tool_wear_min: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(reading: SensorReading):
    loaded_model, loaded_scaler = load_model()

    reading_row = pd.DataFrame([{
        "air_temperature_k": reading.air_temperature_k,
        "process_temperature_k": reading.process_temperature_k,
        "rotational_speed_rpm": reading.rotational_speed_rpm,
        "torque_nm": reading.torque_nm,
        "tool_wear_min": reading.tool_wear_min,
    }])
    scaled_values = loaded_scaler.transform(reading_row)

    prediction = loaded_model.predict(scaled_values)[0]
    failure_probability = loaded_model.predict_proba(scaled_values)[0][1]

    return {
        "failure_predicted": bool(prediction),
        "failure_probability": float(failure_probability),
    }
