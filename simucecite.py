import numpy as np
from PIL import Image

####
## PARTIE MOYENNE 

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


####
## PARTIE CONTRASTE

arc = lambda x : (255./(2.*np.arctan(255./2.)))*np.arctan(x-(255./2.)) + 255./2.

def contraste(i,j,pix):
	return (int(arc(pix[i,j][0])),int(arc(pix[i,j][1])),int(arc(pix[i,j][2])))



#####
###  PARTIE LUMINOSITE

lumiarc = lambda x : ((2*255.)/np.pi)*(np.arctan(x) + (np.pi/2.))
reci_lumiarc = lambda y : np.tan(((y*np.pi)/(2.*255))-(np.pi/2.))
lumi_delta = lambda y,delta : int(lumiarc(reci_lumiarc(y) + delta))

def luminosite(pix, i, j, delta):
	return (lumi_delta(pix[i,j][0],delta),lumi_delta(pix[i,j][1],delta),lumi_delta(pix[i,j][2],delta))