from flask import Flask, request,jsonify
import pandas as pd
import joblib

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    json = request.get_json()
    query_df = pd.DataFrame(json)
    query = pd.get_dummies(query_df)
    classifier = joblib.load('classifier.pkl')
    prediction = classifier.predict(query)
    return jsonify({'prediction': int(prediction)})
    