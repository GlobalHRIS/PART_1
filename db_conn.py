import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# Define database connection string
db_connection_string = "mysql+pymysql://username:password@host:port/database_name"

# Define table name and column names
table_name = "netpay_table"
#column_names = ["col1", "col2", "col3"]

# Streamlit app
def main():
    st.title("Upload data to MySQL database")
    
    # Upload CSV file
    file = st.file_uploader("Choose a CSV file")
    if file is not None:
        df = pd.read_csv(file)
        st.write("Preview of data:")
        st.write(df.head())
        
        # Connect to database
        engine = create_engine(db_connection_string)
        
        # Insert data into database
        df.to_sql(table_name, con=engine, if_exists="append", index=False)
        st.write("Data uploaded to database.")

if __name__ == "__main__":
    main()
