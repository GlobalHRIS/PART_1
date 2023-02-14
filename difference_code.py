#Importing Libraries
import streamlit as st
import pandas as pd

# Streamlit Dashboard          
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Net Pay Difference Calculator")


# Uploading the input file

st.write("Please upload a csv file")
uploaded_file = st.file_uploader("Choose a csv file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    column1 = st.selectbox("Select the first month", df.columns)
    column2 = st.selectbox("Select the second month", df.columns)
    new_column_name = st.text_input("Enter the name of the new column", "Net Pay Difference")
    df[new_column_name] = df[column1] - df[column2]
    #st.write("Net Pay Difference of all the Employees")
    #st.write(df)
    emp_number = st.text_input("Enter the employee number:")
    for row in df:
        if emp_number:
                 empdata = df[df['Employee Number'] == int(emp_number)]
                 st.write("The net pay difference for employee number {} is:".format(emp_number))
                 st.write(empdata)   
                 break
                    
   
     

       
          
