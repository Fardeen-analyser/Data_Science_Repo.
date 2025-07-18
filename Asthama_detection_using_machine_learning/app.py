import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression


st.title( 'Asthma Detection using Machine Learning')

model = pickle.load(open('D:\\data_science_repo\\Asthama_detection_using_machine_learning\\model.pkl','rb'))


Age = st.number_input('Age')
BMI = st.number_input('BMI')
Smoking_Status = st.number_input('Smoking_Status')
Family_History = st.number_input('Family_History')
Allergies = st.number_input('Allergies')
Air_Pollution_Level = st.number_input('Air_Pollution_Level')
Physical_Activity_Level = st.number_input('Physical_Activity_Level')
Occupation_Type = st.number_input('Occupation_Type')
Comorbidities = st.number_input('Comorbidities')
Medication_Adherence = st.number_input('Medication_Adherence')
Number_of_ER_Visits = st.number_input('Number_of_ER_Visits')
Peak_Expiratory_Flow = st.number_input('Peak_Expiratory_Flow')
FeNO_Level = st.number_input('FeNO_Level')


input_data = np.array([[Age, BMI, Smoking_Status, Family_History, Allergies,
       Air_Pollution_Level, Physical_Activity_Level, Occupation_Type,
       Comorbidities, Medication_Adherence, Number_of_ER_Visits,
       Peak_Expiratory_Flow, FeNO_Level]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Asthma Detected")
    else:
        st.success("✅ Asthma Not Detected ")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
