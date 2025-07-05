import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression


st.title( 'Customer Churn Detection using Machine Learning')

model = pickle.load(open('D:\\data_science_repo\\Customers_Churn_Prediction\\model.pkl','rb'))

Gender= st.number_input('gender')
SeniorCitizen = st.number_input('SeniorCitizen')
Partner = st.number_input('Partner')
Dependents = st.number_input('Dependents')
tenure = st.number_input('tenure')
PhoneService = st.number_input('PhoneService')
MultipleLines = st.number_input('MultipleLines')
InternetService = st.number_input('InternetService')
OnlineSecurity = st.number_input('OnlineSecurity')
OnlineBackup = st.number_input('OnlineBackup')
DeviceProtection = st.number_input('DeviceProtection')
TechSupport = st.number_input('TechSupport')
StreamingTV = st.number_input('StreamingTV')
StreamingMovies = st.number_input('StreamingMovies')
Contract = st.number_input('Contract')
PaperlessBilling = st.number_input('PaperlessBilling')
PaymentMethod = st.number_input('PaymentMethod')
MonthlyCharges = st.number_input('MonthlyCharges')

input_data = np.array([[Gender, SeniorCitizen, Partner, Dependents,tenure, PhoneService, MultipleLines, InternetService,OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,StreamingTV, StreamingMovies, Contract, PaperlessBilling,PaymentMethod, MonthlyCharges]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Churn detected")
    else:
        st.success("✅ Churn Not Detected ")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
