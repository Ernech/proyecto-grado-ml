from flask import Flask, request,jsonify
from aritrajeNLP import getParams
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


@app.route('/naive-bayes', methods=['POST'])
def naiveBayes():
    json = request.get_json()
    query_df = pd.DataFrame(json)
    query = pd.get_dummies(query_df)
    classifier = joblib.load('naive_bayes.pkl')
    prediction = classifier.predict(query)
    return jsonify({'prediction': int(prediction)})    
    

@app.route('/random-forest', methods=['POST'])
def randomForest():
    json = request.get_json()
    query_df = pd.DataFrame(json)
    query = pd.get_dummies(query_df)
    classifier = joblib.load('random_forest.pkl')
    prediction = classifier.predict(query)
    return jsonify({'prediction': int(prediction)})    


@app.route('/logistic-regresion', methods=['POST'])
def logisticRegresion():
    json = request.get_json()
    query_df = pd.DataFrame(json)
    query = pd.get_dummies(query_df)
    classifier = joblib.load('logistic_regresion.pkl')
    prediction = classifier.predict(query)
    return jsonify({'prediction': int(prediction)})    

@app.route('/params',methods=['POST'])
def params():
    json=request.get_json()
    text = json['param']
    return jsonify(getParams(text))
    