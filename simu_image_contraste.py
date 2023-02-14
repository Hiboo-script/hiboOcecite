import numpy as np
from PIL import Image

# bibliotheque
arc = lambda x : (255./(2.*np.arctan(255./2.)))*np.arctan(x-(255./2.)) + 255./2.

def contraste(i,j,pix):
	return (int(arc(pix[i,j][0])),int(arc(pix[i,j][1])),int(arc(pix[i,j][2])))

im = Image.open('moyenne_test_11.png')
pix = im.load()

im_test = Image.new('RGB',(256,256))
pix_test = im_test.load()



for i in range(256):
	for j in range(256):
		if (i>=20) and (i<=230) and (j>=20) and (j<=230):
			pix_test[i,j] = contraste(i,j,pix)
		else:
			pix_test[i,j] = pix[i,j]

im_test.save('contraste__test_1.png')
