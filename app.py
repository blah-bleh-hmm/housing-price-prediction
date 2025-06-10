from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)


# Load the trained model pickle file once when app starts
with open('model.pickle', 'rb') as f:
    model = pickle.load(f)

# Load columns.json once when app starts
with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']

@app.route('/')
def home():
    return render_template('index.html')  # loads templates/index.html

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'No input data provided'}), 400
        
        # Extract numerical features from input JSON
        total_sqft = float(data.get('total_sqft', 0))
        bath = float(data.get('bath', 0))
        bhk = float(data.get('bhk', 0))
        location = data.get('location', '').lower().strip()

        # Initialize feature vector with zeros
        x = np.zeros(len(data_columns))

        # Set numerical features - assuming total_sqft, bath, bhk are first 3 columns
        x[0] = total_sqft
        x[1] = bath
        x[2] = bhk

        # One-hot encode location feature
        # Match location case-insensitively
        location_columns = [col.lower() for col in data_columns]
        if location in location_columns:
            loc_index = location_columns.index(location)
            x[loc_index] = 1
        else:
            # If location not found, just leave one-hot as zero vector
            pass

        # Reshape to 2D array for model prediction (1 sample, n features)
        x = x.reshape(1, -1)

        # Make prediction
        predicted_price = model.predict(x)[0]

        # Return prediction rounded to 2 decimal places
        return jsonify({'predicted_price': round(predicted_price, 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Run Flask app on localhost port 5000 with debug on
    app.run(debug=True)
