import pyperclip
#import re
# Read the text from the clipboard
text = pyperclip.paste()
#print("______________________") 
# Print the text
#print(text)
#print("______________________")

global crt


with open('converted.txt',mode ='r') as file:
    x = file.readlines()

def extract_rate_from_pdf():
    
    extracted_rate = []

    for i in result:
        PO_no_pattern = r'\d{1,3}(?:,\d{3})*\.\d{2}'
        POs = re.findall(PO_no_pattern, i)
        extracted_rate.extend(POs)

    return extracted_rate
extract_rate_from_pdf()

rts = extract_rate_from_pdf()
rts = [value.replace(',', '') for value in rts]
rts = [float(value) for value in rts]
list2 = list(set(rts))
list2.sort()
high_rt = list2[-1]
sec_high_rt = list2[-2]
t_rate_gst = "{:,.2f}".format(high_rt)

t_rate = "{:,.2f}".format(sec_high_rt)

print("Total Rate:",t_rate_gst)
print("Total Rate without gst:",t_rate)


try:
    if "," in text:
        crt = float(text.replace(",", ""))
    else:
        crt = text
    print(crt)
except:
    print("ERROR")
