import streamlit as st
import pandas as pd

st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n AI Employee Net Pay Difference Calculator")
emp_number = st.text_input("Enter Employee Number")

# Load the employee data from a CSV file into a Pandas DataFrame
df = pd.read_csv('netpaydata.csv')

if emp_number:
    df['Net Pay Difference'] = df['Net Pay March'] - df['Net Pay Feb']
    st.write(Netpay_Diff)
    
