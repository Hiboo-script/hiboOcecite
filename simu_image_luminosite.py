# importation
import simucecite as sc


# programme
delta = -0.5

im = sc.Image.open('contraste_test_1(v2).png')
pix = im.load()

im_test = sc.Image.new('RGB',(256,256))
pix_test = im_test.load()



for i in range(256):
	for j in range(256):
		if (i>=20) and (i<=230) and (j>=20) and (j<=230):
			pix_test[i,j] = sc.luminosite(pix,i,j,delta)
		else:
			pix_test[i,j] = pix[i,j]

im_test.save('luminosite_test_1.png')
