import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from modules.data_loading import load_data

def data_visualization():
    st.title("Data Visualization")

    # Load data
    df = load_data()

    # Scatter plot of Charges vs Age
    st.write("### Scatter Plot of Charges vs Age")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='age', y='charges', ax=ax)
    ax.set_title('Charges vs Age')
    ax.set_xlabel('Age')
    ax.set_ylabel('Charges')
    st.pyplot(fig)

    # Scatter plot of Charges vs BMI
    st.write("### Scatter Plot of Charges vs BMI")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='bmi', y='charges', ax=ax)
    ax.set_title('Charges vs BMI')
    ax.set_xlabel('BMI')
    ax.set_ylabel('Charges')
    st.pyplot(fig)

    # Box plot of Charges by Smoker Status
    st.write("### Box Plot of Charges by Smoker Status")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='smoker', y='charges', ax=ax)
    ax.set_title('Charges by Smoker Status')
    ax.set_xlabel('Smoker')
    ax.set_ylabel('Charges')
    st.pyplot(fig)

    # Distribution plot of Charges
    st.write("### Distribution of Charges")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['charges'], kde=True, ax=ax)
    ax.set_title('Distribution of Charges')
    ax.set_xlabel('Charges')
    st.pyplot(fig)

    # Pair plot of numerical features
    st.write("### Pair Plot of Numerical Features")
    fig = sns.pairplot(df[['age', 'bmi', 'charges']])
    st.pyplot(fig)

    # Bar plot of average charges by region
    st.write("### Average Charges by Region")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x='region', y='charges', estimator=sum, ax=ax)
    ax.set_title('Average Charges by Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Charges')
    st.pyplot(fig)

if __name__ == "__main__":
    data_visualization()
