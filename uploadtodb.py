import streamlit as st
import pandas as pd
import mysql.connector

# Function to create a MySQL connection
def create_connection(host_name, user_name, user_password, db_name):
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")

    return conn

# Function to create a MySQL table
def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Table created successfully")
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")

# Function to insert data into MySQL table
def insert_data(conn, insert_data_sql, data):
    try:
        cursor = conn.cursor()
        cursor.executemany(insert_data_sql, data)
        conn.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")

# MySQL connection details
host = 'localhost'
user = 'root'
password = 'password'
database = 'database_name'

# Create a MySQL connection
conn = create_connection(localhost, root, LeakTimeBike4242, globalhris)

# Create a Streamlit file uploader
st.set_option('deprecation.showfileUploaderEncoding', False)
file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(file)

    # Create a MySQL table with the same column names as the CSV file
    table_name = 'table_name'
    columns = ', '.join(list(df.columns))
    create_table_sql = f"CREATE TABLE {table_name} ({columns})"
    create_table(conn, create_table_sql)

    # Insert data into MySQL table
    insert_data_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({', '.join(['%s']*len(df.columns))})"
    data = [tuple(row) for row in df.values.tolist()]
    insert_data(conn, insert_data_sql, data)

    st.success("Data successfully uploaded to MySQL database")
