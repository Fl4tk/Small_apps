import itertools
import glob
from PIL import Image
import os

extensions = ['.png','.jpg','.jpeg']
imglist = list(itertools.chain.from_iterable([glob.glob(f'*{_}') for _ in extensions]))
to_png = None

for filename in imglist:
    if not '.png' in filename: # jpg to png
        img = Image.open(filename).convert('RGBA')
        to_png = filename.split('.')[0]
        img.save(f'{to_png}.png')
        img = Image.open(f'{to_png}.png')
    else:
        img = Image.open(filename)
    savefile = filename.split('.')[0]
    img.save(f'{savefile}.ico',format='ICO',sizes=[(32,32)]) # save file as 'ico'
    
    if to_png != None:
        os.remove(f'{to_png}.png') # delete converted png
    else:
        pass