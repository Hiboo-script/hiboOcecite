# importation
import simucecite as sc


# programme
im = sc.Image.open('photo_test.png')
pix = im.load()

im_test = sc.Image.new('RGB',(256,256))
pix_test = im_test.load()

delta = 0.3

for i in range(256):
	for j in range(256):
		if (i>=20) and (i<=230) and (j>=20) and (j<=230):
			pix_test[i,j] = sc.contraste_v2(pix,i,j,delta)
		else:
			pix_test[i,j] = pix[i,j]

im_test.save('photo_test_contraste.png')
