from pdf2image import convert_from_path
import easyocr
import re
from datetime import datetime
import xlwt
from xlwt import Workbook
# import pytesseract

global scanned_text
global result


images = convert_from_path('test.pdf',dpi=300)


for i in range(len(images)):

    images[i].save('page'+ str(i) +'.jpg', 'JPEG')

len_of_image = len(images)



reader = easyocr.Reader(['en']) 
result = reader.readtext('page0.jpg', detail=0)

with open('converted.txt',mode ='w') as file:
    file.write("converted.txt \n \n")


for i in result:
    with open('converted.txt',mode ='a') as file:
        file.write(i)
        file.write("\n")
        scanned_text = i
        # print(scanned_text)


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
        invoice_no_pattern = r'[A-Za-z]{2}\/\d{2}-\d{2}\/\d{3}|[A-Za-z]{2}\/\d{4}-\d{2}\/\d{4}|\d{4}-\d{2}\/\d{4}|\d{4}-\d{2}\/\d{3}'
        invoices = re.findall(invoice_no_pattern, i)
        extracted_invoice_no.extend(invoices)

    return extracted_invoice_no

def extract_PO_no_from_pdf():
    
    extracted_PO_no = []

    for i in result:
        PO_no_pattern = r'^\d{10}$'
        POs = re.findall(PO_no_pattern, i)
        extracted_PO_no.extend(POs)

    return extracted_PO_no




dates = extract_date_from_pdf()
dt_lst = []
for i in dates:
    date_object = datetime.strptime(i, '%d-%b-%y').date()
    dt = date_object.strftime("%d.%m.%y")
    dt_lst.append(dt)
max_dt = max(dt_lst)
try:
    if max_dt!=None:
        print("date: ",max_dt)
    else:
        print("Date No. : CAN'T FIND THE VALUE ")
except:
    print("date error")


# for date in dates:
#     date_object = datetime.strptime(date, '%d-%b-%y').date()
#     dt = date_object.strftime("%d.%m.%y")
#     print("date: ",dt)

invoices = extract_invoice_no_from_pdf()
# for invoice in invoices:
try:
    if invoices!=None:
        print("Invoice No. :", invoices[0])
    else:
        print("Invoice No. : CAN'T FIND THE VALUE ")
except:
    print("Invoice error")

POs = extract_PO_no_from_pdf()
# for PO in POs:
try:
    if POs!=None:
        print("PO No. :", POs[0])
    else:
        print("PO No. : CAN'T FIND THE VALUE ")
except:
    print("PO error")



wb = Workbook()


sheet1 = wb.add_sheet('Sheet 1')



sheet1.write(1, 0, 'Date')
sheet1.write(2, 0, 'Invoice No.')
sheet1.write(3, 0, 'PO No.')

sheet1.write(1, 1, max_dt)
sheet1.write(2, 1, invoices[0])
sheet1.write(3, 1, POs[0])

wb.save('xlwt example.xls')