import streamlit as st
import pandas as pd
import numpy as np
          
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Net Pay Difference Calculator")
emp_number = st.text_input("Enter Employee Number")    


import streamlit as st
import pandas as pd

st.write("Please upload a csv file to perform the operation")
uploaded_file = st.file_uploader("Choose a csv file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Original DataFrame")
    st.write(df)
column1 = st.selectbox("Select the current month netpay", df.columns)
column2 = st.selectbox("Select the previous month netpay", df.columns)
    
new_column_name = st.text_input("Enter the name of the new column", "netpaydifference")
    
for row in df
        if emp_number:
                empdata = df[df['Employee Number'] == int(emp_number)]
                df[netpaydifference] = df[Net Pay March] - df[Net Pay Feb]
                st.write("Resultant DataFrame")
                st.write(df)

# Load the employee data from a CSV file into a Pandas DataFrame
#df = pd.read_csv('netpay_data.csv')
#for row in df:
          #if emp_number:
                    #empdata = df[df['Employee Number'] == int(emp_number)]
                    #st.write(empdata)
                    #current_month_salary = df['Net Pay Feb']
                    #previous_month_salary = df['Net Pay March']
                    #difference = current_month_salary.sub(previous_month_salary)
                    #st.write("The net pay difference for employee number {} is:".format(emp_number), difference)
                    #break
     

       
          
