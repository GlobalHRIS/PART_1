import streamlit as st
import PyPDF2
import pandas as pd

# Define Streamlit app title
st.title("PDF to CSV Converter")

# Create file uploader widget
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Define function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(page).extractText()
    return text

# If file is uploaded, extract text and save as CSV
if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    df = pd.DataFrame({"Text": [text]})
    st.write("Extracted Text:")
    st.write(df)
    csv_file = st.text_input("Enter CSV filename:")
    if csv_file:
        df.to_csv(csv_file, index=False)
        st.success(f"CSV file saved as {csv_file}.")
