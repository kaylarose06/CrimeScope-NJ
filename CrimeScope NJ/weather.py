# Alright, this script is all about figuring out what crime happens most often in certain weather conditions or vice versa. 
# The first function, 'most_common_crime_by_weather', takes the weather condition you give it, normalizes it (just in case you type it in weirdly), 
# and then looks through the data to find the most common crime that happens in that weather. If it finds some data, it’ll tell you what crime is most common, 
# otherwise, it’ll let you know that no data was found for that weather condition.

# The second function, 'most_common_weather_by_crime', works in the opposite direction. It takes the crime type, checks if it’s valid, 
# and then finds the most common weather that happens when that crime occurs. Again, if there’s data for it, it tells you, 
# and if not, it’ll tell you no data was found for that crime.


import pandas as pd

# Analysis functions
def most_common_crime_by_weather(merged_data, weather_condition):
    # Normalize user input
    weather_condition = weather_condition.strip().lower()
    
    # Filter data by normalized weather condition
    filtered_data = merged_data[merged_data["weather_normalized"] == weather_condition]
    if not filtered_data.empty:
        common_crime = filtered_data["crime_type"].mode()[0]
        return f" * The most common crime during '{weather_condition.title()}' is: {common_crime}"
    else:
        return f" * No data found for weather condition: '{weather_condition.title()}'"

def most_common_weather_by_crime(merged_data, crime_type):
    # Normalize user input
    crime_type = crime_type.strip().title()
    valid_crimes = merged_data["crime_type"].unique()
    if crime_type not in valid_crimes:
        return f"'{crime_type}' not found. Valid options are: {', '.join(valid_crimes)}"
    
    filtered_data = merged_data[merged_data["crime_type"] == crime_type]
    if not filtered_data.empty:
        common_weather = filtered_data["weather"].mode()[0]
        return f" * The most common weather during '{crime_type}' incidents is: {common_weather}"
    else:
        return f" * No data found for crime type: '{crime_type}'"
