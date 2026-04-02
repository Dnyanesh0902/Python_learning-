from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression

# Initialize Flask App
app = Flask(__name__)

# Training Data (Study Hours vs Marks)
X = np.array([1, 2, 2.5, 3, 3.5, 4, 5, 6]).reshape(-1, 1)
y = np.array([40, 50, 60, 70, 80, 90, 95, 97])

# Train Machine Learning Model
model = LinearRegression()
model.fit(X, y)


# Home Route
@app.route("/")
def home():
    return "Student Marks Predictor API is Running"


# Prediction API
@app.route("/predict", methods=["POST"])
def predict_marks():

    data = request.get_json()

    # Check if request body exists
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    # Check if hours key exists
    if "hours" not in data:
        return jsonify({"error": "Please provide study hours"}), 400

    try:
        hours = float(data["hours"])
    except:
        return jsonify({"error": "Hours must be a number"}), 400

    # Validate range
    if hours < 0 or hours > 6:
        return jsonify({"error": "Hours must be between 0 and 6"}), 400

    # AI Prediction
    predicted_marks = model.predict(np.array([[hours]]))[0]

    # Limit marks between 0 and 100
    predicted_marks = max(0, min(100, predicted_marks))

    return jsonify({
        "study_hours": hours,
        "predicted_marks": round(predicted_marks, 2)
    })


# Run Flask Server
if __name__ == "__main__":
    app.run(debug=True)