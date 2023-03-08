import simucecite as sc

size = (552,552)

imin = sc.Image.new('RGB',size)
pixin = imin.load()

imout_1 = sc.Image.new('RGB',size)
pixout_1 = imout_1.load()

imout_2 = sc.Image.new('RGB',size)
pixout_2 = imout_2.load()

imout_3 = sc.Image.new('RGB',size)
pixout_3 = imout_3.load()


alpha = -0.6
beta = 0.2
gamma = 0.8

seuil = 255./2

rayon = 5 #rayon pour la moyenne

delta = 1.

nom_save = "images/calque_simulation_3.png"

print("generation d'une image aleatoire de taille : "+str(size[0])+"x"+str(size[1]))
sc.random_image(pixin,size)

print("filtrage des couleurs de l'image : alpha="+str(alpha)+";beta="+str(beta)+";gamma="+str(gamma))
sc.filtre_l(pixin,pixout_1,size,alpha,beta,gamma)

print("application de la moyenne de rayon="+str(rayon))
sc.moyenne_l(pixout_1,pixout_2,size,rayon)

print("calcul du seuil moyen de luminosite...")
seuil = sc.lumi_moyenne_MC(pixout_2,size)
print("seuil="+str(seuil))

seuil=seuil-2.5
print("application du contraste : delta="+str(delta)+" ; seuil="+str(seuil))
sc.contraste_l(pixout_2,pixout_3,size,seuil,delta)

print("sauvegarde sous le nom : "+ nom_save)
imout_3.save(nom_save)
