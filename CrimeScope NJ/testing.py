# Welcome to CrimeScope NJ! This script lets you dig into crime data like a detective on a coffee binge. 
# You can figure out which crimes are most common during certain weather, or which weather shows up with different crime types. 
# Plus, you can check out the demographics of a county based on crime data. 
# And for the big finale, you can make your own crime predictions based on weather or county stats using our shiny trained model. 
# So, pick an option, dive in, and let's solve some crime (or at least talk about it)!


import pandas as pd
import os
from menu import display_menu

# File paths
crime_data_file = '/Users/kaylalugo/Desktop/CrimeScope NJ/datasets/nj_simulated_crime_data_10000.csv'
fake_weather_file = '/Users/kaylalugo/Desktop/CrimeScope NJ/datasets/fake_weather_data.csv'
demographic_data_file = '/Users/kaylalugo/Desktop/CrimeScope NJ/datasets/nj_fake_demographic_data.csv'
output_file = '/Users/kaylalugo/Desktop/CrimeScope NJ/datasets/merged_crime_weather_demographics.csv'
cache_file = '/Users/kaylalugo/Desktop/CrimeScope NJ/datasets/weather_cache_testing.csv'

# Load datasets
crime_data = pd.read_csv(crime_data_file)
fake_weather_data = pd.read_csv(fake_weather_file)
demographics_data = pd.read_csv(demographic_data_file)

# Load cached weather data if available
if os.path.exists(cache_file):
    weather_cache = pd.read_csv(cache_file)
else:
    weather_cache = pd.DataFrame(columns=["lat", "lon", "temp", "weather"])

# Combine weather cache with fake weather data
weather_cache = pd.concat([weather_cache, fake_weather_data]).drop_duplicates(subset=["lat", "lon"]).reset_index(drop=True)

# Save updated weather cache
weather_cache.to_csv(cache_file, index=False)

# Merge all datasets
merged_data = crime_data.merge(weather_cache, on=["lat", "lon"], how="left")
merged_data = merged_data.merge(demographics_data, on=["lat", "lon"], how="left")

# Normalize the weather column for consistency
merged_data["weather_normalized"] = merged_data["weather"].str.strip().str.lower()

# Save the merged data to a CSV file
merged_data.to_csv(output_file, index=False)
print(f"Testing CSV File Updated! Data saved to file: {output_file}")

# Start the menu
display_menu(merged_data)
