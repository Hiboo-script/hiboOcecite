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

def contraste(pix,i,j,seuil_normal,delta):
	seuil = 255*seuil_normal
	moy = moy_pix(pix[i,j])
	
	if(moy>seuil):
		return luminosite(pix,i,j,delta) 
	else: 
		return luminosite(pix,i,j,(-1.)*delta)


def contraste_l(pixin,pixout,size,seuil_normal,delta):
	for i in range(size[0]):
		for j in range(size[1]):
			pixout[i,j] = contraste(pixin, i, j, seuil_normal, delta)


def demi_contraste_m(pixin,i,j,seuil,delta):
	if (lumi_pix_moyenne(pixin,i,j))<seuil:
		return luminosite(pixin,i,j,delta)
	else:
		return pixin[i,j]


def demi_contraste_m_l(pixin,pixout,size,seuil,delta):
	for i in range(size[0]):
		for j in range(size[1]):
			pixout[i,j] = demi_contraste_m(pixin,i,j,seuil,delta)


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

lumi_pix_moyenne = lambda pix,i,j : (pix[i,j][0]+pix[i,j][1]+pix[i,j][2])/3.

def lumi_moyenne_t(pixin,size):
	somme = 0
	ponderation = size[0]*size[1]

	for i in range(size[0]):
		for j in range(size[1]):
			somme += lumi_pix_moyenne(pixin,i,j)
	somme = somme * 1.

	return (somme/ponderation)

def lumi_moyenne_MC(pixin,size):
	somme = 0
	x = size[0]/2
	y = size[1]/2
	for i in range(1000):
		x = rd.randint(0,size[0]-1)
		y = rd.randint(0,size[1]-1)
		somme += lumi_pix_moyenne(pixin,x,y)
	somme = somme*1.
	
	return (somme/1000.)


#####
### PARTIE PHOTOPSIE, CALQUE, POCHOIR

def proportionnelle(ratio,value):
	"""
	[0,255]x[0,255] -> [[0,255]]
	proportionnalise la value a partir du ratio !
	retourne la value proportionne
	"""
	proportion = (ratio*1.)/255
	
	return int(value*proportion)


def propo_pixel(pixin, i, j, ratio):
	"""
	applique la proportionnelle a un pixel,
	retourne le pixel entier
	"""
	
	return (proportionnelle(ratio,pixin[i,j][0]),proportionnelle(ratio,pixin[i,j][1]),proportionnelle(ratio,pixin[i,j][2]))


poly_sigma = lambda x : ((4000.-150.)/(255.**2))*(x-255.)**2 + 150.

normal = lambda x : np.random.normal(255.,poly_sigma(x))


def pix_simuphotopsie(pochoir,calque,i,j):
	"""
	calcul le pixel final a partir du pochoir et du calque
	retourne le pixel	
	"""
	norm = normal(pochoir[i,j][0])
	# gere les cas ou la loi normal part trop loin de 255
	if (norm > 255):
		norm = 510 - norm
	if (norm < 0):
		norm = 0
	return propo_pixel(calque, i, j, norm)

def simuphotopsie(pochoir, calque, pixout, size):
	"""
	itere pix_simuphotopsie sur toute l'image
	retourne rien, applique tout sur pixout
	"""
	for x in range(size[0]):
		for y in range(size[1]):
			pixout[x,y] = pix_simuphotopsie(pochoir, calque, x, y)

