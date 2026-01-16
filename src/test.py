import pandas as pd
import os
import time
import requests
from dotenv import load_dotenv
load_dotenv

max_pages = 10          # adjust as needed
per_page = 200          # max allowed by Strava is 200
sleep_seconds = 1 

AUTH_URL = "https://www.strava.com/oauth/token"
ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"

# --- Replace this with your long-lived refresh token from Strava ---
REFRESH_TOKEN = "8ef06a1d56d38f75b908550960542caab6ef62f4"
CLIENT_ID = "196072"
CLIENT_SECRET = "a6799fbdeff4b573e3a6d32e6512eab24884cfe0"

def get_access_token(refresh_token):
    """
    Use refresh token to get a valid access token.
    Returns new access token and refresh token.
    """
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }

    response = requests.post(AUTH_URL, data=payload)
    response.raise_for_status()
    data = response.json()
    return data["access_token"], data["refresh_token"]

# Get a valid access token
access_token, REFRESH_TOKEN = get_access_token(REFRESH_TOKEN)
headers = {"Authorization": f"Bearer {access_token}"}

# --- Fetch activities ---
activities = []

for page in range(1, max_pages + 1):
    params = {"page": page, "per_page": per_page}

    response = requests.get(ACTIVITIES_URL, headers=headers, params=params)
    
    # If the access token expired mid-loop, refresh and retry
    if response.status_code == 401:
        access_token, REFRESH_TOKEN = get_access_token(REFRESH_TOKEN)
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(ACTIVITIES_URL, headers=headers, params=params)

    response.raise_for_status()
    page_data = response.json()

    if not page_data:
        break

    activities.extend(page_data)
    time.sleep(sleep_seconds)

# --- Save runs to CSV ---
df = pd.DataFrame(activities)
df_runs = df[df["type"] == "Run"]
script_dir = os.path.dirname(os.path.abspath(__file__))
raw_dir = os.path.join(script_dir, "..", "data", "raw")
os.makedirs(raw_dir, exist_ok=True)
file_path = os.path.join(raw_dir, "runs.csv")
df_runs.to_csv(file_path, index=False)