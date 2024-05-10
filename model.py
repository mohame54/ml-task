import pickle
import numpy as np


FEATS = {
    'Age': 'Age (years)',
    'Balance': 'Account Balance',
    'HasCrCard': 'Has Credit Card (Yes/No)',
    'IsActiveMember': 'Is Active Member (Yes/No)',
    'EstimatedSalary': 'Estimated Salary',
    'Geography_France': 'Geography (France)',
    'Geography_Germany': 'Geography (Germany)',
    'Geography_Spain': 'Geography (Spain)',
    'Gender_Female': 'Gender (Female)',
    'Gender_Male': 'Gender (Male)',
    'Card Type_DIAMOND': 'Card Type (DIAMOND)',
    'Card Type_GOLD': 'Card Type (GOLD)',
    'Card Type_PLATINUM': 'Card Type (PLATINUM)',
    'Card Type_SILVER': 'Card Type (SILVER)',
}

def load_comp():
    model  =  pickle.load(open("modelv2.pkl", "rb"))
    scaler = pickle.load(open("preprocessing.pkl", "rb"))
    return model, scaler


def preprocess_feats(feature_map) -> np.ndarray:   
    inputs = [feature_map.get(k) for k in FEATS.keys()] 
    inputs = np.array(inputs)[None]
    return inputs


def predict_model(model, inputs: np.ndarray):
    prob = model.predict_proba(inputs).squeeze()
    output = np.argmax(prob).tolist()
    prob = prob.tolist()[output]
    output = output == 1
    return output, prob
