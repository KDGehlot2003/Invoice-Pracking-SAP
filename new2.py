import easyocr
reader = easyocr.Reader(['en'], gpu=False) # this needs to run only once to load the model into memory
result = reader.readtext('page0.jpg', detail=0)

for i in result:
    print(i)