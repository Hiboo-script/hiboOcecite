import simucecite as sc

size = (256,256)

imin = sc.Image.open("test01.png")
pixin = imin.load()

imout = sc.Image.new('RGB',size)
pixout = imout.load()

alpha = -0.6
beta = 0.2
gamma = 0.8

seuil = 255./2

rayon = 10 #rayon pour la moyenne

delta = 0.6

sc.filtre_l(pixin,pixout,size,alpha,beta,gamma)
sc.moyenne_l(pixout,pixout,size,rayon)

seuil = sc.lumi_moyenne_MC(pixout,size)

sc.contraste_l(pixout,pixout,size,seuil,delta)

imout.save("test_pochoir_photopsie.png")
