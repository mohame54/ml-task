import pickle
import numpy as np


def load_comp():
    model  =  pickle.load(open("model.pkl", "rb"))
    scaler = pickle.load(open("preprocessing.pkl", "rb"))
    return model, scaler


def preprocess_feats(scaler,feature_map) -> np.ndarray:    
    inputs = list(feature_map.values())
    inputs = np.array(inputs)[None]
    return scaler.transform(inputs)


def predict_model(model, inputs: np.ndarray):
    prob = model.predict_proba(inputs).squeeze()
    output = np.argmax(prob).tolist()
    prob = prob.tolist()[output]
    output = output == 1
    return output, prob
