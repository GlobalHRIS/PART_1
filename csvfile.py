import streamlit as st
import PyPDF2
import pandas as pd

def pdf_to_csv(file):
    # Read the PDF file
    pdf_reader = PyPDF2.PdfFileReader(file)

    # Extract all the pages of the PDF file
    pages = []
    for i in range(pdf_reader.getNumPages()):
        pages.append(pdf_reader.getPage(i).extractText())

    # Convert the text to a pandas DataFrame
    df = pd.DataFrame(pages, columns=['text'])

    # Split the text into rows and columns
    df = df['text'].str.split('\n', expand=True)

    return df

st.title("PDF to CSV Converter")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Convert the PDF file to a CSV file
    df = pdf_to_csv(uploaded_file)

    # Download link for the CSV file
    csv_file = df.to_csv(index=False)
    st.download_button(
        label="Download CSV file",
        data=csv_file,
        file_name="converted_file.csv",
        mime="text/csv"
    )

    # Show the DataFrame
    st.write(df)
