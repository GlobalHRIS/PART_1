

import streamlit as st
import pandas as pd

# Streamlit User Interface part
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Employee Data Search")


df1 =  pd.read_csv('netpaydata.csv')

print(df1.head(n=5))



emp_number = input("Enter Employee Number")

# Condition checking  
            
for emp_number in df1:
  if(df1['Employee_Number'] == emp_number):
      df1['diff_value']= df1['Net pay Feb'] - df1['Net pay March']
      print(diff_value)
 


 
