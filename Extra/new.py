import pytesseract
from pdf2image import convert_from_path
import re

def extract_data_from_scanned_pdf(pdf_path):
    extracted_data = []

    # Convert scanned PDF to images
    images = convert_from_path(pdf_path, dpi=300)

    for image in images:
        # Perform OCR on each image
        text = pytesseract.image_to_string(image, lang='eng')
        extracted_data.append(text)

    return extracted_data

# Provide the path to your scanned PDF file
pdf_path = 'test.pdf'
data = extract_data_from_scanned_pdf(pdf_path)
# print(data)
# Print the extracted data
# for item in data:
    # print(item)
#     text = item

def extract_dates_from_scanned_pdf(pdf_path):
    extracted_dates = []

    # Convert scanned PDF to images
    images = convert_from_path(pdf_path, dpi=300)

    for image in images:
        # Perform OCR on each image
        ocr_text = pytesseract.image_to_string(image, lang='eng')
        print("-----------------------------------------------------------------")
        print(ocr_text)
        print("-----------------------------------------------------------------")
        try:
            # Extract dates using regular expressions
            date_pattern = r'\b\d{1,2}-[A-Za-z]{3}-\d{2}\b'   # Example date pattern: 1-may-22
            dates = re.findall(date_pattern, ocr_text)
            extracted_dates.extend(dates)
            # print(date_pattern)
            # print(dates)
        except:
            print("Date Error")
        

    return extracted_dates

dates = extract_dates_from_scanned_pdf(pdf_path)
for date in dates:
    print(date)

def extract_invoice_from_scanned_pdf(pdf_path):
    extracted_invoice = []

    # Convert scanned PDF to images
    images = convert_from_path(pdf_path, dpi=300)

    for image in images:
        # Perform OCR on each image
        ocr_text = pytesseract.image_to_string(image, lang='eng')
        try:
            # Extract dates using regular expressions
            # invoice_pattern = r'[A-Za-z]{2}\/\d{4}-\d{2}\/\d{4}' or r'\$[\d.]+\/\d{4}-\d{2}\/\d{4}\/\d{4}'  or r'\$[\d.]+/\d{4}/\d{2}/\d{4}' 
            invoice_pattern = r'[A-Za-z]{2}\/\d{2}-\d{2}\/\d{3}' or r'\$[\d.]+\/\d{2}-\d{2}\/\d{2}\/\d{3}'  or r'\$[\d.]+/\d{2}/\d{2}/\d{3}' 
            dates = re.findall(invoice_pattern, ocr_text)
            extracted_invoice.extend(dates)
        except:
            print("invoice Error")
        

    return extracted_invoice

invoice = extract_invoice_from_scanned_pdf(pdf_path)
for i in invoice:
    print(i)


# try:
#     invoice_number = re.search(r'Invoice No.\s*\n(.+?)\s*\n', text).group(1).strip() or re.search(r'Invoice Number\s*\n(.+?)\s*\n', text).group(1).strip()

#     invoice_date = re.search(r'Dated\s*\n(.+?)\s*\n', text).group(1).strip() or re.search(r'Date\s*\n(.+?)\s*\n', text).group(1).strip()

#     Total = re.search(r'Total\s*\n\S*\n(.+?)\s*\n', text).group(1).strip()  

#     services = re.search(r'Services\s*\n\S*\n(.+?)\s*\n', text).group(1).strip()
# except:
#     print('stop')


# print("Reference :", invoice_number)
# print("Invoice Date :", invoice_date)
# print("Total amount :", Total)
# print("Service :", services)

