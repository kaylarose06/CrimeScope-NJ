# This is just user input stuff and display stuff! Not super important!

from weather import most_common_crime_by_weather, most_common_weather_by_crime
from demographics import get_demographic_info_by_county, get_county_with_most_crime
from predictions import train_crime_prediction_model, predict_most_common_crime

def display_menu(merged_data):
    # Train the model
    model, weather_conditions = train_crime_prediction_model(merged_data)
    counties = merged_data['county'].unique()  # List of unique counties

    while True:
        print("\nWelcome to CrimeScope NJ!\n")
        print("Choose an option:")
        print("1. Query most common crime by weather condition")
        print("2. Query most common weather by crime type")
        print("3. Query demographic information by crime type")
        print("4. Predict most common crime based on weather and demographics")
        print("5. Predict most common crime based on county and weather")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            print("\nWeather Conditions:\n"
                  "- Clear sky\n"
                  "- Mainly clear\n"
                  "- Partly cloudy\n"
                  "- Overcast\n"
                  "- Fog\n"
                  "- Depositing rime fog\n"
                  "- Drizzle: light\n"
                  "- Drizzle: moderate\n"
                  "- Drizzle: dense intensity\n"
                  "- Rain: slight\n"
                  "- Rain: moderate\n"
                  "- Rain: heavy intensity\n"
                  "- Snow fall: slight\n"
                  "- Snow fall: moderate\n"
                  "- Snow fall: heavy intensity\n"
                  "- Thunderstorm: slight or moderate\n")
            weather_condition = input("Enter a weather condition: ").strip()
            result = most_common_crime_by_weather(merged_data, weather_condition)
            print(f"\n{result}\n")

        elif choice == "2":
            print("\nCrime Types:\n"
                  "- Theft\n"
                  "- Shoplifting\n"
                  "-Arson\n"
                  "- Trespassing\n"
                  "- Homicide\n"
                  "- Vandalism\n"
                  "- Sexual Assault\n"
                  "- Burglary\n"
                  "- Drug Possession\n"
                  "- Domestic Violence\n"
                  "- DUI\n"
                  "- Identity Theft\n"
                  "- Cybercrime\n"
                  "- Kidnapping\n"
                  "- Robbery\n"
                  "- Public Intoxication\n"
                  "- Weapons Violation\n"
                  "- Assault\n"
                  "- Fraud\n")
            crime_type = input("Enter a crime type: ").strip().title()
            result = most_common_weather_by_crime(merged_data, crime_type)
            print(f"\n{result}\n")

        elif choice == "3":
            print("\nCrime Types:\n"
                  "- Theft\n"
                  "- Shoplifting\n"
                  "- Arson\n"
                  "- Trespassing\n"
                  "- Homicide\n"
                  "- Vandalism\n"
                  "- Sexual Assault\n"
                  "- Burglary\n"
                  "- Drug Possession\n"
                  "- Domestic Violence\n"
                  "- DUI\n"
                  "- Identity Theft\n"
                  "- Cybercrime\n"
                  "- Kidnapping\n"
                  "- Robbery\n"
                  "- Public Intoxication\n"
                  "- Weapons Violation\n"
                  "- Assault\n"
                  "- Fraud\n")
            crime_type = input("Enter a crime type: ").strip().title()
            county = get_county_with_most_crime(merged_data, crime_type)
            if county:
                print(f"\n * The county with the most '{crime_type}' incidents is: {county}\n")
                demographic_info = get_demographic_info_by_county(merged_data, county)
                if demographic_info:
                    print(f"Demographic Information for {county} County:")
                    for key, value in demographic_info.items():
                        print(f"{key.title()}: {value}")
                else:
                    print(" * No demographic information available for this county.")
            else:
                print(f" * No data found for the crime type: '{crime_type}'\n")

        elif choice == "4":
            # Collect user inputs for prediction
            weather_input = {
                'temp': float(input("Enter the temperature: ")),
                'weather': input("Enter weather condition: ").strip()
            }
            demographic_input = {
                # Collect any additional demographic inputs here (if required)
            }

            # Predict the most common crime based on input
            predicted_crime = predict_most_common_crime(model, weather_input, demographic_input, weather_conditions)
            print(f"\n * The predicted most common crime is: {predicted_crime}\n")
        
        elif choice == "5":
            print("\nSelect a county from the list below:")
            counties = [county for county in counties if str(county).lower() != 'nan']  # Remove 'nan' from the list
            for county in counties:
                print(f"- {county}")
            
            county_input = input("Enter the county: ").strip()

            print("\nWeather Conditions:\n"
                  "- Clear sky\n"
                  "- Mainly clear\n"
                  "- Partly cloudy\n"
                  "- Overcast\n"
                  "- Fog\n"
                  "- Depositing rime fog\n"
                  "- Drizzle: light\n"
                  "- Drizzle: moderate\n"
                  "- Drizzle: dense intensity\n"
                  "- Rain: slight\n"
                  "- Rain: moderate\n"
                  "- Rain: heavy intensity\n"
                  "- Snow fall: slight\n"
                  "- Snow fall: moderate\n"
                  "- Snow fall: heavy intensity\n"
                  "- Thunderstorm: slight or moderate\n")
            weather_condition = input("Enter a weather condition: ").strip()

            # Prepare weather input
            weather_input = {
                'temp': 75,  # Set a default value or allow user to input
                'weather': weather_condition
            }

            # Get demographic data for the selected county
            demographic_input = get_demographic_info_by_county(merged_data, county_input)
            
            # Ensure the demographic input contains all required features
            required_columns = ['population_density', 'average_family_size', 'unemployment_rate']
            for col in required_columns:
                if col not in demographic_input:
                    demographic_input[col] = 0  # Set default values for missing columns

            # Predict the most common crime for the given county and weather
            predicted_crime = predict_most_common_crime(model, weather_input, demographic_input, weather_conditions)
            print(f"\n * The predicted most common crime for {county_input} with {weather_condition} weather is: {predicted_crime}\n")

        elif choice == "6":
            print("Goodbye!\n")
            break
        
        else:
            print("Invalid choice. Please try again.\n")
