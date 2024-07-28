import streamlit as st

def project_overview():
    st.title("Project Overview")

    st.markdown("""
    ## Insurance Cost Prediction
    This application aims to predict insurance costs based on user inputs using a machine learning model. 
    The following features are considered for the prediction:
    - Age
    - Sex
    - BMI
    - Number of Children
    - Smoking Status
    - Region

    The machine learning model used is a Random Forest Regressor, which has been trained on a dataset of insurance information.
    """)
