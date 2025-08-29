from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import redis
from rq import Queue
import numpy as np

app = Flask(__name__)
CORS(app)

# Redis queue
r = redis.Redis()
q = Queue(connection=r)

# Dummy ML model (linear regression)
def train_model():
    from sklearn.linear_model import LinearRegression
    import numpy as np
    X = np.array([[1, 1], [2, 2], [3, 1.5], [4, 3]])
    y = np.array([10, 20, 22, 35])
    model = LinearRegression().fit(X, y)
    joblib.dump(model, 'model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    X = [[data['distance_km'], data['fuel_used']]]

    model = joblib.load('model.pkl')
    prediction = model.predict(X)[0]
    return jsonify({'eta_minutes': round(prediction, 2)})

if __name__ == '__main__':
    train_model()  # Only once
    app.run(port=5000)
