from pdf2image import convert_from_path
import easyocr

global scanned_text
global result
global images

def convert_pdf_to_image():
    images = convert_from_path('D:\\folder_1\\test.pdf',dpi=300)


    for i in range(len(images)):

        images[i].save('page'+ str(i) +'.jpg', 'JPEG')

def convert_image_txt():

    reader = easyocr.Reader(['en'], gpu=False) 
    result = reader.readtext('D:\\folder_1\\page0.jpg', detail=0)


    with open('D:\\folder_1\\converted.txt',mode ='w') as file:
        file.write("D:\\folder_1\\converted.txt \n \n")


    for i in result:
        with open('D:\\folder_1\\converted.txt',mode ='a') as file:
            file.write(i)
            file.write("\n")
            scanned_text = i
            # print(scanned_text)


convert_pdf_to_image()
convert_image_txt()