import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQfmIm5g0hp_ZROgC1e-A_NVhvieSaOI8u2ICBJLSXOMT7pmqgb");
  background-size: cover;
  color:purple
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)

st.title( 'Loan Prediction using Machine Learning', )

model = pickle.load(open('D:\\data_science_repo\\Load_Prediction\\model.pkl','rb'))

Gender = st.number_input('Gender')
Married = st.number_input('Married')
Dependents = st.number_input('Dependents')
Self_Employed = st.number_input('Self_Employed')
LoanAmount = st.number_input('LoanAmount')
Loan_Amount_Term = st.number_input('Loan_Amount_Term')
Property_Area = st.number_input('Property_Area')
Total_Income = st.number_input('Total_Income')

input_data = np.array([[Gender, Married, Dependents, Self_Employed, LoanAmount,
       Loan_Amount_Term,  Property_Area, Total_Income]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Credit History found")
    else:
        st.success("✅ Credit History not found ")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
