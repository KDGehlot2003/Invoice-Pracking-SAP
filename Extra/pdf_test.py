import pdftotext
import re


with open('invoice.pdf', 'rb') as f:
    pdf = pdftotext.PDF(f)
    text = '\n\n'.join(pdf)

invoice_number = re.search(r'Invoice Number\s*\n\s*\n(.+?)\s*\n', text).group(1).strip()
total_amount_due = re.search(r'Total Due\s*\n\s*\n(.+?)\s*\n', text).group(1).strip()

# Extract the invoice date
invoice_date_pattern = re.compile(r'Invoice Date\s*\n\s*\n(.+?)\s*\n')
invoice_date_match = invoice_date_pattern.search(text)
if invoice_date_match:
    invoice_date = invoice_date_match.group(1).strip()
else:
    invoice_date = None

# Extract the due date
due_date_pattern = re.compile(r'Due Date\s*\n\s*\n(.+?)\s*\n')
due_date_match = due_date_pattern.search(text)
if due_date_match:
    due_date = due_date_match.group(1).strip()
else:
    due_date = None

print('Invoice Number:', invoice_number)
print('Date:', date)
print('Total Amount Due:', total_amount_due)
print('Invoice Date:', invoice_date)
print('Due Date:', due_date)