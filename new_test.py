import os
import pandas as pd
from openpyxl import load_workbook
import streamlit as st

# Streamlit page configuration
st.title("Excel Data Appender")

# Step 1: Upload the Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    # Load the workbook from the uploaded file
    wb = load_workbook(uploaded_file)
    sheet = wb.active

    # Step 2: Display the current data in the uploaded file (if any)
    st.subheader("Current Data in the Excel File:")
    df = pd.read_excel(uploaded_file)
    st.write(df)

    # Step 3: Create a form for user input (Name, Class)
    with st.form(key="data_form"):
        name = st.text_input("Enter Name")
        class_value = st.text_input("Enter Class")
        submit_button = st.form_submit_button("Add Data")

        if submit_button:
            # Step 4: Append the new data to the Excel file
            if name and class_value:
                # Append the new row to the dataframe
                new_row = {"Name": name, "Class": class_value}
                df = df.append(new_row, ignore_index=True)

                # Save the updated DataFrame back to the Excel file
                temp_file_path = "/tmp/modified_file.xlsx"
                df.to_excel(temp_file_path, index=False)

                # Provide a download link for the modified file
                with open(temp_file_path, "rb") as f:
                    st.download_button(
                        label="Download Updated Excel",
                        data=f,
                        file_name="modified_excel.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                st.success(f"Successfully added '{name}' and '{class_value}' to the file.")
            else:
                st.error("Please fill in both fields (Name and Class).")

# Instructions
st.sidebar.subheader("Instructions")
st.sidebar.write("""
1. Upload your Excel file.
2. Enter the data you want to append in the form and click 'Add Data'.
3. Download the updated Excel file from the link provided after adding data.
""")
