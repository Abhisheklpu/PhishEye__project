import re
import joblib
import pandas as pd

# Load the trained model once
model = joblib.load("phishing_model.pkl")

def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['has_ip'] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    features['has_at'] = 1 if '@' in url else 0
    features['has_dash'] = 1 if '-' in url else 0
    features['has_https'] = 1 if url.startswith('https') else 0
    features['num_dots'] = url.count('.')
    return pd.DataFrame([features])

def predict_url(url):
    features = extract_features(url)
    prediction = model.predict(features)[0]
    return prediction