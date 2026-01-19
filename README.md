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
- distance_km: total distance in kilometers
- total_time_min: total moving time in minutes
- pace_per_km: average pace in min/km
- avg_hr: average heart rate during the run
- avg_cadence: average running cadence
- elevation_per_km: elevation gain per kilometer
- weekly_km: total distance run in past 7 days
- rolling_pace: average pace over recent runs
- hr_percent_max: average heart rate as a % of est. max heart rate
- effort_pace: pace adjusted to heart rate

## Model
Trains a Random Forest Regression Model to predict total_time_min and evaluates performance through MAE and MSE. Uses 80/20 split and uses most recent activities for testing.

## Setup
Clone repo and create a .env file in the project root with:
- STRAVA_CLIENT_ID=your_client_id
- STRAVA_CLIENT_SECRET=your_client_secret
- STRAVA_REFRESH_TOKEN=your_refresh_token
