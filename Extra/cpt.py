# # import cv2 as cv    
# # import pytesseract
# # gray = cv.imread('get-captcha-image.jpeg', cv.IMREAD_GRAYSCALE)
# # cv.threshold(gray, gray, 231, 255, cv.THRESH_BINARY)
# # api = pytesseract.TessBaseAPI()
# # api.Init(".","eng",pytesseract.OEM_DEFAULT)
# # api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz")
# # api.SetPageSegMode(pytesseract.PSM_SINGLE_WORD)
# # pytesseract.SetCvImage(gray,api)
# # print(api.GetUTF8Text())



# from PIL import Image
# from PIL import ImageEnhance
# import PIL.ImageOps
# import pytesseract
# import argparse
# import cv2
# import os
# import numpy

# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="Screenshot from 2023-05-18 17-34-06.png'd")
# args = vars(ap.parse_args())

# # load the example image and convert it to RGB, invert it and adjust brightness
# image = Image.open(args["image"]).convert('RGB')
# image = PIL.ImageOps.invert(image)
# image = ImageEnhance.Brightness(image)
# image = image.enhance(10)
# imageArray = numpy.array(image)
# imageArray = imageArray[:, :, ::-1].copy()

# filename = "Screenshot from 2023-05-18 17-34-06.png".format(os.getpid())
# image.save(filename)

# # load the image as a PIL/Pillow image, apply OCR, and then delete
# # the temporary file
# text = pytesseract.image_to_string(Image.open(filename))
# os.remove(filename)
# print(text)

# # show the output images
# cv2.imshow("Image", imageArray)
# cv2.waitKey(0)


# import driver
# from selenium import webdriver

# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# import time

def solve():
    import sys
    from twocaptcha import TwoCaptcha
    result = None

    sitekey = '<your_site_key_from_two_captcha>'
    api_key = '<your_api_key_from_two_captcha>'
    solver = TwoCaptcha(api_key)
    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url='https://www.deezer.com/en/login'
        )

    except Exception as e:
        sys.exit(e)

    return result




# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.python.org/")





# textarea = driver.find_element(By.ID,"ID")
# solution = solve()
# code = solution['code']
# driver.execute_script(f"var ele=arguments[0]; ele.innerHTML = '{code}';", textarea)
# time.sleep(1) # waiting is mandatory
# textarea = driver.find_element_by_xpath('//*[@id="login-btn"]/button').click()







# from selenium import webdriver
# import urllib
# from selenium.webdriver.common.by import By


# driver = webdriver.Firefox()
# driver.get("http://sistemas.cvm.gov.br/?fundosreg")

# # Change frame.
# driver.switch_to.frame("Main")


# # Download image/captcha.
# img = driver.find_element(By.XPATH, ".//*[@id='trRandom3']/td[2]/img")
# src = img.get_attribute('src')
# urllib.request.urlretrieve(src, "captcha.jpeg")



# import pytesseract
# from PIL import Image

# # Load the captcha image
# captcha_image = Image.open("Screenshot from 2023-05-18 17-34-06.png")

# # Convert the image to grayscale
# captcha_image = captcha_image.convert('L')

# # Apply some pre-processing to the image
# captcha_image = captcha_image.point(lambda x: 0 if x < 200 else 255)

# # Use pytesseract to read the captcha text
# captcha_text = pytesseract.image_to_string(captcha_image)

# # Print the captcha text
# print(captcha_text)



import cv2
import pytesseract

# Set up the screen capture
screen = cv2.VideoCapture(0)

# Continuously capture the screen and process the captcha image
while True:
    # Capture the screen image
    ret, frame = screen.read()

    # Crop the captcha region from the screen image
    captcha = frame[100:150, 400:550]

    # Convert the captcha image to grayscale
    captcha = cv2.cvtColor(captcha, cv2.COLOR_BGR2GRAY)

    # Apply some pre-processing to the image
    captcha = cv2.threshold(captcha, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Use pytesseract to read the captcha text
    captcha_text = pytesseract.image_to_string(captcha)

    # Print the captcha text
    print(captcha_text)

    # Show the processed captcha image
    cv2.imshow("Captcha", captcha)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) == ord("q"):
        break