import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression


# Load the trained model
model = pickle.load(open("D:\\data_science_repo\\Stock_Price_Pridction\\model.pkl", "rb"))

# Streamlit app
st.title("Stock Price Prediction App")

# Input fields
Open = st.number_input("Open")
High = st.number_input("High")
Low = st.number_input("Low")
Volume = st.number_input('Volume')

# Prediction
input_data = np.array([[Open, High, Low, Volume]])


if st.button("Predict"):
  prediction = model.predict(input_data)
  st.success(f"🎓 Predicted Stock: {prediction[0]:.2f}")
    

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
