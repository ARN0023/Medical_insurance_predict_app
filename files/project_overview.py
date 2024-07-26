import streamlit as st

def project_overview():
    st.title("Project Overview")

    st.write("""
    ## Overview

    This project aims to build a predictive model for insurance costs using the Random Forest algorithm. The model takes several input features such as age, sex, BMI, smoking status, and region to predict the insurance charges. 

    ## Features

    - **Data Preprocessing**: The dataset is cleaned and transformed, including encoding categorical variables and feature scaling.
    - **Model Training**: A Random Forest model is trained using hyperparameter tuning to find the best parameters.
    - **Model Evaluation**: The model is evaluated using various metrics like R^2, MAE, MSE, and RMSE to ensure its performance.
    - **Prediction**: A Streamlit app is used to make predictions based on user inputs.
    - **Data Visualization**: Visualizations are provided to understand the relationships between different features and the target variable.

    ## Installation

    To run this project, you need to install the required packages. Use the following command to install them:

    ```bash
    pip install -r requirements.txt
    ```

    ## Usage

    1. **Train the Model**: Run the `train_model.py` script to train and save the Random Forest model.
    2. **Evaluate the Model**: Run the `evaluate_model.py` script to evaluate the model's performance.
    3. **Run the Streamlit App**: Use the following command to start the Streamlit app:

    ```bash
    streamlit run streamlit_app.py
    ```

    ## File Structure

    - `backend/`
      - `rf_model.pkl`: Saved model file
      - `model_training.py`: Script to train the model
      - `model_evaluation.py`: Script to evaluate the model
    - `modules/`
      - `data_loading.py`: Function to load data
      - `preprocessing.py`: Function to preprocess data
      - `project_overview.py`: Overview page for Streamlit app
    - `requirements.txt`: Required Python packages
    - `.gitignore`: Files and directories to ignore in Git
    - `streamlit_app.py`: Main Streamlit app file

    ## License

    This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
    """)

if __name__ == "__main__":
    project_overview()
