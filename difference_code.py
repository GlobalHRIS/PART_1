import streamlit as st
import pandas as pd

def calculate_difference():
    # Load the employee data from a CSV file into a Pandas DataFrame
    df = pd.read_csv('netpaydata.csv')
    
    # Calculate the net pay difference between February and March
    df['Net Pay Difference'] = df['Net Pay March'] - df['Net Pay Feb']
    
    # Display the result
    st.write("Net pay difference between February and March:")
    st.write(df)

# Call the calculate_difference function
calculate_difference()
