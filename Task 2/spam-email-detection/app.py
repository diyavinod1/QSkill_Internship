from flask import Flask, render_template, request, jsonify

import joblib
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

app = Flask(__name__)

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):

    text = text.lower()

    text = ''.join(
        ch for ch in text
        if ch not in string.punctuation
    )

    words = text.split()

    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    message = request.form["message"]

    clean_text = preprocess_text(message)

    vectorized = vectorizer.transform(
        [clean_text]
    )

    prediction = model.predict(vectorized)[0]

    probabilities = model.predict_proba(vectorized)[0]

    print("Original Message:", message)
    print("Clean Text:", clean_text)
    print("Prediction:", prediction)
    print("Probabilities:", probabilities)

    confidence = max(probabilities) * 100

    result = "Spam" if prediction == 1 else "Ham"

    return jsonify({
        "prediction": result,
        "confidence": round(confidence, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)