import streamlit as st
import pandas as pd
@st.cache
def read_data(file_name):
    df = pd.read_csv(file_name)
    return df

# Reading the employee data 
df1 = pd.read_csv('Feb_Data.csv')
#usecols = ['Employee Number','First Name','Last Name','Net Pay'])
df2 = pd.read_csv('March_Data.csv)
                  #usecols = ['Employee Number','First Name','Last Name','Net Pay'])

# Streamlit User Interface part
st.set_page_config(page_title="GlobalHRIS", page_icon=":guardsman:", layout="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Employee Data Search")
emp_number = st.text_input("Enter Employee Number") 


#df = pd.concat(map(pd.read_csv, ['Feb_Data.csv','March_Data.csv']))
# Condition checking              
if emp_number:
    feb_emp_data = df1[df1['Employee Number'] == int(emp_number)]
    Mar_emp_data = df2[df2['Employee Number'] == int(emp_number)]
    st.title("The Employee data for february")
    st.write(feb_emp_data)
    st.title("The Employee data for March")
    st.write(Mar_emp_data)
    
    #netpay_differnce = df1-df2
    #st.write('netpay differnce of the employee is:'netpay_differnce )
   

