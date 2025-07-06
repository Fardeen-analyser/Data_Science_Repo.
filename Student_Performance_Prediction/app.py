import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression


# Load the trained model
model = pickle.load(open("D:\data_science_repo\\Student_Performance_Prediction\\model.pkl", "rb"))

# Streamlit app
st.title("Student Academic Performance Prediction App")
st.write("Enter the student academic details below:")

# Input fields
Gender = st.number_input("Gender")

HoursStudiedperWeek = st.number_input("HoursStudied/Week")
Tutoring = st.number_input("Tutoring")
Region = st.number_input("Region")

Attendance = st.number_input("Attendance(%)")
Parent_Education = st.number_input("Parent Education")


# Prediction
input_data = np.array([[Gender, HoursStudiedperWeek, Tutoring, Region, Attendance,Parent_Education]])


if st.button("Predict"):
  prediction = model.predict(input_data)
  st.success(f"🎓 Predicted Academic Performance: {prediction[0]:.2f}")
    

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
