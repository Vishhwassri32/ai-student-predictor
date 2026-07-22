import streamlit as st
import joblib
import numpy as np
model = joblib.load("student_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)
st.title("🎓 AI-Powered Student Performance Predictor")
st.write("Predict the student's grade based on academic performance.")
st.divider()
study_hours = st.number_input(
    "Weekly Self Study Hours",
    min_value=0,
    max_value=100,
    value=15
)
attendance = st.slider(
    "Attendance Percentage",
    0,
    100,
    85
)

participation = st.slider(
    "Class Participation",
    0,
    10,
    5
)
if st.button("Predict Grade"):
    input_data = np.array([[study_hours,
                            attendance,
                            participation]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    grade = encoder.inverse_transform(prediction)
    st.success(f"Predicted Grade : {grade[0]}")