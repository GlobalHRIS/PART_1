import csv
import streamlit as st

@st.cache
def load_data(AI_March_Data):
    data = []
    with open('AI_March_Data.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            data.append(dict(zip(header, row)))
    return data

def search_employee(employee_id, data):
    for employee in data:
        if employee['Employee ID'] == employee_id:
            return employee
    return None

data = load_data('employee_data.csv')

st.title('Employee Data Search')
employee_id = st.text_input('Enter Employee ID:')

employee = search_employee(employee number, data)
if employee:
    st.write(employee)
else:
    st.write('Employee not found')
