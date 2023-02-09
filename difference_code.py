

import streamlit as st
import pandas as pd

# Streamlit User Interface part
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Employee Data Search")


df1 =  pd.read_csv('netpaydata.csv')
emp_number = st.text_input("Enter Employee Number")

# Condition checking  
            
if emp_number:
     df1['diff_value']= df1['Net pay Feb'] - df1['Net pay March']
     st.write(diff_value)
 


 
