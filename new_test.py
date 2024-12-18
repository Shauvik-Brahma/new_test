import os
import pandas as pd
import streamlit as st
from openpyxl import load_workbook
from kaggle.api.kaggle_api_extended import KaggleApi

# Step 1: Access Kaggle API credentials from Streamlit secrets
kaggle_credentials = st.secrets["kaggle"]

os.environ["KAGGLE_USERNAME"] = kaggle_credentials["username"]
os.environ["KAGGLE_KEY"] = kaggle_credentials["key"]

api = KaggleApi()
api.authenticate()

# Step 2: Download the dataset from Kaggle
dataset_identifier = "shauvikbrahma/testttt"
api.dataset_download_files(dataset_identifier, path="./", unzip=True)

# Step 3: List files and find the Excel file in the downloaded dataset
downloaded_files = os.listdir("./")
excel_file = None
for file in downloaded_files:
    if file.endswith(".xlsx"):
        excel_file = file
        break

# Step 4: If Excel file exists, proceed with the Streamlit form for adding data
if excel_file:
    # Load the existing workbook
    wb = load_workbook(excel_file)
    sheet = wb.active

    # Step 5: Create a form to input Name and Class
    st.title("Append Data to Kaggle Excel Dataset")

    with st.form(key="append_form"):
        name = st.text_input("Enter Name")
        class_value = st.text_input("Enter Class")
        submit_button = st.form_submit_button("Add Data")

        if submit_button:
            if name and class_value:
                # Step 6: Append the new row to the Excel sheet
                new_row = [name, class_value]
                sheet.append(new_row)

                # Step 7: Save the workbook after appending the data
                wb.save(excel_file)

                st.success(f"Successfully added '{name}' and '{class_value}' to the dataset.")

                # Step 8: Display the updated DataFrame in Streamlit
                df = pd.read_excel(excel_file)
                st.subheader("Updated Data in the Excel File:")
                st.write(df)

            else:
                st.error("Both Name and Class are required fields.")
else:
    st.error("No Excel file found in the downloaded dataset.")

# Instructions on the sidebar
st.sidebar.subheader("Instructions")
st.sidebar.write("""
1. The app will automatically download your Kaggle dataset.
2. You can input data through the form (Name, Class).
3. After submitting, the data will be appended to the Kaggle Excel dataset.
4. The updated data will be displayed, and the file will be saved with the new row.
""")
