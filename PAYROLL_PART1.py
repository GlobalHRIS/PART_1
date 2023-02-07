import streamlit as st
import pandas as pd

@st.cache
def read_data(file_name):
    df = pd.read_csv(file_name)
    return df

# Reading the employee data 
#df1 = pd.read_csv('Feb_Data.csv', usecols = ['Employee Number', 'Forename', 'Surname', 'Net Pay'])
#df2 = pd.read_csv('March_Data.csv',usecols = ['Employee Number', 'Forename', 'Surname', 'Net Pay'])

# Streamlit User Interface part
st.set_page_config(page_title="GlobalHRIS", page_icon=":guardsman:", layout="wide")
st.image("logo.png", width=400)
st.title("Global HR Implementation Services Limited \n Employee Data Search")
emp_number = st.text_input("Enter Employee Number") 

df = pd.merge(map(pd.read_csv, ['Feb_Data.csv','March_Data.csv']))
              
if emp_number:
    emp_data = df[df['Employee Number'] == int(emp_number)]
    st.write(emp_data)
    
    
    
    #netpay_differnce = df1-df2
    #st.write(netpay_differnce)
   

