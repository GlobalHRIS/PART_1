import streamlit as st
import pandas as pd
import mysql.connector

# Create a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="LeakTimeBike4242",
    database="globalhris"
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Define a function to upload the CSV file and load the data into MySQL
def upload_csv_to_mysql(file):
    # Load the CSV file into a pandas dataframe
    df = pd.read_csv(file)

    # Create a table in MySQL with the same columns as the CSV file
    table_name = "my_table"
    cols = ",".join(df.columns)
    create_table_query = f"CREATE TABLE {table_name} ({cols})"
    cursor.execute(create_table_query)
    conn.commit()

    # Load the data from the dataframe into MySQL
    for i, row in df.iterrows():
        values = "','".join(str(x) for x in row)
        insert_query = f"INSERT INTO {table_name} ({cols}) VALUES ('{values}')"
        cursor.execute(insert_query)
        conn.commit()

# Create the Streamlit app
def main():
    st.title("Upload CSV and load data into MySQL")

    # Create a file uploader and get the uploaded file
    file = st.file_uploader("Upload CSV", type=["csv"])

    # If a file is uploaded, load it into MySQL
    if file is not None:
        upload_csv_to_mysql(file)
        st.success("CSV uploaded and data loaded into MySQL")

if __name__ == "__main__":
    main()
