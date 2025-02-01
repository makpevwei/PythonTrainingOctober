# What is streamlit
# A open source python library that makes it easy to create and share beautiful, 
# custom web apps for, python, machine learning and data science.
# It requires no frontend exoerience.

# Key Features
# Write apps entitrely in python
# Automatically reloads our app when code changes
# Supports interactive widgets like sliders, buttons, file uploads, etc
# Easily integrates with machine learning and visualizations

# pip install streamlt

import streamlit as st
import pandas as pd

# print(st.__version__)

# Display different types of text

# st.title("This is a title")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is a text")
# st.info("This is an info")
# st.markdown("# **This is a markdown**")
# st.write("Using the write widget")

# # Interactive Widgets
# number = st.slider("Pick a number", 0, 100)
# st.write(f"Selected number: {number}")

# # Text Input
# name = st.text_input("What is your name: ")
# st.write(f"My name is {name}")


# # Numnber Input
# age = st.number_input("Enter your age: ", min_value=1, max_value=120, value=25)
# st.write(f"My age is {age}")


# # Multi-line Text Input
# message = st.text_area("Write a message: ", height=150,
#                        placeholder="Write your message here")
# st.write(f"My message is {message}")

# first_name = st.text_input("Enter your first name: ")
# last_name = st.text_input("Enter your last name: ")
# age = st.number_input("Enter your age: ", min_value=1, max_value=120, value=25)
# submit = st.button("Submit")
# if submit:
#     st.write(f"My first name is {first_name} and \
#              my last name is {last_name}. My age is {age}")
    

first_name = st.text_input("Enter your first name: ")
last_name = st.text_input("Enter your last name: ")
age = st.number_input("Enter your age: ", min_value=1, max_value=120, value=25)
if st.button("Submit"):
    if first_name and last_name and age:
        st.write(f"My first name is {first_name} and \
             my last name is {last_name}. My age is {age}")
    else:
        st.warning("Please fill in all fields")
        
# Intercative widgets - Buttons
primary_btn = st.button("Primary", type="primary")
secondary_btn = st.button("Secondary", type="secondary")

if primary_btn:
    st.write("Primary button clicked")
else:
    st.write("secondary button clicked")
    
names = ["Mike", "Bob", "Mary"]
age = [30, 40, 50]

students = pd.DataFrame(
    {"Name":names,
     "Age":age}
)

# Addin radio buttons for slecting a name
selected_name = st.radio(
    "Choose a name from the DataFrame:",
    students["Name"],
    index=1
)

if selected_name:
    selected_person = students[students["Name"] == selected_name]
    st.write(f"You selected {selected_name}. Here are their details:")
    st.write(selected_person)
    
# Using Multi-select widget
options = ["Python", "Java", "C#", "JavaScript"]
selected_languages = st.multiselect("Select programming languages:", options)

selected_string = ",".join(selected_languages)

if selected_string:
    st.write(f"You selected: {selected_string}")
else:
    st.write("No Languages Selected")
    
    
with st.form(key="Student form"):
    fn = st.text_input("Enter your first name: ")
    ln = st.text_input("Enter your last name: ")
    
    btn_submit = st.form_submit_button("Submit")
    
    
if btn_submit:
    st.write(f"{fn}:{ln}")