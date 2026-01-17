import pandas as pd
from src.model import RunTimeRegressor

FEATURE_COLUMNS = [
    "distance_km",
    "avg_hr",
    "avg_cadence",
    "elevation_per_km",
    "weekly_km",
    "rolling_pace"
]

def predict_time(model, input_features: dict):
    df = pd.DataFrame([input_features])
    return model.predict(df)[0]

predict_time(RunTimeRegressor,FEATURE_COLUMNS)