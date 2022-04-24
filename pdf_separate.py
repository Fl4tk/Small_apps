import glob
import fitz

pdf = glob.glob('*.pdf')

for name in pdf:
    file = fitz.open(name)
    for i in range(0,file.page_count):
        separated = fitz.open()
        separated.insert_pdf(file,from_page=i,to_page=i)
        separated.save(f'{name.replace(".pdf","")}-p{i+1}.pdf')
        separated.close()