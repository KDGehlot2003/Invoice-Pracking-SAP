import pdftotext
import re


with open('SINTEX_INDUSTRIES_LTD_-_KALASAGAR_SALES_-_GST_2023-24_0628_1-May-23.pdf','rb') as f:
    pdf = pdftotext.PDF(f)
    text = '\n\n'.join(pdf)

# print(text)

invoice_number = re.search(r'Invoice No.\s*\n\s*\n(.+?)\s*\n', text).group(1).strip()

invoice_date = re.search(r'Dated\s*\n\s*\n(.+?)\s*\n', text).group(1).strip()

reference = re.search(r'Reference No. & Date.\s*\n\s*\n(.+?)\s*\n', text).group(1).strip()

print("Invoice Number :", invoice_number)
print("Invoice Date :", invoice_date)
print("PO Number :", reference)

