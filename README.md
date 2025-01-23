# Dynamic Pricing Optimization: Predicting Ride Fares with Machine Learning

<img src="https://github.com/AFARNOOD/Dynamic-Pricing-ML/blob/main/imgs/Dynamic%20Pricing%20ML.webp " width="700" height="400">

---

## Contents

- [1. Overview](#overview)
- [2. Project Goals](#project-goals)
- [3. Project Features](#project-features)
- [4. Tools and Frameworks](#tools-and-frameworks)
- [5. Directory Structure](#directory-structure)
- [6. Reproducibility](#reproducibility)
- [7. How to Use the API](#api-usage)
- [8. Data Sources](#data-sources)

---

## 1. Overview <a name="overview"></a>

Dynamic pricing is a strategy employed by businesses to adjust prices in response to real-time market conditions such as demand, supply, and customer behavior. In the context of ride-sharing companies, dynamic pricing ensures optimal fare calculation, balancing customer satisfaction, driver availability, and company profitability.

This project aims to leverage machine learning techniques to build a dynamic pricing model using historical ride data. The model predicts ride fares by considering multiple factors, such as the number of riders, drivers, location, customer loyalty status, and ride duration. This data-driven approach enables the ride-sharing company to optimize pricing strategies, improve operational efficiency, and meet real-time market needs.

### Purpose:
The primary purpose of this project is to develop a predictive model that helps a ride-sharing company implement dynamic pricing. Currently, the company calculates fares solely based on ride duration, limiting its ability to adapt to fluctuating demand and supply conditions. By incorporating additional features into a machine learning model, the company can:

- **Optimize Pricing**: Dynamically adjust fares to reflect market conditions.
- **Enhance Customer Satisfaction**: Prevent overpricing during low-demand periods and ensure availability during peak times.
- **Improve Driver Retention**: Set competitive fares to attract drivers during high-demand periods.
- **Increase Profitability**: Use data-driven insights to maximize revenue.

### Goals of the Analysis:

1. Understand Historical Ride Data
Perform an exploratory data analysis (EDA) to:
Identify key trends and patterns in ride demand and pricing.
Investigate correlations between features (e.g., Number_of_Riders, Location_Category) and the target variable (Historical_Cost_of_Ride).
Understand how different factors like time of booking, vehicle type, and location influence ride costs.
2. Develop a Predictive Model
Build and evaluate machine learning models to:
Accurately predict ride fares based on the provided features.
Compare performance across various algorithms (e.g., Linear Regression, Random Forest, XGBoost).
Tune hyperparameters for optimal performance.

3. Feature Engineering
Create additional features to enhance model accuracy:
Demand-Supply Ratio: Ratio of riders to drivers.
Interaction terms like Expected_Ride_Duration × Average_Ratings.

4. Model Deployment
Develop a real-time prediction system by:
Creating an API using Flask or FastAPI for predicting ride fares.
Containerizing the application with Docker for scalability.
Deploying the application to a cloud platform (e.g., Heroku, AWS, Render).
---

## 2. Project Goals <a name="project-goals"></a>

The goals of this project are:
1. To analyze how weather conditions affect the duration of bike-sharing trips.
2. To build and deploy a machine learning model that predicts trip durations.
3. To provide actionable insights for bike-sharing companies to optimize bike availability.

---

## 3. Project Features <a name="project-features"></a>

- **Weather and Trip Data Integration**: Combining weather observations with BIXI trip data for comprehensive analysis.
- **Machine Learning Model**: A Random Forest model trained to predict trip durations.
- **API Deployment**: A Flask API for serving predictions based on user-input weather and temporal features.

---

## 4. Tools and Frameworks <a name="tools-and-frameworks"></a>

### Tools:
- **Python**: Data preprocessing, model training, and API development.
- **Jupyter Notebooks**: For exploratory data analysis (EDA) and feature engineering.

### Libraries:
- **Scikit-learn**: Model development and evaluation.
- **Flask**: Deployment of the prediction API.
- **Pandas/NumPy**: Data manipulation.
- **Matplotlib/Seaborn**: Visualization.

### Other Tools:
- **Git LFS**: For tracking large files in the repository.
- **Docker** (Optional): For containerizing the API.

---

## 5. Directory Structure <a name="directory-structure"></a>

```plaintext
BikeML-API/
│
├── data/
│   ├── bixi_data_2021.csv                      # BIXI bike-sharing trip data (Git LFS tracked)
│   ├── weather_data_2021.csv                   # Weather data for Montreal (Git LFS tracked)
│   ├── refined_combined_data_with_features.xls # Final processed dataset (Git LFS tracked)
│   └── ...
│
├── imgs/                                       # (Optional) Visualization images
│   └── ...
│
├── models/
│   ├── bike_duration_predictor.pkl             # Trained model for predictions
│   ├── tuned_random_forest.pkl                 # Tuned Random Forest model
│   └── ...
│
├── notebooks/
│   ├── BikeML01.ipynb                          # Data preprocessing and feature engineering
│   ├── BikeML02.ipynb                          # Model training and evaluation
│   └── ...
│
├── app.py                                      # Flask API script
├── predict_request.ps1                         # Script for making POST requests to the API
├── requirements.txt                            # Python dependencies
├── Dockerfile                                  # Dockerfile for containerization (optional)
└── README.md                                   # Project description and instructions

plaintext

```

---

## 6. Reproducibility <a name="reproducibility"></a>

### Steps to Reproduce:
1. Clone this repository:
   ```bash
   git clone https://github.com/AFARNOOD/BikeML-API.git
   cd BikeML-API

2. Set up Python dependencies:
   ```bash
   pip install -r requirements.txt

3. Download the required datasets or ensure they are placed in the `data/` directory.
4. Run the Jupyter Notebooks in the `notebooks/` directory to preprocess the data or retrain the model.


## 7. How to Use the API <a name="api-usage"></a>

To use the API for predictions, follow these steps:

1. **Run the Flask App**:
   Ensure the Flask API is running locally. Start the API by executing the following command in your terminal:

   ```bash
   python app.py
      ```

   The server will run on `http://127.0.0.1:5000`.

2. **Send a POST Request**:
   Use the provided `predict_request.ps1` script or your preferred tool (e.g., Postman, cURL) to send a request with input data for prediction. The input JSON must include the following features:

   ```json
   {
       "max_temp_c": 20,
       "min_temp_c": 7,
       "temp_range_c": 18,
       "total_precip_mm": 2,
       "snow_on_grnd_cm": 0,
       "spd_of_max_gust_kmh": 10,
       "is_rainy": 1,
       "is_snowy": 0,
       "is_windy": 0,
       "start_hour": 9,
       "start_weekday": 1,
       "is_weekend": 0
   }
   ```
   
3. **Example PowerShell Command**:
   Run the following command in PowerShell to send the prediction request:

   ```powershell
   Invoke-RestMethod -Uri http://127.0.0.1:5000/predict `
       -Method POST `
       -ContentType "application/json" `
       -Body '{"max_temp_c": 20, "min_temp_c": 7, "temp_range_c": 18, "total_precip_mm": 2, "snow_on_grnd_cm": 0, "spd_of_max_gust_kmh": 10, "is_rainy": 1, "is_snowy": 0, "is_windy": 0, "start_hour": 9, "start_weekday": 1, "is_weekend": 0}'
   ```

4. **Example cURL Command**:
   If you prefer using cURL, run this command in your terminal:

   ```powershell
   curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"max_temp_c": 20, "min_temp_c": 7, "temp_range_c": 18, "total_precip_mm": 2, "snow_on_grnd_cm": 0, "spd_of_max_gust_kmh": 10, "is_rainy": 1, "is_snowy": 0, "is_windy": 0, "start_hour": 9, "start_weekday": 1, "is_weekend": 0}'

   ```

5. **Expected Output**:
   The API will respond with the predicted trip duration in seconds. Example response:

   ```powershell
   {
    "predicted_duration_sec": 789
   }
   ```


> **Note**: For other tools or environments, ensure the JSON request body matches the required format and is sent as a POST request to the `/predict` endpoint.

---

## 8. Data Sources <a name="data-sources"></a>

This project uses two primary datasets:

1. **Weather Data**:
   - Source: Environment and Climate Change Canada (ECCC).
   - Description: Includes daily and hourly weather data for Montreal in 2021.
   - Features: Temperature, precipitation, wind speed, and other climatic conditions.

   [Download Weather Data](https://climate.weather.gc.ca/)

2. **BIXI Data**:
   - Source: BIXI Montreal Open Data Portal.
   - Description: Contains detailed trip records of BIXI bike-sharing users for 2021.
   - Features: Trip start and end times, station locations, and duration.

   [Download BIXI Data](https://bixi.com/en/open-data)

