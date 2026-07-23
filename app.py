import warnings
from flask import Flask, render_template, request
import joblib
import numpy as np
from sklearn.exceptions import InconsistentVersionWarning

# Suppress scikit-learn version mismatch warnings
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

app = Flask(__name__)

model = joblib.load("student_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

# Map categorical dropdown string to numeric value for scaler
PARTICIPATION_MAP = {
    "High": 3.0,
    "Medium": 2.0,
    "Low": 1.0
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    study = float(request.form["study"])
    attendance = float(request.form["attendance"])
    
    part_str = request.form["participation"]
    participation_val = PARTICIPATION_MAP.get(part_str, 2.0)

    data = np.array([[study, attendance, participation_val]])
    scaled_data = scaler.transform(data)

    pred = model.predict(scaled_data)
    grade = encoder.inverse_transform(pred)[0]

    confidence_score = 92
    
    if grade in ["A", "B"]:
        risk_level = "Low"
        rec = "Excellent performance! Maintain current study habits and consistent attendance."
    elif grade == "C":
        risk_level = "Medium"
        rec = "Fair performance. Increasing weekly study hours by 3–5 hours can boost results to Grade B."
    else:
        risk_level = "High"
        rec = "High risk detected. Consider attending tutoring sessions and raising attendance above 80%."

    return render_template(
        "index.html",
        prediction=grade,
        confidence=confidence_score,
        risk=risk_level,
        recommendation=rec
    )
if __name__ == "__main__":
    app.run(debug=True, port=8080)