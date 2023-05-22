
from PyPDF2 import PdfReader

pdf_document = "SINTEX_INDUSTRIES_LTD_-_KALASAGAR_SALES_-_GST_2023-24_0628_1-May-23.pdf"
with open(pdf_document, "rb") as filehandle:
    pdf = PdfReader(filehandle)
    info = pdf.metadata
    pages = pdf.getNumPages()

    # print (info)
    # print ("number of pages: %i" % pages)

    page1 = pdf.getPage(0)
    # print(page1)
    # print(page1.extractText())
    text = page1.extract_text()
    print(text)



from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('SINTEX_INDUSTRIES_LTD_-_KALASAGAR_SALES_-_GST_2023-24_0628_1-May-23.pdf')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')

# import the following libraries
# will convert the image to text string
import pytesseract	

# adds image processing capabilities
from PIL import Image	



# opening an image from the source path
img = Image.open('page0.jpg')	

# describes image format in the output
# print(img)						
# path where the tesseract module is installed

# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
# with open('abc.txt',mode ='w') as file:	
	
# 				file.write(result)
# 				print(result)
			


# import pdftotext
import re
from  datetime import datetime


def mtn(x):
    months = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'aug': '08',
        'sep': '09',
        'oct': 10,
        'nov': 11,
        'dec': 12
        }
    a = x.strip()[:3].lower()
    global ez
    try:
        ez = months[a]
        # print (ez)
    except:
        raise ValueError('Not a month')
    

def year(x):
    year = {
        '22': '2022',
        '23': '2023',
        '24': '2024',
        '21': '2021',
        '20': '2020',
        '19': '2019',
        '25': '2025',
        }
    # a = x.strip()[:3].lower()
    global yr
    try:
        yr = year[x]
        # print (yr)
    except:
        raise ValueError('Not a month')


# year('23')



def date(x):
    global xdt
    x = int(x)
    if x in range(0,10):
        x = str(x)
        xdt= "0" + x
    else:
        x = str(x)
        xdt = x
    # print(xdt)
    

# date('23')
 

# with open('SINTEX_INDUSTRIES_LTD_-_KALASAGAR_SALES_-_GST_2023-24_0628_1-May-23.pdf','rb') as f:
#     pdf = pdftotext.PDF(f)
#     text = '\n\n'.join(pdf)

# print(text)

invoice_number = re.search(r'Invoice No.\s*\n(.+?)\s*\n', text).group(1).strip() or re.search(r'Invoice Number\s*\n(.+?)\s*\n', text).group(1).strip()

invoice_date = re.search(r'Dated\s*\n(.+?)\s*\n', text).group(1).strip() or re.search(r'Date\s*\n(.+?)\s*\n', text).group(1).strip()

Total = re.search(r'Total\s*\n\S*\n(.+?)\s*\n', text).group(1).strip()  

services = re.search(r'Services\s*\n\S*\n(.+?)\s*\n', text).group(1).strip()

# for i in range(0,8):
    # print(invoice_date[i])
# month = invoice_date[2:5]
mtn(invoice_date[2:5])
# print(invoice_date[:-7])
year(invoice_date[-2:])
date(invoice_date[:-7])




invoice_date = invoice_date.split("-")
dt = xdt+'.'+ ez +"."+yr






print("Reference :", invoice_number)
print("Invoice Date :", dt)
print("Total amount :", Total)
print("Service :", services)


