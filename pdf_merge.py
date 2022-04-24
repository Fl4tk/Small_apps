import fitz
import glob
import os

pdflist = glob.glob('*.pdf')
print(len(pdflist))

for i in range(0,len(pdflist)):
    if i == 0:
        file = fitz.open(pdflist[i])
    elif os.path.isfile(f'{i-1}.pdf'):
        file = fitz.open(f'{i-1}.pdf')
        file2 = fitz.open(pdflist[i])
        file.insert_pdf(file2)
        file.save(f'{i}.pdf')
        file.close()
        file2.close()
    else:
        file2 = fitz.open(pdflist[i])
        file.insert_pdf(file2)
        file.save(f'{i}.pdf')
        file.close()
        file2.close()

for i in range(1,len(pdflist)-1):
    os.remove(f'{i}.pdf')
os.rename(f'{len(pdflist)-1}.pdf','merged.pdf')