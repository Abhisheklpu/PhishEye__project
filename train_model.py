# ✅ Import the required libraries
import pandas as pd
import re
from urllib.parse import urlparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# ✅ Load the dataset
print("🔄 Loading dataset...")
df = pd.read_csv("phishing_site_urls.csv")

# ✅ Clean and map label column: "bad" => 1, "good" => 0
df['Label'] = df['Label'].str.strip().str.lower()  # Clean spaces and lowercase
df['Label'] = df['Label'].map({'bad': 1, 'good': 0})

# ✅ Feature extraction function
def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['has_ip'] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    features['has_at'] = 1 if '@' in url else 0
    features['has_dash'] = 1 if '-' in url else 0
    features['has_https'] = 1 if url.startswith('https') else 0
    features['num_dots'] = url.count('.')
    return features

# ✅ Apply feature extraction to dataset
features = df['URL'].apply(extract_features)
X = pd.DataFrame(features.tolist())
y = df['Label']

# ✅ Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train the machine learning model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ✅ Predict and show accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"🎯 Model Accuracy: {accuracy*100:.2f}%")

# ✅ Save the trained model
joblib.dump(model, "phishing_model.pkl")
print("✅ Model saved as phishing_model.pkl")