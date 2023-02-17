import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

# Function to establish a connection with the MySQL database
def create_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='LeakTimeBike4242',
            database='globalhris'
        )
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn

    except Error as e:
        print(e)

# Streamlit app
def app():
    st.title("Load data into MySQL database")

    # Create file uploader
    uploaded_file = st.file_uploader("Choose a CSV file to upload", type="csv")

    if uploaded_file is not None:
        # Read uploaded CSV file
        df = pd.read_csv(uploaded_file)

        # Create connection to MySQL database
        conn = create_connection()
        cursor = conn.cursor()

        # Loop through each row in the DataFrame and insert into MySQL database
        for i, row in df.iterrows():
            insert_query = "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)"
            values = (row['column1'], row['column2'], row['column3'])
            cursor.execute(insert_query, values)
            conn.commit()

        st.write("Data loaded successfully into MySQL database")

if __name__ == '__main__':
    app()
