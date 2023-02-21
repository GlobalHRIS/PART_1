import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

     
# Create a function to load the data into a database
def load_data_to_database(dataframe, db_name, table_name):
     # Create a connection to the database
     engine = create_engine(f'sqlite:///globalhris.db', echo=True)
     # Write the data to the database
     dataframe.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Create a Streamlit app
def main():
    # Set the title and the header
    # Streamlit Dashboard          
    st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
    st.image("logo.png", width = 400)
    st.title("Global HR Implementation Services Limited")
    st.title('Data Upload and Database Load')
    st.header('Upload your data and load it into a database')

    # Create a file uploader
    uploaded_file = st.file_uploader('Choose a CSV file', type=['csv'])

    # If a file was uploaded
    if uploaded_file is not None:
        # Read the file into a DataFrame
        df = pd.read_csv(uploaded_file)
        # Show the DataFrame in the app
        st.write('Original Data', df)
        month1 = st.selectbox("Select the first month", df.columns)
        month2 = st.selectbox("Select the second month", df.columns) 
        Net_Pay_Diff = st.text_input("Enter the name of the new column", "Net Pay Difference")
        df[Net_Pay_Diff] = df[month1] - df[month2]
	#st.write("Net Pay Difference of all the Employees")
	#st.write(df)
	emp_number = st.text_input("Enter the employee number:")
	for row in df:
		if emp_number:
			empdata = df[df['Employee Number'] == int(emp_number)]
			st.write("The net pay difference for employee number {} is:".format(emp_number))
			st.write(empdata)
			
        
        # Get the name of the database and table
        db_name = st.text_input('Database name', 'my_database')
        table_name = st.text_input('Table name', 'my_table')
        # If the user entered a name for the database and table
        if db_name and table_name:
            # Load the data into the database
            load_data_to_database(df, db_name, table_name)
            st.write('Data loaded into database')
        else:
            st.write('Please enter a database name and table name')
    else:
        st.write('Please upload a CSV file')
    
if __name__ == '__main__':
    main()
