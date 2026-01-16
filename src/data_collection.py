import pandas as pd
import os
import time
import requests

max_pages = 10          # adjust as needed
per_page = 200          # max allowed by Strava is 200
sleep_seconds = 1 

AUTH_URL = "https://www.strava.com/oauth/token"
ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"
code="8bb0770e52b49f74f3e0e70259b5cf50eebd2dea"


def get_access_token():
    """
    Refresh access token
    """
    load = {
        "client_id": "196072",           # your Strava app client ID
        "client_secret": "a6799fbdeff4b573e3a6d32e6512eab24884cfe0",  # your app secret
        "code": "8bb0770e52b49f74f3e0e70259b5cf50eebd2dea",
        "grant_type": "authorization_code"
    }

    response = requests.post(AUTH_URL, data=load)
    print(response.status_code, response.text)
    response.raise_for_status()
    return response.json()["access_token"]


access_token = get_access_token()
headers = {"Authorization": f"Bearer {access_token}"}

activities=[]

for page in range(1, max_pages + 1):
    params={
        "page":page,
        "per_page":per_page
    }

    response=requests.get(ACTIVITIES_URL, headers=headers, params=params)

    response.raise_for_status()
    page_data=response.json()

    if not page_data:
        break

    activities.extend(page_data)
    time.sleep(sleep_seconds)

df = pd.DataFrame(activities)
df=df[df["type"]=="Run"]

os.makedirs("../data/raw", exist_ok=True)
file_path="../data/raw/runs.csv"
df.to_csv(file_path, index=False)