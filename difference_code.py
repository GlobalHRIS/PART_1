import streamlit as st
import pandas as pd
import numpy as np
          
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Net Pay Difference Calculator")
emp_number = st.text_input("Enter Employee Number")    

# Load the employee data from a CSV file into a Pandas DataFrame
df = pd.read_csv('netpay_data.csv')
for row in df:
     if df[row['Employee Number'] == int(emp_number)]:
             current_month_salary = int(row['Net intPay Feb'])
             previous_month_salary = int(row['Net Pay March'])
             difference = current_month_salary - previous_month_salary
             st.write("The net pay difference for employee number {} is:".format(emp_number), difference)
             break
     
        
   
                    
                    
                    
                    
          
                    
                    
                    
                    
           #netpay = df[df['Employee Number'] == int(emp_number)]
           #st.write("Employee Data Found")
           #st.write(netpay)
           #netpay_diff = df['Netpay_Diff']
           #st.write(netpay_diff)
           
       
          
