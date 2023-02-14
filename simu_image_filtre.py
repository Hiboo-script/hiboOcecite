# importation
import simucecite as sc


# programme
im = sc.Image.open('photo_test.png')
pix = im.load()

im_test = sc.Image.new('RGB',(256,256))
pix_test = im_test.load()

alpha = -0.9
beta = 0.4
gamma = 1.3 

for i in range(256):
	for j in range(256):
		if (i>=20) and (i<=230) and (j>=20) and (j<=230):
			pix_test[i,j] = sc.filtre(pix,i,j,alpha,beta,gamma)
		else:
			pix_test[i,j] = pix[i,j]

im_test.save('photo_test_filtre.png')
