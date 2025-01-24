# Dynamic Pricing Optimization: Predicting Ride Fares with Machine Learning

<img src="https://github.com/AFARNOOD/Dynamic-Pricing-ML/blob/main/imgs/Dynamic%20Pricing%20ML.webp" width="700" height="400">

---
## Table of Contents
- [Introduction](#introduction)
- [Problem Description](#problem-description)
- [Why This Project?](#why-this-project)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis)
- [Dataset](#dataset)
- [Tools and Frameworks](#tools-and-frameworks)](#dataset)
- [Directory Structure](#directory-structure)
- [Model Training and Selection](#model-training-and-selection)
- [Model Deployment](#model-deployment)
- [Reproducibility](#reproducibility)
- [Dependency and Environment Management](#dependency-and-environment-management)
- [Containerization](#containerization)
- [Cloud Deployment](#cloud-deployment)
- [How to Run](#how-to-run)
- [Acknowledgments](#acknowledgments)

---

## Introduction
Dynamic pricing has become an essential part of many industries, especially for ride-hailing platforms such as Uber, Lyft, and similar services. These platforms rely on pricing algorithms to adjust ride costs based on a combination of factors such as supply-demand imbalances, location, trip duration, customer loyalty, and more. This project aims to develop a machine learning model to predict ride costs dynamically, providing fair and accurate pricing that benefits both customers and service providers.

The solution involves building a robust machine learning pipeline that includes data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and deployment as a REST API. This API enables real-time predictions of ride costs for practical use cases.

---

## Problem Description
The primary challenge in ride-hailing services is to dynamically and accurately determine the cost of a ride based on various factors while ensuring:
1. **Customer Satisfaction**: Pricing should reflect fairness and transparency to retain user trust.
2. **Profitability for Providers**: The model should balance supply and demand effectively to maximize revenue while maintaining affordability for customers.
3. **Scalability**: The solution must handle large-scale data inputs for real-time predictions.

In this project, we predict the **cost of rides** using features like:
- Number of available drivers and riders.
- Ratings and past ride history.
- Supply-demand metrics and location categories.
- Trip-specific factors such as ride duration and vehicle type.

This predictive model is built with the intention of:
1. Supporting **pricing teams** in optimizing ride costs.
2. **Enhancing transparency** by providing an explainable model.
3. Offering real-time predictions for **dynamic pricing strategies**.

---

## Why This Project?
Dynamic pricing is a critical operational component in the ride-hailing industry, and it serves multiple purposes:
- **Demand-Supply Management**: Ensuring sufficient driver availability by incentivizing driver participation during high-demand periods.
- **Customer Retention**: Offering affordable pricing options to customers in less competitive locations or periods.
- **Profit Optimization**: Calculating optimal ride costs to maximize profitability while maintaining high utilization rates.

This prediction model can be implemented in:
- **Operational Dashboards**: Enabling service providers to view real-time predictions and adjust strategies.
- **Customer Applications**: Offering upfront cost estimates that align with dynamic pricing algorithms.

By leveraging machine learning, we aim to create a scalable, efficient, and accurate model for dynamic pricing.

---

## Exploratory Data Analysis (EDA)
A critical step in the project was to explore the dataset to uncover insights, handle missing values, and prepare the data for modeling. Key analyses include:

1. **Understanding Feature Distributions**:
   - Distribution of numerical features such as `number_of_riders`, `average_ratings`, and `expected_ride_duration`.
   - Relationships between features and the target variable (`ride_cost`).
   - Histograms, box plots, and density plots.

2. **Target Variable Analysis**:
   - Investigated the distribution of ride costs, looking for outliers or skewness.

3. **Feature Correlations**:
   - Used heatmaps to identify correlated features to reduce multicollinearity.
   - Determined important features using feature importance scores from tree-based models.

4. **Handling Missing Values**:
   - Checked for missing data in each feature.
   - Imputed missing values based on statistical methods or domain knowledge.

5. **Outlier Detection**:
   - Identified and handled outliers in numerical features to avoid biased predictions.

---


## Dataset <a name="dataset"></a>

The dataset contains the following features:

| Feature Name               | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `Number_of_Riders`         | Total number of ride requests.                                              |
| `Number_of_Drivers`        | Total number of available drivers.                                          |
| `Location_Category`        | Type of location (e.g., Urban, Suburban, Rural).                            |
| `Customer_Loyalty_Status`  | Customer loyalty level (e.g., Silver, Regular).                             |
| `Number_of_Past_Rides`     | Total number of rides completed by the customer.                            |
| `Average_Ratings`          | Customer’s average ride ratings.                                           |
| `Time_of_Booking`          | Time of day when the ride was booked (e.g., Night, Evening, Afternoon).      |
| `Vehicle_Type`             | Type of vehicle used (e.g., Premium, Economy).                              |
| `Expected_Ride_Duration`   | Predicted duration of the ride in minutes.                                  |
| `Historical_Cost_of_Ride`  | Actual cost of the ride (target variable for prediction).                    |


---

## Tools and Frameworks <a name="tools-and-frameworks"></a>

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

## Directory Structure <a name="directory-structure"></a>

```plaintext
BikeML-API/
│
├── data/
│   ├── gradient_boosting_model.csv             # BIXI bike-sharing trip data (Git LFS tracked)
│   ├── weather_data_2021.csv                   # Weather data for Montreal (Git LFS tracked)
│   ├── refined_combined_data_with_features.xls # Final processed dataset (Git LFS tracked)
│   └── ...
│
├── imgs/                                       # (Optional) Visualization images
│   └── ...
│
├── models/
│   ├── gradient_boosting_model.pkl             # Trained model for predictions
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

## Model Training and Selection
### **Training Process**
We trained multiple models to ensure robust performance and selected the best-performing one:
1. **Trained Models**:
   - Linear Regression: Provided a baseline model for comparison.
   - Decision Trees: Used for capturing non-linear relationships.
   - Random Forests: Improved performance through ensemble learning.
   - Gradient Boosting Regressor: Achieved the best overall performance with hyperparameter tuning.

2. **Hyperparameter Tuning**:
   - Utilized GridSearchCV and RandomizedSearchCV to optimize parameters such as learning rate, tree depth, and the number of estimators.

3. **Evaluation Metrics**:
   - Mean Absolute Error (MAE).
   - Root Mean Squared Error (RMSE).
   - R² Score.

### **Final Model**
The **Gradient Boosting Regressor** was chosen for its superior performance in capturing complex relationships between features and the target variable.

---

## Model Deployment
The trained model was deployed as a REST API using Flask:
1. **Endpoints**:
   - `/`: Returns a welcome message.
   - `/predict`: Accepts JSON input and returns a predicted cost.

2. **Input Example**:
```json
{
  "number_of_riders": 50,
  "number_of_drivers": 30,
  "number_of_past_rides": 15,
  "average_ratings": 4.5,
  "expected_ride_duration": 60,
  "location_category_Urban": 1,
  "location_category_Suburban": 0,
  "customer_loyalty_status_Regular": 0,
  "demand_supply_ratio": 1.0
}
```

3. **Output Example**:
```json
{
  "predicted_cost": 652.77
}
```

---

## Reproducibility
To ensure the project can be reproduced:
1. **Data**:
   - Dataset is provided in the repository or includes instructions for downloading.
2. **Scripts**:
   - Separate Python scripts are available for training and testing the model.
3. **Instructions**:
   - A step-by-step guide is included to run the project.

---

## Dependency and Environment Management
1. **Dependencies**:
   - Listed in `requirements.txt` for easy installation.
   - Key dependencies: Flask, scikit-learn, pandas, numpy.
2. **Virtual Environment**:
   - Instructions to set up the environment:
     ```bash
     python -m venv env
     source env/bin/activate  # Linux/Mac
     env\Scripts\activate  # Windows
     pip install -r requirements.txt
     ```

---
---

## How to Run
### Local Setup
1. Clone the repository:
   ```bash
   git clone <repo-url>
   ```
2. Navigate to the project directory and set up dependencies.
3. Start the Flask API:
   ```bash
   python app.py
   ```

### Docker Setup
1. Build the image:
   ```bash
   docker build -t dynamic-pricing-api .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 dynamic-pricing-api
   ```

### Testing the API
Use tools like Postman or a Python script to send POST requests to the `/predict` endpoint.

---

## Acknowledgments
This project was developed as part of the ML Zoomcamp course. Special thanks to the course team for providing a structured learning environment and clear evaluation criteria.

---
