from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

species_names = [
    "Iris Setosa",
    "Iris Versicolor",
    "Iris Virginica"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    features = np.array([
        [
            float(data["sepal_length"]),
            float(data["sepal_width"]),
            float(data["petal_length"]),
            float(data["petal_width"])
        ]
    ])

    prediction = model.predict(features)[0]

    confidence = (
        np.max(
            model.predict_proba(features)
        ) * 100
    )

    return jsonify({
        "species":
            species_names[prediction],
        "confidence":
            round(confidence, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)