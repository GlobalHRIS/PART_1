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
     if emp_number:
           netpay = df[df['Employee Number'] == int(emp_number)]
           st.write("Employee Data Found")
           st.write(netpay)
         
           netpay_diff = df[df['Netpay_Diff']]
           st.write(netpay_diff)
  
          #netpay = df[df['Employee Number'] == int(emp_number)]
      
        
        #df['netpaydiff'] = df.apply(lambda x: diff(x['Net Pay March'], x['Net Pay Feb']), axis=1)
          #current_month_netpay = int(df['Net Pay March'])
          #st.write(current_month_netpay)
          #previous_month_netpay = int(df['Net Pay Feb'])
          #st.write(previous_month_netpay)
          # Calculate the difference
          #netpaydiff = current_month_netpay - previous_month_netpay
          # Display the result
          
