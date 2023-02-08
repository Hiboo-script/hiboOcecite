from PIL import Image
import random as rd

size = (256,256)
im = Image.new('RGB',size)
pix = im.load()

for i in range(size[0]):
	for j in range(size[1]):
		pix[i,j] = (rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))

im.save('test03.png')
