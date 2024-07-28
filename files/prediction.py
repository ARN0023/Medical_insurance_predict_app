import streamlit as st
import numpy as np
import joblib

# Load model
MODEL_PATH = 'models/rf_model.pkl'
model = joblib.load(MODEL_PATH)

def prediction():
    st.title("Prediction Using User Inputs")

    age = st.slider("Age", min_value=18, max_value=100, value=28)
    sex = st.radio("Sex", ["Male", "Female"], horizontal=True)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
    children = st.slider("Children", min_value=0, max_value=10, value=0)
    smoker = st.radio("Smoker", ["Yes", "No"], horizontal=True)
    region = st.radio("Region", ["Southeast", "Southwest", "Northeast", "Northwest"])

    sex = 0 if sex == "Male" else 1
    smoker = 1 if smoker == "Yes" else 0
    region_dict = {"Southeast": 0, "Southwest": 1, "Northeast": 2, "Northwest": 3}
    region = region_dict[region]

    # Create input array with correct order and number of features
    input_data = np.array([[age, sex, bmi, children, smoker, region]])

    # Add CSS to center and style the button and output
    st.markdown("""
        <style>
            .center-button {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100%;
            }
            .large-button {
                font-size: 20px;
                padding: 10px 20px;
                border-radius: 5px;
                border: none;
                color: white;
                background-color: #007bff;
                cursor: pointer;
            }
            .large-button:hover {
                background-color: #0056b3;
            }
            .result-text {
                font-size: 24px;
                font-weight: bold;
                color: #333;
                text-align: center;
            }
        </style>
        """, unsafe_allow_html=True)

    # Create a container for the button
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Predict", key="predict_button", help="Click to predict insurance cost", use_container_width=True):
                prediction_result = model.predict(input_data)
                st.markdown(f"""
                    <div class="result-text">
                        The predicted insurance cost is <br><br>
                        <span style="font-size: 36px; color: #007bff;">${prediction_result[0]:,.2f}</span>
                    </div>
                    """, unsafe_allow_html=True)

if __name__ == "__main__":
    prediction()
