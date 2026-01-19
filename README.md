# Strava Runs Regression Model
This project uses data from the Strava API to build a machine learning model that predicts running time based on features such as distance, heart rate, cadence, elevation, and recent training load.

The goal is to learn patterns from past runs and use them to estimate future performance over different distances.

(Project Context)

This project is based on my own running data. I began running regularly about six months ago, transitioning from a beginner to a more structured runner over time. In this period, my training evolved from short, easy runs to more varied workouts including longer runs, tempo efforts, and progressive mileage.

## How It Works
Fetch Data From Strava
Use your Strava refresh token to obtain an access token to pull your recent activities from the Strava API. This project saves running activities in runs.csv.

## Features
features.csv contains additional variables calculated for modeling: 
- distance_km
- total_time_min
- pace_per_km
- elevation_per_km
- weekly_km
- rolling_pace
- hr_percent_max
- effort_pace

## Model
Trains a Random Forest Regression Model to predict total_time_min and evaluates performance through MAE and MSE. Uses 80/20 split and uses most recent activities for testing.

## Setup
Clone repo and create a .env file in the project root with:
- STRAVA_CLIENT_ID=your_client_id
- STRAVA_CLIENT_SECRET=your_client_secret
- STRAVA_REFRESH_TOKEN=your_refresh_token
