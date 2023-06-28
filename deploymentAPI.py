from flask import Flask, request, jsonify
import pickle
import pandas as pd
import json

app = Flask(__name__)

# Load the pickled model
with open('svm_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    data = request.get_json()
    # Perform prediction using the loaded model
    
    input_entry = pd.DataFrame(data)

    prediction = model.predict(input_entry)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)