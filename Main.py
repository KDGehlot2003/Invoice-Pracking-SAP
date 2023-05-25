from pdf2image import convert_from_path
import easyocr
import re
# import pytesseract

global scanned_text
global result


images = convert_from_path('test.pdf',dpi=300)


for i in range(len(images)):

    images[i].save('page'+ str(i) +'.jpg', 'JPEG')

len_of_image = len(images)



reader = easyocr.Reader(['en'], gpu=False) 
result = reader.readtext('page0.jpg', detail=0)

with open('converted.txt',mode ='w') as file:
    file.write("converted.txt \n \n")


for i in result:
    with open('converted.txt',mode ='a') as file:
        file.write(i)
        file.write("\n")
        scanned_text = i
        print(scanned_text)


def extract_date_from_pdf():
    
    extracted_dates = []

    for i in result:
        date_pattern = r'\b\d{1,2}-[A-Za-z]{3}-\d{2}\b'   # Example date pattern: 1-may-22
        dates = re.findall(date_pattern, i)
        extracted_dates.extend(dates)
        # print(dates)
        # print(date_pattern)

    return extracted_dates

def extract_invoice_no_from_pdf():
    
    extracted_invoice_no = []

    for i in result:
        invoice_no_pattern = r'[A-Za-z]{2}\/\d{2}-\d{2}\/\d{3}'
        invoices = re.findall(invoice_no_pattern, i)
        extracted_invoice_no.extend(invoices)

    return extracted_invoice_no


dates = extract_date_from_pdf()
for date in dates:
    print("date: ",date)


invoices = extract_invoice_no_from_pdf()
for invoice in invoices:
    print("Invoice No.", invoice)

