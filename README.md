# CrimeScope NJ

Developed by: Kayla Lugo and Anushka Singh 

CrimeScope NJ is an interactive web tool that allows users to examine crime statistics in New Jersey according to a number of criteria, including demographics, crime categories, and weather. The user has a number of possibilities, such as searching for the most frequent crimes by weather, figuring out which weather patterns correspond to which kinds of crimes, or getting demographic data about certain crimes. The application also enables users to forecast the most frequent crime by county and weather conditions, or by specific weather and demographic data. To help the user do these activities, the program offers an interactive, dialogue-style interface that presents real-time data insights in an easy-to-understand way.

# Code Files: 

**testing.py** - This script lets you dig into crime data like a detective on a coffee binge. You can figure out which crimes are most common during certain weather, or which weather shows up with different crime types. Plus, you can check out the demographics of a county based on crime data. And for the big finale, you can make your own crime predictions based on weather or county stats using our shiny trained model. So, pick an option, dive in, and let's solve some crime (or at least talk about it)!

**menu.py** - This script prints out everything that is displayed in the program. 

**demographics.py** - This script helps you figure out where crime is most common in New Jersey and what the demographics of those places look like. The first function, get_county_with_most_crime, takes a crime type and searches through all the data to find out which county is the crime hotspot. The second function, get_demographic_info_by_county, looks up the demographics of any given county. It grabs things like average income, median age, education level, and other juicy details about the county's population. If there's no data for a county, it just gives back None. So, it's a nice mix of crime and census info.

**weather.py** - This script is all about figuring out what crime happens most often in certain weather conditions or vice versa. The first function, 'most_common_crime_by_weather', takes the weather condition you give it, normalizes it (just in case you type it in weirdly), and then looks through the data to find the most common crime that happens in that weather. If it finds some data, it’ll tell you what crime is most common, otherwise, it’ll let you know that no data was found for that weather condition. The second function, 'most_common_weather_by_crime', works in the opposite direction. It takes the crime type, checks if it’s valid, and then finds the most common weather that happens when that crime occurs. Again, if there’s data for it, it tells you, and if not, it’ll tell you no data was found for that crime.


**predictions.py** - This script is all about predicting crimes in New Jersey based on weather and demographics. The first function, 'predict_most_common_crime', takes in data about the weather and the county's demographics (like population density, family size, etc.) Then it spits out the most likely crime based on a model we trained earlier. It’s basically saying, “Hey, based on the weather and where you live, what crime do we expect most? The second function, 'train_crime_prediction_model', is where all the magic happens. It sets up a pipeline to preprocess the data: cleaning it up, scaling it, and encoding it in a way that makes sense for the model. Then, it splits the data into training and testing sets, trains a logistic regression model to predict crime, and evaluates its accuracy. So, you input some weather and demographic data, and the model tells you what crime is most likely to happen next.

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


