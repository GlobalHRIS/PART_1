import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Create a function to load the data into a database
def load_data_to_database(dataframe, db_name, table_name):
    # Create a connection to the database
    engine = create_engine(f'sqlite:///{db_name}.db', echo=False)
    
    # Write the data to the database
    dataframe.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Create a Streamlit app
def main():
    # Set the title and the header
    st.title('Data Upload and Database Load')
    st.header('Upload your data and load it into a database')

    # Create a file uploader
    uploaded_file = st.file_uploader('Choose a CSV file', type=['csv'])

    # If a file was uploaded
    if uploaded_file is not None:
        # Read the file into a DataFrame
        data = pd.read_csv(uploaded_file)

        # Show the DataFrame in the app
        st.write('Original Data', data)

        # Get the name of the database and table
        db_name = st.text_input('Database name', 'my_database')
        table_name = st.text_input('Table name', 'my_table')

        # If the user entered a name for the database and table
        if db_name and table_name:
            # Load the data into the database
            load_data_to_database(data, db_name, table_name)
            st.write('Data loaded into database')
        else:
            st.write('Please enter a database name and table name')
    else:
        st.write('Please upload a CSV file')

if __name__ == '__main__':
    main()
