import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression


# Load the trained model
model = pickle.load(open("D:\\data_science_repo\\Sales\\model.pkl", "rb"))

# Streamlit app
st.title("Sales Prediction App")

# Input fields
Product_Category = st.number_input("Product Category")
Quantity = st.number_input("Quantity")
Price_per_Unit = st.number_input("Price per Unit")

# Prediction
input_data = np.array([[Product_Category,Quantity, Price_per_Unit]])


if st.button("Predict"):
  prediction = model.predict(input_data)
  st.success(f"🎓 Predicted sales: {prediction[0]:.2f}")
    

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
