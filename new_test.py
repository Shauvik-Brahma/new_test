import os
import streamlit as st
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Function to authenticate and download the dataset
def download_kaggle_dataset():
    kaggle_username = st.secrets["kaggle"]["username"]
    kaggle_key = st.secrets["kaggle"]["key"]

    # Set the environment variables for Kaggle API
    os.environ["KAGGLE_USERNAME"] = kaggle_username
    os.environ["KAGGLE_KEY"] = kaggle_key

    # Authenticate the Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Define the dataset identifier (replace with your dataset's identifier)
    dataset_identifier = "shauvikbrahma/testttt"  # Replace with your dataset identifier
    api.dataset_download_files(dataset_identifier, path="./", unzip=True)

    return "./test.xlsx"  # Path to the downloaded dataset

# Streamlit App Interface
st.title("Student Information Form")

# Form for inputting Name and Class
with st.form(key='student_form'):
    name = st.text_input("Name")
    student_class = st.text_input("Class")
    
    submit_button = st.form_submit_button(label="Submit")

# After form submission
if submit_button:
    st.write(f"Name: {name}")
    st.write(f"Class: {student_class}")

    # Download and load Kaggle dataset
    try:
        dataset_path = download_kaggle_dataset()
        st.write(f"Dataset downloaded and ready: {dataset_path}")
        
        # Load the Excel file into a dataframe
        df = pd.read_excel(dataset_path)
        
        # Show the dataset content
        st.write("Dataset content:")
        st.dataframe(df)

    except Exception as e:
        st.error(f"An error occurred while fetching the dataset: {e}")
