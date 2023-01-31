

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

    file_name = "March_Data.csv"
    df = read_data(file_name)
    #file_name = "Feb_Data.csv"
    #df2 = read_data(file_name)

    emp_number = st.text_input("Enter Employee Number")
    if emp_number:
        March_emp_data = df[df['Employee Number'] == int(emp_number)]
        st.write(March_emp_data)
     #else:
        #st.write("Employee details not found in this month")
    #emp_number = st.text_input("Enter Employee Number")
    #if emp_number:
        #Feb_emp_data = df[df2['Employee Number'] == int(emp_number)]
        #st.write(emp_data)
        #else 
        #st.write("Employee details not found in this month")    

if __name__ == '__main__':
    main()
