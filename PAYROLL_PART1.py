import streamlit as st
import pandas as pd

@st.cache
def read_data(file_name):
    df = pd.read_csv(file_name)
    return df

def main():
    st.title("Employee Data Search")

    file_name = "AI_March_Data.csv"
    df = read_data(file_name)

    emp_number = st.text_input("Enter Employee Number")
    if emp_number:
        emp_data = df[df['Employee Number'] == int(emp_number)]
        st.write(emp_data)

if __name__ == '__main__':
    main()
