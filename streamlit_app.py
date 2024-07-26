import streamlit as st

# Set up page config
st.set_page_config(
    page_title="Insurance Cost Prediction",
    page_icon="🧑‍💼", 
    layout="centered" 
)

# Import the functions for each page
from files.project_overview import project_overview
from files.data_visualization import data_visualization
from files.prediction import prediction

# Define pages
PAGES = {
    "Project Overview": project_overview,
    "Data Visualization": data_visualization,
    "Prediction Using User Inputs": prediction
}

# Page selector
page = st.sidebar.selectbox("Select a Page", options=list(PAGES.keys()))

# Call the appropriate page function
PAGES[page]()
