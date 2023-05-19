import spacy
import codecs
# Load the English pre-trained model with NER
nlp = spacy.load('en_core_web_sm')

with codecs.open("INV_1.pdf",'r') as f:
    print(f)
    text = f.read()
# print(text)

#Apply the NER model to the invoice text
doc = nlp(text)
# print(doc)
invoice_number = None
invoice_date = None
total_amount_due = None

for ent in doc.ents:
    if ent.label_ == 'Head':
        invoice_number = ent.text.strip()
        print("hello")
    # elif ent.label_ == 'DATE':
    #     if ent.text.strip().lower().startswith('invoice'):
    #         invoice_date = ent.text.strip()
    # elif ent.label_ == 'MONEY':
    #     if 'total' in ent.text.strip().lower():
    #         total_amount_due = ent.text.strip()


print('Invoice Number:', invoice_number)
print('Invoice Date:', invoice_date)
print('Total Amount Due:', total_amount_due)