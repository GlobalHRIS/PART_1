import streamlit as st
import pandas as pd

import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='root',  
                        password='LeakTimeBike4242')
    if conn.is_connected():        
        # Execute query
        sql = "SELECT * FROM globalhris.Feb_Data"
        cursor.execute(sql)
        # Fetch all the records
        result = cursor.fetchall()
        for i in result:
            print(i)
 
    
@st.cache
def read_data(file_name):
    df = pd.read_csv(file_name)
    return df
# Streamklit User Interface part
st.set_page_config(page_title="GlobalHRIS", page_icon=":guardsman:", layout="wide")
st.image("logo.png", width=400)
st.title("Global HR Implementation Services Limited \n Employee Data Search")
emp_number = st.text_input("Enter Employee Number")

def calculate_change(previous_net_pay, current_net_pay):
    return current_net_pay - previous_net_pay

# Load the employee data from two CSV files
employee_data_1 = pd.read_csv('Feb_Data.csv')
employee_data_2 = pd.read_csv('March_Data.csv')


# Combine the two dataframes into one
employee_data = pd.concat([employee_data_1, employee_data_2], ignore_index=True)
if emp_number:
    # Calculate the net pay for each month
    employee_data['Net Pay'] = employee_data.apply(lambda row: calculate_net_pay(row['Salary'], row['Deductions']), axis=1)

    # Calculate the change in net pay between each month
    employee_data['Change in Net Pay'] = employee_data['Net Pay'].diff()

    # Display the updated dataframe
    st.write(employee_data)

# Reading the February employee data  
#df1 = read_data("Feb_Data.csv")
#if emp_number:
    #Feb_emp_data = df1[df1['Employee Number'] == int(emp_number)]
   # st.write(Feb_emp_data)
# Reading the March employee data
#df2 = read_data("March_Data.csv")
#if emp_number:
    #Mar_emp_data = df2[df2['Employee Number'] == int(emp_number)]
    #st.write(Mar_emp_data)
   

