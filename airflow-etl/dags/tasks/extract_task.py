import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def write_text_to_txt(text, txt_path):
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)




def extract(**context):
    
    dags = os.path.join(os.getcwd(), 'dags')
    res_path = os.path.join(dags, 'resources')
    pdf_path = os.path.join(res_path, "level1.pdf")
    txt_path = os.path.join(res_path, "level1.txt") 

    parsed_text = extract_text_from_pdf(pdf_path)
    write_text_to_txt(parsed_text, txt_path)
    return "level1.txt"
