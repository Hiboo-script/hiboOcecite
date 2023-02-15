"""
J'essaye ici dans la mesure du possible de reproduire un domaine 
qui correspond a mon debut de degenerescence !
"""


import simucecite as sc

size = (256,256)

im = sc.Image.new('RGB',(256,256))
pix = im.load()

disque = lambda x0,y0,x1,y1 : (x0-x1)**2 + (y0-y1)**2
indisque = lambda x0,y0,x1,y1,r : disque(x0,y0,x1,y1) <= r**2

centre = (size[0]/2,size[1]/2)
foyer = (centre[0]+50,centre[1]+40)
r1 = 100
r2 = 90

for y in range(size[1]):
	for x in range(size[0]):
		if indisque(centre[0],centre[1],x,y,r1) and (indisque(foyer[0],foyer[1],x,y,r2)==False):
			pix[x,y] = (255,255,255)
		else:
			pix[x,y] = (0,0,0)


im.save("disque_4.png")
