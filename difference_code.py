import streamlit as st
import pandas as pd

st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Net Pay Difference Calculator")
emp_number = st.text_input("Enter Employee Number")

# Load the employee data from a CSV file into a Pandas DataFrame
df = pd.read_csv('netpay_data.csv')

if emp_number:
     data = df[df['Employee Number'] == int(emp_number)]
     current_month_salary = int(row['Net Pay March'])
     current_month_salary = int(row['Net Pay Feb'])
     Net_Pay_difference = current_month_salary - current_month_salary
     st.write(Net_Pay_difference)
else:
 # If employee number is not found in the CSV file
     st.write("Employee number not found in the CSV file.")
       
