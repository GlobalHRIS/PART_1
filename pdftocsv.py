import streamlit as st
import tabula
import pandas as pd

# Set page title
st.set_page_config(page_title="PDF to CSV Converter")

# Define function to convert PDF to CSV
def convert_pdf_to_csv(pdf_file):
    # Use tabula to read table data from PDF
    df = tabula.read_pdf(pdf_file, pages='all')
    # Concatenate tables if multiple tables in one page
    df = pd.concat(df)
    # Convert dataframe to CSV format
    csv = df.to_csv(index=False)
    return csv

# Define Streamlit app
def app():
    # Set app title
    st.title("PDF to CSV Converter")

    # Upload PDF file
    st.header("Upload PDF file")
    pdf_file = st.file_uploader("Choose a PDF file", type="pdf")

    # Convert PDF to CSV and download CSV file
    if pdf_file is not None:
        st.header("Convert to CSV and download")
        csv = convert_pdf_to_csv(pdf_file)
        st.download_button(label="Download CSV", data=csv, file_name="converted.csv", mime="text/csv")

# Run Streamlit app
if __name__ == "__main__":
    app()
