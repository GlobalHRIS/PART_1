import streamlit as st
import pandas as pd
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="LeakTimeBike4242",
    database="globalhris"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Streamlit interface to upload the CSV file
st.title("Upload a CSV file to MySQL")
file = st.file_uploader("Choose a CSV file", type="csv", accept_multiple_files=False)

if file is not None:
    # Read the contents of the CSV file into a Pandas DataFrame
    df = pd.read_csv(file)

    # Create a MySQL table with the same column names as the DataFrame
    columns = ", ".join(df.columns)
    cursor.execute(f"CREATE TABLE IF NOT EXISTS my_table ({columns})")

    # Insert the rows of the DataFrame into the MySQL table
    for i, row in df.iterrows():
        values = tuple(row)
        placeholders = ", ".join(["%s"] * len(row))
        query = f"INSERT INTO my_table ({columns}) VALUES ({placeholders})"
        cursor.execute(query, values)

    # Commit the changes to the MySQL database
    db.commit()

    st.write("CSV file uploaded and loaded into MySQL database!")
