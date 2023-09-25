import re
import PyPDF2

# open the PDF file in binary mode
with open('Q2.pdf', 'rb') as f:
    # create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(f)

    # loop through each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        # get the text from the current page
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # search for the pattern "CL xxx" with up to one space in the string before "CL"
        # pattern = r'(\S+\s)?\S+ CL \d{3}'
        pattern = r"CL\d{3}"
        matches = re.findall(pattern, text)

        # loop through the matches and print the three strings to the left of each match
        for match in matches:
            # split the match into individual strings
            strings = match.split()
            # get the three strings to the left of "CL"
            index = strings.index('CL')
            if index >= 3:
                result = ' '.join(strings[index-3:index])
                print(result)


# 1. find CL og tilhørende navn, find alle item_codes og descriptions til det cl (gem cl), hvis codelisten har været der før = pass, ellers print