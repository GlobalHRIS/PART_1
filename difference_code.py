import streamlit as st
import pandas as pd

st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Net Pay Difference Calculator")
emp_number = st.text_input("Enter Employee Number")

# Load the employee data from a CSV file into a Pandas DataFrame
df = pd.read_csv('netpaydata.csv')

for row in df:
    if df['Employee_number'] == int(emp_number):
        Net_Pay_difference = df['Net Pay March'] - df['Net Pay Feb']
        st.write(Net_Pay_difference)
