import streamlit as st
import csv

def calculate_difference(employee_number):
    # Open the CSV file containing employee data
    with open('netpaydata.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        # Loop through each row in the CSV file
        for row in reader:
            if row['Employee_number'] == int(employee_number):
                current_month_salary = int(row['Current Month Salary'])
                previous_month_salary = int(row['Previous Month Salary'])
                break
        else:
            # If employee number is not found in the CSV file
            st.write("Employee number not found in the CSV file.")
            return
        
    # Calculate the difference
    difference = current_month_salary - previous_month_salary
    
    # Display the result
    st.write("The net pay difference for employee number {} is:".format(employee_number), difference)

# Get the employee number from the user
employee_number = st.number_input("Enter the employee number:")

# Call the calculate_difference function
calculate_difference(employee_number)
