import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression


st.title( 'Breast Cancer Prediction using Machine Learning')

model = pickle.load(open('D:\\python\\html_projects\\Breast_cancer_prediction\\model.pkl','rb'))

texture_mean = st.number_input('texture_mean')
smoothness_mean = st.number_input('smoothness_mean')
compactness_mean = st.number_input('compactness_mean')
concave_points_mean = st.number_input('concave points_mean')
symmetry_mean = st.number_input('symmetry_mean')
fractal_dimension_mean = st.number_input('fractal_dimension_mean')
texture_se = st.number_input('texture_se')
area_se = st.number_input('area_se')
smoothness_se = st.number_input('smoothness_se')
compactness_se = st.number_input('compactness_se')
concavity_se = st.number_input('concavity_se')
concave_points_se = st.number_input('concave points_se')
symmetry_se = st.number_input('symmetry_se')
fractal_dimension_se = st.number_input('fractal_dimension_se')
texture_worst = st.number_input('texture_worst')
area_worst = st.number_input('area_worst')
smoothness_worst = st.number_input('smoothness_worst')
compactness_worst = st.number_input('compactness_worst')
concavity_worst = st.number_input('concavity_worst')
concave_points_worst = st.number_input('concave points_worst')
symmetry_worst = st.number_input('symmetry_worst')
fractal_dimension_worst = st.number_input('fractal_dimension_worst')

input_data = np.array([[texture_mean,smoothness_mean, compactness_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, texture_se, area_se, smoothness_se,
   compactness_se, concavity_se, concave_points_se, symmetry_se,
       fractal_dimension_se, texture_worst, area_worst, smoothness_worst,
       compactness_worst, concavity_worst, concave_points_worst,
       symmetry_worst, fractal_dimension_worst]
])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Fraud detected")
    else:
        st.success("✅ Fraud Not Detected ")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
