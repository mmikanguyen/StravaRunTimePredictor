import pandas as pd
from sklearn.model_selection import train_test_split
from data import load_activities
from features import feature_engineer
from random_forest import RunTimeRegressor
import seaborn as sns
import matplotlib.pyplot as plt

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
preds = model.predict(X_val)

plt.figure(figsize=(6,6))
sns.scatterplot(x=y_val, y=preds)
plt.plot([y_val.min(), y_val.max()], [y_val.min(), y_val.max()], 'r--')
plt.xlabel("Actual Time (min)")
plt.ylabel("Predicted Time (min)")
plt.title("Predicted vs Actual Running Times")
plt.show()

residuals = y_val - preds

plt.figure(figsize=(8,4))
sns.histplot(residuals, bins=20, kde=True)
plt.title("Residual Distribution (Actual - Predicted)")
plt.xlabel("Residual (min)")
plt.show()

# Residuals vs predicted
plt.figure(figsize=(8,4))
sns.scatterplot(x=preds, y=residuals)
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals vs Predicted Time")
plt.xlabel("Predicted Time")
plt.ylabel("Residual")
plt.show()

importances = model.feature_importances(FEATURE_COLUMNS)
feat_importance = pd.Series(importances).sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=feat_importance.values, y=feat_importance.index)
plt.title("Feature Importance")
plt.show()
