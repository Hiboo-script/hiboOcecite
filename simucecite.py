import numpy as np
import random as rd
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

def moyenne_l(pixin,pixout,size,r):
	for i in range(20,size[0]-20):
		for j in range(20,size[1]-20):
			pixout[i,j] = moyenne(i,j,r,pixin)


####
## PARTIE CONTRASTE

arc = lambda x : (255./(2.*np.arctan(255./2.)))*np.arctan(x-(255./2.)) + 255./2.

def contraste_explo(i,j,pix):
	return (int(arc(pix[i,j][0])),int(arc(pix[i,j][1])),int(arc(pix[i,j][2])))


def contrasteExplo_l(pixin,pixout,size):
	for i in range(size[0]):
		for j in range(size[1]):
			pixout[i,j] = contraste(i,j,pixin)



moy_pix = lambda pix : (pix[0]+pix[1]+pix[2])/3.

def contraste(pix,i,j,delta):
	seuil = 255./2.
	moy = moy_pix(pix[i,j])
	
	if(moy>seuil):
		return luminosite(pix,i,j,delta) 
	else: 
		return luminosite(pix,i,j,(-1.)*delta)


def contraste_l(pixin,pixout,size,delta):
	for i in range(size[0]):
		for j in range(size[1]):
			pixout[i,j] = contraste(pixin, i, j, delta)



#####
###  PARTIE LUMINOSITE

lumiarc = lambda x : ((2*255.)/np.pi)*(np.arctan(x) + (np.pi/2.))
reci_lumiarc = lambda y : np.tan(((y*np.pi)/(2.*255))-(np.pi/2.))
lumi_delta = lambda y,delta : int(lumiarc(reci_lumiarc(y) + delta))

def luminosite(pix, i, j, delta):
	return (lumi_delta(pix[i,j][0],delta),lumi_delta(pix[i,j][1],delta),lumi_delta(pix[i,j][2],delta))



def luminosite_l(pixin,pixout,size,delta):
	for i in range(size[0]):
		for j in range(size[1]):
			pixout[i,j] = luminosite(pixin, i, j, delta)




####
##  PARTIE FILTRE COULEUR

def filtre(pix,i,j,alpha,beta,gamma):
	return (lumi_delta(pix[i,j][0],alpha),lumi_delta(pix[i,j][1],beta),lumi_delta(pix[i,j][2],gamma))

def filtre_l(pixin,pixout,size,alpha,beta,gamma):
	for i in range(size[0]):
		for j in range(size[1]):
			pixout[i,j] = filtre(pixin, i, j, alpha, beta, gamma)


#####
##  PARTIE LUMINOSITE MOYENNE

def lumi_moyenne_t(pixin,size):
	somme = 0
	ponderation = size[0]*size[1]*3

	for i in range(size[0]):
		for j in range(size[1]):
			somme += pixin[i,j][0] + pixin[i,j][1] + pixin[i,j][2]
	somme = somme * 1.

	return (somme/ponderation)

def lumi_moyenne_MC(pixin,size):
	somme = 0
	x = size[0]/2
	y = size[1]/2
	for i in range(1000):
		x = rd.randint(0,size[0]-1)
		y = rd.randint(0,size[1]-1)
		somme += pixin[x,y][0] + pixin[x,y][1] + pixin[x,y][2]
	somme = somme*1.
	
	return (somme/3000.)
