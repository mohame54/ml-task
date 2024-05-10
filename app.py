from flask import Flask, request, jsonify
from model import preprocess_feats, predict_model, load_comp


app = Flask(__name__)
model, scaler = load_comp()

@app.route('/predict', methods=["POST"])
def predict():
    req = request
    #print(req.get_json())
    #print(req.is_json)
    if req.is_json:
        req = req.json
        data = preprocess_feats(req)
        will_exit, prob = predict_model(model, data)
        return jsonify({"Will exit":will_exit, "prob":prob}), 200
    else:
        return  jsonify({"error": "Request does not contain JSON data"}), 400
    
