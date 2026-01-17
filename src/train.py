import pandas as pd
from sklearn.model_selection import train_test_split
from data import load_activities
from features import feature_engineer
from random_forest import RunTimeRegressor

RANDOM_STATE = 42

FEATURE_COLUMNS = [
    "distance_km",
    "avg_hr",
    "avg_cadence",
    "elevation_per_km",
    "weekly_km",
    "rolling_pace",
    "hr_percent_max",
    "effort_pace"
]

TARGET_COLUMN = "total_time_min"

# Load & process data
raw_df = load_activities()
run_features = feature_engineer("data/raw/runs_test.csv")
df = pd.read_csv("data/processed/features.csv")
df = df.dropna(subset=FEATURE_COLUMNS + [TARGET_COLUMN])


# Split data
X = df[FEATURE_COLUMNS]
y = df[TARGET_COLUMN]

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE
)

# Train model
model = RunTimeRegressor()
model.train(X_train, y_train)

# Evaluate
metrics = model.evaluate(X_val, y_val)
print(metrics)
