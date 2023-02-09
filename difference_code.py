import streamlit as st
import pandas as pd

# Streamlit User Interface part
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Net Pay Difference Calculator")

df1 =  pd.read_csv('netpaydata.csv')
emp_number = st.text_input("Enter Employee Number")



# Condition checking    
#ok = st.button("Calculate Netpay Difference")
if emp_number:
    #Calculate the Net Pay difference
    diff = df1['Net Pay Feb']- df1['Net pay March']
    st.write(diff)
    st.subheader(f"The netpay diffeernce is ${diff[0]:.2f}")


 
