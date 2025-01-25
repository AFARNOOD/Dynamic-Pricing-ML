# Define the API endpoint URL
$apiUrl = "http://127.0.0.1:5000/predict"

# Create the test data payload as a JSON object
$testData = @{
    "number_of_riders" = 50
    "number_of_drivers" = 30
    "number_of_past_rides" = 15
    "average_ratings" = 4.5
    "expected_ride_duration" = 60
    "demand_supply_ratio" = 1.0
    "location_category_Suburban" = 1
    "location_category_Urban" = 0
    "customer_loyalty_status_Regular" = 0
    "customer_loyalty_status_Silver" = 0
    "time_of_booking_Evening" = 1
    "time_of_booking_Morning" = 0
    "time_of_booking_Night" = 0
    "vehicle_type_Premium" = 0
    "duration_ratings_interaction" = 4.5
} | ConvertTo-Json -Depth 2

# Make a POST request to the API
$response = Invoke-RestMethod -Uri $apiUrl -Method Post -Body $testData -ContentType "application/json"

# Print the response
Write-Output "Response from the API:"
Write-Output $response
