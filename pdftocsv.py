import streamlit as st
import PyPDF2
import csv

def extract_text(pdf_file):
    with pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        text = []
        for page in range(read_pdf.getNumPages()):
            page_obj = read_pdf.getPage(page)
            text.append(page_obj.extractText())
        return '\n'.join(text)

def convert_to_csv(pdf_file):
    text = extract_text(pdf_file)
    csv_data = [line.split(",") for line in text.split("\n")]
    with open("output.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for row in csv_data:
            writer.writerow(row)

st.title("PDF to CSV Converter")
st.write("Upload a PDF file to convert to CSV.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    convert_to_csv(uploaded_file)
    st.download_button(label="Download CSV", data="output.csv", file_name="output.csv")
