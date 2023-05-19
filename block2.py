import fitz

filename = "example.pdf"
search_term = "invoice"
pdf_document = fitz.open(filename)

for current_page in range(len(pdf_document)):
    page = pdf_document.loadPage(current_page)
    if page.searchFor(search_term):
        print("%s found on page %i" % (search_term, current_page))