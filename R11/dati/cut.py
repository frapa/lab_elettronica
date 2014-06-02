import glob
from PIL import Image
import PIL.ImageOps

for i in glob.glob('*.png'):
        im = Image.open(i)
        im = im.crop((16, 43, 800, 443))
        ni = PIL.ImageOps.invert(im)
        
        ni.save('new_'+i)