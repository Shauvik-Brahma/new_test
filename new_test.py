import streamlit as st

# Title of the web page
st.title("Student Information Form")

# Create a form
with st.form(key='student_form'):
    # Input fields for Name and Class
    name = st.text_input("Name")
    student_class = st.text_input("Class")
    
    # Submit button for the form
    submit_button = st.form_submit_button(label="Submit")

# After form submission, display the entered data
if submit_button:
    st.write("Submitted Information:")
    st.write(f"Name: {name}")
    st.write(f"Class: {student_class}")
