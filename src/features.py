import pandas as pd
import os

os.makedirs("../data/processed", exist_ok=True)
runs = pd.read_csv("../data/raw/runs.csv")


def feature_engineer(df):
    df["distance_km"] = df["distance"]/1000
    df["total_time_min"]=df["moving_time"]/60
    df["pace_per_km"]=df["total_time_min"]/df["distance_km"]
    df["elevation_per_km"]=df["total_elevation_gain"]/df["distance_km"]
    df["avg_hr"]=df["average_heartrate"]
    df["avg_cadence"]=df["average_cadence"]

    df=df.sort_values("start_date")

    df["weekly_km"]=(
        df["distance_km"].rolling(window=7,min_periods=1).sum()
    )
    df["rolling_pace"]=(
        df["pace_per_km"].rolling(window=5,min_periods=1).mean()
    )

    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_dir = os.path.join(script_dir, "..", "data", "processed")
    os.makedirs(raw_dir, exist_ok=True)

    file_path = os.path.join(raw_dir, "features.csv")
    df.to_csv(file_path, index=False)

#print(runs)
feature_engineer(runs)
