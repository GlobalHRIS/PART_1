import streamlit as st
import pandas as pd
import mysql.connector

# Create a connection to your MySQL database
cnx = mysql.connector.connect(user='root', password='LeakTimeBike4242',
                              host='localhost', database='globalhris')

# Define a function to create a table in your database and insert the data from a pandas dataframe
def create_table(df, table_name):
    cursor = cnx.cursor()
    columns = list(df.columns)
    col_types = []
    for column in columns:
        if pd.api.types.is_integer_dtype(df[column]):
            col_types.append(column + " INT")
        elif pd.api.types.is_float_dtype(df[column]):
            col_types.append(column + " FLOAT")
        else:
            col_types.append(column + " VARCHAR(255)")
    query = "CREATE TABLE {} ({})".format(table_name, ", ".join(col_types))
    cursor.execute(query)
    for i,row in df.iterrows():
        query = "INSERT INTO {} ({}) VALUES ({})".format(table_name, ", ".join(columns), ", ".join(["%s"]*len(columns)))
        cursor.execute(query, tuple(row))
    cnx.commit()

# Create a file uploader in Streamlit and define the function to handle the uploaded file
file = st.file_uploader("Upload a CSV file", type=["csv"])
if file is not None:
    # Load the uploaded file into a pandas dataframe
    df = pd.read_csv(file)
    # Get the table name from the user
    table_name = st.text_input("Enter the table name")
    # Create the table and insert the data into the database
    if st.button("Create Table and Insert Data"):
        create_table(df, table_name)
        st.success("Data inserted successfully!")
