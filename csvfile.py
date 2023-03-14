
import streamlit as st
import streamlit.components.v1 as stc

# File Processing Pkgs
import pandas as pd
import docx2txt
from PIL import Image 
from PyPDF2 import PdfFileReader
import pdfplumber

# pdf to text file
import pdf2image
import pytesseract
from pytesseract import Output, TesseractError
from functions import convert_pdf_to_txt_pages, convert_pdf_to_txt_file, save_pages, displayPDF, images_to_txt


def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()
	return all_page_text

def read_pdf2(file):
	with pdfplumber.open(file) as pdf:
	    page = pdf.pages[0]
	    return page.extract_text()


@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 
	
			
def main():
	
	# Streamlit Dashboard          
	st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
	st.image("logo.png", width = 400)
	st.title("Global HR Implementation Services Limited")
	menu = ["About Us","Upload Payslip","AI Net Pay Difference Finder", "AI Decision Tool"]
	choice = st.sidebar.selectbox("Menu",menu)


				                   				
	if choice == "Upload Payslip":
		st.subheader("Upload your payslip")
		docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])
		if st.button("Process"):
			if docx_file is not None:
				file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
				st.write(file_details)
				# Check File Type
				if docx_file.type == "text/plain":
					st.text(str(docx_file.read(),"utf-8")) # empty
					raw_text = str(docx_file.read(),"utf-8") # works with st.text and st.write,used for further processing
					st.write(raw_text) # works
				elif docx_file.type == "application/pdf":		
					html_temp = """
                                <div style="background-color:{};padding:1px">
            
                                </div>
                                """

                    st.markdown("""
                                ## Text data extractor: PDF to Text
    
                              """)
                    languages = {
                                'English': 'eng',
                                'French': 'fra',
                                'Arabic': 'ara',
                                'Spanish': 'spa',
                               }		
                    with st.sidebar:
                        st.title(":outbox_tray: PDF to Text")
                        textOutput = st.selectbox(
                            "How do you want your output text?",
                            ('One text file (.txt)', 'Text file per page (ZIP)'))
                        ocr_box = st.checkbox('Enable OCR (scanned document)')
    
                    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
                    st.markdown("""
                        # How does it work?
                                Simply load your PDF and convert it to single-page or multi-page text.
                            """)
                    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
      
                    pdf_file = st.file_uploader("Load your Payslip", type="pdf")
                    hide="""
                        <style>
                        footer{
                            visibility: hidden;
                                position: relative;
                        }
                        .viewerBadge_container__1QSob{
                            visibility: hidden;
                        }
                        #MainMenu{
                            visibility: hidden;
                        }
                        <style>
                        """
                        st.markdown(hide, unsafe_allow_html=True)
                        if pdf_file:
                            path = pdf_file.read()
                            # display document
                            with st.expander("Display document"):
                                displayPDF(path)
                            if ocr_box:
                                option = st.selectbox('Select the document language', list(languages.keys()))
                            # pdf to text
                            if textOutput == 'One text file (.txt)':
                                if ocr_box:
                                    texts, nbPages = images_to_txt(path, languages[option])
                                    totalPages = "Pages: "+str(nbPages)+" in total"
                                    text_data_f = "\n\n".join(texts)
                                else:
                                    text_data_f, nbPages = convert_pdf_to_txt_file(pdf_file)
                                    totalPages = "Pages: "+str(nbPages)+" in total"

                                st.info(totalPages)
                                st.download_button("Download txt file", text_data_f)
                            else:
                                if ocr_box:
                                    text_data, nbPages = images_to_txt(path, languages[option])
                                    totalPages = "Pages: "+str(nbPages)+" in total"
                                else:
                                    text_data, nbPages = convert_pdf_to_txt_pages(pdf_file)
                                    totalPages = "Pages: "+str(nbPages)+" in total"
                                st.info(totalPages)
                                zipPath = save_pages(text_data)
                                # download text data   
                                with open(zipPath, "rb") as fp:
                                    btn = st.download_button(
                                        label="Download ZIP (txt)",
                                        data=fp,
                                        file_name="pdf_to_txt.zip",
                                        mime="application/zip"
                                    )

                            st.markdown('''
                            <a target="_blank" style="color: black" href="https://twitter.com/intent/tweet?text=You%20can%20extract%20text%20from%20your%20PDF%20using%20this%20PDF%20to%20Text%20streamlit%20app%20by%20@nainia_ayoub!%0A%0Ahttps://nainiayoub-pdf-text-data-extractor-app-p6hy0z.streamlit.app/">
                                <button class="btn">
                                    Spread the word!
                                </button>
                            </a>
                            <style>
                            .btn{
                                display: inline-flex;
                                -moz-box-align: center;
                                align-items: center;
                                -moz-box-pack: center;
                                justify-content: center;
                                font-weight: 400;
                                padding: 0.25rem 0.75rem;
                                border-radius: 0.25rem;
                                margin: 0px;
                                line-height: 1.6;
                                color: rgb(49, 51, 63);
                                background-color: #fff;
                                width: auto;
                                user-select: none;
                                border: 1px solid rgba(49, 51, 63, 0.2);
                                }
                            .btn:hover{
                                color: #00acee;
                                background-color: #fff;
                                border: 1px solid #00acee;
                            }
                            </style>
                            ''',
                            unsafe_allow_html=True
                                       )

				elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
				# Use the right file processor ( Docx,Docx2Text,etc)
					raw_text = docx2txt.process(docx_file) # Parse in the uploadFile Class 
					st.write(raw_text)
					
	elif choice == "AI Net Pay Difference Finder":
		st.subheader("AI Net Pay Difference Finder")
		file = st.file_uploader("Upload File",type=["csv"])
		if file is not None:
			df = pd.read_csv(file, usecols =["Employee Number", "Forename","Surname",
							 "Net Pay Jan","Net Pay Feb","Net Pay March","Net Pay April","Net Pay May","Net Pay June","Net Pay Change last 6 Months"])	
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
					break
					
	elif choice =="AI Decision Tool":
		st.subheader("AI Solution Provider")
		file = st.file_uploader("Upload File",type=["csv"])
		if file is not None:
			df = pd.read_csv(file, usecols=["Employee Number", "Net Pay Change last 6 Months", "AI Decision","AI Solution_1(Based on Net Pay)"])
			emp_number = st.text_input("Enter the employee number:")
			for row in df:
				if emp_number:
					empdata = df[df['Employee Number'] == int(emp_number)]
					st.write("The net pay difference for employee number {} is:".format(emp_number))
					st.write(empdata)
					break
					
							
	else:
		st.subheader("About Us")
		st.info("Global HR Implementataion Sevices Ltd")
		st.text("Here at Global HRIS, we specialise in global payroll implementation services. \nFrom data migration services to payroll project management. \nWe support clients on their digital transformation journey.")
		st.info("+44 161 317 2903")
		st.info("info@globalhris.co.uk")
		st.info("International House, 61 Mosley Street, Manchester, M2 3HZ")
		

if __name__ == '__main__':
	main()         
    
		 
