import streamlit as st
import pandas as pd
          
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Net Pay Difference Calculator")
emp_number = st.text_input("Enter Employee Number")    

# Load the employee data from a CSV file into a Pandas DataFrame
df = pd.read_csv('netpay_data.csv')
for row in df:
     if emp_number:
          netpay = df[df['Employee Number'] == int(emp_number)]
          st.write("Employee Data Found")
          st.write(netpay)
          #current_month_salary = df['Net Pay March']
          #previous_month_salary = df['Net Pay Feb']
          difference = df[int(row['Net Pay March'] - df['Net Pay Feb'])]
          st.write("The net pay difference for employee number {} is:".format(emp_number), difference)   



          
          #current_month_salary = int(row['Net Pay March'])
          #previous_month_salary = int(row['Net Pay Feb'])
          #break
     #else:
         # If employee number is not found in the CSV file
          #st.write("Employee number not found in the CSV file.")
          
# Calculate the difference
#difference = current_month_salary - previous_month_salary  
# Display the result
#st.write("The net pay difference for employee number {} is:".format(employee_number), difference)
