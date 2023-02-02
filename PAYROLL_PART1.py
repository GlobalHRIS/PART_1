

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
    emp_number = st.text_input("Enter Employee Number")
   
    df1 = read_data("Feb_Data.csv")
  
    if emp_number:
        Feb_emp_data = df1[df1['Employee Number'] == int(emp_number)]
        st.write(Feb_emp_data)
   
      
if __name__ == '__main__':
    main()
