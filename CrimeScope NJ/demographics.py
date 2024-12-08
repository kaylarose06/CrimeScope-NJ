# This script helps you figure out where crime is most common in New Jersey and what the demographics of those places look like.
# The first function, get_county_with_most_crime, takes a crime type and searches through all the data to find out which county is the crime hotspot.
# The second function, get_demographic_info_by_county, looks up the demographics of any given county. It grabs things like average income, median age,
# education level, and other juicy details about the county's population. If there's no data for a county, it just gives back None. So, it's a nice mix of crime and census info.


def get_county_with_most_crime(merged_data, crime_type):
    """Find the county with the most occurrences of a specific crime type."""
    filtered_data = merged_data[merged_data["crime_type"] == crime_type]
    if not filtered_data.empty:
        most_common_county = filtered_data["county"].value_counts().idxmax()
        return most_common_county
    else:
        return None

def get_demographic_info_by_county(merged_data, county):
    """Fetch demographic details for a specific county."""
    filtered_data = merged_data[merged_data["county"] == county]
    if not filtered_data.empty:
        # Aggregate demographic information (e.g., averages or most common values)
        demographic_info = {
            "household_income": filtered_data["household_income"].mean(),
            "median_age": filtered_data["median_age"].mean(),
            "education_level": filtered_data["education_level"].mode()[0],
            "population_density": filtered_data["population_density"].mean(),
            "unemployment_rate": filtered_data["unemployment_rate"].mean(),
            "race_majority": filtered_data["race_majority"].mode()[0],
            "average_family_size": filtered_data["average_family_size"].mean(),
        }
        return demographic_info
    else:
        return None
