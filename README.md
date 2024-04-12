Sensor Dashboard Documentation
Overview
The Sensor Dashboard is a web application designed to display real-time data from various environmental sensors located at a specific location. It provides a user-friendly interface for monitoring sensor readings and includes features such as fetching data from a database, visualizing data using charts and graphs, and displaying wind speed and direction using a custom wind barb SVG.

Architecture
The application is built using Python for the backend logic, Flask framework for creating web endpoints, and JavaScript for client-side interactions and data visualization using the Chart.js library. HTML and CSS are used for structuring the web pages and styling the interface.

Components

Backend (Python Flask):

from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Route for fetching real-time sensor data
@app.route('/airport_data_fetch')
def airport_data_fetch():
    # Logic to fetch real-time sensor data from the database
    # Example:
    sensor_data = {
        'wind_speed': 10.5,
        'wind_direction': 180,
        'temperature': 25.3,
        'humidity': 60,
        'pressure': 1013.25,
        'rainfall': 0.2
    }
    return jsonify(sensor_data)

# Route for fetching historical sensor data (e.g., 10 minutes interval)
@app.route('/airport_data_fetch_10m')
def airport_data_fetch_10m():
    # Logic to fetch historical sensor data for specific intervals
    # Example:
    historical_data = {
        'timestamps': ['2024-04-12T08:00:00', '2024-04-12T08:10:00', ...],
        'temperature': [25.1, 25.2, ...],
        'humidity': [61, 60, ...],
        # Other sensor readings
    }
    return jsonify(historical_data)

if __name__ == '__main__':
    app.run(debug=True)
    
Frontend (HTML/CSS/JavaScript):

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sensor Dashboard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/style.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/chart.min.js"></script>
</head>
<body>
    <div class="container">
        <div class="sensor-readings">
            <!-- Sensor readings displayed here -->
        </div>
        <div class="charts">
            <!-- Charts and graphs displayed here -->
        </div>
        <div class="wind-barb">
            <!-- Custom wind barb SVG displayed here -->
        </div>
    </div>
    <script src="dashboard.js"></script>
</body>
</html>

// dashboard.js

// Fetch real-time sensor data from backend
function fetchSensorData() {
    fetch('/airport_data_fetch')
    .then(response => response.json())
    .then(data => {
        // Update UI with real-time sensor readings
        updateSensorReadings(data);
    })
    .catch(error => console.error('Error fetching sensor data:', error));
}

// Update UI with real-time sensor readings
function updateSensorReadings(data) {
    // Update sensor readings in the UI
    // Example:
    document.querySelector('.sensor-readings').innerHTML = `
        <p>Wind Speed: ${data.wind_speed} m/s</p>
        <p>Wind Direction: ${data.wind_direction}°</p>
        <p>Temperature: ${data.temperature} °C</p>
        <p>Humidity: ${data.humidity} %</p>
        <p>Pressure: ${data.pressure} hPa</p>
        <p>Rainfall: ${data.rainfall} mm</p>
    `;
}

// Fetch historical sensor data for specific intervals (e.g., 10 minutes)
function fetchHistoricalData() {
    fetch('/airport_data_fetch_10m')
    .then(response => response.json())
    .then(data => {
        // Create charts and graphs using historical data
        createCharts(data);
    })
    .catch(error => console.error('Error fetching historical data:', error));
}

// Create charts and graphs using historical sensor data
function createCharts(data) {
    // Create charts using Chart.js library
    // Example:
    const ctx = document.getElementById('temperature-chart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.timestamps,
            datasets: [{
                label: 'Temperature (°C)',
                data: data.temperature,
                borderColor: 'rgb(255, 99, 132)',
                tension: 0.1
            }]
        },
        options: {
            // Chart options
        }
    });
}
Features
Real-time Data Fetching:

The backend server fetches real-time sensor data from a database using predefined endpoints.
Data is fetched asynchronously using AJAX requests in the frontend to ensure smooth updates without page reloads.
Sensor Readings Display:

Sensor readings such as wind speed, direction, temperature, humidity, pressure, and rainfall are displayed on the dashboard in real-time.
The UI is updated dynamically as new data is fetched from the backend, providing users with up-to-date information.
Data Visualization:

Sensor data is visualized using charts and graphs created with the Chart.js library.
Charts display trends and historical data for sensor readings over specific intervals (e.g., 10 minutes).
Custom Wind Barb SVG:

Wind speed and direction are represented visually using a custom wind barb SVG embedded in the dashboard.
The wind barb dynamically updates based on real-time sensor data, providing a clear indication of current wind conditions.
// Fetch real-time sensor data and historical data on page load
window.onload = function() {
    fetchSensorData();
    fetchHistoricalData();
};

Usage
Installation:

Clone the repository to your local machine.
Install dependencies using pip install -r requirements.txt.
Running the Application:

Run the Flask application using python app.py.
Access the dashboard interface in a web browser at http://localhost:5000/airport_ui.
Interacting with the Dashboard:

Monitor real-time sensor readings displayed on the dashboard.
Explore charts and graphs to visualize historical data trends.
Observe wind speed and direction represented by the custom wind barb SVG.

Conclusion
The Sensor Dashboard provides a comprehensive solution for monitoring environmental conditions in real-time. By leveraging Flask for backend development and Chart.js for data visualization, it offers users an intuitive and interactive interface for accessing and analyzing sensor data. With its customizable features and user-friendly design, the dashboard serves as a valuable tool for various applications, including weather monitoring, aviation, and environmental research.
