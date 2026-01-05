from flask import Flask, request, jsonify, render_template # Add render_template
import util

app = Flask(__name__)

util.load_saved_artifacts()

# THIS IS THE KEY: This connects the URL to your HTML file
@app.route('/')
def index():
    return render_template('app.html')

# ... (keep your other routes /get_location_names and /predict_home_price below)
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    # 'total_sqft' here acts as the 'Area' column in your dataframe
    area_marla = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # Pass the area_marla to your util function
    price = util.get_estimated_price(location, area_marla, bath, bhk)

    response = jsonify({
        'estimated_price': price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run() # This ensures the server DOES NOT exit with code 0