

import streamlit as st
import pandas as pd

@st.cache
def read_data(file_name):
    df = pd.read_csv(file_name)
    return df

def main():
    st.set_page_config(page_title="GlobalHRIS", page_icon=":guardsman:", layout="wide")
    st.image("logo.png", width=400)
    st.title("Global HR Implementation Services Limited \n Employee Data Search")

    file_name = "Feb_Data.csv"
    df1 = read_data(file_name)
    file_name = "March_Data.csv"
    df2 = read_data(file_name)

    emp_number = st.text_input("Enter Employee Number")
    if emp_number:
        Feb_emp_data = df1[df1['Employee Number'] == int(emp_number)]
        st.write(Feb_emp_data)
    if emp_number:
        Mar_emp_data = df2[df2['Employee Number'] == int(emp_number)]
        st.write(Mar_emp_data) 
        #elif:
        #st.write("Employee details not found in this month")
        
    #emp_number = st.text_input("Enter Employee Number")
  
        #else 
        #st.write("Employee details not found in this month")    

if __name__ == '__main__':
    main()
