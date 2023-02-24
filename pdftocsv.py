import streamlit as st
import tabula
import pandas as pd

# Set page title
st.set_page_config(page_title="PDF to CSV Converter")

# Set page header
st.header("PDF to CSV Converter")

# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])


# Check if file is uploaded
if pdf_file is not None:
    # Read PDF file and extract tables using tabula-py
    df = tabula.read_pdf(pdf_file)

    # Concatenate all tables into a single dataframe
    df_concat = pd.concat(df)

    # Save the dataframe as a CSV file
    csv_file = df_concat.to_csv(index=False)

    # Display the CSV file as a download link
    st.download_button("Download CSV", data=csv_file, file_name="output.csv")
