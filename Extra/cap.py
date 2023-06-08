# import numpy as np 
import easyocr
import cv2 
# from PIL import Image 
# import PIL 

from matplotlib import pyplot as plt 

image = cv2.imread('Screenshot from 2023-06-01 11-25-18.png',1) 

# image_bw = cv2.imread('Screenshot from 2023-06-01 10-51-26.png',0)


# noiseless_image_bw = cv2.fastNlMeansDenoising(image_bw, None, 20, 7, 21) 

noiseless_image_colored = cv2.fastNlMeansDenoisingColored(image,None,20,20,7,21) 

print(type(noiseless_image_colored))

titles = ['Original Image(colored)','Image after removing the noise (colored)', 'Original Image (grayscale)','Image after removing the noise (grayscale)']
images = [image,noiseless_image_colored]
plt.figure(figsize=(13,5))
for i in range(2):
    plt.subplot(2,2,i+1)
    plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
plt.show()



from PIL import Image
im = Image.fromarray(noiseless_image_colored)
im.save("your_file.jpeg")


reader = easyocr.Reader(['en'], gpu=False) 
result = reader.readtext('your_file.jpeg', detail=0)
print(result)



# im1 = noiseless_image_colored.save(r'/home/kdgehlot/Desktop/Office/Project_2/Main/Invoice-Pracking-SAP/Screenshot from 2023-06-01 10-50-08.png')