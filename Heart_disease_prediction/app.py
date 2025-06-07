import streamlit as st
import numpy as np
import pandas as pd
import pickle


page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://media.istockphoto.com/id/1448453929/photo/cardiogram-pulse-trace-with-red-heart-on-pastel-blue-background.jpg?s=612x612&w=0&k=20&c=vROYnUeWCFJQ7uAV0Z_H1gQcwtBTygDg0aIB2YggbY0=");
  background-size: cover;
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Streamlit app
st.title("💓 Heart Disease Prediction App")
st.write("Enter the patient details below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=45)

cp = st.selectbox("Chest Pain Type (cp)", options=[0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", value=120)
chol = st.number_input("Serum Cholestoral in mg/dl (chol)", value=200)

thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", options=[0, 1])
oldpeak = st.number_input("ST depression induced by exercise (oldpeak)", value=1.0)
slope = st.selectbox("Slope of peak exercise ST segment (slope)", options=[0, 1, 2])
ca = st.selectbox("Number of major vessels colored by fluoroscopy (ca)", options=[0, 1, 2, 3, 4])


# Prediction
input_data = np.array([[age, cp, trestbps, chol, thalach,
                        exang, oldpeak, slope, ca]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ The patient is likely to have heart disease.")
    else:
        st.success("✅ The patient is unlikely to have heart disease.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")






