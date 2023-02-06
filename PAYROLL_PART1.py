import streamlit as st
import pandas as pd

@st.cache
def read_data(file_name):
    df = pd.read_csv(file_name)
    return df
    
# Streamlit User Interface part
st.set_page_config(page_title="GlobalHRIS", page_icon=":guardsman:", layout="wide")
st.image("logo.png", width=400)
st.title("Global HR Implementation Services Limited \n Employee Data Search")
emp_number = st.text_input("Enter Employee Number")
# Reading the February employee data  
df1 = read_data("Feb_Data.csv")
if emp_number:
    Feb_emp_data = df1[df1['Employee Number'] == int(emp_number)]
    st.write(Feb_emp_data)
# Reading the March employee data
df2 = read_data("March_Data.csv")
if emp_number:
    Mar_emp_data = df2[df2['Employee Number'] == int(emp_number)]
    st.write(Mar_emp_data)
   

