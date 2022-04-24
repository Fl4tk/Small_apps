import fitz
import glob

zoom_x = 1.0
zoom_y = 1.0
mat = fitz.Matrix(zoom_x,zoom_y) #zoom_ の値が大きいほど解像度がたかくなる

pdf = glob.glob('*.pdf')

for name in pdf:
    doc = fitz.open(name)
    for page in doc:
        pix = page.get_pixmap(matrix=mat)
        if doc.page_count == 1:
            pix.save(f'{name.replace(".pdf","")}.png')
        else:
            pix.save(f'{name.replace(".pdf","")}-p{page.number + 1}.png')
    doc.close()