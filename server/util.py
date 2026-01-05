import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, total_sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    # Create an array of zeros with the length of our 93 columns
    x = np.zeros(len(__data_columns))
    x[0] = bhk
    x[1] = total_sqft  # This is your Marla value
    x[2] = bath

    if loc_index >= 0:
        x[loc_index] = 1

    # Return the prediction from our 91% accurate model
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # Load the Column Names (JSON)
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

        # Based on your JSON image, "bedroom(s)" is the first item.
        # We start from index 1 to skip it and only show locations in the dropdown.
        __locations = __data_columns[5:]

    # Load the Model (Pickle)
    with open("./artifacts/lahore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("loading saved artifacts...done")


# This allows you to test util.py independently
if __name__ == '__main__':
    load_saved_artifacts()
    print(f"Successfully loaded {len(__locations)} locations.")
    # Example test: 5 Marla, 2 Bath, 2 BHK in DHA Defence
    # print(get_estimated_price('dha defence', 5, 2, 2))