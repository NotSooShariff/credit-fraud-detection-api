from flask import Flask, request, jsonify
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential, load_model
import joblib
import numpy as np

app = Flask(__name__)
model = load_model('model.h5')
vectorization_components = joblib.load('vectorize.pkl')
robust_scaler = vectorization_components['robust_scaler']
time_min = vectorization_components['time_min']
time_max = vectorization_components['time_max']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        features = [
            data['V1'], data['V2'], data['V3'], data['V4'], data['V5'],
            data['V6'], data['V7'], data['V8'], data['V9'], data['V10'],
            data['V11'], data['V12'], data['V13'], data['V14'], data['V15'],
            data['V16'], data['V17'], data['V18'], data['V19'], data['V20'],
            data['V21'], data['V22'], data['V23'], data['V24'], data['V25'],
            data['V26'], data['V27'], data['V28'],
        ]
        amount = data['Amount']
        time = data['Time']

        amount = float(amount)
        time = float(time)

        scaled_amount = robust_scaler.transform(np.array([[amount]]))
        scaled_time = (time - time_min) / (time_max - time_min)

        input_features = np.concatenate((features, scaled_amount.flatten(), [scaled_time]))

        prediction = model.predict(np.array([input_features]))

        response = {'fraud_probability': float(prediction[0][0])}

        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
