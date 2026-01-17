import pandas as pd
from sklearn.model_selection import train_test_split
from src.data import load_raw_activities
from src.features import feature_engineer
from src.model import RunTimeRegressor

RANDOM_STATE = 42

FEATURE_COLUMNS = [
    "distance_km",
    "avg_hr",
    "avg_cadence",
    "elevation_per_km",
    "weekly_km",
    "rolling_pace"
]

TARGET_COLUMN = "total_time_min"

raw_df = load_raw_activities("data/raw/runs.csv")
df=feature_engineer(raw_df)
df.to_csv("data/processed/run_features.csv", index=False)

split_idx = int(len(df)*0.8)
train_df = df.iloc[:split_idx]
val_df = df.iloc[split_idx]

X_train = train_df(FEATURE_COLUMNS)
y_train = train_df[TARGET_COLUMN]

X_val = val_df[FEATURE_COLUMNS]
y_val = val_df[TARGET_COLUMN]

model = RunTimeRegressor(alpha=1.0)
model.train(X_train, y_train)

metrics = model.evaluate(X_val,y_val)
print(metrics)
