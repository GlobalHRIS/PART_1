import streamlit as st
import pandas as pd

st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n AI Employee Net Pay Difference Calculator")
emp_number = st.text_input("Enter Employee Number")

def calculate_difference():
    # Load the employee data from a CSV file into a Pandas DataFrame
    df = pd.read_csv('netpaydata.csv')
    
    # Calculate the net pay difference between February and March
    if emp_number:
        df['Net Pay Difference'] = df['Net Pay March'] - df['Net Pay Feb']
        # Display the result
        st.write("The net pay difference for employee number {} is:".format(emp_number), Net Pay Difference) 
    

# Call the calculate_difference function
calculate_difference()

    
