import glob
import itertools
import img2pdf

extensions = ['.png','.jpg','jpeg']
imglist = list(itertools.chain.from_iterable([glob.glob(f'*{_}') for _ in extensions]))

with open('output.pdf','wb') as f:
    f.write(img2pdf.convert(imglist))