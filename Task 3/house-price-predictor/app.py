from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# ==========================
# LOAD MODEL & SCALER
# ==========================

model = joblib.load("models/house_price_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# ==========================
# HOME PAGE
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# PREDICTION
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        area = float(request.form["area"])
        bedrooms = float(request.form["bedrooms"])
        bathrooms = float(request.form["bathrooms"])
        stories = float(request.form["stories"])
        parking = float(request.form["parking"])

        mainroad = 1 if request.form["mainroad"] == "yes" else 0
        guestroom = 1 if request.form["guestroom"] == "yes" else 0
        basement = 1 if request.form["basement"] == "yes" else 0
        hotwaterheating = 1 if request.form["hotwaterheating"] == "yes" else 0
        airconditioning = 1 if request.form["airconditioning"] == "yes" else 0
        prefarea = 1 if request.form["prefarea"] == "yes" else 0

        furnishing = request.form["furnishingstatus"]

        semi_furnished = 0
        unfurnished = 0

        if furnishing == "semi-furnished":
            semi_furnished = 1

        elif furnishing == "unfurnished":
            unfurnished = 1

        data = np.array([[
            area,
            bedrooms,
            bathrooms,
            stories,
            parking,
            mainroad,
            guestroom,
            basement,
            hotwaterheating,
            airconditioning,
            prefarea,
            semi_furnished,
            unfurnished
        ]])

        scaled_data = scaler.transform(data)

        prediction = model.predict(scaled_data)[0]

        return render_template(
            "index.html",
            prediction=f"₹ {prediction:,.0f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}"
        )


# ==========================
# RUN APP
# ==========================

if __name__ == "__main__":
    app.run(debug=True)