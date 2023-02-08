import numpy as np
from PIL import Image

# bibliotheque
poids = lambda r,n : (-1.)*((r**2)*(1.)/((n+1)**2)) + 1.
r_circle = lambda i,j,x,y : np.sqrt(((x-i)**2 + (y-j)**2)*1.)
check_disk = lambda r,r_pos : r_pos <= r
def moyenne(i,j,r,pix):
	"""
	calcul la moyenne sur un pixel (i,j)
	"""
	somme = np.array([0.,0.,0.])
	ponderation = np.array([0.,0.,0.])
	r_pos = 0.
	v_poids = 0.
	for n in range(i-r,i+r):
		for m in range(j-r,j+r):
			r_pos = r_circle(i,j,n,m)
			if check_disk(r,r_pos) and ((n,m)!=(i,j)):
				v_poids = poids(r_pos,r)
				pixel = pix[n,m]
				somme += np.array([pixel[0]*v_poids,pixel[1]*v_poids,pixel[2]*v_poids])
				ponderation += np.array([1.,1.,1.])*v_poids

	return (int(somme[0]/ponderation[0]),int(somme[1]/ponderation[1]),int(somme[2]/ponderation[2]))

im = Image.open('moyenne_test_11.png')
pix = im.load()

im_test = Image.new('RGB',(256,256))
pix_test = im_test.load()



for i in range(256):
	for j in range(256):
		if (i>=20) and (i<=230) and (j>=20) and (j<=230):
			pix_test[i,j] = moyenne(i,j,3,pix)
		else:
			pix_test[i,j] = pix[i,j]

im_test.save('moyenne_test_11_reset_1.png')
