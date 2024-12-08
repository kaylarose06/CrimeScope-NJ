# Okay, so this script is all about predicting crimes in New Jersey based on weather and demographics. 
# The first function, 'predict_most_common_crime', takes in data about the weather and the county's demographics (like population density, family size, etc.)
# Then it spits out the most likely crime based on a model we trained earlier. It’s basically saying, “Hey, based on the weather and where you live, 
# what crime do we expect most?”
# The second function, 'train_crime_prediction_model', is where all the magic happens. It sets up a pipeline to preprocess the data: 
# cleaning it up, scaling it, and encoding it in a way that makes sense for the model. Then, it splits the data into training and testing sets, 
# trains a logistic regression model to predict crime, and evaluates its accuracy.
# So, you input some weather and demographic data, and the model tells you what crime is most likely to happen next.


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
import pandas as pd


def predict_most_common_crime(model, weather_input, demographic_input, weather_conditions):
    # Ensure all required features are included in the input data
    input_data = {
        'temp': weather_input['temp'],
        'weather_normalized': weather_input['weather'].lower(),
        'county': demographic_input.get('county', ''),  # Assuming demographic input is a dictionary
        'population_density': demographic_input.get('population_density', 0),
        'unemployment_rate': demographic_input.get('unemployment_rate', 0),
        'average_family_size': demographic_input.get('average_family_size', 0),
    }

    input_df = pd.DataFrame([input_data])  # Convert the input data to a DataFrame

    # Predict the most common crime
    predicted_crime = model.predict(input_df)[0]  # Predict and get the first value
    return predicted_crime


def train_crime_prediction_model(merged_data):
    # Preprocess the data: handle missing values, encode categorical data
    categorical_columns = ['weather_normalized', 'county']  # Add other categorical columns if necessary
    numeric_columns = ['temp', 'population_density', 'unemployment_rate', 'average_family_size']  # Example of numeric columns

    # Preprocessing pipeline for numeric and categorical data
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),  # Impute missing numeric values
        ('scaler', StandardScaler())  # Scale numeric data
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),  # Impute missing categorical values
        ('onehot', OneHotEncoder(handle_unknown='ignore'))  # One-hot encode categorical variables
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_columns),
            ('cat', categorical_transformer, categorical_columns)
        ])

    # Combine preprocessing with the classifier (Logistic Regression)
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(max_iter=2000, solver='lbfgs'))  # Increased max_iter
    ])

    # Prepare the data for training
    X = merged_data[numeric_columns + categorical_columns]  # Features
    y = merged_data['crime_type']  # Target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # # Evaluate the model
    # y_pred = model.predict(X_test)
    # accuracy = accuracy_score(y_test, y_pred)

    return model, merged_data['weather_normalized'].unique()
