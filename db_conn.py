import streamlit as st
import pandas as pd
import mysql.connector


# Set up MySQL connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="LeakTimeBike4242",
  database="globalhris"
)

# Define function to insert data into MySQL table
def insert_data(table_name, data):
    cursor = mydb.cursor()
    cols = "`,`".join([str(i) for i in data.columns.tolist()])
    for i,row in data.iterrows():
        sql = "INSERT INTO " + table_name + " (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
        cursor.execute(sql, tuple(row))
        mydb.commit()

# Streamlit app
st.title("Upload CSV to MySQL")

# Get user input
file = st.file_uploader("Choose a CSV file", type="csv")
table_name = st.text_input("Enter table name")

# Process file and insert data into MySQL
if file is not None:
    data = pd.read_csv(file)
    st.write(data)
    if st.button("Insert into MySQL"):
        insert_data(table_name, data)
        st.success("Data inserted into MySQL!")
