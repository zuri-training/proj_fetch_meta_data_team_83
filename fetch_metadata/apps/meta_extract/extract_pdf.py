#pip install pikepdf
#then run python <filename.py> <file>.pdf 

import pikepdf
import sys

pdf_filename = sys.argv[1]

#read pdf file
pdf = pikepdf.Pdf.open(pdf_filename)
docinfo = pdf.docinfo
for key, value in docinfo.items():
    print(key, ":", value)
    
