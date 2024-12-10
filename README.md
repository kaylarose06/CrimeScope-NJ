# CrimeScope NJ

CrimeScope NJ is an interactive web tool that allows users to examine crime statistics in New Jersey according to a number of criteria, including demographics, crime categories, and weather. The user has a number of possibilities, such as searching for the most frequent crimes by weather, figuring out which weather patterns correspond to which kinds of crimes, or getting demographic data about certain crimes. The application also enables users to forecast the most frequent crime by county and weather conditions, or by specific weather and demographic data. To help the user do these activities, the program offers an interactive, dialogue-style interface that presents real-time data insights in an easy-to-understand way.

<img width="1676" alt="Screenshot 2024-12-10 at 12 16 47 AM" src="https://github.com/user-attachments/assets/6d6c3b50-6a5a-496b-9bba-57d239732eb2">
<img width="1678" alt="Screenshot 2024-12-10 at 12 16 56 AM" src="https://github.com/user-attachments/assets/49c1e791-94b1-4216-a0b2-4c1d8d501e8f">


# Demo Video Backend: 
https://youtu.be/8xeAs8dRwfY

# Demo Video Frontend: 
https://youtu.be/GXRI_2Xs_Hc

# Setup Instructions: 

**Download these libraries:**

```
pip install scikit-learn pandas
```

```
pip install pandas
```

```
pip install flask
```


**Update your file paths in testing.py:** 

```
crime_data_file = '/yourpath/CrimeScope NJ/datasets/nj_simulated_crime_data_10000.csv'
fake_weather_file = '/yourpath/CrimeScope NJ/datasets/fake_weather_data.csv'
demographic_data_file = '/yourpath/CrimeScope NJ/datasets/nj_fake_demographic_data.csv'
output_file = '/yourpath/CrimeScope NJ/datasets/merged_crime_weather_demographics.csv'
cache_file = '/yourpath/CrimeScope NJ/datasets/weather_cache_testing.csv'

```

**Update your file paths in app.py:** 

```

sys.path.append('/yourpath/CrimeScope NJ')
from weather import most_common_crime_by_weather

sys.path.append('/yourpath/CrimeScope NJ')
from demographics import get_county_with_most_crime, get_demographic_info_by_county

app = Flask(__name__)

merged_data = pd.read_csv('/yourpath/merged_crime_weather_demographics.csv')
```

**To run:**

```
cd src       
python app.py
```


# Code Files: 

**testing.py:** Explore crime data—find patterns by weather, demographics, or counties. Use the trained model to predict crimes based on weather or stats.

**menu.py:** Displays the program's options and menus.

**demographics.py:** Analyze crime hotspots and county demographics in NJ.

get_county_with_most_crime: Finds the county with the highest crime for a given type.
get_demographic_info_by_county: Fetches county demographics like income, age, and education.

**weather.py:** Links crimes and weather patterns.

most_common_crime_by_weather: Finds the top crime for a specific weather type.
most_common_weather_by_crime: Finds the most frequent weather during a specific crime.
predictions.py: Predict NJ crimes based on weather and demographics.

predict_most_common_crime: Predicts likely crimes using a trained model.
train_crime_prediction_model: Trains and evaluates a logistic regression crime prediction model.

# Future Plans: 

In the future, we would like to implement the following: 

**Event Data**

Goal: Explore if public events correlate with increased crime activity, focusing on dates, locations, and event types 

Data Source: Eventbrite API, Facebook Graph API (info on public events and large-scale events) 

Implementation:
Pull event data for specific time frames and locations.
Store the event name, type, location, and date in a table, then join it with the crime data by date and location to identify if events coincide with increased incidents.

**Social Media Data**

Goal:  Capture real-time crime signals, using keywords from social media posts as early indicators or to verify crime incidents.

Data Source: Twitter API, Reddit API 

Implementation:
Use Twitter’s API to retrieve posts containing relevant crime-related keywords (e.g., “fight,” “shooting,” “police”) within specific geographic locations.
Filter and clean these posts, saving information on date, location, and keywords, which could be matched with the crime dataset to analyze real-time trends.

**Mapping and Geolocation Data**

Goal: Visualize crime hotspots and trends using geographic data.

Data Source: Google Maps API, OpenStreetMap  

Implementation:
Use latitude and longitude data from crime records to create a map of incidents.
Apply data visualization libraries like folium to plot crime data on an interactive map, with hotspot density, weather, and event overlays to show patterns.


