import streamlit as st
import pandas as pd
from streamlit.scriptrunner.script_run_context import get_script_run_ctx

# Get the employee number from the user
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n AI Employee Net Pay Difference Calculator")
employee_number = st.text_input("Enter the employee number:")


df1 = pd.read_csv('netpaydata.csv')
if employee_number:
    data = df1[df1['Employee_number'] == int(employee_number)]
    current_month_salary = int(row['Net Pay March'])
    previous_month_salary = int(row['Net Pay Feb'])
    difference = current_month_salary - previous_month_salary
    st.write("The net pay difference for employee number {} is:".format(employee_number), difference)
    
else:
    st.write("Employee number not found in the CSV file.")
                
        
 


