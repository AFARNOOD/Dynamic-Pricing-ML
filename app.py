from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd  # Ensure pandas is imported

app = Flask(__name__)

# Load the trained model
with open('../models/gradient_boosting_model.pkl', 'rb') as f:
    model = pickle.load(f)


# Print the feature names used by the model
print("Expected feature names:", model.feature_names_in_)

@app.route('/')
def home():
    return "Welcome to the Dynamic Pricing API. Use the /predict endpoint to get predictions."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Create a DataFrame for prediction using the exact feature names
        features = pd.DataFrame([[  # Create a DataFrame for prediction
            data['number_of_riders'],
            data['number_of_drivers'],
            data['number_of_past_rides'],
            data['average_ratings'],
            data['expected_ride_duration'],
            data['demand_supply_ratio'],
            data['location_category_Suburban'],
            data['location_category_Urban'],
            data['customer_loyalty_status_Regular'],
            data['customer_loyalty_status_Silver'],
            data['time_of_booking_Evening'],
            data['time_of_booking_Morning'],
            data['time_of_booking_Night'],
            data['vehicle_type_Premium'],
            data['duration_ratings_interaction']
        ]], columns=[
            'number_of_riders',
            'number_of_drivers',
            'number_of_past_rides',
            'average_ratings',
            'expected_ride_duration',
            'demand_supply_ratio',
            'location_category_Suburban',
            'location_category_Urban',
            'customer_loyalty_status_Regular',
            'customer_loyalty_status_Silver',
            'time_of_booking_Evening',
            'time_of_booking_Morning',
            'time_of_booking_Night',
            'vehicle_type_Premium',
            'duration_ratings_interaction'
        ])

        # Make a prediction
        prediction = model.predict(features)[0]

        return jsonify({'predicted_cost': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
