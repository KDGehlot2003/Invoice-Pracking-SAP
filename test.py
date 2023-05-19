# import module
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
print(img)						
# path where the tesseract module is installed

# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('abc.txt',mode ='w') as file:	
	
				file.write(result)
				print(result)
				


import re
