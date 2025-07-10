import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression


st.title( 'Sleep Health Lifestyle Detection using Machine Learning')

model = pickle.load(open('D:\\data_science_repo\\Sleep__Health_Lifestyle\\model.pkl','rb'))

Gender = st.number_input('Gender')
Age = st.number_input('Age')
Occupation = st.number_input('Occupation')
Sleep_Duration = st.number_input('Sleep Duration')
Quality_of_Sleep = st.number_input('Quality of Sleep')
Physical_Activity_Level = st.number_input('Physical Activity Level')
Stress_Level = st.number_input('Stress Level')
BMI_Category = st.number_input('BMI Category')
Heart_Rate = st.number_input('Heart Rate')
Daily_Steps = st.number_input('Daily Steps')
High_BP = st.number_input('High_BP')
Low_BP = st.number_input('Low_BP')

input_data = np.array([[Gender, Age, Occupation, Sleep_Duration, Quality_of_Sleep, Physical_Activity_Level, Stress_Level, BMI_Category, Heart_Rate, Daily_Steps,High_BP, Low_BP]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 0:
        st.error("⚠️ Sleep Apnea")
    elif prediction[0]<=0.5:
        st.success("⚠️ Insomnia ")
    else:
        st.success("✅ No Disorder")

        

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
