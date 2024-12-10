from flask import Flask, render_template, request
import pandas as pd
import sys
import os

sys.path.append('/Users/kaylalugo/Desktop/CrimeScope NJ')
from weather import most_common_crime_by_weather

sys.path.append('/Users/kaylalugo/Desktop/CrimeScope NJ')
from demographics import get_county_with_most_crime, get_demographic_info_by_county

app = Flask(__name__)

# merged dataset
merged_data = pd.read_csv('/Users/kaylalugo/Desktop/CrimeScope NJ/datasets/merged_crime_weather_demographics.csv')

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('input.html')

@app.route('/weather-query', methods=['POST'])
def weather_query():
    # Get the user input for weather condition
    weather_condition = request.form['weather_condition']
    
    # Call the function to get the result
    result = most_common_crime_by_weather(merged_data, weather_condition)
    
    # Pass the result to a new page
    return render_template('output.html', result=result)

@app.route('/crime-query', methods=['POST'])
def crime_query():
    # Get the user input for crime type
    crime_type = request.form['crime_type']
    
    # Call the function to get the result
    from weather import most_common_weather_by_crime
    result = most_common_weather_by_crime(merged_data, crime_type)
    
    # Pass the result to a new page
    return render_template('output.html', result=result)

@app.route('/demographics-query', methods=['POST'])
def demographics_query():
    # Get the user input for crime type
    crime_type = request.form['crime_type']
    
    # Import the functions
    sys.path.append('/Users/kaylalugo/Desktop/CrimeScope NJ')
    from demographics import get_county_with_most_crime, get_demographic_info_by_county
    
    # Find the county with the most incidents
    county = get_county_with_most_crime(merged_data, crime_type)
    if county:
        # Get demographic information for the county
        demographic_info = get_demographic_info_by_county(merged_data, county)
        if demographic_info:
            # Prepare demographic information for display
            info = f"<h3>Demographic Information for {county} County:</h3><ul>"
            for key, value in demographic_info.items():
                info += f"<li>{key.title()}: {value}</li>"
            info += "</ul>"
            result = info
        else:
            result = f"<p>No demographic information available for {county} County.</p>"
    else:
        result = f"<p>No data found for the crime type: '{crime_type}'.</p>"
    
    # Pass the result to a new page
    return render_template('output.html', result=result)

@app.route('/predict-crime', methods=['POST'])
def predict_crime():
    # Get user inputs
    temperature = float(request.form['temperature'])
    weather_condition = request.form['weather_condition']

    # Prepare inputs for the model
    weather_input = {'temp': temperature, 'weather': weather_condition}
    demographic_input = {}  # Assuming demographic inputs are optional or not needed for now

    # Train
    from predictions import train_crime_prediction_model, predict_most_common_crime
    model, weather_conditions = train_crime_prediction_model(merged_data)

    # PREDICT!!
    predicted_crime = predict_most_common_crime(model, weather_input, demographic_input, weather_conditions)

    # Display
    result = f"<p>The predicted most common crime is: <strong>{predicted_crime}</strong></p>"
    return render_template('output.html', result=result)

@app.route('/predict-county-crime', methods=['POST'])
def predict_county_crime():
    # Get user inputs
    county = request.form['county']
    weather_condition = request.form['weather_condition']

    # Prepare inputs for the model
    weather_input = {'temp': 75, 'weather': weather_condition}  # Default temp for simplicity
    demographic_input = get_demographic_info_by_county(merged_data, county)

    # Ensure demographic input has all required fields
    required_columns = ['population_density', 'average_family_size', 'unemployment_rate']
    for col in required_columns:
        demographic_input[col] = demographic_input.get(col, 0)  # Set default for missing values

    # Train 
    from predictions import train_crime_prediction_model, predict_most_common_crime
    model, weather_conditions = train_crime_prediction_model(merged_data)

    # PREDICT!
    predicted_crime = predict_most_common_crime(model, weather_input, demographic_input, weather_conditions)

    # Prepare the result for display
    result = (f"<p>The predicted most common crime in <strong>{county}</strong> "
              f"under <strong>{weather_condition}</strong> weather is: "
              f"<strong>{predicted_crime}</strong></p>")
    return render_template('output.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)
